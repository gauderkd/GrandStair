# TODO: How do we have Kivy run alongside our python function?

import os
from random import shuffle
import csv

keys = ['a', 'bb', 'b', 'c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab']

def play_stim(stimulus):
	print(stimulus)
	# pg.mixer.music.load(stimulus)
	# pg.mixer.music.play()

	# while pg.mixer.music.get_busy():
	# 	pg.time.wait(50)

def play_stim_set(stimulus_list):
	for stim in stimulus_list:
		play_stim(stim)

def generate_stim_name(key_1, key_2, time, events, IOI):
	# time in seconds

	# Convert inputs to strings
	time = str(time)
	events = str(events)
	IOI = str(IOI)

	# Make sure inputs have leading identiy character
	if time[0] is not "t":
		time = "t" + time
	if events[0] is not "e":
		events = "e" + events
	if IOI[0] is not "i":
		IOI = "i" + IOI

	stimulus = "stim_" + key_1 + "_" + key_2 + "_" + time + "_" + events + "_" + IOI + ".mid"
	return stimulus.lower()

def generate_probe_name(tone):
	probe = "probe_" + tone + ".mid"
	return probe

def generate_pilot1_list():
	list_of_stimuli = []
	list_of_probes = []

	time = 't5'
	events = 'e5'
	IOI = 'i5'

	for i, key in enumerate(keys):
		next_key_index = (i+4)%2
		next_key = keys[next_key_index]

		stimuli1_name = generate_stim_name(key, next_key, time, events, IOI)
		stimuli2_name = generate_stim_name(key, 'whole', time, events, IOI)
		probe_name = generate_probe_name(key)

		list_of_stimuli.append([stimuli1_name, key, next_key, time, events, IOI])
		list_of_stimuli.append([stimuli2_name, key, 'whole', time, events, IOI])
		list_of_probes.append([probe_name, key])
	return list_of_stimuli, list_of_probes

def generate_random_stimuli_set():
	stimuli, probes = generate_pilot1_list()

	stim_master = [[],[],[],[],[],[],[],[],[]] # stim_name, probe_name, key1, key2, time, events, IOI, probe_key
	# col1 = index, col2 = stimulus name, col3 = probe name

	index = 0
	for s in stimuli:
		for p in probes:
			stim_master[0].append(index)
			stim_master[1].append(s[0])
			stim_master[2].append(p[0])
			for i in range(3,8):
				stim_master[i].append(s[(i-3)+1])
			stim_master[8].append(p[1])

			index += 1
	shuffle(stim_master[0])

	# You can use the following snippet to present stimuli from this list
	# for i in stim_master[0]:
	# 	print(stim_master[1][i], stim_master[2][i])

	return stim_master

###

def create_csv_of_stimuli():
	stim_master = generate_random_stimuli_set()
	
	with open('stimuli_list.csv', 'a', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Random_index','Stimuli_name', 'Probe_name', 'Key_1', 'Key_2', 'Time', 'Events', 'IOI', 'Proke_key'])

		for i in range(0, len(stim_master[0])):

			row = []
			for stim in stim_master:
				row.append(stim[i])
			writer.writerow(row)
	print('file saved!')
