from intervening_key import *
import os

import pygame_textinput
import pygame
from pygame.locals import *

# This is an implementation using pygame

# # Create stimuli set
stim_master = generate_random_stimuli_set()

# Initialize Pygame
pygame.init()
FPS = 30  # Speed at which the game loops
frames = 18  # Speed of the sprite

def update_text(text_to_draw):
    screen.blit(font.render(text_to_draw, True, (0, 0, 0)), (0, 250))
    # Set up text box
    screen.blit(text, (20, 275))
    screen.blit(textinput.get_surface(), text_loc)


clock = pygame.time.Clock()

# Create text inputs
textinput = pygame_textinput.TextInput()

# Create screen
screen = pygame.display.set_mode((800, 800))

font = pygame.font.SysFont("monospace", 20)
text = font.render(">", True, (0, 0, 0))
text_loc = (50, 275)

done = False
white = Color('white')

done = False
while not done:
    events = pygame.event.get()
    if textinput.update(events):
        owner_name = textinput.get_text()
        textinput.blank_text()
        done = True
    for event in events:
        if event.type == pygame.QUIT:
            done = True
    # Draw screen
    screen.fill(white)
    update_text("Enter your name")
    pygame.display.flip()  # flips screen    

screen.fill(white)
update_text("Hi, " + owner_name)
pygame.display.flip()  # flips screen

pygame.time.wait(1000)

screen.fill(white)
update_text("This is an experiment text. next screen experiment starts.")
pygame.display.flip()  # flips screen

pygame.time.wait(1000)

# Experiment Loop
for i, pair in enumerate(stim_master[0]):  
    # Grab stimulus
    stimulus_name = stim_master[1][pair]
    probe_name = stim_master[2][pair]

    screen.fill(white)
    update_text("Stimulus is playing")
    pygame.display.flip()
    # play_stim_set([stimulus_name, probe_name]) <- NEEDS FILES TO RUN
    print(stimulus_name, probe_name)

    pygame.time.wait(1000)

    screen.fill(white)
    update_text("Input response. stimulus was " + stimulus_name)
    pygame.display.flip()

    done = False
    while not done:
        events = pygame.event.get()
        if textinput.update(events):
            screen.fill(white)
            update_text("recorded!")
            pygame.display.flip()
            done = True



