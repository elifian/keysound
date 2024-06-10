# keysound
---
Plays 1 of 3 randomly selected sounds when a key is pressed on the keyboard

Воспроизводит 1 из 3 случайно выбранных звуков при нажатии клавиши на клавиатуре

---
## Compilation
Requires: pygame, pynput, pyinstaller

Требуется: pygame, pynput, pyinstaller

pyinstaller --onefile --add-data "mouse1.mp3;." --add-data "mouse2.mp3;." --add-data "mouse3.mp3;." --icon=icon.ico --noconsole keysound.py
