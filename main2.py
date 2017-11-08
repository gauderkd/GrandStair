# This is an attempt at implementing screen changes
import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

# # Defining multiple screens to be used throughout experiment. 
# # This way, different elements/buttons can be shown/have different functions.
class IntroScreen(Screen):
    pass

class ExitScreen(Screen):
    pass

class MyScreenManager(ScreenManager):
	pass

root_widget = Builder.load_file("main2.kv")

class ScreenManagerApp(App):
    def build(self):
        return root_widget

ScreenManagerApp().run()