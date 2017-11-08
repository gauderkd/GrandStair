import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, StringProperty, ObjectProperty

from intervening_key import *

stim_master = generate_random_stimuli_set()


class SubmitButton(Button):
	pass

class Controller(BoxLayout):
	trial = NumericProperty(0) # keeps track of current trial #
	trial_index = NumericProperty(0) # the stimulus index for the current trial (part of randomness)
	stimulus = StringProperty() # Stimulus file name
	probe = StringProperty() # Probe file name
	response = NumericProperty(0) # Participant Response, from Slider
	response_made = ObjectProperty(False) # checks if response has been made

	def __init__(self):
		super(Controller, self).__init__()
		self.lbl.text = "Welcome to the experiment. Please Press the button to start!"

	def slide_response(self, *args):
		self.response = round(args[1], 1)
		self.response_made = 1
		self.lbl.text = str(self.response)

	def run_trial(Self):
		self.lbl.text = "Trial #" + str(self.trial)
		self.trial_index = stim_master[0][self.trial]
		self.stimulus = stim_master[1][self.trial_index]
		self.probe = stim_master[2][self.trial_index]
		play_stim_set([self.stimulus, self.probe])

	def increase_trial(self):
		if self.response_made is True:
			self.trial += 1
			self.response_made = False

class GrandStairApp(App):
    def build(self):
    	self.title = "GrandStair"

    	return Controller()    	

if __name__ == '__main__':
    GrandStairApp().run()