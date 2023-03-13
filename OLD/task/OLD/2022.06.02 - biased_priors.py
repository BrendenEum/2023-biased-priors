## Libraries

from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Circle
from psychopy.core import Clock, wait, quit
from psychopy.hardware.keyboard import Keyboard
import pandas as pd
import numpy as np

################################################################################
## Things you can set

# Screen and window stuff
scrwidth = 16*70
scrlength = 9*70
fullscr = False
background_color = 'black'

# Trial stuff
nReps = 1 #how many times you want each trial condition to repeat
n_dots = 100 #number of dots
bounds = [-150, 150] #dimensions of the square that contains stimuli
threshold = 0.15*n_dots #how close are dots allowed to be?
dotsize = 4 #hmmm, what could this be...
choice_time = 1 #how long do subjects have to make a choice?
cross_time = 1 #how long to display the fixation cross?

################################################################################

## Before experiment

exec(open("dot_functions.py").read()) #functions to generate dot stimuli
exp_info = {"Participant":"", "Session":""}
dlg = DlgFromDict(exp_info)
cond_df = pd.read_csv("conditions.csv") #experiment conditions
df = pd.DataFrame() #output dataframe

## To start the experiment

win = Window(
    fullscr=fullscr, 
    size=(scrwidth, scrlength),
    units = 'pix',
    monitor = 'default',
    color = background_color
) 

kb = Keyboard()

## Welcome screen

welcome_txt_stim = TextStim(
    win, 
    text=
        """
        Welcome!
        Count the number of red balls.
        
        When prompted to respond, select:
        L = Less red balls than green.
        R = More red balls than green.
        
        Press space to continue.
        """,
    color=(1,0,-1),
    font="Calibri",
    alignText='left'
)
welcome_txt_stim.draw()
win.flip()
while True:
    keys = kb.getKeys()
    if "space" in keys:
        global_clock = Clock()
        break
    if 'q' in keys:
        quit()

## Trials

trial_clock = Clock()
trial_number = 0

### Reps

for _ in range(nReps):
    
    ### all conditions (48 or 52)
    
    cond_df = cond_df.sample(frac=1)
    
    for ind, row in cond_df.iterrows():
        
        ##############
        ### one trial 
        ##############
        
        ### Generate dot locations
        
        dots = generate(
            n_dots = n_dots,
            bounds = bounds,
            test_func = test_func,
            threshold = threshold
        )
        
        ### trial information and preparation
        
        trial_number += 1
        press_name = ''
        press_rt = None
        difficulty = int(row['difficulty'])
        iti = row['stim_end'] + 0.5
        stim_on = True
        stim_onset_recorded = False
        trial_clock.reset()
        kb.clock.reset()
        
        while trial_clock.getTime() < iti:
            
            #################
            ### within trial 
            #################
            
            ### Check response
            
            keys = kb.getKeys()
            for key in keys:
                if key == 'q':
                    quit()
                if stim_on:
                    if key == 'left' or key == 'right':
                        press_name = key.name
                        press_rt = key.rt
                        stim_on = False
            
            ### Stimulus
            
            if stim_on:
                dot = Circle(
                    win,
                    edges = 128,
                    radius = dotsize,
                )
                for dot_loc in dots[0:difficulty-1]: #red
                    dot.pos = [dot_loc[0], dot_loc[1]]
                    dot.fillColor = (1,-1,-1)
                    dot.lineColor = (1,-1,-1)
                    dot.draw()
                for dot_loc in dots[difficulty:len(dots)-1]: #green
                    dot.pos = [dot_loc[0], dot_loc[1]]
                    dot.fillColor = (-1,1,-1)
                    dot.lineColor = (-1,1,-1)
                    dot.draw()
                win.flip()
                
                if not stim_onset_recorded:
                    stim_onset_time = global_clock.getTime()
                    stim_onset_recorded = True
            
            ### ITI
            
            if trial_clock.getTime() > iti-0.5:
                stim_on = False
            
            if stim_on == False and trial_clock.getTime() < iti:
                iti_txt_stim = TextStim(
                    win,
                    text="+",
                    height=200
                )
                iti_txt_stim.draw()
                win.flip()
                
        ### Record data at end of trial
        
        df.loc[trial_number, 'subject'] = exp_info['Participant']
        df.loc[trial_number, 'session'] = exp_info['Session']
        df.loc[trial_number, 'trial'] = trial_number
        df.loc[trial_number, 'difficulty'] = difficulty
        df.loc[trial_number, 'stim_end'] = iti-0.5
        df.loc[trial_number, 'response'] = press_name
        df.loc[trial_number, 'rt'] = press_rt
        df.loc[trial_number, 'stim_onset'] = stim_onset_time

## End of experiment

win.flip()
wait(0.5)
win.close()
df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
quit()
