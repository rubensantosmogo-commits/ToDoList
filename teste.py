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
from kivymd.app import MDApp
import os
import sqlite3

class MainWindow(Screen):

    def logger(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        username = self.ids.user.text
        password = self.ids.password.text
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        if result:
            self.ids.welcome_label.text = f"Welcome, {username}!"
            self.manager.current = "second"
            self.manager.transition.direction = "left" 
        else:
            self.ids.welcome_label.text = "Invalid username or password"
        conn.close()

    def clear(self):
        self.ids.user.text = ""
        self.ids.password.text = ""
        self.ids.welcome_label.text = "Welcome"
    
    def register(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        username = self.ids.user.text
        password = self.ids.password.text
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            self.ids.welcome_label.text = f"User {username} registered successfully!"
        except sqlite3.IntegrityError:
            self.ids.welcome_label.text = "Username already exists!"
            
        conn.close()
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

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')
        conn.commit()
        conn.close()
        
        return Builder.load_file("new_window.kv")

if __name__ == '__main__':
    MainApp().run()