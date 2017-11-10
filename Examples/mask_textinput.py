import kivy
import re
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

kivy.require('1.10.0')

__version__ = '0.0.3'

main_widget_kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

FloatLayout:
    BoxLayout:
        size_hint: .8, None
        height: 33
        pos_hint: {"center_x": .5, "center_y": .5}
        Label:
            text: 'CPF:'
            size_hint_x: .2
            text_size: self.size
            halign: 'left'
            valign: 'middle'
        CpfTextInput:
            multiline: False
            size_hint_x: 1.

"""


class CpfTextInput(TextInput):

    only_n = re.compile('[^0-9]')

    def insert_text(self, substring, from_undo=False):

        if len(self.text) < 14:
            only_n = self.only_n
            s = re.sub(only_n, '', substring)
            cpf = self.text.replace('.', '')

            if len(cpf) > 8:
                cpf = cpf[:3] + '{0}' + cpf[3:6] + '{0}' + cpf[6:9] + '{1}' + cpf[10:]
                cpf = cpf.format('.', '-')
            elif len(cpf) > 5:
                cpf = cpf[:3] + '{0}' + cpf[3:6] + '{0}' + cpf[6:]
                cpf = cpf.format('.')
            elif len(cpf) > 2:
                cpf = cpf[:3] + '{0}' + cpf[3:]
                cpf = cpf.format('.')

            self.text = cpf
            return super(CpfTextInput, self).insert_text(s, from_undo=from_undo)

        else:
            self.text = self.text[:14]


class AlingApp(App):
    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        return main_widget


AlingApp().run()

