from kivy.app import App
from kivy.uix.label import Label

class Msgr(App):
    def build(self):
        return Label(text="hello from kindmops")

Msgr().run()
