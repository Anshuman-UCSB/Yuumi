import pyautogui

while True:
    try:
        print(pyautogui.position())
    except KeyboardInterrupt:
        print('interrupted!')
