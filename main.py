# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.label import MDLabel,MDIcon
from kivymd.uix.button import MDRectangleFlatButton

class DemoApp (MDApp):
    def build(self):
        self.theme_cls.primary_palette="Blue"
        self.theme_cls.primary_hue = "200"
        screen = Screen()
        screen.add_widget(
            MDRectangleFlatButton(text='Hello People',
                                  pos_hint={"center_x":0.5,"center_y":0.5})
        )
        return screen

DemoApp().run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
