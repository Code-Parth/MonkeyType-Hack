# import some packages that we are use in python program
import cv2
import pyautogui
import numpy as np
from PIL import Image
from os import remove
from time import sleep
from playsound import playsound
from pytesseract import pytesseract

# Give some time for program
sleep(2)

# take screenshot using pyautogui and save as file
ScreenShot = pyautogui.screenshot()
FullScreen_Image = cv2.cvtColor(np.array(ScreenShot), cv2.COLOR_RGB2BGR)
cv2.imwrite("./Image/FullScreen.png", FullScreen_Image)

# after taking screenshot program will notify
playsound('./Screenshot_Capture.wav')

# processing FullScreen.png Image for Cropping
Processing_Image = cv2.imread('./Image/FullScreen.png')

height, width = Processing_Image.shape[:2]

# Extracted Line 01 from Image
start_row_01, start_col_01 = int(height*.375), int(width*.06)
end_row_01, end_col_01 = int(height*.425), int(width*.92)

Cropped_Line_01 = Processing_Image[start_row_01:end_row_01,
                                   start_col_01:end_col_01]
cv2.imwrite("./Image/Cropped_Line_01.png", Cropped_Line_01)

# Extracted Line 02 from Image
start_row_02, start_col_02 = int(height*.425), int(width*.06)
end_row_02, end_col_02 = int(height*.475), int(width*.92)

Cropped_Line_02 = Processing_Image[start_row_02:end_row_02,
                                   start_col_02:end_col_02]
cv2.imwrite("./Image/Cropped_Line_02.png", Cropped_Line_02)

# Extracted Line 03 from Image
start_row_03, start_col_03 = int(height*.475), int(width*.06)
end_row_03, end_col_03 = int(height*.525), int(width*.92)

Cropped_Line_03 = Processing_Image[start_row_03:end_row_03,
                                   start_col_03:end_col_03]
cv2.imwrite("./Image/Cropped_Line_03.png", Cropped_Line_03)

# Extract text from images
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path_01 = r".\Image\Cropped_Line_01.png"
image_path_02 = r".\Image\Cropped_Line_02.png"
image_path_03 = r".\Image\Cropped_Line_03.png"
img_01 = Image.open(image_path_01)
img_02 = Image.open(image_path_02)
img_03 = Image.open(image_path_03)
pytesseract.tesseract_cmd = path_to_tesseract
text_01 = pytesseract.image_to_string(img_01)
text_02 = pytesseract.image_to_string(img_02)
text_03 = pytesseract.image_to_string(img_03)

# generating the whole string
Full_Text = (text_01[:-1] + " " + text_02[:-1] + " " + text_03[:-1])

# Typing will start
pyautogui.write(Full_Text, interval=0.03)

# Delete Temporary Files
remove("./Image/FullScreen.png")
remove("./Image/Cropped_Line_01.png")
remove("./Image/Cropped_Line_02.png")
remove("./Image/Cropped_Line_03.png")