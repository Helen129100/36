# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.equation = TextInput(font_size=40, multiline=False)
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.equation)

        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["C", "0", "=", "+"],
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current = self.equation.text
        if instance.text == "C":
            self.equation.text = ""
        elif instance.text == "=":
            try:
                self.equation.text = str(eval(current))
            except Exception as e:
                self.equation.text = "Error"
        else:
            self.equation.text = current + instance.text


if __name__ == "__main__":
    CalculatorApp().run()
