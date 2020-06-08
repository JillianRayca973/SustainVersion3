
import kivy
from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.lang import Builder
from Heartbeatsensot import hearbeatsensot
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ListProperty
from kivy.uix.widget import Widget
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.effectwidget import EffectWidget
from database import DataBase
from Heartbeatsensot import hearbeatsensot

class ShadowLabel(Label):
    decal = ListProperty([0, 0])
    tint = ListProperty([1, 1, 1, 1])

class CustomPopup(Popup):
    pass

class CustomAbout(Popup):
    pass

class CustomPrivacy(Popup):
    pass

class CustomTerms(Popup):
    pass


class IndexWindow(Screen):
    title = ObjectProperty(None)
    logn = ObjectProperty(None)
    getstart= ObjectProperty(None)
    help = ObjectProperty(None)
    about = ObjectProperty(None)
    privacy = ObjectProperty(None)
    terms = ObjectProperty(None)
    closepopup1 = ObjectProperty(None)
    closepopup2 = ObjectProperty(None)
    closepopup3 = ObjectProperty(None)
    closepopup4 = ObjectProperty(None)

    LabelBase.register(name= "Antique Olive Regular",
        fn_regular="Antique Olive Regular.ttf"
            )

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)

    def popup_about(self):
        popup = CustomAbout()
        popup.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)

    def popup_privacy(self):
        popup_privacy = CustomPrivacy()
        popup_privacy.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)


    def popup_terms(self):
        popup_terms = CustomTerms()
        popup_terms.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)



    def login(self):
        sm.current = "login"

    def createBtn(self):
        sm.current = "create"

class CreateAccountWindow(Screen):
    title = ObjectProperty(None)
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    image = ObjectProperty(None)
    help = ObjectProperty(None)
    about = ObjectProperty(None)
    privacy = ObjectProperty(None)
    terms = ObjectProperty(None)
    closepopup1 = ObjectProperty(None)
    closepopup2 = ObjectProperty(None)
    closepopup3 = ObjectProperty(None)
    closepopup4 = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)

    def popup_about(self):
        popup = CustomAbout()
        popup.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)

    def popup_privacy(self):
        popup_privacy = CustomPrivacy()
        popup_privacy.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)


    def popup_terms(self):
        popup_terms = CustomTerms()
        popup_terms.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)


class LoginWindow(Screen):
    title = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    help = ObjectProperty(None)
    about = ObjectProperty(None)
    privacy = ObjectProperty(None)
    terms = ObjectProperty(None)
    closepopup1 = ObjectProperty(None)
    closepopup2 = ObjectProperty(None)
    closepopup3 = ObjectProperty(None)
    closepopup4 = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""

    def open_popup(self):
        the_popup = CustomPopup()
        the_popup.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)

    def popup_about(self):
        popup = CustomAbout()
        popup.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)

    def popup_privacy(self):
        popup_privacy = CustomPrivacy()
        popup_privacy.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)


    def popup_terms(self):
        popup_terms = CustomTerms()
        popup_terms.open()
        self.pscroll = ScrollView(do_scroll_x=False)
        self.pscroll = ScrollView(do_scroll_y=True)


class MainWindow(Screen):

    BPM_string = StringProperty('BPM: Not Detected')

    def on_enter(self, *args):
        Thread(target=hearbeatsensot, args=(self,)).start()



    def on_enter(self, *args):
        self.__init__()
        pass

class ScreenManagement(ScreenManager):
    pass



class WindowManager(ScreenManager):
    pass


def invalidLogin():
    pop = Popup(content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")

screens = [IndexWindow(name="original"), LoginWindow(name="login"), CreateAccountWindow(name="create"),MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "original"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()