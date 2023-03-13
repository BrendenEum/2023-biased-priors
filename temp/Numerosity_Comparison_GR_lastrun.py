#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on June 02, 2022, at 18:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Numerosity_Comparison_GR'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\OneDrive - California Institute of Technology\\PhD\\Rangel Lab\\2022-biased-priors\\temp\\Numerosity_Comparison_GR_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
Welcome_ = visual.TextStim(win=win, name='Welcome_',
    text='Welkom bij het experiment!\n\nLees de instructies zorgvuldig alstublieft.\n\nDruk op SPATIE om verder te gaan.\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_welcome = keyboard.Keyboard()

# Initialize components for Routine "instr_train"
instr_trainClock = core.Clock()
Instr_training = visual.TextStim(win=win, name='Instr_training',
    text='We zullen starten met een korte training om de taak te begrijpen. \n\nJe zult twee sets van stippen zien verschijnen op het scherm.\nJou taak is om te beoordelen welke het \nGROOTSTE AANTAL STIPPEN HEEFT.\n\nHint: hou je ogen op het centrale witte kruis!\n\nDruk op SPATIE om verder te gaan.\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_instr_training = keyboard.Keyboard()

# Initialize components for Routine "instr_train2"
instr_train2Clock = core.Clock()
Resp_explain = visual.TextStim(win=win, name='Resp_explain',
    text='Druk op de toets ‘f’ als je denkt dat de LINKER set groter is. \n\nDruk op de toets ‘j’ als je denkt dat de RECHTER set groter is.\n \nProbeer zo snel en accuraat als je kan te antwoorden.\n\nJe zal feedback krijgen van je antwoord (juist/fout).\n\nAls je klaar bent om te oefenen, druk op SPATIE.\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
end_explain = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Dots_1 = visual.ImageStim(
    win=win,
    name='Dots_1', units='height', 
    image='sin', mask=None,
    ori=0, pos=(-0.45, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
Dots_2 = visual.ImageStim(
    win=win,
    name='Dots_2', units='height', 
    image='sin', mask=None,
    ori=0, pos=(+0.45, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
Feedback = visual.TextStim(win=win, name='Feedback',
    text='',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instr_main"
instr_mainClock = core.Clock()
Instr_main = visual.TextStim(win=win, name='Instr_main',
    text='Nu zal het hoofd experiment beginnen.\n\nDe taak is hetzelfde:\nje zult twee sets van stippen zien verschijnen op het scherm.\nJou taak is om te beoordelen welke het \nGROOTSTE AANTAL STIPPEN HEEFT.\n\nHint: hou je ogen op het centrale witte kruis!\n\nDruk op SPATIE om verder te gaan.\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=1, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space_to_continue = keyboard.Keyboard()

# Initialize components for Routine "instr_main2"
instr_main2Clock = core.Clock()
resp_expl2_main = visual.TextStim(win=win, name='resp_expl2_main',
    text='Druk op de toets ‘f’ als je denkt dat de LINKER set groter is. \n\nDruk op de toets ‘j’ als je denkt dat de RECHTER set groter is. \n\nProbeer zo snel en accuraat als je kan te antwoorden.\n\nDeze keer, zal je geen feedback krijgen. \n\nAls je klaar bent om te oefenen, druk op SPATIE.\n',
    font='Arial',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start_the_exp = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Dots_1 = visual.ImageStim(
    win=win,
    name='Dots_1', units='height', 
    image='sin', mask=None,
    ori=0, pos=(-0.45, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
Dots_2 = visual.ImageStim(
    win=win,
    name='Dots_2', units='height', 
    image='sin', mask=None,
    ori=0, pos=(+0.45, 0), size=(0.7, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
key_resp = keyboard.Keyboard()

# Initialize components for Routine "final_screen"
final_screenClock = core.Clock()
Thanks = visual.TextStim(win=win, name='Thanks',
    text='Dit is het einde van het experiment!\n\nDankje voor je medewerking!',
    font='Arial',
    pos=(0, 0), height=0.12, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
end_welcome.keys = []
end_welcome.rt = []
_end_welcome_allKeys = []
# keep track of which components have finished
WelcomeComponents = [Welcome_, end_welcome]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Welcome_* updates
    if Welcome_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome_.frameNStart = frameN  # exact frame index
        Welcome_.tStart = t  # local t and not account for scr refresh
        Welcome_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome_, 'tStartRefresh')  # time at next scr refresh
        Welcome_.setAutoDraw(True)
    
    # *end_welcome* updates
    waitOnFlip = False
    if end_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_welcome.frameNStart = frameN  # exact frame index
        end_welcome.tStart = t  # local t and not account for scr refresh
        end_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_welcome, 'tStartRefresh')  # time at next scr refresh
        end_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_welcome.status == STARTED and not waitOnFlip:
        theseKeys = end_welcome.getKeys(keyList=['space'], waitRelease=False)
        _end_welcome_allKeys.extend(theseKeys)
        if len(_end_welcome_allKeys):
            end_welcome.keys = _end_welcome_allKeys[-1].name  # just the last key pressed
            end_welcome.rt = _end_welcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Welcome_.started', Welcome_.tStartRefresh)
thisExp.addData('Welcome_.stopped', Welcome_.tStopRefresh)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_train"-------
continueRoutine = True
# update component parameters for each repeat
end_instr_training.keys = []
end_instr_training.rt = []
_end_instr_training_allKeys = []
# keep track of which components have finished
instr_trainComponents = [Instr_training, end_instr_training]
for thisComponent in instr_trainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_trainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_train"-------
while continueRoutine:
    # get current time
    t = instr_trainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_trainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_training* updates
    if Instr_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_training.frameNStart = frameN  # exact frame index
        Instr_training.tStart = t  # local t and not account for scr refresh
        Instr_training.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_training, 'tStartRefresh')  # time at next scr refresh
        Instr_training.setAutoDraw(True)
    
    # *end_instr_training* updates
    waitOnFlip = False
    if end_instr_training.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_instr_training.frameNStart = frameN  # exact frame index
        end_instr_training.tStart = t  # local t and not account for scr refresh
        end_instr_training.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_instr_training, 'tStartRefresh')  # time at next scr refresh
        end_instr_training.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_instr_training.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_instr_training.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_instr_training.status == STARTED and not waitOnFlip:
        theseKeys = end_instr_training.getKeys(keyList=['space'], waitRelease=False)
        _end_instr_training_allKeys.extend(theseKeys)
        if len(_end_instr_training_allKeys):
            end_instr_training.keys = _end_instr_training_allKeys[-1].name  # just the last key pressed
            end_instr_training.rt = _end_instr_training_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_trainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_train"-------
for thisComponent in instr_trainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_training.started', Instr_training.tStartRefresh)
thisExp.addData('Instr_training.stopped', Instr_training.tStopRefresh)
# the Routine "instr_train" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_train2"-------
continueRoutine = True
# update component parameters for each repeat
end_explain.keys = []
end_explain.rt = []
_end_explain_allKeys = []
# keep track of which components have finished
instr_train2Components = [Resp_explain, end_explain]
for thisComponent in instr_train2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_train2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_train2"-------
while continueRoutine:
    # get current time
    t = instr_train2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_train2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Resp_explain* updates
    if Resp_explain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Resp_explain.frameNStart = frameN  # exact frame index
        Resp_explain.tStart = t  # local t and not account for scr refresh
        Resp_explain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Resp_explain, 'tStartRefresh')  # time at next scr refresh
        Resp_explain.setAutoDraw(True)
    
    # *end_explain* updates
    waitOnFlip = False
    if end_explain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_explain.frameNStart = frameN  # exact frame index
        end_explain.tStart = t  # local t and not account for scr refresh
        end_explain.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_explain, 'tStartRefresh')  # time at next scr refresh
        end_explain.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_explain.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_explain.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_explain.status == STARTED and not waitOnFlip:
        theseKeys = end_explain.getKeys(keyList=['space'], waitRelease=False)
        _end_explain_allKeys.extend(theseKeys)
        if len(_end_explain_allKeys):
            end_explain.keys = _end_explain_allKeys[-1].name  # just the last key pressed
            end_explain.rt = _end_explain_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_train2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_train2"-------
for thisComponent in instr_train2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Resp_explain.started', Resp_explain.tStartRefresh)
thisExp.addData('Resp_explain.stopped', Resp_explain.tStopRefresh)
# the Routine "instr_train2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Num_Comp_GR_practice.xlsx'),
    seed=None, name='practice_trials')
thisExp.addLoop(practice_trials)  # add the loop to the experiment
thisPractice_trial = practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial:
        exec('{} = thisPractice_trial[paramName]'.format(paramName))

for thisPractice_trial in practice_trials:
    currentLoop = practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial:
            exec('{} = thisPractice_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Dots_1.setImage(Stim1)
    Dots_2.setImage(Stim2)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation_cross, Dots_1, Dots_2, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        
        # *Dots_1* updates
        if Dots_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Dots_1.frameNStart = frameN  # exact frame index
            Dots_1.tStart = t  # local t and not account for scr refresh
            Dots_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dots_1, 'tStartRefresh')  # time at next scr refresh
            Dots_1.setAutoDraw(True)
        
        # *Dots_2* updates
        if Dots_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Dots_2.frameNStart = frameN  # exact frame index
            Dots_2.tStart = t  # local t and not account for scr refresh
            Dots_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dots_2, 'tStartRefresh')  # time at next scr refresh
            Dots_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(CorrAns)) or (key_resp.keys == CorrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    practice_trials.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    practice_trials.addData('Dots_1.started', Dots_1.tStartRefresh)
    practice_trials.addData('Dots_1.stopped', Dots_1.tStopRefresh)
    practice_trials.addData('Dots_2.started', Dots_2.tStartRefresh)
    practice_trials.addData('Dots_2.stopped', Dots_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice_trials (TrialHandler)
    practice_trials.addData('key_resp.keys',key_resp.keys)
    practice_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        practice_trials.addData('key_resp.rt', key_resp.rt)
    practice_trials.addData('key_resp.started', key_resp.tStartRefresh)
    practice_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.500000)
    # update component parameters for each repeat
    if key_resp.corr == 1: #stored on last run routine
        msg = "Juist!"
    else:
        msg = "Oeps! Dat was fout"
    Feedback.setColor('white', colorSpace='rgb')
    Feedback.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [Feedback]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Feedback* updates
        if Feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Feedback.frameNStart = frameN  # exact frame index
            Feedback.tStart = t  # local t and not account for scr refresh
            Feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Feedback, 'tStartRefresh')  # time at next scr refresh
            Feedback.setAutoDraw(True)
        if Feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Feedback.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                Feedback.tStop = t  # not accounting for scr refresh
                Feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Feedback, 'tStopRefresh')  # time at next scr refresh
                Feedback.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice_trials.addData('Feedback.started', Feedback.tStartRefresh)
    practice_trials.addData('Feedback.stopped', Feedback.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice_trials'

# get names of stimulus parameters
if practice_trials.trialList in ([], [None], None):
    params = []
else:
    params = practice_trials.trialList[0].keys()
# save data for this loop
practice_trials.saveAsExcel(filename + '.xlsx', sheetName='practice_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
practice_trials.saveAsText(filename + 'practice_trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "instr_main"-------
continueRoutine = True
# update component parameters for each repeat
Space_to_continue.keys = []
Space_to_continue.rt = []
_Space_to_continue_allKeys = []
# keep track of which components have finished
instr_mainComponents = [Instr_main, Space_to_continue]
for thisComponent in instr_mainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_main"-------
while continueRoutine:
    # get current time
    t = instr_mainClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_mainClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr_main* updates
    if Instr_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_main.frameNStart = frameN  # exact frame index
        Instr_main.tStart = t  # local t and not account for scr refresh
        Instr_main.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_main, 'tStartRefresh')  # time at next scr refresh
        Instr_main.setAutoDraw(True)
    
    # *Space_to_continue* updates
    waitOnFlip = False
    if Space_to_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Space_to_continue.frameNStart = frameN  # exact frame index
        Space_to_continue.tStart = t  # local t and not account for scr refresh
        Space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space_to_continue, 'tStartRefresh')  # time at next scr refresh
        Space_to_continue.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Space_to_continue.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Space_to_continue.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Space_to_continue.status == STARTED and not waitOnFlip:
        theseKeys = Space_to_continue.getKeys(keyList=['space'], waitRelease=False)
        _Space_to_continue_allKeys.extend(theseKeys)
        if len(_Space_to_continue_allKeys):
            Space_to_continue.keys = _Space_to_continue_allKeys[-1].name  # just the last key pressed
            Space_to_continue.rt = _Space_to_continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_mainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_main"-------
for thisComponent in instr_mainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr_main.started', Instr_main.tStartRefresh)
thisExp.addData('Instr_main.stopped', Instr_main.tStopRefresh)
# the Routine "instr_main" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instr_main2"-------
continueRoutine = True
# update component parameters for each repeat
start_the_exp.keys = []
start_the_exp.rt = []
_start_the_exp_allKeys = []
# keep track of which components have finished
instr_main2Components = [resp_expl2_main, start_the_exp]
for thisComponent in instr_main2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instr_main2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr_main2"-------
while continueRoutine:
    # get current time
    t = instr_main2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instr_main2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *resp_expl2_main* updates
    if resp_expl2_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp_expl2_main.frameNStart = frameN  # exact frame index
        resp_expl2_main.tStart = t  # local t and not account for scr refresh
        resp_expl2_main.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp_expl2_main, 'tStartRefresh')  # time at next scr refresh
        resp_expl2_main.setAutoDraw(True)
    
    # *start_the_exp* updates
    waitOnFlip = False
    if start_the_exp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_the_exp.frameNStart = frameN  # exact frame index
        start_the_exp.tStart = t  # local t and not account for scr refresh
        start_the_exp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_the_exp, 'tStartRefresh')  # time at next scr refresh
        start_the_exp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start_the_exp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start_the_exp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start_the_exp.status == STARTED and not waitOnFlip:
        theseKeys = start_the_exp.getKeys(keyList=['space'], waitRelease=False)
        _start_the_exp_allKeys.extend(theseKeys)
        if len(_start_the_exp_allKeys):
            start_the_exp.keys = _start_the_exp_allKeys[-1].name  # just the last key pressed
            start_the_exp.rt = _start_the_exp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instr_main2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr_main2"-------
for thisComponent in instr_main2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('resp_expl2_main.started', resp_expl2_main.tStartRefresh)
thisExp.addData('resp_expl2_main.stopped', resp_expl2_main.tStopRefresh)
# the Routine "instr_main2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test_trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Num_Comp_GR_test.xlsx'),
    seed=None, name='test_trials')
thisExp.addLoop(test_trials)  # add the loop to the experiment
thisTest_trial = test_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
if thisTest_trial != None:
    for paramName in thisTest_trial:
        exec('{} = thisTest_trial[paramName]'.format(paramName))

for thisTest_trial in test_trials:
    currentLoop = test_trials
    # abbreviate parameter names if possible (e.g. rgb = thisTest_trial.rgb)
    if thisTest_trial != None:
        for paramName in thisTest_trial:
            exec('{} = thisTest_trial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    Dots_1.setImage(Stim1)
    Dots_2.setImage(Stim2)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trialComponents = [fixation_cross, Dots_1, Dots_2, key_resp]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        
        # *Dots_1* updates
        if Dots_1.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Dots_1.frameNStart = frameN  # exact frame index
            Dots_1.tStart = t  # local t and not account for scr refresh
            Dots_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dots_1, 'tStartRefresh')  # time at next scr refresh
            Dots_1.setAutoDraw(True)
        
        # *Dots_2* updates
        if Dots_2.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            Dots_2.frameNStart = frameN  # exact frame index
            Dots_2.tStart = t  # local t and not account for scr refresh
            Dots_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Dots_2, 'tStartRefresh')  # time at next scr refresh
            Dots_2.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # was this correct?
                if (key_resp.keys == str(CorrAns)) or (key_resp.keys == CorrAns):
                    key_resp.corr = 1
                else:
                    key_resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test_trials.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    test_trials.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    test_trials.addData('Dots_1.started', Dots_1.tStartRefresh)
    test_trials.addData('Dots_1.stopped', Dots_1.tStopRefresh)
    test_trials.addData('Dots_2.started', Dots_2.tStartRefresh)
    test_trials.addData('Dots_2.stopped', Dots_2.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           key_resp.corr = 1;  # correct non-response
        else:
           key_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for test_trials (TrialHandler)
    test_trials.addData('key_resp.keys',key_resp.keys)
    test_trials.addData('key_resp.corr', key_resp.corr)
    if key_resp.keys != None:  # we had a response
        test_trials.addData('key_resp.rt', key_resp.rt)
    test_trials.addData('key_resp.started', key_resp.tStartRefresh)
    test_trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'test_trials'

# get names of stimulus parameters
if test_trials.trialList in ([], [None], None):
    params = []
else:
    params = test_trials.trialList[0].keys()
# save data for this loop
test_trials.saveAsExcel(filename + '.xlsx', sheetName='test_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])
test_trials.saveAsText(filename + 'test_trials.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "final_screen"-------
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
final_screenComponents = [Thanks]
for thisComponent in final_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
final_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "final_screen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = final_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=final_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thanks* updates
    if Thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.tStart = t  # local t and not account for scr refresh
        Thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thanks, 'tStartRefresh')  # time at next scr refresh
        Thanks.setAutoDraw(True)
    if Thanks.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Thanks.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            Thanks.tStop = t  # not accounting for scr refresh
            Thanks.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Thanks, 'tStopRefresh')  # time at next scr refresh
            Thanks.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in final_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "final_screen"-------
for thisComponent in final_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Thanks.started', Thanks.tStartRefresh)
thisExp.addData('Thanks.stopped', Thanks.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
