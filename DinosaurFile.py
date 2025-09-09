import pyautogui as pag
import keyboard as kb
import getpixelcolor as gpc
import time as t

#Time the space bar is held down for each duck
duckTime = .4
#Time the space bar is held down for the jump
jumpHoldTime = .1
#How much less time a key will be held down for
TimeDecrease = 0.05

def short_jump():
    #Presses the space bar to make the dinosaur jump
    kb.press('space')
    kb.release('space')

def long_jump(mult=0):
    #Presses and holds the space bar to make the dinosaur jumpa bit higher.
    kb.press('space')
    t.sleep(jumpHoldTime - (mult * TimeDecrease))
    kb.release('space')

def duck(mult=0):
    #Presses the down arrow key to duck the dinosaur.
    kb.press('down')
    t.sleep(duckTime - (mult * TimeDecrease))
    kb.release('down')



