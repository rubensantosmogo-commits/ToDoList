from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

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
        return Builder.load_file("login.kv")
    def logger(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=?", (self.root.ids.user.text, self.root.ids.password.text))
        result = c.fetchone()
        if result:
            self.root.ids.welcome_label.text = f"Welcome, {self.root.ids.user.text}!"   
        else:
            self.root.ids.welcome_label.text = "Invalid username or password"
        conn.close()

    def clear(self):
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""
        self.root.ids.welcome_label.text = "Welcome"
    
    def register(self):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (self.root.ids.user.text, self.root.ids.password.text))
        conn.commit()
        conn.close()
        self.root.ids.welcome_label.text = f"User {self.root.ids.user.text} registered successfully!"


MainApp().run()