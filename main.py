from PIL.ImageOps import grayscale
from pyautogui import *
import pyautogui
import time
import keyboard
import win32api
import win32con
from pynput.mouse import Controller


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


counter = 0
while keyboard.is_pressed('q') == False:
    addEmojiButton = pyautogui.locateOnScreen(
        'add_emoji_button.png', grayscale=True)
    counter = counter+1
    if addEmojiButton != None:
        print('Sticker: ', counter)
        click(addEmojiButton.left, addEmojiButton.top)
        time.sleep(0.08)
        blankEmoji = pyautogui.locateOnScreen(
            'blank_emoji.png')
        if blankEmoji != None:
            click(blankEmoji.left, blankEmoji.top)

    else:
        Controller().scroll(0, -3)
        click(50, 200)
        time.sleep(0.1)
