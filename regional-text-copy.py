from PIL import Image
import pytesseract
from pynput import mouse
import pyautogui
import os
import math
import time

# Example usage of Tesseract OCR in Python
def extract_text(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(img)

    return text

def on_click(x, y, button, pressed):
    x = math.floor(x)
    y = math.floor(y)
    if pressed:
        global top_left
        top_left = (x, y)
    else:
        global bottom_right
        bottom_right = (x, y)
        # Stop listener
        return False

def select_area():
    print("Click and hold at one corner of the desired area, then release at the opposite corner.")

    # Collect events until released
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    return (top_left[0], top_left[1], bottom_right[0] - top_left[0], bottom_right[1] - top_left[1])

def take_screenshot(region, file_path):
    # Taking a screenshot of the selected area
    screenshot = pyautogui.screenshot(region=region)

    # Save the screenshot
    screenshot.save(file_path)

if __name__ == "__main__":
    selected_region = select_area()

    save_path = os.path.join(os.getcwd(), f"screenshot.png")

    take_screenshot(selected_region, save_path)

    print(f"Screenshot saved")

    extracted_text = extract_text("screenshot.png")
    print(extracted_text)
