import pyttsx3
import webbrowser
import speech_recognition as sr
import os
import library
import urllib.parse
import pyautogui
import time

rcn=sr.Recognizer()
sk=pyttsx3.init()
a=1

def speak(t):
    sk.say(t)
    sk.runAndWait()

def Commands(command):

    if command[0]=="play":
        song=command[1]
        # song=sen
        link=library.music[song]
        os.startfile(link)
    elif command[0]=="open":
        app=command[1]
        file=library.apps[app]
        if app=="youtube":
            os.startfile(file)
        else:
            os.system(file)

def google(com):
    phrase=com.replace("search on google","")
    encode=urllib.parse.quote(phrase)
    webbrowser.open(f"https://www.google.com/search?q={encode}")

def chatGPT(com):
    # phrase=com.replace("search on chat gpt","")
    os.system("start shell:AppsFolder\\OpenAI.ChatGPT-Desktop_2p2nqsd0c76g0!ChatGPT")
    time.sleep(5)
    pyautogui.write(com)
    pyautogui.press("enter")

def screenshot():
    with open("number.txt","r") as f:
        i=int(f.read())      
    image=pyautogui.screenshot()
    image.save(f"ss{i}.png")
    i+=1  
    with open("number.txt","w") as f:
        f.write(str(i))

def message(name):
    sentence=com.lower().replace(f"message {name}","")
    os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
    time.sleep(10)
    pyautogui.click(400,166)
    pyautogui.write(name , interval=0.25)
    time.sleep(3)
    pyautogui.click(535,391)
    time.sleep(1)
    pyautogui.click(1030,1023)
    pyautogui.write(sentence,interval=0.25)
    time.sleep(3)
    pyautogui.click(1871,1025)
  
if __name__=="__main__":
    speak("hello sir")
    while True:
        try:
            with sr.Microphone() as source:   
                print("Listening...")
                audio = rcn.listen(source, timeout=3, phrase_time_limit=1)
            word = rcn.recognize_google(audio)
            words=word.lower().split()
            
            if "mercury" in words:
                sk.say("yes sir")
                with sr.Microphone() as source:
                    print("Mercury Active...")
                    audio = rcn.listen(source)
                    com = rcn.recognize_google(audio)  
                    command=com.lower().split()
                    
                    if command[0]=="open" or command[0]=="play":
                        Commands(command)
                    elif command[0]=="search":
                        if command[2]=="google":
                            google(com.lower())
                        elif command[3]=="gpt":
                            chatGPT(com.lower())
                    elif command[1]=="screenshot":
                        screenshot()
                    elif command[0]=="message":
                        n=command[1]
                        message(n)
                        pass
                    else:
                        chatGPT(com.lower())
                with open("history.txt","a+") as f:
                    f.write(word + "\n")
                    f.write(com + "\n")
                
            elif words[0]=="exit":
                break

        except Exception as e:
            pass

        finally:
            speak("thank you")