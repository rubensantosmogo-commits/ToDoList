from kivymd.app import App
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import MDWidget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.factory import Factory
import os

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

Factory.register('MainWindow', cls=MainWindow)
Factory.register('SecondWindow', cls=SecondWindow)
Factory.register('ThirdWindow', cls=ThirdWindow)
Factory.register('WindowManager', cls=WindowManager)

kv_path = os.path.join(os.path.dirname(__file__), 'new_window.kv')
kv = Builder.load_file(kv_path)

class TesteApp(App):
    def build(self):
        return kv
    
if __name__ == '__main__':
    TesteApp().run()