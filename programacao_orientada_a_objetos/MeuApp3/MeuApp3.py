import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button
from kivy.uix.layout import Layout

kivy.require('1.9.1')

var=0
def soma_um(instance):
    global var
    var += 1
    instance.text = str(var)

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        layout.add_widget(Label(text='Olá do kivy!'))
        btn = Button(text='Pressione-me!',size=(100,50))

        btn.bind(on_press=soma_um)
        layout.add_widget(btn)
        return layout

MeuApp().run()