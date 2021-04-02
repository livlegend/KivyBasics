# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.taptargetview import MDTapTargetView

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Mon toolbar"
            left_action_items: [["menu", lambda x: app.callback()]]
        
        
        MDCard:
            orientation: "vertical"
            padding: "8dp"
            size_hint: None, None
            size: "280dp", "180dp"
            halign: "center"
            pos_hint: {"center_x": .5, "center_y": .5}
    
            MDLabel:
                text: "Test de lecture"
                theme_text_color: "Secondary"
                size_hint_y: None
                height: self.texture_size[1]
    
            MDSeparator:
                height: "1dp"
    
            MDLabel:
                text: "Body"
                
        MDFloatingActionButton:
            id: button
            icon: "plus"
            pos: 10, 10
            on_release: app.tap_target_start()
            
'''

class DemoApp (MDApp):
    def build(self):
        screen=Builder.load_string(KV)
        self.tap_target_view = MDTapTargetView(
            widget=screen.ids.button,
            title_text="Lire",
            description_text="Patientez en écoutant la lecture de ce texte",
            widget_position="left_bottom",
        )
        return screen


    def tap_target_start(self):
        if self.tap_target_view.state == "close":
            self.tap_target_view.start()
        else:
            self.tap_target_view.stop()

DemoApp().run()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
