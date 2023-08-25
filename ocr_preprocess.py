import cv2
import sys
import subprocess

def preprocess_image(image_path):
    print("preprocess func started")
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply preprocessing steps here
    image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)
    #image = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)


    new_width = 2500  # Adjust as needed
    aspect_ratio = image.shape[1] / image.shape[0]
    new_height = int(new_width / aspect_ratio)
# Resize
    resized_image = cv2.resize(image, (new_width, new_height))

# Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(resized_image, (5, 5), 0)
    print("image blurred")
# Binarization using adaptive thresholding
    binary_image = cv2.adaptiveThreshold(
        blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

# Noise reduction using morphological operations
    #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    #denoised_image = cv2.morphologyEx(binary_image, cv2.MORPH_CLOSE, kernel)
    #print("noise reduced")
# Text Localization using contours
    contours, _ = cv2.findContours(blurred_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Localized Text', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    
    # ...
    print("image input")
   
   # preprocessed_image = preprocess_image(input_image)
    print("image return")
    return image

def main():
    print("entered main")
    if len(sys.argv) != 2:
        print("Usage: python ocr_preprocess.py input_image.jpg")
        return

    input_image = sys.argv[1]
    output_image = "preprocessed_image1.jpg"

    # Preprocess the image
    print("preprocee fun in main")
    input_image="input_image.jpg"
    preprocessed_image = preprocess_image(input_image)

    # Save the preprocessed image
    print("preprocee save in main")
    cv2.imwrite(output_image, preprocessed_image)

    # Run Tesseract on the preprocessed image
    print("start tess in main")
    tesseract_cmd = f"tesseract {output_image} output24 -l eng --psm 11"
    subprocess.run(tesseract_cmd, shell=True)

if __name__ == "__main__":
    main()
