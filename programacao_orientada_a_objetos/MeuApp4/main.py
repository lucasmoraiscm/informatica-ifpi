import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button


kivy.require('1.9.1')

class Incrementador(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        return Incrementador()


TestApp().run()