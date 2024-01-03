import pyautogui as pag
from functions import make_screenshot, is_left_log, is_right_log
from Constants import logs, LEFT_LOG, RIGHT_LOG
from Position import Position
from Rectangle import Rectangle
import time


pag.moveTo(LEFT_LOG.get_pos())
time.sleep(2)

for i in range(5):
    make_screenshot()
    if i != 0:
        for j in range(0, 8, 2):
            time.sleep(0.1)
            if steps[j] == 0:
                pag.press('right')
                print(1)
            elif steps[j+1] == 0:
                pag.press('left')
                print(2)
            elif not is_left_log(LEFT_LOG.get_pos()):
                pag.press('left')
                print(3)
            else:
                pag.press('right')
                print(4)
    steps = []
    for j in range(8):
        if j % 2 == 0:
            if not is_left_log(logs[j]):
                steps.append(1)
            else:
                steps.append(0)
        elif j % 2 != 0:
            if not is_right_log(logs[j]):
                steps.append(1)
            else:
                steps.append(0)
    print(steps)
