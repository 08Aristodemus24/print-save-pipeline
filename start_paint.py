from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from subprocess import PIPE, Popen
import keyboard

while True:
    event = keyboard.read_event()
    print(event.name)

    # # if print screen already detected once stop loop
    # flag = True if event.name == 'print screen' else False

    if event.event_type == keyboard.KEY_DOWN and event.name == 'print screen':
        p = Popen(["C:/Windows/System32/mspaint.exe"], stdin=PIPE, shell=True)
        desk_app = Desktop(backend="uia")
        paint = desk_app['Paint']
        paint.wait('ready')
        send_keys('^V^S')




