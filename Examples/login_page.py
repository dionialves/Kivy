from kivy.app import App
from kivy.lang import Builder

main_widget_kv = """
#:import get_color_from_hex kivy.utils.get_color_from_hex

FloatLayout:
    canvas.before:
        Color:
            rgba: get_color_from_hex('#D3D4D5')
        Rectangle:
            pos: self.pos
            size: self.size
    Image:
        size_hint: .3, .3
        pos_hint: {"center_x": .5, "center_y": .75}
        source: 'data/img/kivy-logo.png'
    Label:
        id: msg
        size_hint: .7, .1
        pos_hint: {"center_x": .5, "center_y": .55}
        text:
    GridLayout:
        cols: 1
        spacing: 5
        size_hint: .7, .37
        pos_hint: {"center_x": .5, "center_y": .3}

        Label:
            text: "Usuário"
            size_hint_x: .3
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: get_color_from_hex('#000000')
        TextInput:
            id: usuario
            multiline: False
        Label:
            text: "Senha"
            size_hint_x: .3                
            text_size: self.size
            halign: 'left'
            valign: 'middle'
            color: get_color_from_hex('#000000')
        TextInput:
            id: senha
            multiline: False
            password: True
        Label:
        Button:
            size_hint: 1., 1.
            text: "Login"
            on_release: app.login()
"""


class LoginApp(App):

    def build(self):
        main_widget = Builder.load_string(main_widget_kv)
        return main_widget

    def login(self):
        usuario = self.root.ids.usuario.text
        senha = self.root.ids.senha.text

        # Implemesta regras para acesso. Exemplo:
        if usuario == 'admin' and senha == 'admin':
            pass


LoginApp().run()
