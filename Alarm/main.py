import datetime

import pygame
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

Window.size = (350, 600)

KV = '''
MDFloatLayout:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: 'andrea-de-santis-zwd435-ewb4-unsplash.jpg'
    MDLabel:
        text: "ALARM"
        font_size: "30sp"
        pos_hint:{"center_y": .935}
        halign: "center"
        font_name: "Comic"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        bold: True
    MDIconButton:
        icon: "plus"
        pos_hint:{"center_x": .87, "center_y": .94}
        md_bg_color: 0, 0, 0, 1
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        on_release: app.time_picker()

    MDLabel:
        id: alarm_time
        text: ""
        pos_hint: {"center_y": .2}
        halign: "center"
        font_size: "30sp"
        bold: True
    MDRaisedButton:
        text: "Stop"
        pos_hint: {"center_x": .5, "center_y":  .4}
        on_release: app.stop()

'''

class Alarm(MDApp):

    
    pygame.init()
    sound = pygame.mixer.Sound("alarm.mp3")
    volume = 0

    def build(self):

        # self.theme_cls.primary_palette = "Pink"
        # self.theme_cls.primary_hue = "300"
        # self.theme_cls.theme_style = "Dark"

        return Builder.load_string(KV)
    


    def time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time, on_save=self.schedule)
        time_dialog.open()


    def schedule(self, *args):
        Clock.schedule_once(self.alarm, 1)

    def alarm(self, *args):
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if self.root.ids.alarm_time.text == str(current_time):
                self.start()
                break
    def set_volume(self, *args):
        self.volume += 0.05
        if self.volume < 1.0:
            Clock.schedule_interval(self.set_volume, 10)
            self.sound.set_volume(self.volume)
            print(self.volume)

        else:
            self.sound.set_volume(1)
            print("Reach Maximum Volume!")

    def start(self, *args):
        self.sound.play(-1)
        self.set_volume()

    def stop(self, *args):
        self.sound.stop()
        Clock.schedule(self.set_volume)
        self.volume = 0


    def get_time(self, instance, time):
        self.root.ids.alarm_time.text = str(time)

    

    
Alarm().run()