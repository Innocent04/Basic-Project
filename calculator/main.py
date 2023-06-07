from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    solution = ObjectProperty(None)

    def on_button_press(self, button):
        if button.text == "C":
            self.solution.text = ""
        elif button.text == "=":
            self.solution.text = str(eval(self.solution.text))
        else:
            self.solution.text += button.text

if __name__ == "__main__":
    CalculatorApp().run()