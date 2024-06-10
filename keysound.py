import pygame
import random
import sys
import os
from pynput import keyboard

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

pygame.init()
pygame.mixer.init()

sounds = [pygame.mixer.Sound(resource_path(f'sound{i}.mp3')) for i in range(1, 4)]
for sound in sounds:
    sound.set_volume(0.2)

key_pressed = False

def play_random_sound():
    random.choice(sounds).play()

def on_press(key):
    global key_pressed
    if not key_pressed:
        key_pressed = True
        play_random_sound()

def on_release(key):
    global key_pressed
    key_pressed = False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()