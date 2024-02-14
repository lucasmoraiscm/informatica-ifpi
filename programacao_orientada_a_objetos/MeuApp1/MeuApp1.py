from kivy.app import App
from kivy.core import text
from kivy.uix.label import Label

class HelloApp(App):
    def build(self):
        return Label(text="Hello World!!")

HelloApp().run()