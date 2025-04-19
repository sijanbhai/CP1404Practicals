from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window


class ConvertMilesKmApp(App):
    """App to convert miles to kilometers."""
    output_text = StringProperty("0.0")  # StringProperty for the output label

    def build(self):
        """Build the Kivy app."""
        Window.size = (400, 300)  # Adjust window size for testing
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_conversion(self, miles_text):
        """Convert miles to kilometers and update the output label."""
        try:
            miles = float(miles_text)
            km = miles * 1.60934
            self.output_text = f"{km:.5f}"
        except ValueError:
            self.output_text = "Invalid input"

    def handle_increment(self, miles_text, increment):
        """Increment or decrement the miles value."""
        try:
            miles = float(miles_text)
            miles += increment
            self.root.ids.input_miles.text = str(miles)
        except ValueError:
            self.root.ids.input_miles.text = "0"


if __name__ == '__main__':
    ConvertMilesKmApp().run()
