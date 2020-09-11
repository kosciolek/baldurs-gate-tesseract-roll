import keyboard
import webbrowser
def asd():
    webbrowser.open('http://net-informations.com', new=2)

keyboard.add_hotkey('ctrl+shift+a', asd)
keyboard.wait()
