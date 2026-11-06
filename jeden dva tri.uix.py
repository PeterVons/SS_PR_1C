from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class MojaApp(App):

    

 def build(self) -> GridLayout:
    koren = GridLayout(cols=2)
    koren.add_widget(Button(text="A"))
    koren.add_widget(Button(text="B"))
    koren.add_widget(Button(text="C"))
    koren.add_widget(Button(text="D"))
    return koren
MojaApp().run()