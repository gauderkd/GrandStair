import os
import pygame
import glob

from random import choice
from psychopy import visual, event, core, gui


def draw_ins(window, word, colour, skipkeys=['space']):
    
    feedback = visual.TextStim(window, text = word, height = 30, color = colour)
    feedback.draw()
    window.flip()
    core.wait(0.2)
    event.waitKeys(keyList=skipkeys)

def draw_exp(window, word, colour):
    
    feedback = visual.TextStim(window, text = word, height = 30, color = colour)
    feedback.draw()
    window.flip()
    core.wait(0.5)

def save_data(part_num, block, trial_num, my_place, StimA, StimB, resp, corr, accuracy):
    if not os.path.exists('FC_data.csv'):
        f = open('FC_data.csv', 'w')
        f.write("Participant, Block, Trial, Place, Stimulus A, Stimulus B, Response, Correct, Accuracy")
        f.close()
    
    trial_text = '\n%s,%s,%s,%s,%s, %s, %s, %s, %s' % (part_num, block, trial_num, my_place, StimA, StimB, resp, corr, accuracy)
    
    f = open('FC_data.csv', 'a')
    f.write(trial_text)
    f.close()

def play_mus(StimA, StimB):
    
    pygame.init()
    
    # StimA
    pygame.mixer.music.load(StimA)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(50)

    core.wait(1)

    # StimB
    pygame.mixer.music.load(StimB)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.wait(50)
    
    pygame.quit()


# Window

WIN = visual.Window(fullscr=False, size = (1000,800), units = 'pix', color = 'black')

# GUI input

myDlg = gui.Dlg(title="2IFC Task", pos=(200, 400))
myDlg.addText('Participant & Block Info', color='Green')
myDlg.addField('Participant Number:', tip="subject number")
myDlg.addField('Block:', tip="experimental block")

myDlg.show()
if myDlg.OK:
    thisinfo = myDlg.data
    print(thisinfo)
    part_num = int(thisinfo[0])
    block = int(thisinfo[1])
else:
    print('user cancelled')
    exit()


# Intro Instructions:

instruction_text = """
Listen to both musical stimuli and
choose which one sounds more correct.

Press %s for the first stimulus.
Press %s for the second stimulus.

Press space to begin.""" % ('j', 'k')

draw_ins(WIN, instruction_text, 'white')


# Draw Instructions During Experiment:

in_exp_text = '''
Listen to both musical stimuli and
choose which one sounds more correct.

Press %s for the first stimulus.
Press %s for the second stimulus.''' % ('j', 'k')

draw_exp(WIN, in_exp_text, 'cyan')


# Settings for the experiment:

trials = 10
my_place = 3
step_size = 1

trial_num = 0
count = 1


# Grand Stair:
# Choses stimuli from files, plays them and records input

for tri in range(trials):

    # Chose stimuli

    stim_ID_A = 0
    stim_ID_B = 0
    exp_block = ''
    StimA = ''
    StimB = ''
    stim_flag = False

    # Chose proper block

    if block == 1:
        exp_block = glob.glob('2IFC_01/*.mid')
    elif block == 2:
        exp_block = glob.glob('2IFC_02/*.mid')
    else:
        print('That block does not exist')
        exit()

    # Chose proper stimuli

    while stim_flag == False:
        try:
            StimA = choice(exp_block)
            stim_ID_A = int(StimA[-6:-4])

            for this_stim in exp_block:
                stim_ID_B = int(this_stim[-6:-4])
                
                if abs(stim_ID_B - stim_ID_A) == my_place:
                    StimB = this_stim
                    stim_flag = True
                    break
        except:
            print('something in the while loop broke')
            stim_flag = True

    # Assign correct key based on the smaller stimulus
    
    if stim_ID_A >= stim_ID_B:
        corr = 'j'
    elif stim_ID_A < stim_ID_B:
        corr = 'k'
    else:
        print("Can't find a correct key!")
        exit()

    # Play stimuli

    play_mus(StimA, StimB)


    # Get response, check accuracy, save

    trial_num += 1
    
    resp = event.waitKeys(keyList = ['j', 'k', 'q'])
    if corr in resp:
        accuracy = 1
    else:
        accuracy = 0

    print(trial_num, block, count, my_place, resp) # Actually a good indicator that a key press was registered!
    
    save_data(part_num, block, trial_num, my_place, StimA, StimB, resp, corr, accuracy)


    # Adjust next stimulus presentation according to response

    if 'q' in resp:
        print('Participant quit prematurely')
        exit()

    elif corr in resp and count > 1.5:
        my_place += step_size
        count = 1
        if my_place >= 6:
            my_place = 5    #So you can't go beyond the stimuli available
    elif corr in resp and count < 1.5:
        count += 1
    else:
        my_place -= step_size
        count = 1


# End Experiment:

finish_text = '''
Thank you for participating!

This block is now finished,
Please call your experimenter.
'''

draw_ins(WIN, finish_text, 'white')