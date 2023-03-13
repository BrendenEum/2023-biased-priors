## Libraries

from psychopy.gui import DlgFromDict
from psychopy.visual import Window, TextStim, ImageStim, Circle, Polygon
from psychopy.core import Clock, wait, quit
from psychopy.hardware.keyboard import Keyboard
import pandas as pd
import numpy as np
import math

################################################################################
################################################################################
## THINGS YOU CAN SET

# Screen and window stuff
scrwidth = 16*70
scrlength = 9*70
fullscr = True
background_color = 'grey'
text_height = 40

# Trial stuff
# See '010 Power Analysis' code.
nBlocks = 4 #how many blocks? There are breaks between blocks.
n_dots = 100 #number of dots
bounds = [185.0, 360.0] #boundary for dots, polar coordinates (radius pix, angle)
dotsize = 7 #hmmm, what could this be...
threshold = (0.13+0.01*dotsize)*n_dots #how close are dots allowed to be?
choice_time = 2.0 #how long do subjects have to make a choice? (secs)
fb_time = 1.0 #how long to display the feedback screen?
cross_time = 0.5 #how long to display the fixation cross?

# Payment
marginal_pay = 5 # $5 per correct answer.

################################################################################
################################################################################

################################################################################
## WELCOME

## Before experiment

exec(open("dot_functions.py").read()) #functions to generate dot stimuli
exp_info = {"Participant":"", "Session":""}
dlg = DlgFromDict(exp_info)
praccond_df = pd.read_csv("practice_conditions.csv") #practice conditions
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
        green and red balls. Balls will only be
        displayed for a short period of time
        (between 0.1 and 7 secs).
        
        When prompted to respond, select:
        L arrow = More green balls than red.
        R arrow = More red balls than green.
        
        You'll have 2 seconds to respond. If
        you're too slow, the experiment will
        tell you to be quicker next time.
        
        Trials are 60% likely to be in favor
        of red balls.
        
        In addition to the $15 show up fee,
        you will be paid $5 for the accuracy
        of a randomly selected trial in
        each of 4 blocks, up to $20.
        
        Press space to start practicing.
        """,
    color=(1,1,1),
    font="Calibri",
    alignText='left',
    height = text_height-14
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

#############################################################################
## PRACTICE TRIALS

iti_clock = Clock() # clock resets prior to fixation cross
trial_clock = Clock() #clock resets at stimulus presentation
choice_clock = Clock() # clock resets at start of choice prompt
fb_clock = Clock() #clock resets as soon as choice is made
trial_number = 0

pracstart_txt_stim = TextStim(
    win, 
    text=f"Practice beginning.",
    color=(1,1,1),
    font="Calibri",
    height = text_height
)
pracstart_txt_stim.draw()
win.flip()
wait(2)

praccond_df = praccond_df.sample(frac=1)

for ind, row in praccond_df.iterrows():
    
    # trial information and preparation
    
    press_key = None
    press_rt = None
    difficulty = int(row['difficulty'])
    stim_time = row['stim_end']
    
    # Generate dots
    
    dots = generate(
        n_dots = n_dots,
        bounds = bounds,
        test_func = test_func,
        threshold = threshold
    )
    
    # Fixation cross segment
    
    cross_txt_stim = TextStim(
            win,
            text="+",
            height=300
        )
    
    iti_clock.reset()
    while iti_clock.getTime() <= cross_time:
        cross_txt_stim.draw()
        win.flip()

    # Stimulus segment

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
    stim_onset_time = global_clock.getTime()
    
    trial_clock.reset()
    while trial_clock.getTime() <= stim_time:
        if trial_clock.getTime() > stim_time:
            break
        
    # Choice segment
        
    L_txt_stim = TextStim(
        win,
        text = "Green",
        height = 75,
        pos = [-scrwidth/3, 0]
    )
    R_txt_stim = TextStim(
        win,
        text="Red",
        height=75,
        pos = [scrwidth/3, 0]
    )
    L_txt_stim.draw()
    R_txt_stim.draw()
    win.flip()
    
    keys = kb.waitKeys(
        maxWait = choice_time,
        keyList = ['left','right','q'],
        clear = True
    )
    
    if keys is not None:
        if 'left' in keys:
            press_key = 1
        if 'right' in keys:
            press_key = 2
        if 'q' in keys:
            win.flip()
            wait(0.5)
            win.close()
            quit()

    # No choice made segment (if no choice made)
    
    quicker_txt_stim = TextStim(
            win,
            text="Quicker!",
            height=100
        )
    
    fb_clock.reset()
    while press_key == None and fb_clock.getTime() <= fb_time:
        quicker_txt_stim.draw()
        win.flip()

    # Feedback segment

    fb_polygon_stim = Polygon(
            win,
            edges = 4,
            radius = 250,
            lineWidth = 8,
            lineColor = (-1,-1,1),
            ori = 45
        )
    if press_key == 1:
        fb_polygon_stim.pos = [-scrwidth/3, 0]
    if press_key == 2:
        fb_polygon_stim.pos = [scrwidth/3, 0]
    
    L_txt_stim = TextStim(
        win,
        text="Green",
        height=75,
        pos = [-scrwidth/3, 0]
    )
    R_txt_stim = TextStim(
        win,
        text="Red",
        height=75,
        pos = [scrwidth/3, 0]
    )
    
    fb_clock.reset()
    while press_key != None and fb_clock.getTime() <= fb_time:
        fb_polygon_stim.draw()
        L_txt_stim.draw()
        R_txt_stim.draw()
        win.flip()

# end of practice

pracend_txt_stim = TextStim(
    win, 
    text=
        """
        Practice is finished.
        
        Press space to begin the 
        experiment.
        """,
    color=(1,1,1),
    font="Calibri",
    alignText='left',
    height = text_height
)
pracend_txt_stim.draw()
win.flip()
kb.start()
while True:
    keys = kb.getKeys()
    if "space" in keys:
        global_clock = Clock()
        break
    if 'q' in keys:
        quit()

################################################################################
## START OF THE EXPERIMENT

beginning_txt_stim = TextStim(
    win, 
    text=
        """
        Experiment is beginning.
        """,
    color=(1,1,1),
    font="Calibri",
    height = text_height
)
beginning_txt_stim.draw()
win.flip()
wait(2)

## Before experiment begins

iti_clock = Clock() # clock resets prior to fixation cross
trial_clock = Clock() #clock resets at stimulus presentation
choice_clock = Clock() # clock resets at start of choice prompt
trial_number = 0


################################################################################
## DURING THE EXPERIMENT

### Blocks

for block in range(nBlocks):
    
    blockstart_txt_stim = TextStim(
        win, 
        text=f"Block {block+1} of {nBlocks}.",
        color=(1,1,1),
        font="Calibri",
        height = text_height
    )
    blockstart_txt_stim.draw()
    win.flip()
    wait(2)
    
    cond_df = cond_df.sample(frac=1) #Randomize the order of trials in a block, for each rep
    
    for ind, row in cond_df.iterrows():
        
        ########################################################################
        ### DURING A SINGLE TRIAL
        
        
        ### trial information and preparation
        
        trial_number += 1
        press_key = None
        press_rt = None
        difficulty = int(row['difficulty'])
        stim_time = row['stim_end']
        dots_generated = False
        
        ### Generate dots
        
        dots = generate(
            n_dots = n_dots,
            bounds = bounds,
            test_func = test_func,
            threshold = threshold
        )
        
        ### Fixation cross segment
        
        cross_txt_stim = TextStim(
                win,
                text="+",
                height=300
            )
        
        iti_clock.reset()
        while iti_clock.getTime() <= cross_time:
            cross_txt_stim.draw()
            win.flip()

        ### Stimulus segment

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
        stim_onset_time = global_clock.getTime()
        
        trial_clock.reset()
        while trial_clock.getTime() <= stim_time:
            if trial_clock.getTime() > stim_time:
                break
            
        ### Choice segment
            
        L_txt_stim = TextStim(
            win,
            text = "Green",
            height = 75,
            pos = [-scrwidth/3, 0]
        )
        R_txt_stim = TextStim(
            win,
            text="Red",
            height=75,
            pos = [scrwidth/3, 0]
        )
        L_txt_stim.draw()
        R_txt_stim.draw()
        win.flip()
        
        choice_clock.reset()
        
        keys = kb.waitKeys(
            maxWait = choice_time,
            keyList = ['left','right','q'],
            clear = True
        )
        
        if keys is not None:
            press_rt = choice_clock.getTime()
            if 'left' in keys:
                press_key = 1
            if 'right' in keys:
                press_key = 2
            if 'q' in keys:
                win.flip()
                wait(0.5)
                win.close()
                df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
                quit()

        ### No choice made segment (if no choice made)
        
        quicker_txt_stim = TextStim(
                win,
                text="Quicker!",
                height=100
            )
        
        fb_clock.reset()
        while press_key == None and fb_clock.getTime() <= fb_time:
            quicker_txt_stim.draw()
            win.flip()

        ### Feedback segment

        fb_polygon_stim = Polygon(
                win,
                edges = 4,
                radius = 250,
                lineWidth = 8,
                lineColor = (-1,-1,1),
                ori = 45
            )
        if press_key == 1:
            fb_polygon_stim.pos = [-scrwidth/3, 0]
        if press_key == 2:
            fb_polygon_stim.pos = [scrwidth/3, 0]
        
        L_txt_stim = TextStim(
            win,
            text="Green",
            height=75,
            pos = [-scrwidth/3, 0]
        )
        R_txt_stim = TextStim(
            win,
            text="Red",
            height=75,
            pos = [scrwidth/3, 0]
        )
        
        fb_clock.reset()
        while press_key != None and fb_clock.getTime() <= fb_time:
            fb_polygon_stim.draw()
            L_txt_stim.draw()
            R_txt_stim.draw()
            win.flip()
        
        ### Record data at end of trial
        
        df.loc[trial_number, 'subject'] = exp_info['Participant']
        df.loc[trial_number, 'session'] = exp_info['Session']
        df.loc[trial_number, 'block'] = block + 1
        df.loc[trial_number, 'trial'] = trial_number
        df.loc[trial_number, 'difficulty'] = difficulty
        df.loc[trial_number, 'stim_end'] = stim_time
        df.loc[trial_number, 'response'] = press_key
        df.loc[trial_number, 'rt'] = press_rt
        df.loc[trial_number, 'stim_onset'] = stim_onset_time
        df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
    
    ### End of block, press space to continue
    
    blockend_txt_stim = TextStim(
        win, 
        text=
            """
            End of block.
            
            Press b to continue.
            """,
        color=(1,1,1),
        font="Calibri",
        height = text_height
    )
    blockend_txt_stim.draw()
    win.flip()
    kb.start()
    
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


################################################################################
## PAYMENT SCREEN

#calculate payment
pay = 0
size = 1
replace = False  # with replacement
fn = lambda obj: obj.loc[np.random.choice(obj.index, size, replace),:]
paydf = df.groupby('block', as_index=True).apply(fn)

for block in range(nBlocks):
    correct = None
    if int(paydf['difficulty'][block])>50:
        correct = 2.0
    else:
        correct = 1.0
    if float(paydf['response'][block]) == correct:
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
    font="Calibri",
    height = text_height
)
pay_txt_stim.draw()
win.flip()

while True:
    keys = kb.getKeys()
    if "p" in keys:
        break

################################################################################
## END OF THE EXPERIMENT

win.flip()
wait(0.5)
win.close()
df.to_csv(f"../../data/subject{exp_info['Participant']}_session{exp_info['Session']}.csv", sep=",")
quit()
