import kivy
from kivy.app import App
from kivy.uix.label import Label

kivy.require('1.10.0')


class PrimeiroApp(App):

    def build(self):
        return Label(text='Hello world')


PrimeiroApp().run()
