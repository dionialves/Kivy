import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label


class PrimeiroApp(App):

    def build(self):
        return Label(text='Hello world')


PrimeiroApp().run()
