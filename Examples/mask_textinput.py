import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

kivy.require('1.10.0')

main_widget_kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

FloatLayout:
    CpfTextInput:
        multiline: False
        size_hint: .8, None
        height: 33
        pos_hint: {"center_x": .5, "center_y": .5}
"""


class CpfTextInput(TextInput):

    def insert_text(self, substring, from_undo=False):
        s = substring

        if len(self.text) < 13:
            self.text = self.text.replace('.', '')

            if len(self.text) > 8:
                self.text = self.text[:9] + '.' + self.text[9:]
                self.text = self.text[:6] + '.' + self.text[6:]
                self.text = self.text[:3] + '.' + self.text[3:]
            elif len(self.text) > 5:
                self.text = self.text[:6] + '.' + self.text[6:]
                self.text = self.text[:3] + '.' + self.text[3:]
            elif len(self.text) > 2:
                self.text = self.text[:3] + '.' + self.text[3:]

        else:
            self.text = self.text[:13]
        return super(CpfTextInput, self).insert_text(s, from_undo=from_undo)


class AlingApp(App):
    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        return main_widget


AlingApp().run()

