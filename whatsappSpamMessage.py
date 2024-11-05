"""
This code is just for fun

This code send message to the person you want
You can send word single time or spam till they block you
also you can send word directly or use multiple word let random module choose one by itself

This code close tab automatically close tab for less ram resource usage
"""

import random
import pywhatkit
import time

phone_number = ""  # Enter Person phone number whom you wanna send message with country code
waitTime = 10  # How long do you want to wait before sending your message(in seconds min 15s)
word = ("Hola", "Bello")  # add multiple words in word variable
NumberOfTimes = 2  # Number of times message to be sent
for ran in range(NumberOfTimes):
    pywhatkit.sendwhatmsg_instantly(f"{phone_number}", random.choice(word), wait_time=waitTime, tab_close=True)
    time.sleep(10)
