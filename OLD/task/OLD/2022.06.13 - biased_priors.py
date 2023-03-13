## Libraries

from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Circle, Polygon
from psychopy.core import Clock, wait, quit
from psychopy.hardware.keyboard import Keyboard
import pandas as pd
import numpy as np
import math

################################################################################
## Things you can set

# Screen and window stuff
scrwidth = 16*70
scrlength = 9*70
fullscr = False
background_color = 'grey'

# Trial stuff
# 205 trials per block. 123 "More Red", 82 "Less Red". See '010 Power Analysis' code.
nBlocks = 4 #how many blocks? There are breaks between blocks.
n_dots = 100 #number of dots
bounds = [150.0, 360.0] #boundary for dots, polar coordinates (radius pix, angle)
threshold = 0.15*n_dots #how close are dots allowed to be?
dotsize = 4 #hmmm, what could this be...
choice_time = 2.0 #how long do subjects have to make a choice? (secs)
fb_time = 1.0 #how long to display the feedback screen?
cross_time = 0.5 #how long to display the fixation cross?

# Payment
marginal_pay = 5 # $5 per correct answer.

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
        
        Count the number of red balls out of 100
        green and red balls. All 100 balls will
        only be displayed for 0.5 to 3 seconds.
        
        When prompted to respond, select:
        L arrow = Less red balls than green.
        R arrow = More red balls than green.
        
        You'll have 2 seconds to respond. If
        you're too slow, the experiment will
        tell you to be quicker next time.
        
        60% of trials will have more red balls.
        
        Press space to continue.
        """,
    color=(1,1,1),
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

beginning_txt_stim = TextStim(
    win, 
    text=
        """
        Experiment is beginning.
        """,
    color=(1,1,1),
    font="Calibri"
)
beginning_txt_stim.draw()
win.flip()
wait(2)

## Before experiment begins

trial_clock = Clock() #clock resets at start of trial
fb_clock = Clock() #clock resets as soon as choice is made
trial_number = 0

## During experiment

### Blocks

for block in range(nBlocks):
    
    blockstart_txt_stim = TextStim(
        win, 
        text=f"Block {block+1} of {nBlocks}.",
        color=(1,1,1),
        font="Calibri"
    )
    blockstart_txt_stim.draw()
    win.flip()
    wait(2)
    
    cond_df = cond_df.sample(frac=1) #Randomize the order of trials in a block, for each rep
    
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
        stim_time = row['stim_end']
        stim_onset_recorded = False
        trial_on = True
        trial_clock.reset()
        
        while trial_on:
            
            #################
            ### within trial 
            #################
            
            ### Allow quit out at any time
            
            keys = kb.getKeys()
            for key in keys:
                if key == 'q':
                    win.flip()
                    wait(0.5)
                    win.close()
                    df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
                    quit()
            
            ### Stimulus segment
            
            if trial_clock.getTime() <= stim_time:
                
                dot = Circle(
                    win,
                    edges = 128,
                    radius = dotsize,
                )
                for dot_loc in dots[0:difficulty-1]: #red
                    
                    dot.pos = [float(dot_loc[0]), float(dot_loc[1])]
                    dot.fillColor = (1,-1,-1)
                    dot.lineColor = (1,-1,-1)
                    dot.draw()
                for dot_loc in dots[difficulty:len(dots)-1]: #green
                    dot.pos = [float(dot_loc[0]), float(dot_loc[1])]
                    dot.fillColor = (-1,.75,-1)
                    dot.lineColor = (-1,.75,-1)
                    dot.draw()
                    
                win.flip()
                fb_clock.reset()
                
                if not stim_onset_recorded:
                    
                    stim_onset_time = global_clock.getTime()
                    stim_onset_recorded = True
                    
            ### Choice segment
            
            if (stim_time < trial_clock.getTime() <= stim_time+choice_time) and press_rt == None: 
                
                L_txt_stim = TextStim(
                    win,
                    text = "Less Red",
                    height = 50,
                    pos = [-scrwidth/4, 0]
                )
                R_txt_stim = TextStim(
                    win,
                    text="More Red",
                    height=50,
                    pos = [scrwidth/4, 0]
                )
                L_txt_stim.draw()
                R_txt_stim.draw()
                
                win.flip()
                fb_clock.reset()
                
                keys = kb.getKeys()
                for key in keys:
                    if key == 'left' or key == 'right':
                        press_name = key.name
                        press_rt = trial_clock.getTime() #works better than key.rt
            
            ### No choice made segment (if no choice made)
            
            if press_name == '' and stim_time+choice_time < trial_clock.getTime() and fb_clock.getTime() <= fb_time:
                
                quicker_txt_stim = TextStim(
                    win,
                    text="Quicker!",
                    height=50
                )
                quicker_txt_stim.draw()
                win.flip()
            
            ### Feedback segment
            
            if press_name != '' and fb_clock.getTime() <= fb_time:
                
                fb_polygon_stim = Polygon(
                        win,
                        edges = 4,
                        radius = 175,
                        lineWidth = 8,
                        lineColor = (-1,-1,1),
                        ori = 45
                    )
                if press_name == 'left':
                    fb_polygon_stim.pos = [-scrwidth/4, 0]
                if press_name == 'right':
                    fb_polygon_stim.pos = [scrwidth/4, 0]
                fb_polygon_stim.draw()
                
                L_txt_stim = TextStim(
                    win,
                    text="Less Red",
                    height=50,
                    pos = [-scrwidth/4, 0]
                )
                R_txt_stim = TextStim(
                    win,
                    text="More Red",
                    height=50,
                    pos = [scrwidth/4, 0]
                )
                L_txt_stim.draw()
                R_txt_stim.draw()
                
                win.flip()
            
            ### Fixation cross segment
            
            if fb_time < fb_clock.getTime() <= fb_time+cross_time:
                cross_txt_stim = TextStim(
                    win,
                    text="+",
                    height=200
                )
                cross_txt_stim.draw()
                win.flip()
            
            ### End the trial
            
            if fb_clock.getTime() > fb_time+cross_time:
                trial_on = False
                
        ### Record data at end of trial
        
        df.loc[trial_number, 'subject'] = exp_info['Participant']
        df.loc[trial_number, 'session'] = exp_info['Session']
        df.loc[trial_number, 'block'] = block
        df.loc[trial_number, 'trial'] = trial_number
        df.loc[trial_number, 'difficulty'] = difficulty
        df.loc[trial_number, 'stim_end'] = stim_time
        df.loc[trial_number, 'response'] = press_name
        df.loc[trial_number, 'rt'] = press_rt
        df.loc[trial_number, 'stim_onset'] = stim_onset_time
    
    ### End of block, press space to continue
    
    blockend_txt_stim = TextStim(
        win, 
        text=
            """
            End of block.
            
            Press b to continue.
            """,
        color=(1,1,1),
        font="Calibri"
    )
    blockend_txt_stim.draw()
    win.flip()
    
    while True:
        keys = kb.getKeys()
        if "b" in keys:
            break
        if 'q' in keys:
            win.flip()
            wait(0.5)
            win.close()
            df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
            quit()

## Payment screen

#calculate payment
pay = 0
size = 1
replace = False  # with replacement
fn = lambda obj: obj.loc[np.random.choice(obj.index, size, replace),:]
paydf = df.groupby('block', as_index=True).apply(fn)

for block in range(nBlocks):
    if int(paydf['difficulty'][block])>50:
        correct = 'right'
    else:
        correct = 'left'
    if paydf['response'][block].values==correct:
        pay = pay + marginal_pay

#display payment
pay_txt_stim = TextStim(
    win, 
    text=
        f"""
        $15 + ${pay}
        
        Please wait for ex[p]erimenter.
        """,
    color=(1,1,1),
    font="Calibri"
)
pay_txt_stim.draw()
win.flip()

while True:
    keys = kb.getKeys()
    if "p" in keys:
        break

## End of experiment

win.flip()
wait(0.5)
win.close()
df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
quit()
