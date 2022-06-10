import kivy

kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from kivy.core.text import LabelBase
LabelBase.register(name='Han_Font',fn_regular='./fonts/b.ttf')
Builder.load_file("main.kv")
class WarningPopup(Popup):
    def __init__(self, parent_inst, *args,  **kwargs):
        super(WarningPopup, self).__init__(*args, **kwargs)
        self.parent_inst = parent_inst
class ChoseFile(BoxLayout):
    def __init__(self, *args, **kwargs):
        super(ChoseFile, self).__init__(*args, **kwargs)
        self.orientation = "vertical"
        self.fichoo = FileChooserListView(font_name="Han_Font")
        self.popup = WarningPopup(self)
        btn_delete = Button(text="Chose file", on_release=self.popup.open, size_hint_y=0.1,font_name="Han_Font")

        self.add_widget(self.fichoo)
        self.add_widget(btn_delete)

    def selete(self, *args):
        pass
class SaltZip(App):
    def build(self):
        return ChoseFile()

if __name__ == '__main__':
    SaltZip().run()
