import os

import pytesseract

TESSERACT_CMD = pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
FOLDER_PATH = os.getcwd() + '\pic'
TEXT = " "
COUNT = 0