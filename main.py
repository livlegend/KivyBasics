# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon
class DemoApp (MDApp):
    def build(self):
        label=MDLabel(text='Hello word', halign='center', theme_text_color='Secondary',font_style='H1')
        icon_label=MDIcon(icon='language-python')
        return icon_label

DemoApp().run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
