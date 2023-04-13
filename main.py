from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang.builder import Builder
from start_page import StartPage
from connexion_page import ConnexionPage
from home_page import HomePage
from kivymd.uix.label import MDLabel


class PhonePage(MDScreen):

    pass


class GpsPage(MDScreen):
    pass


class MusicPage(MDScreen):
    pass


class VideoPage(MDScreen):
    pass


class SettingsPage(MDScreen):
    pass


class MessagePage(MDScreen):
    def display_chat(self):
        self.ids.chat.clear_widgets()
    pass


class App(MDApp):

    default_text_color = "#C9C5C5"
    default_bg_color = "#0F0332"
    default_bar_color = "#39585B"

    def build(self):
        Window.size = [836, 584]
        self.title = "LIION ASSIST"
        self.load_all_kv_files()
        self.sm = ScreenManager(transition=SlideTransition())

        screens = [
            MessagePage(name='message'),
            StartPage(name='LIION'),
            ConnexionPage(name='CONNECTION'),
            HomePage(name='home'),
            PhonePage(name='phone'),
            GpsPage(name='gps'),
            MusicPage(name='music'),
            VideoPage(name='video'),
            SettingsPage(name='settings')
        ]
        for screen in screens:
            self.sm.add_widget(screen)
        self.load_chatlist()

        return self.sm

    def on_start(self):
        Clock.schedule_once(self.toscreen1, 3)

    def load_discussion(self):
        w = Builder.load_string("""
MDLabel:
    text: 'good job'
""")
        self.sm.screens[0].ids.chat.add_widget(w)

    def change_screen(self, screen):
        self.sm.current = screen

    def toscreen1(self, *args):
        # self.sm.current = 'CONNECTION'
        pass

    def load_chatlist(self):
        w = []
        for i in range(50):
            w.append(Builder.load_string("""
#:import get_color_from_hex kivy.utils.get_color_from_hex

MDCard:
    on_press: app.load_discussion()
    size_hint: 0.9, None
    height: 85
    pos_hint: {'center_x': 0.5}
    md_bg_color: 1, 1, 1, 0
    MDBoxLayout:
        orientation: 'vertical'
        MDBoxLayout:
            orientation: 'horizontal'
            md_bg_color: get_color_from_hex("#C7C7C7")
            radius: 15
            MDBoxLayout:
                size_hint_x: None
                width: 10
            MDAnchorLayout:
                size_hint: None, None
                size: 60, 60
                radius: 30
                pos_hint: {'center_y': 0.5}
                md_bg_color: 1, 2, 3, 1
                MDLabel:
                    text: 'P'
                    font_size: 20
                    valign: 'middle'
                    halign: 'center'
            MDBoxLayout:
                size_hint_x: None
                width: 20
            MDBoxLayout:
                orientation: 'vertical'
                MDBoxLayout:
                    size_hint_y: 1.7
                    MDLabel:
                        text: 'Papa'
                        anchor: 'left'
                        font_size: 25
                    MDLabel:
                        text: '07:50'
                        halign: 'right'
                        font_size: 12
                MDBoxLayout:
                    MDLabel:
                        text: 'je vais bien'
                        anchor: 'left'
                        font_size: 12
                        color: get_color_from_hex("#4E4C4C")
        MDBoxLayout:
            size_hint_y: None
            height: 10
            """))
            self.sm.screens[0].ids.chatlist.add_widget(w[i])

    def load_all_kv_files(self, **kwargs):
        Builder.load_file('start_page.kv')
        Builder.load_file('connexion_page.kv')
        Builder.load_file('home_page.kv')
        Builder.load_file('phone_page.kv')
        Builder.load_file('gps_page.kv')
        Builder.load_file('music_page.kv')
        Builder.load_file('video_page.kv')
        Builder.load_file('settings_page.kv')
        Builder.load_file('message_page.kv')


if __name__ == "__main__":
    App().run()
