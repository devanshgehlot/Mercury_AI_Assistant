import pyautogui
import os
import time
import speech_recognition as sr

rcn=sr.Recognizer()
# screenWidth, screenHeight = pyautogui.size()

# print(screenWidth, screenHeight)
# for i in range (1,100000):
#     currentMouseX, currentMouseY = pyautogui.position()
#     print(currentMouseX,currentMouseY)
#     i+=1
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
# pyautogui.write('Hello world!', interval=0.25)
# pyautogui.click(745,368)
# pyautogui.keyDown("shift")
# pyautogui.write(["left"] * 12)
# pyautogui.keyUp("shift")
# pyautogui.hotkey("ctrl","c")
# pyautogui.click(199,289)
# pyautogui.click(500,500)
# pyautogui.hotkey("ctrl","v")
745/368
199/289

# def message():
#     os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
#     time.sleep(10)
#     pyautogui.click(400,166)
#     pyautogui.write("aman", interval=0.25)
#     time.sleep(3)
#     pyautogui.click(535,391)
#     time.sleep(1)
#     pyautogui.click(1030,1023)
#     pyautogui.write("i am god", interval=0.25)
#     pyautogui.keyDown("shift")
#     pyautogui.press("enter")
#     pyautogui.keyUp("shift")
#     pyautogui.write("this is written by mercury", interval=0.25)
#     time.sleep(3)
#     pyautogui.click(1871,1025)

# message()
# for i in range(1,100):
#     try:
#         with sr.Microphone() as source:   
#             print("Listening...")
#             audio = rcn.listen(source, timeout=3, phrase_time_limit=1)
#         word = rcn.recognize_google(audio)
#         words=word.lower().split()
#         print(words)
#         i+=1
#     except Exception as e:
#         print(e)
# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Shall I proceed?')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
# name=pyautogui.prompt('What is your name?')
# print(name)
# password=pyautogui.password('Enter password (text will be hidden)')
# print(password)
os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")

time.sleep(5)  # time to open target app

button = pyautogui.locateCenterOnScreen('send.png')

if button:
    pyautogui.click(button)