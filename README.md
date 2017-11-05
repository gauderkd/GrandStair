# GrandStair

Experiment using a two up, one down version of the staircase method.
Stimuli are midi files separated into different folders by Block number 
input through a GUI at the beggining of the experiment.

## TODO

* Design & create a new front end using Kivy. Psychopy is overkill 
for the needs of this project
* There is no consistant way of dealing with hitting either the roof 
or the bottom of the staircase (when participant is too good or 
too impaired and goes beyond the stimuli available). This experiment 
sets the boundary but allows the experiment to continue.
* Set the correct kivy version requirement
* Enable saving/exporting to database

## Dependencies
* kivy
* pygame
