from turtle import onrelease
import kivy
kivy.require('2.1.0')
from kivy.uix.filechooser import FileChooserListView
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDLabel
from kivymd.uix.button import MDFlatButton
from kivy.uix.popup import Popup
from kivy.lang.builder import Builder
from library.Core.Hash import des
from library.Core.Zip import zip as Izip
from library.Core.Bitlayer import BitString
from os.path import dirname,exists
from kivy.core.text import LabelBase
#from kivy.core.text import 
from kivy.utils import platform
from kivymd.app import MDApp
from kivymd.toast import toast
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE
        ])
LabelBase.register(name='Han_Font',fn_regular='./fonts/b.ttf')

Builder.load_file("main.kv")

class NotChosePopupBox(Popup):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class FailPopupBox(Popup):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

class FinishPopupBox(Popup):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
class StartPopup(Popup):
    def __init__(self, *args,  **kwargs):
        super(StartPopup, self).__init__(*args, **kwargs)
    def selete(self, *args):
        ChoseFile()
class WarningPopup(Popup):
    def __init__(self, parent_inst, *args,  **kwargs):
        super(WarningPopup, self).__init__(*args, **kwargs)
        self.parent_inst = parent_inst
class ChoseFile(MDBoxLayout):
    def __init__(self, *args, **kwargs):
        super(ChoseFile, self).__init__(*args, **kwargs)
        from plyer import filechooser
        #self.fichoo = FileChooserListView(font_name="Han_Font")
        #self.popup = WarningPopup(self)
        #btn_delete = MDFlatButton(text="选择文件", on_release=self.popup.open, size_hint_y=0.1,font_name="Han_Font")
        try:
            path = filechooser.open_file()[0]
            toast(path)
            self.selete(path)
        except:
            return
        #self.add_widget(self.fichoo)
        #self.add_widget(btn_delete)

    def selete(self,path, *args):
        try:
            hkpath=path
        except:
            FailPopupBox().open()
            pass
        if ".zip" in hkpath:
            try:
                Izip.unzip(hkpath,None,dirname(hkpath))
                FinishPopupBox().open()
            except:
                FailPopupBox().open()
            return
        if ".rar" in hkpath:
            try:
                Izip.unrarfile(hkpath,dirname(hkpath))
                FinishPopupBox().open()
            except:
                FailPopupBox().open()
            return
        if ".hk" in hkpath:
            try:
                con=open(hkpath,"r").read()
                filepath=hkpath.replace(".hk",".sip")
                if not exists(filepath):
                    filepath.replace(".sip",".zip")
                con=con.replace("saltzip://","")
                conlist=con.split("|")
                chuck1,chuck2,chuck3=conlist[0],conlist[1],conlist[2]
                chuck3=des.b64d(chuck3).split("/!")
                chuck2=des.b64d(chuck2).split("/!")
                password=des.decodeStringhash(chuck1,chuck2[0],chuck2[1])
                Izip.unzip(filepath,password,dirname(filepath))
                FinishPopupBox().open()
            except:
                FailPopupBox().open()
        elif ".h2k" in hkpath:
            try:
                con=open(hkpath,"rb").read()
                lenstr=hkpath.replace(".h2k","").split(".")[-1]
                res=BitString.readrbtostring(hkpath,int(lenstr)+64+10)
                password=des.decodeStringhash(res[:32],res[32:40],res[40:48])
                dictory=dirname(hkpath)
                unfilepath=hkpath.replace(lenstr+".h2k","sip")
                Izip.unzip(unfilepath,password,dictory)
                FinishPopupBox().open()
            except:
                FailPopupBox().open()
        else:
            NotChosePopupBox().open()

class SaltZip(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return ChoseFile()

if __name__ == '__main__':
    SaltZip().run()
