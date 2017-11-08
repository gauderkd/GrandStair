# This is an attempt at implementing screen changes
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty, ObjectProperty


from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand') #removes multitouch simulation

from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

from intervening_key import * # loads functions for experiment

# # Defining multiple screens to be used throughout experiment. 
# # This way, different elements/buttons can be shown/have different functions.
class IntroScreen(Screen):
    pass

class ResponseScreen(Screen):
	def __init__(self, **kwargs):
		super(ResponseScreen, self).__init__(**kwargs)

	def slide_response(self, *args):
		self.response = round(args[1], 1)
		print(self.response) # Proves that we have access to this number!
		self.response_made = True

class ExitScreen(Screen):
	def on_enter(self): # This code will run when exit screen is entered!
		print('in exit screen') 

class MyScreenManager(ScreenManager):
	trial = NumericProperty(0) # keeps track of current trial #
	trial_index = NumericProperty(0) # the stimulus index for the current trial (part of randomness)
	stimulus = StringProperty() # Stimulus file name
	probe = StringProperty() # Probe file name
	response = NumericProperty(0) # Participant Response, from Slider
	response_made = ObjectProperty(False) # checks if response has been made

	stim_master = ObjectProperty(generate_random_stimuli_set())

	pass

root_widget = Builder.load_file("main3.kv")

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()