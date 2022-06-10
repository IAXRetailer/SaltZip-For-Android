import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label

class SaltZip(App):

    def build(self):
        return Label(text='Hello world')

if __name__ == '__main__':
    SaltZip().run() # 译者注：这里就是运行了。
