from kivy.app import App # You always need an App
from kivy.uix.button import Button # Widget Button
from kivy.uix.widget import Widget

class GameScreen(Widget):
    pass

class KivyBasicsApp(App): # Make an subclass of App, always. You can call it whatever you want, but preferably end it with App.
    def build(self): # Need build to return a widget all the time. 
        return GameScreen()

if __name__ == "__main__":
    KivyBasicsApp().run() # This is just how you would run it.