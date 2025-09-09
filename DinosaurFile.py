import pyautogui as pag
import keyboard as kb
import getpixelcolor as gpc
import time as t


def short_jump():
    #Presses the space bar to make the dinosaur jump
    kb.press('space')
    kb.release('space')

def long_jump():
    #Presses and holds the space bar to make the dinosaur jumpa bit higher.
    kb.press('space')
    t.sleep(.05)
    kb.release('space')

def duck():

    #Presses the down arrow key to duck the dinosaur.
    kb.press('down')
    t.sleep(.25)
    kb.release('down')

