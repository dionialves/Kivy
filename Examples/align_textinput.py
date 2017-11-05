import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require('1.10.0')

main_widget_kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

FloatLayout:
    TextInput:
        text: "Alinhamento normal"
        multiline: False
        size_hint: .8, None
        height: 33
        pos_hint: {"center_x": .5, "center_y": .6}
    TextInput:
        text: "Alinhamento Centralizado"
        multiline: False
        size_hint: .8, None
        height: 33
        pos_hint: {"center_x": .5, "center_y": .5}
        padding_x:
            (self.width - self._get_text_width((self.text), self.tab_width, self._label_cached)) / 2
    TextInput:
        text: "Alinhamento à direita"
        multiline: False
        size_hint: .8, None
        height: 33
        pos_hint: {"center_x": .5, "center_y": .4}
        padding_x:
            [(self.width-6) - (self._get_text_width((self.text*2), self.tab_width, self._label_cached)) / 2.0, 0]
"""


class AlingApp(App):
    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        return main_widget


AlingApp().run()

