# simple_ocr.py
# A simple OCR (Optical Character Recognition) project using Python
# This script extracts text from an image and prints it.

from PIL import Image
import pytesseract

# Update this with your image file name (place it in the same folder as this code)
image_path = "sample_image.png"

try:
    # Open the image
    img = Image.open(image_path)

    # Extract text using Tesseract OCR
    extracted_text = pytesseract.image_to_string(img)

    print("===== Extracted Text =====")
    print(extracted_text)

except FileNotFoundError:
    print(f"Error: The file '{image_path}' was not found. Please add it to the project folder.")

except Exception as e:
    print("An error occurred:", e)

# Note:
# 1. You must install 'pillow' and 'pytesseract' before running:
#    pip install pillow pytesseract
# 2. Also install Tesseract OCR engine on your device:
#    - Windows: https://github.com/UB-Mannheim/tesseract/wiki
#    - Mac: brew install tesseract
#    - Android (Pydroid 3): Install Tesseract plugin
