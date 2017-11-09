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

import time

from intervening_key import * # loads functions for experiment

# # Defining multiple screens to be used throughout experiment. 
# # This way, different elements/buttons can be shown/have different functions.
class IntroScreen(Screen):
	pass


class SetupTrialScreen(Screen):
	def on_enter(self):
		# Load local variables
		trial = App.get_running_app().trial
		stim_master = App.get_running_app().stim_master

		# perform functions
		trial_index = stim_master[0][trial]
		stimulus = stim_master[1][trial_index]
		probe = stim_master[2][trial_index]

		self.lbl.text = "Trial #" + str(trial + 1) + ", stimulus = " + str(stimulus)

		# upload local variables into properties
		App.get_running_app().trial_index = trial_index
		App.get_running_app().trial = trial
		App.get_running_app().stimulus = stimulus
		App.get_running_app().probe = probe


class RunTrialScreen(Screen):
	def on_enter(self):
		play_stim_set([App.get_running_app().stimulus, App.get_running_app().probe])

class ResponseScreen(Screen):
	def __init__(self, **kwargs):
		super(ResponseScreen, self).__init__(**kwargs)

	def slide_response(self, *args):
		App.get_running_app().response = round(args[1], 1)
		print(App.get_running_app().response) # Proves that we have access to this number!
		App.get_running_app().response_made = True

	def gotoExit(self):
		if App.get_running_app().response_made is True:
			App.get_running_app().response_made = False
			if App.get_running_app().trial < App.get_running_app().trials_to_run:
				App.get_running_app().trial += 1
				App.get_running_app().root.current = 'setup'
			else:
				App.get_running_app().root.current = 'exit'


class ExitScreen(Screen):
	def on_enter(self): # This code will run when exit screen is entered!
		print('in exit screen') 
		print(App.get_running_app().response) # Note this reference to the app class is an easy way to point to these properties!
		

class MyScreenManager(ScreenManager):
	pass

root_widget = Builder.load_file("main3.kv")

class ScreenManagerApp(App):
	trial = NumericProperty(0) # keeps track of current trial #
	trials_to_run = NumericProperty(4)
	trial_index = NumericProperty(0) # the stimulus index for the current trial (part of randomness)
	stimulus = StringProperty('default') # Stimulus file name
	probe = StringProperty('default') # Probe file name
	response = NumericProperty(0) # Participant Response, from Slider
	response_made = ObjectProperty(False) # checks if response has been made

	stim_master = ObjectProperty(generate_random_stimuli_set())

	def build(self):
		return root_widget

ScreenManagerApp().run()