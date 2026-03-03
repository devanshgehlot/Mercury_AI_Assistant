import pyautogui
import library

# i=library.a()
# print(i)
def screenshot():
    with open("number.txt","r") as f:
        i=int(f.read())
        
    image=pyautogui.screenshot()
    image.save(f"ss{i}.png")
    i+=1
    
    with open("number.txt","w") as f:
        f.write(str(i))

screenshot()