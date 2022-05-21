from kivy.app import App # You always need an App
from kivy.uix.button import Button # Widget Button

class FunkyButton(Button):
    # This is a way to set the same attributes to all funky buttons, instead of doing so when returning it on the build method.
    def __init__(self, **kwargs):
        super(FunkyButton, self).__init__(**kwargs)
        self.text="FunkyButton"
        self.pos=(100,100)
        self.size_hint=(.25,.25)


class KivyBasicsApp(App): # Make an subclass of App, always. You can call it whatever you want, but preferably end it with App.
    def build(self): # Need build to return a widget all the time. 
        # return FunkyButton(
        #     text="FunkyButton",
        #     pos=(100,100),
        #     size_hint=(.5,.5),)
        return FunkyButton()


if __name__ == "__main__":
    KivyBasicsApp().run() # This is just how you would run it.