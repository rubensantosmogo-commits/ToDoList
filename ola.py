from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.widget import MDWidget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.screenmanager import ScreenManager, Screen


class MyApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')
        button = MDFlatButton(text='Hello, World!', on_release=self.on_button_press, halign='center')
        layout.add_widget(button)
        text_field = MDTextField(hint_text='Enter text here', on_text=self.on_text_change)
        layout.add_widget(text_field)
        return layout

    def on_button_press(self, instance):
        print("Button pressed!")
        button1 = MDFlatButton(text='Hello, World!', on_release=self.on_button_press, halign='right')
        self.root.add_widget(button1)
        self.root.remove_widget(instance)

    def on_text_change(self, instance, value):
        print(f'Text changed: {value}')

if __name__ == '__main__':
    MyApp().run()

