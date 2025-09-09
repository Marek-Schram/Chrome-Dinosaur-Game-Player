import pyautogui as pag
import keyboard as kb
import getpixelcolor as gpc
import time as t

duckTime = .4
jumpHoldTime = .1

def short_jump():
    #Presses the space bar to make the dinosaur jump
    kb.press('space')
    kb.release('space')

def long_jump(mult=1):
    #Presses and holds the space bar to make the dinosaur jumpa bit higher.
    kb.press('space')
    t.sleep(jumpHoldTime * mult)
    kb.release('space')

def duck(mult=1):
    #Presses the down arrow key to duck the dinosaur.
    kb.press('down')
    t.sleep(duckTime * mult)
    kb.release('down')



