from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
import qrcode
import plyer
Window.size = (360, 640)

class Function(ScreenManager):
    def generate_qr_code(self, root):
        if self.ids.link_text.text != '' and self.ids.image_name.text != '':
            code = qrcode.QRCode(version=1.0, box_size=15, border=4)
            code.add_data(self.ids.link_text.text)
            code.make(fit=True)
            img = code.make_image(fill='Black', back_color = 'White')
            img.save(f'{self.ids.image_name.text}.png')
            plyer.notification.notify(
                title = 'QR Code  Generator',
                message = 'QR code generated'
            )
        else:
            plyer.notification.notify(
                title = 'QR Code  Generator',
                message = 'Type some in the text fields'
            )


    def view_image(self, root):
        self.ids.img_.source = f"{self.ids.image_name.text}.png"
        root.current = "image"

    def make_another(self, root):
        self.ids.link_text.text = " "
        self.ids.image_name.text = " "
        root.current = "first"

class Main(MDApp):
    Builder.load_file('layout.kv')
    def build(self):
        return Function()
    

Main().run()