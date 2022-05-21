from kivy.app import App # You always need an App
from kivy.uix.button import Button # Widget Button

class KivyBasicsApp(App): # Make an subclass of App, always. You can call it whatever you want, but preferably end it with App.
    def build(self): # Need build to return a widget all the time. 
        return Button(
            text="Hello World!",
            pos=(50,50),
            size=(500,500), # Manual sizing
            size_hint=(None,None)) # Automatic size, should be none otherwise manual sizing wont work.


if __name__ == "__main__":
    KivyBasicsApp().run() # This is just how you would run it.