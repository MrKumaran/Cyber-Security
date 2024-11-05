import pyttsx3 as tts
import pyautogui
import time


def block_mouse():
    while True:
        pyautogui.moveTo(0, 0)  # Move mouse to top-left corner


if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    block_mouse()
