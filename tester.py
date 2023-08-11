import pyautogui

def teste():
    mouseX,mouseY = pyautogui.position()
    print(mouseX,",",mouseY)

def mover(x,y):
    pyautogui.moveTo(x,y)
if __name__ == "__main__":
    teste()
    # mover(674,467)