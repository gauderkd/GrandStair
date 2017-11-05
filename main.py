import kivy
kivy.require('1.10.0') # ToDo: Update

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Controller(BoxLayout):
	def __init__(self):
		super(Controller, self).__init__()

	def new_thickness(self, *args):
		self.lbl.text = str(int(args[1]))

class GrandStairApp(App):
    def build(self):
    	return Controller()

if __name__ == '__main__':
    GrandStairApp().run()