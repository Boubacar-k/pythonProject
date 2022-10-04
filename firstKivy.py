from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class HelloApp(App):
    def build(self):
        SL = StackLayout(orientation ='lr-tb')

        btn1 = Button(text="B1",font_size=20,size_hint=(.2, .1))
        btn2 = Button(text="B2",font_size=20,size_hint=(.2, .1))
        btn3 = Button(text="B3",font_size=20,size_hint=(.2, .1))
        btn4 = Button(text="B4",font_size=20,size_hint=(.2, .1))
        btn5 = Button(text="B5", font_size=20, size_hint=(.2, .1))
        btn6 = Button(text="B6", font_size=20, size_hint=(.2, .1))
        btn7 = Button(text="B7", font_size=20, size_hint=(.2, .1))
        btn8 = Button(text="B8", font_size=20, size_hint=(.2, .1))
        self.title = 'Hello World!'
        SL.add_widget(btn1)
        SL.add_widget(btn2)
        SL.add_widget(btn3)
        SL.add_widget(btn4)
        SL.add_widget(btn5)
        SL.add_widget(btn6)
        SL.add_widget(btn7)
        SL.add_widget(btn8)
        return SL

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '150')

HelloApp().run()