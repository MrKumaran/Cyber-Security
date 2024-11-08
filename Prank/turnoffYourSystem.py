import pyautogui


def freezeCursor():
    while True:
        pyautogui.moveTo(0, 0)


pyautogui.FAILSAFE = False
print("Alright, that's enough. \nYou've spent enough time on your system—it's time to shut it down and let it rest. \nStep away, go outside, and have some fun! No more screen time; \njust hit the power button and turn it off.")
while True:
    try:
        freezeCursor()
    except KeyboardInterrupt:
        print("\nJust hit the power button and turn it off no other war around!")
        freezeCursor()
