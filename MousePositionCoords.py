import pyautogui
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print (positionStr + "\r", end="", sep="", flush=True)
except KeyboardInterrupt:
    exit()