import pyttsx3 as tts
import pyautogui
import time


def annoyingPart():  # works on 64-bit win 11
    while True:
        pyautogui.moveTo(0, 0)  # Move mouse to top-left corner
        engine.say("Hi, Hope you're enjoying this because I've hand crafted this for specially you hehehehehehehe! (Evil laugh)")
        engine.runAndWait()


if __name__ == "__main__":
    pyautogui.FAILSAFE = False
    print("Hi, Hope you're enjoying this because I've hand crafted this for specially you hehehehehehehe! (Evil laugh)")
    engine = tts.init()
    engine.say("Hi, Hope you're enjoying this because I've hand crafted this for specially you hehehehehehehe! (Evil laugh)")
    engine.runAndWait()
    annoyingPart()
