# ocrprocessing
Image to Text conversion using tesseract


Run ocr_preprocess.py file to extract text from images

tesseract: This is the command-line executable for Tesseract OCR.

{output_image}: This part seems to be a placeholder for the path to the input image file that you want to perform OCR on.

"output24": This is likely the base name for the output files that Tesseract will generate. The actual output files will have extensions like .txt appended to this base name.

"-l eng": This option specifies the language for OCR. In this case, it's set to English (eng). You can replace "eng" with other language codes supported by Tesseract.

"--psm 11": This option sets the page segmentation mode (psm) for Tesseract. 11 corresponds to the "Sparse text with OSD" mode. Page segmentation mode determines how Tesseract treats the layout and structure of the input image.
