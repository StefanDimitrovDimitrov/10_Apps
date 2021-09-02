
import random
from pathlib import Path


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
import json, glob
from datetime import datetime
from hoverable import HoverBehavior

Builder.load_file('design.kv')


class SignInScreen(Screen):
    def sign_up(self):
        self.manager.current = "sign_up_screen"

    def sign_in(self, uname, pword):
        with open("users.json") as f:
            users = json.load(f)
        if uname in users and users[uname]["password"] == pword:
            self.manager.current = 'sign_in_screen_success'
        else:
            self.ids.sign_in_wrong.text = "Wrong username or password!"


class BootWidget(ScreenManager):
    pass


class SignUpScreen(Screen):

    def add_user(self, uname, pword):
        with open("users.json", ) as file:
            try:
                data = json.load(file)
            except:
                data = {}

        data[uname] = {
            'username': uname,
            'password': pword,
            'created': datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        }
        with open("users.json", "w") as file:
            json.dump(data, file)
            print(f'User named {uname} was added')
        self.manager.current = "sign_up_screen_success"


class SignUpScreenSuccess(Screen):
    def sign_in(self):
        self.manager.transition.direction = 'up'
        self.manager.current = "sign_in_screen"


class SignInScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = "up"
        self.manager.current = "sign_in_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")

        available_feelings = [Path(filename).stem for filename in available_feelings]

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", encoding="utf8", errors='ignore') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.txt = "Try another feeling"

class ImageButton(ButtonBehavior,HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        return BootWidget()


if __name__ == "__main__":
    MainApp().run()
