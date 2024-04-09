#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.3),
    on April 09, 2024, at 14:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.3'
expName = 'prof_rating'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\hiyab\\OneDrive\\Documents\\Hiya\\Stevens\\CS 555\\PsycoPy\\Prof_Rating\\prof_rating.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=False, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = True
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "WelcomeScreen" ---
    text = visual.TextStim(win=win, name='text',
        text='Welcome to the Test!\n\nPlease press the spacebar to continue',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    keySpacebar = keyboard.Keyboard()
    
    # --- Initialize components for Routine "Prof1_taken_prof" ---
    HaveYouTakenThisProf = visual.TextStim(win=win, name='HaveYouTakenThisProf',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf1 = visual.ImageStim(
        win=win,
        name='imageProf1', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton = visual.ImageStim(
        win=win,
        name='imageYesButton', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton = visual.ImageStim(
        win=win,
        name='imageNoButton', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof1_enjoy_class" ---
    DidYouEnjoyThisProf = visual.TextStim(win=win, name='DidYouEnjoyThisProf',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf1_1 = visual.ImageStim(
        win=win,
        name='imageProf1_1', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image1.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_18 = visual.ImageStim(
        win=win,
        name='imageYesButton_18', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_18 = visual.ImageStim(
        win=win,
        name='imageNoButton_18', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_18 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_18.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof2" ---
    HaveYouTakenThisProf_2 = visual.TextStim(win=win, name='HaveYouTakenThisProf_2',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf2 = visual.ImageStim(
        win=win,
        name='imageProf2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_2 = visual.ImageStim(
        win=win,
        name='imageYesButton_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_2 = visual.ImageStim(
        win=win,
        name='imageNoButton_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_2 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_2.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof2_enjoy_class" ---
    DidYouEnjoyThisProf_2 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_2',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf2_2 = visual.ImageStim(
        win=win,
        name='imageProf2_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image2.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_19 = visual.ImageStim(
        win=win,
        name='imageYesButton_19', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_19 = visual.ImageStim(
        win=win,
        name='imageNoButton_19', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_19 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_19.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof3" ---
    HaveYouTakenThisProf_3 = visual.TextStim(win=win, name='HaveYouTakenThisProf_3',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf3 = visual.ImageStim(
        win=win,
        name='imageProf3', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_3 = visual.ImageStim(
        win=win,
        name='imageYesButton_3', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_3 = visual.ImageStim(
        win=win,
        name='imageNoButton_3', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_3 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_3.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof3_enjoy_class" ---
    DidYouEnjoyThisProf_3 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_3',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf3_2 = visual.ImageStim(
        win=win,
        name='imageProf3_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image3.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_20 = visual.ImageStim(
        win=win,
        name='imageYesButton_20', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_20 = visual.ImageStim(
        win=win,
        name='imageNoButton_20', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_20 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_20.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof4" ---
    HaveYouTakenThisProf_4 = visual.TextStim(win=win, name='HaveYouTakenThisProf_4',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf4 = visual.ImageStim(
        win=win,
        name='imageProf4', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image4.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_4 = visual.ImageStim(
        win=win,
        name='imageYesButton_4', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_4 = visual.ImageStim(
        win=win,
        name='imageNoButton_4', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_4 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_4.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof4_enjoy_class" ---
    DidYouEnjoyThisProf_4 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_4',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf4_2 = visual.ImageStim(
        win=win,
        name='imageProf4_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image4.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_21 = visual.ImageStim(
        win=win,
        name='imageYesButton_21', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_21 = visual.ImageStim(
        win=win,
        name='imageNoButton_21', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_21 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_21.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof5" ---
    HaveYouTakenThisProf_5 = visual.TextStim(win=win, name='HaveYouTakenThisProf_5',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf5 = visual.ImageStim(
        win=win,
        name='imageProf5', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image5.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_5 = visual.ImageStim(
        win=win,
        name='imageYesButton_5', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_5 = visual.ImageStim(
        win=win,
        name='imageNoButton_5', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_5 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_5.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof5_enjoy_class" ---
    DidYouEnjoyThisProf_5 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_5',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf5_2 = visual.ImageStim(
        win=win,
        name='imageProf5_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image5.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_22 = visual.ImageStim(
        win=win,
        name='imageYesButton_22', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_22 = visual.ImageStim(
        win=win,
        name='imageNoButton_22', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_22 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_22.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof6" ---
    HaveYouTakenThisProf_6 = visual.TextStim(win=win, name='HaveYouTakenThisProf_6',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf6 = visual.ImageStim(
        win=win,
        name='imageProf6', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image6.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_6 = visual.ImageStim(
        win=win,
        name='imageYesButton_6', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_6 = visual.ImageStim(
        win=win,
        name='imageNoButton_6', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_6 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_6.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "Prof6_enjoy_class" ---
    DidYouEnjoyThisProf_6 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_6',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf6_2 = visual.ImageStim(
        win=win,
        name='imageProf6_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image6.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_23 = visual.ImageStim(
        win=win,
        name='imageYesButton_23', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_23 = visual.ImageStim(
        win=win,
        name='imageNoButton_23', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_23 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_23.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof7" ---
    HaveYouTakenThisProf_7 = visual.TextStim(win=win, name='HaveYouTakenThisProf_7',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf7 = visual.ImageStim(
        win=win,
        name='imageProf7', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image7.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_7 = visual.ImageStim(
        win=win,
        name='imageYesButton_7', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_7 = visual.ImageStim(
        win=win,
        name='imageNoButton_7', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_7 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_7.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof7_enjoy_class" ---
    DidYouEnjoyThisProf_7 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_7',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf7_2 = visual.ImageStim(
        win=win,
        name='imageProf7_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image7.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_24 = visual.ImageStim(
        win=win,
        name='imageYesButton_24', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_24 = visual.ImageStim(
        win=win,
        name='imageNoButton_24', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_24 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_24.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof8" ---
    HaveYouTakenThisProf_8 = visual.TextStim(win=win, name='HaveYouTakenThisProf_8',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf8 = visual.ImageStim(
        win=win,
        name='imageProf8', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image8.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_8 = visual.ImageStim(
        win=win,
        name='imageYesButton_8', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_8 = visual.ImageStim(
        win=win,
        name='imageNoButton_8', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_8 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_8.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof8_enjoy_class" ---
    DidYouEnjoyThisProf_8 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_8',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf8_2 = visual.ImageStim(
        win=win,
        name='imageProf8_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image8.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_25 = visual.ImageStim(
        win=win,
        name='imageYesButton_25', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_25 = visual.ImageStim(
        win=win,
        name='imageNoButton_25', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_25 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_25.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof9" ---
    HaveYouTakenThisProf_9 = visual.TextStim(win=win, name='HaveYouTakenThisProf_9',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf9 = visual.ImageStim(
        win=win,
        name='imageProf9', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image9.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_9 = visual.ImageStim(
        win=win,
        name='imageYesButton_9', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_9 = visual.ImageStim(
        win=win,
        name='imageNoButton_9', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_9 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_9.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof9_enjoy_class" ---
    DidYouEnjoyThisProf_9 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_9',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf9_2 = visual.ImageStim(
        win=win,
        name='imageProf9_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image9.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_26 = visual.ImageStim(
        win=win,
        name='imageYesButton_26', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_26 = visual.ImageStim(
        win=win,
        name='imageNoButton_26', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_26 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_26.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof10" ---
    HaveYouTakenThisProf_10 = visual.TextStim(win=win, name='HaveYouTakenThisProf_10',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf10 = visual.ImageStim(
        win=win,
        name='imageProf10', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image10.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_10 = visual.ImageStim(
        win=win,
        name='imageYesButton_10', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_10 = visual.ImageStim(
        win=win,
        name='imageNoButton_10', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_10 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_10.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof10_enjoy_class" ---
    DidYouEnjoyThisProf_10 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_10',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf10_2 = visual.ImageStim(
        win=win,
        name='imageProf10_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image10.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_27 = visual.ImageStim(
        win=win,
        name='imageYesButton_27', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_27 = visual.ImageStim(
        win=win,
        name='imageNoButton_27', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_27 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_27.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof11" ---
    HaveYouTakenThisProf_11 = visual.TextStim(win=win, name='HaveYouTakenThisProf_11',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf11 = visual.ImageStim(
        win=win,
        name='imageProf11', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image11.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_11 = visual.ImageStim(
        win=win,
        name='imageYesButton_11', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_11 = visual.ImageStim(
        win=win,
        name='imageNoButton_11', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_11 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_11.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof11_enjoy_class" ---
    DidYouEnjoyThisProf_11 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_11',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf11_2 = visual.ImageStim(
        win=win,
        name='imageProf11_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image11.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_28 = visual.ImageStim(
        win=win,
        name='imageYesButton_28', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_28 = visual.ImageStim(
        win=win,
        name='imageNoButton_28', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_28 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_28.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof12" ---
    HaveYouTakenThisProf_12 = visual.TextStim(win=win, name='HaveYouTakenThisProf_12',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf12 = visual.ImageStim(
        win=win,
        name='imageProf12', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image12.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_12 = visual.ImageStim(
        win=win,
        name='imageYesButton_12', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_12 = visual.ImageStim(
        win=win,
        name='imageNoButton_12', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_12 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_12.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof12_enjoy_class" ---
    DidYouEnjoyThisProf_12 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_12',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf12_2 = visual.ImageStim(
        win=win,
        name='imageProf12_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image12.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_29 = visual.ImageStim(
        win=win,
        name='imageYesButton_29', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_29 = visual.ImageStim(
        win=win,
        name='imageNoButton_29', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_29 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_29.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof13" ---
    HaveYouTakenThisProf_13 = visual.TextStim(win=win, name='HaveYouTakenThisProf_13',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf13 = visual.ImageStim(
        win=win,
        name='imageProf13', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image13.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_13 = visual.ImageStim(
        win=win,
        name='imageYesButton_13', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_13 = visual.ImageStim(
        win=win,
        name='imageNoButton_13', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_13 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_13.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof13_enjoy_class" ---
    DidYouEnjoyThisProf_13 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_13',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf13_2 = visual.ImageStim(
        win=win,
        name='imageProf13_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image13.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_30 = visual.ImageStim(
        win=win,
        name='imageYesButton_30', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_30 = visual.ImageStim(
        win=win,
        name='imageNoButton_30', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_30 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_30.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof14" ---
    HaveYouTakenThisProf_14 = visual.TextStim(win=win, name='HaveYouTakenThisProf_14',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf14 = visual.ImageStim(
        win=win,
        name='imageProf14', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image14.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_14 = visual.ImageStim(
        win=win,
        name='imageYesButton_14', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_14 = visual.ImageStim(
        win=win,
        name='imageNoButton_14', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_14 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_14.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof14_enjoy_class" ---
    DidYouEnjoyThisProf_14 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_14',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf14_2 = visual.ImageStim(
        win=win,
        name='imageProf14_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image14.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_31 = visual.ImageStim(
        win=win,
        name='imageYesButton_31', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_31 = visual.ImageStim(
        win=win,
        name='imageNoButton_31', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_31 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_31.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof15" ---
    HaveYouTakenThisProf_15 = visual.TextStim(win=win, name='HaveYouTakenThisProf_15',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf15 = visual.ImageStim(
        win=win,
        name='imageProf15', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image15.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_15 = visual.ImageStim(
        win=win,
        name='imageYesButton_15', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_15 = visual.ImageStim(
        win=win,
        name='imageNoButton_15', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_15 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_15.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof15_enjoy_class" ---
    DidYouEnjoyThisProf_15 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_15',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf15_2 = visual.ImageStim(
        win=win,
        name='imageProf15_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image15.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_33 = visual.ImageStim(
        win=win,
        name='imageYesButton_33', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_32 = visual.ImageStim(
        win=win,
        name='imageNoButton_32', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_32 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_32.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof16" ---
    HaveYouTakenThisProf_16 = visual.TextStim(win=win, name='HaveYouTakenThisProf_16',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf16 = visual.ImageStim(
        win=win,
        name='imageProf16', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image16.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_16 = visual.ImageStim(
        win=win,
        name='imageYesButton_16', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_16 = visual.ImageStim(
        win=win,
        name='imageNoButton_16', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_16 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_16.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof16_enjoy_class" ---
    DidYouEnjoyThisProf_16 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_16',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf16_2 = visual.ImageStim(
        win=win,
        name='imageProf16_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image16.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_34 = visual.ImageStim(
        win=win,
        name='imageYesButton_34', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_33 = visual.ImageStim(
        win=win,
        name='imageNoButton_33', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_33 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_33.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof17" ---
    HaveYouTakenThisProf_17 = visual.TextStim(win=win, name='HaveYouTakenThisProf_17',
        text='Have you taken a class with this Professor?',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf17 = visual.ImageStim(
        win=win,
        name='imageProf17', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image17.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_17 = visual.ImageStim(
        win=win,
        name='imageYesButton_17', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_17 = visual.ImageStim(
        win=win,
        name='imageNoButton_17', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_17 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_17.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "BlankScreen" ---
    Next_prof = visual.TextStim(win=win, name='Next_prof',
        text='The next question is coming up...',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "Prof17_enjoy_class" ---
    DidYouEnjoyThisProf_17 = visual.TextStim(win=win, name='DidYouEnjoyThisProf_17',
        text='Did you enjoy the class with this Professor? If not applicable, do not click on the screen.',
        font='Open Sans',
        pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    imageProf17_2 = visual.ImageStim(
        win=win,
        name='imageProf17_2', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/image17.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.15), size=(0.5, 0.45),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    imageYesButton_35 = visual.ImageStim(
        win=win,
        name='imageYesButton_35', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/yes_button.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    imageNoButton_34 = visual.ImageStim(
        win=win,
        name='imageNoButton_34', 
        image='C:/Users/hiyab/OneDrive/Desktop/Lab Images/no_button.png', mask=None, anchor='center',
        ori=0.0, pos=(0.25, -0.3), size=(0.25, 0.25),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    mouse_34 = event.Mouse(win=win)
    x, y = [None, None]
    mouse_34.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "ThankYouScreen" ---
    textThankYouMessage = visual.TextStim(win=win, name='textThankYouMessage',
        text='Thank you for your time!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "WelcomeScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('WelcomeScreen.started', globalClock.getTime())
    keySpacebar.keys = []
    keySpacebar.rt = []
    _keySpacebar_allKeys = []
    # keep track of which components have finished
    WelcomeScreenComponents = [text, keySpacebar]
    for thisComponent in WelcomeScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "WelcomeScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *keySpacebar* updates
        waitOnFlip = False
        
        # if keySpacebar is starting this frame...
        if keySpacebar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keySpacebar.frameNStart = frameN  # exact frame index
            keySpacebar.tStart = t  # local t and not account for scr refresh
            keySpacebar.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keySpacebar, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keySpacebar.started')
            # update status
            keySpacebar.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keySpacebar.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keySpacebar.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keySpacebar.status == STARTED and not waitOnFlip:
            theseKeys = keySpacebar.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _keySpacebar_allKeys.extend(theseKeys)
            if len(_keySpacebar_allKeys):
                keySpacebar.keys = _keySpacebar_allKeys[-1].name  # just the last key pressed
                keySpacebar.rt = _keySpacebar_allKeys[-1].rt
                keySpacebar.duration = _keySpacebar_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in WelcomeScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "WelcomeScreen" ---
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('WelcomeScreen.stopped', globalClock.getTime())
    # check responses
    if keySpacebar.keys in ['', [], None]:  # No response was made
        keySpacebar.keys = None
    thisExp.addData('keySpacebar.keys',keySpacebar.keys)
    if keySpacebar.keys != None:  # we had a response
        thisExp.addData('keySpacebar.rt', keySpacebar.rt)
        thisExp.addData('keySpacebar.duration', keySpacebar.duration)
    thisExp.nextEntry()
    # the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Prof1_taken_prof" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof1_taken_prof.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse
    mouse.x = []
    mouse.y = []
    mouse.leftButton = []
    mouse.midButton = []
    mouse.rightButton = []
    mouse.time = []
    mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof1_taken_profComponents = [HaveYouTakenThisProf, imageProf1, imageYesButton, imageNoButton, mouse]
    for thisComponent in Prof1_taken_profComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof1_taken_prof" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf* updates
        
        # if HaveYouTakenThisProf is starting this frame...
        if HaveYouTakenThisProf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf.started')
            # update status
            HaveYouTakenThisProf.status = STARTED
            HaveYouTakenThisProf.setAutoDraw(True)
        
        # if HaveYouTakenThisProf is active this frame...
        if HaveYouTakenThisProf.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf is stopping this frame...
        if HaveYouTakenThisProf.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf.stopped')
                # update status
                HaveYouTakenThisProf.status = FINISHED
                HaveYouTakenThisProf.setAutoDraw(False)
        
        # *imageProf1* updates
        
        # if imageProf1 is starting this frame...
        if imageProf1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf1.frameNStart = frameN  # exact frame index
            imageProf1.tStart = t  # local t and not account for scr refresh
            imageProf1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf1.started')
            # update status
            imageProf1.status = STARTED
            imageProf1.setAutoDraw(True)
        
        # if imageProf1 is active this frame...
        if imageProf1.status == STARTED:
            # update params
            pass
        
        # if imageProf1 is stopping this frame...
        if imageProf1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf1.tStop = t  # not accounting for scr refresh
                imageProf1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf1.stopped')
                # update status
                imageProf1.status = FINISHED
                imageProf1.setAutoDraw(False)
        
        # *imageYesButton* updates
        
        # if imageYesButton is starting this frame...
        if imageYesButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton.frameNStart = frameN  # exact frame index
            imageYesButton.tStart = t  # local t and not account for scr refresh
            imageYesButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton.started')
            # update status
            imageYesButton.status = STARTED
            imageYesButton.setAutoDraw(True)
        
        # if imageYesButton is active this frame...
        if imageYesButton.status == STARTED:
            # update params
            pass
        
        # if imageYesButton is stopping this frame...
        if imageYesButton.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton.tStop = t  # not accounting for scr refresh
                imageYesButton.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton.stopped')
                # update status
                imageYesButton.status = FINISHED
                imageYesButton.setAutoDraw(False)
        
        # *imageNoButton* updates
        
        # if imageNoButton is starting this frame...
        if imageNoButton.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton.frameNStart = frameN  # exact frame index
            imageNoButton.tStart = t  # local t and not account for scr refresh
            imageNoButton.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton.started')
            # update status
            imageNoButton.status = STARTED
            imageNoButton.setAutoDraw(True)
        
        # if imageNoButton is active this frame...
        if imageNoButton.status == STARTED:
            # update params
            pass
        
        # if imageNoButton is stopping this frame...
        if imageNoButton.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton.tStop = t  # not accounting for scr refresh
                imageNoButton.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton.stopped')
                # update status
                imageNoButton.status = FINISHED
                imageNoButton.setAutoDraw(False)
        # *mouse* updates
        
        # if mouse is starting this frame...
        if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse.frameNStart = frameN  # exact frame index
            mouse.tStart = t  # local t and not account for scr refresh
            mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse.started', t)
            # update status
            mouse.status = STARTED
            mouse.mouseClock.reset()
            prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse is stopping this frame...
        if mouse.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse.tStop = t  # not accounting for scr refresh
                mouse.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse.stopped', t)
                # update status
                mouse.status = FINISHED
        if mouse.status == STARTED:  # only update if started and not finished!
            buttons = mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse):
                            gotValidClick = True
                            mouse.clicked_name.append(obj.name)
                    x, y = mouse.getPos()
                    mouse.x.append(x)
                    mouse.y.append(y)
                    buttons = mouse.getPressed()
                    mouse.leftButton.append(buttons[0])
                    mouse.midButton.append(buttons[1])
                    mouse.rightButton.append(buttons[2])
                    mouse.time.append(mouse.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof1_taken_profComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof1_taken_prof" ---
    for thisComponent in Prof1_taken_profComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof1_taken_prof.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse.x', mouse.x)
    thisExp.addData('mouse.y', mouse.y)
    thisExp.addData('mouse.leftButton', mouse.leftButton)
    thisExp.addData('mouse.midButton', mouse.midButton)
    thisExp.addData('mouse.rightButton', mouse.rightButton)
    thisExp.addData('mouse.time', mouse.time)
    thisExp.addData('mouse.clicked_name', mouse.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof1_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof1_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_18
    mouse_18.x = []
    mouse_18.y = []
    mouse_18.leftButton = []
    mouse_18.midButton = []
    mouse_18.rightButton = []
    mouse_18.time = []
    mouse_18.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof1_enjoy_classComponents = [DidYouEnjoyThisProf, imageProf1_1, imageYesButton_18, imageNoButton_18, mouse_18]
    for thisComponent in Prof1_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof1_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf* updates
        
        # if DidYouEnjoyThisProf is starting this frame...
        if DidYouEnjoyThisProf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf.started')
            # update status
            DidYouEnjoyThisProf.status = STARTED
            DidYouEnjoyThisProf.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf is active this frame...
        if DidYouEnjoyThisProf.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf is stopping this frame...
        if DidYouEnjoyThisProf.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf.stopped')
                # update status
                DidYouEnjoyThisProf.status = FINISHED
                DidYouEnjoyThisProf.setAutoDraw(False)
        
        # *imageProf1_1* updates
        
        # if imageProf1_1 is starting this frame...
        if imageProf1_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf1_1.frameNStart = frameN  # exact frame index
            imageProf1_1.tStart = t  # local t and not account for scr refresh
            imageProf1_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf1_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf1_1.started')
            # update status
            imageProf1_1.status = STARTED
            imageProf1_1.setAutoDraw(True)
        
        # if imageProf1_1 is active this frame...
        if imageProf1_1.status == STARTED:
            # update params
            pass
        
        # if imageProf1_1 is stopping this frame...
        if imageProf1_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf1_1.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf1_1.tStop = t  # not accounting for scr refresh
                imageProf1_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf1_1.stopped')
                # update status
                imageProf1_1.status = FINISHED
                imageProf1_1.setAutoDraw(False)
        
        # *imageYesButton_18* updates
        
        # if imageYesButton_18 is starting this frame...
        if imageYesButton_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_18.frameNStart = frameN  # exact frame index
            imageYesButton_18.tStart = t  # local t and not account for scr refresh
            imageYesButton_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_18.started')
            # update status
            imageYesButton_18.status = STARTED
            imageYesButton_18.setAutoDraw(True)
        
        # if imageYesButton_18 is active this frame...
        if imageYesButton_18.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_18 is stopping this frame...
        if imageYesButton_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_18.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_18.tStop = t  # not accounting for scr refresh
                imageYesButton_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_18.stopped')
                # update status
                imageYesButton_18.status = FINISHED
                imageYesButton_18.setAutoDraw(False)
        
        # *imageNoButton_18* updates
        
        # if imageNoButton_18 is starting this frame...
        if imageNoButton_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_18.frameNStart = frameN  # exact frame index
            imageNoButton_18.tStart = t  # local t and not account for scr refresh
            imageNoButton_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_18.started')
            # update status
            imageNoButton_18.status = STARTED
            imageNoButton_18.setAutoDraw(True)
        
        # if imageNoButton_18 is active this frame...
        if imageNoButton_18.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_18 is stopping this frame...
        if imageNoButton_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_18.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_18.tStop = t  # not accounting for scr refresh
                imageNoButton_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_18.stopped')
                # update status
                imageNoButton_18.status = FINISHED
                imageNoButton_18.setAutoDraw(False)
        # *mouse_18* updates
        
        # if mouse_18 is starting this frame...
        if mouse_18.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_18.frameNStart = frameN  # exact frame index
            mouse_18.tStart = t  # local t and not account for scr refresh
            mouse_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_18.started', t)
            # update status
            mouse_18.status = STARTED
            mouse_18.mouseClock.reset()
            prevButtonState = mouse_18.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_18 is stopping this frame...
        if mouse_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_18.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_18.tStop = t  # not accounting for scr refresh
                mouse_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_18.stopped', t)
                # update status
                mouse_18.status = FINISHED
        if mouse_18.status == STARTED:  # only update if started and not finished!
            buttons = mouse_18.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_18):
                            gotValidClick = True
                            mouse_18.clicked_name.append(obj.name)
                    x, y = mouse_18.getPos()
                    mouse_18.x.append(x)
                    mouse_18.y.append(y)
                    buttons = mouse_18.getPressed()
                    mouse_18.leftButton.append(buttons[0])
                    mouse_18.midButton.append(buttons[1])
                    mouse_18.rightButton.append(buttons[2])
                    mouse_18.time.append(mouse_18.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof1_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof1_enjoy_class" ---
    for thisComponent in Prof1_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof1_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_18.x', mouse_18.x)
    thisExp.addData('mouse_18.y', mouse_18.y)
    thisExp.addData('mouse_18.leftButton', mouse_18.leftButton)
    thisExp.addData('mouse_18.midButton', mouse_18.midButton)
    thisExp.addData('mouse_18.rightButton', mouse_18.rightButton)
    thisExp.addData('mouse_18.time', mouse_18.time)
    thisExp.addData('mouse_18.clicked_name', mouse_18.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof2.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_2
    mouse_2.x = []
    mouse_2.y = []
    mouse_2.leftButton = []
    mouse_2.midButton = []
    mouse_2.rightButton = []
    mouse_2.time = []
    mouse_2.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof2Components = [HaveYouTakenThisProf_2, imageProf2, imageYesButton_2, imageNoButton_2, mouse_2]
    for thisComponent in Prof2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_2* updates
        
        # if HaveYouTakenThisProf_2 is starting this frame...
        if HaveYouTakenThisProf_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_2.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_2.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_2.started')
            # update status
            HaveYouTakenThisProf_2.status = STARTED
            HaveYouTakenThisProf_2.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_2 is active this frame...
        if HaveYouTakenThisProf_2.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_2 is stopping this frame...
        if HaveYouTakenThisProf_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_2.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_2.stopped')
                # update status
                HaveYouTakenThisProf_2.status = FINISHED
                HaveYouTakenThisProf_2.setAutoDraw(False)
        
        # *imageProf2* updates
        
        # if imageProf2 is starting this frame...
        if imageProf2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf2.frameNStart = frameN  # exact frame index
            imageProf2.tStart = t  # local t and not account for scr refresh
            imageProf2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf2.started')
            # update status
            imageProf2.status = STARTED
            imageProf2.setAutoDraw(True)
        
        # if imageProf2 is active this frame...
        if imageProf2.status == STARTED:
            # update params
            pass
        
        # if imageProf2 is stopping this frame...
        if imageProf2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf2.tStop = t  # not accounting for scr refresh
                imageProf2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf2.stopped')
                # update status
                imageProf2.status = FINISHED
                imageProf2.setAutoDraw(False)
        
        # *imageYesButton_2* updates
        
        # if imageYesButton_2 is starting this frame...
        if imageYesButton_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_2.frameNStart = frameN  # exact frame index
            imageYesButton_2.tStart = t  # local t and not account for scr refresh
            imageYesButton_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_2.started')
            # update status
            imageYesButton_2.status = STARTED
            imageYesButton_2.setAutoDraw(True)
        
        # if imageYesButton_2 is active this frame...
        if imageYesButton_2.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_2 is stopping this frame...
        if imageYesButton_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_2.tStop = t  # not accounting for scr refresh
                imageYesButton_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_2.stopped')
                # update status
                imageYesButton_2.status = FINISHED
                imageYesButton_2.setAutoDraw(False)
        
        # *imageNoButton_2* updates
        
        # if imageNoButton_2 is starting this frame...
        if imageNoButton_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_2.frameNStart = frameN  # exact frame index
            imageNoButton_2.tStart = t  # local t and not account for scr refresh
            imageNoButton_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_2.started')
            # update status
            imageNoButton_2.status = STARTED
            imageNoButton_2.setAutoDraw(True)
        
        # if imageNoButton_2 is active this frame...
        if imageNoButton_2.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_2 is stopping this frame...
        if imageNoButton_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_2.tStop = t  # not accounting for scr refresh
                imageNoButton_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_2.stopped')
                # update status
                imageNoButton_2.status = FINISHED
                imageNoButton_2.setAutoDraw(False)
        # *mouse_2* updates
        
        # if mouse_2 is starting this frame...
        if mouse_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_2.frameNStart = frameN  # exact frame index
            mouse_2.tStart = t  # local t and not account for scr refresh
            mouse_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_2.started', t)
            # update status
            mouse_2.status = STARTED
            mouse_2.mouseClock.reset()
            prevButtonState = mouse_2.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_2 is stopping this frame...
        if mouse_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_2.tStop = t  # not accounting for scr refresh
                mouse_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_2.stopped', t)
                # update status
                mouse_2.status = FINISHED
        if mouse_2.status == STARTED:  # only update if started and not finished!
            buttons = mouse_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_2):
                            gotValidClick = True
                            mouse_2.clicked_name.append(obj.name)
                    x, y = mouse_2.getPos()
                    mouse_2.x.append(x)
                    mouse_2.y.append(y)
                    buttons = mouse_2.getPressed()
                    mouse_2.leftButton.append(buttons[0])
                    mouse_2.midButton.append(buttons[1])
                    mouse_2.rightButton.append(buttons[2])
                    mouse_2.time.append(mouse_2.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof2" ---
    for thisComponent in Prof2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof2.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_2.x', mouse_2.x)
    thisExp.addData('mouse_2.y', mouse_2.y)
    thisExp.addData('mouse_2.leftButton', mouse_2.leftButton)
    thisExp.addData('mouse_2.midButton', mouse_2.midButton)
    thisExp.addData('mouse_2.rightButton', mouse_2.rightButton)
    thisExp.addData('mouse_2.time', mouse_2.time)
    thisExp.addData('mouse_2.clicked_name', mouse_2.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof2_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof2_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_19
    mouse_19.x = []
    mouse_19.y = []
    mouse_19.leftButton = []
    mouse_19.midButton = []
    mouse_19.rightButton = []
    mouse_19.time = []
    mouse_19.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof2_enjoy_classComponents = [DidYouEnjoyThisProf_2, imageProf2_2, imageYesButton_19, imageNoButton_19, mouse_19]
    for thisComponent in Prof2_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof2_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_2* updates
        
        # if DidYouEnjoyThisProf_2 is starting this frame...
        if DidYouEnjoyThisProf_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_2.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_2.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_2.started')
            # update status
            DidYouEnjoyThisProf_2.status = STARTED
            DidYouEnjoyThisProf_2.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_2 is active this frame...
        if DidYouEnjoyThisProf_2.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_2 is stopping this frame...
        if DidYouEnjoyThisProf_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_2.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_2.stopped')
                # update status
                DidYouEnjoyThisProf_2.status = FINISHED
                DidYouEnjoyThisProf_2.setAutoDraw(False)
        
        # *imageProf2_2* updates
        
        # if imageProf2_2 is starting this frame...
        if imageProf2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf2_2.frameNStart = frameN  # exact frame index
            imageProf2_2.tStart = t  # local t and not account for scr refresh
            imageProf2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf2_2.started')
            # update status
            imageProf2_2.status = STARTED
            imageProf2_2.setAutoDraw(True)
        
        # if imageProf2_2 is active this frame...
        if imageProf2_2.status == STARTED:
            # update params
            pass
        
        # if imageProf2_2 is stopping this frame...
        if imageProf2_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf2_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf2_2.tStop = t  # not accounting for scr refresh
                imageProf2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf2_2.stopped')
                # update status
                imageProf2_2.status = FINISHED
                imageProf2_2.setAutoDraw(False)
        
        # *imageYesButton_19* updates
        
        # if imageYesButton_19 is starting this frame...
        if imageYesButton_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_19.frameNStart = frameN  # exact frame index
            imageYesButton_19.tStart = t  # local t and not account for scr refresh
            imageYesButton_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_19.started')
            # update status
            imageYesButton_19.status = STARTED
            imageYesButton_19.setAutoDraw(True)
        
        # if imageYesButton_19 is active this frame...
        if imageYesButton_19.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_19 is stopping this frame...
        if imageYesButton_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_19.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_19.tStop = t  # not accounting for scr refresh
                imageYesButton_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_19.stopped')
                # update status
                imageYesButton_19.status = FINISHED
                imageYesButton_19.setAutoDraw(False)
        
        # *imageNoButton_19* updates
        
        # if imageNoButton_19 is starting this frame...
        if imageNoButton_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_19.frameNStart = frameN  # exact frame index
            imageNoButton_19.tStart = t  # local t and not account for scr refresh
            imageNoButton_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_19.started')
            # update status
            imageNoButton_19.status = STARTED
            imageNoButton_19.setAutoDraw(True)
        
        # if imageNoButton_19 is active this frame...
        if imageNoButton_19.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_19 is stopping this frame...
        if imageNoButton_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_19.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_19.tStop = t  # not accounting for scr refresh
                imageNoButton_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_19.stopped')
                # update status
                imageNoButton_19.status = FINISHED
                imageNoButton_19.setAutoDraw(False)
        # *mouse_19* updates
        
        # if mouse_19 is starting this frame...
        if mouse_19.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_19.frameNStart = frameN  # exact frame index
            mouse_19.tStart = t  # local t and not account for scr refresh
            mouse_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_19.started', t)
            # update status
            mouse_19.status = STARTED
            mouse_19.mouseClock.reset()
            prevButtonState = mouse_19.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_19 is stopping this frame...
        if mouse_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_19.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_19.tStop = t  # not accounting for scr refresh
                mouse_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_19.stopped', t)
                # update status
                mouse_19.status = FINISHED
        if mouse_19.status == STARTED:  # only update if started and not finished!
            buttons = mouse_19.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_19):
                            gotValidClick = True
                            mouse_19.clicked_name.append(obj.name)
                    x, y = mouse_19.getPos()
                    mouse_19.x.append(x)
                    mouse_19.y.append(y)
                    buttons = mouse_19.getPressed()
                    mouse_19.leftButton.append(buttons[0])
                    mouse_19.midButton.append(buttons[1])
                    mouse_19.rightButton.append(buttons[2])
                    mouse_19.time.append(mouse_19.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof2_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof2_enjoy_class" ---
    for thisComponent in Prof2_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof2_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_19.x', mouse_19.x)
    thisExp.addData('mouse_19.y', mouse_19.y)
    thisExp.addData('mouse_19.leftButton', mouse_19.leftButton)
    thisExp.addData('mouse_19.midButton', mouse_19.midButton)
    thisExp.addData('mouse_19.rightButton', mouse_19.rightButton)
    thisExp.addData('mouse_19.time', mouse_19.time)
    thisExp.addData('mouse_19.clicked_name', mouse_19.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof3.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_3
    mouse_3.x = []
    mouse_3.y = []
    mouse_3.leftButton = []
    mouse_3.midButton = []
    mouse_3.rightButton = []
    mouse_3.time = []
    mouse_3.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof3Components = [HaveYouTakenThisProf_3, imageProf3, imageYesButton_3, imageNoButton_3, mouse_3]
    for thisComponent in Prof3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_3* updates
        
        # if HaveYouTakenThisProf_3 is starting this frame...
        if HaveYouTakenThisProf_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_3.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_3.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_3.started')
            # update status
            HaveYouTakenThisProf_3.status = STARTED
            HaveYouTakenThisProf_3.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_3 is active this frame...
        if HaveYouTakenThisProf_3.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_3 is stopping this frame...
        if HaveYouTakenThisProf_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_3.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_3.stopped')
                # update status
                HaveYouTakenThisProf_3.status = FINISHED
                HaveYouTakenThisProf_3.setAutoDraw(False)
        
        # *imageProf3* updates
        
        # if imageProf3 is starting this frame...
        if imageProf3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf3.frameNStart = frameN  # exact frame index
            imageProf3.tStart = t  # local t and not account for scr refresh
            imageProf3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf3.started')
            # update status
            imageProf3.status = STARTED
            imageProf3.setAutoDraw(True)
        
        # if imageProf3 is active this frame...
        if imageProf3.status == STARTED:
            # update params
            pass
        
        # if imageProf3 is stopping this frame...
        if imageProf3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf3.tStop = t  # not accounting for scr refresh
                imageProf3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf3.stopped')
                # update status
                imageProf3.status = FINISHED
                imageProf3.setAutoDraw(False)
        
        # *imageYesButton_3* updates
        
        # if imageYesButton_3 is starting this frame...
        if imageYesButton_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_3.frameNStart = frameN  # exact frame index
            imageYesButton_3.tStart = t  # local t and not account for scr refresh
            imageYesButton_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_3.started')
            # update status
            imageYesButton_3.status = STARTED
            imageYesButton_3.setAutoDraw(True)
        
        # if imageYesButton_3 is active this frame...
        if imageYesButton_3.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_3 is stopping this frame...
        if imageYesButton_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_3.tStop = t  # not accounting for scr refresh
                imageYesButton_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_3.stopped')
                # update status
                imageYesButton_3.status = FINISHED
                imageYesButton_3.setAutoDraw(False)
        
        # *imageNoButton_3* updates
        
        # if imageNoButton_3 is starting this frame...
        if imageNoButton_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_3.frameNStart = frameN  # exact frame index
            imageNoButton_3.tStart = t  # local t and not account for scr refresh
            imageNoButton_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_3.started')
            # update status
            imageNoButton_3.status = STARTED
            imageNoButton_3.setAutoDraw(True)
        
        # if imageNoButton_3 is active this frame...
        if imageNoButton_3.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_3 is stopping this frame...
        if imageNoButton_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_3.tStop = t  # not accounting for scr refresh
                imageNoButton_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_3.stopped')
                # update status
                imageNoButton_3.status = FINISHED
                imageNoButton_3.setAutoDraw(False)
        # *mouse_3* updates
        
        # if mouse_3 is starting this frame...
        if mouse_3.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_3.frameNStart = frameN  # exact frame index
            mouse_3.tStart = t  # local t and not account for scr refresh
            mouse_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_3.started', t)
            # update status
            mouse_3.status = STARTED
            mouse_3.mouseClock.reset()
            prevButtonState = mouse_3.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_3 is stopping this frame...
        if mouse_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_3.tStop = t  # not accounting for scr refresh
                mouse_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_3.stopped', t)
                # update status
                mouse_3.status = FINISHED
        if mouse_3.status == STARTED:  # only update if started and not finished!
            buttons = mouse_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_3):
                            gotValidClick = True
                            mouse_3.clicked_name.append(obj.name)
                    x, y = mouse_3.getPos()
                    mouse_3.x.append(x)
                    mouse_3.y.append(y)
                    buttons = mouse_3.getPressed()
                    mouse_3.leftButton.append(buttons[0])
                    mouse_3.midButton.append(buttons[1])
                    mouse_3.rightButton.append(buttons[2])
                    mouse_3.time.append(mouse_3.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof3" ---
    for thisComponent in Prof3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof3.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_3.x', mouse_3.x)
    thisExp.addData('mouse_3.y', mouse_3.y)
    thisExp.addData('mouse_3.leftButton', mouse_3.leftButton)
    thisExp.addData('mouse_3.midButton', mouse_3.midButton)
    thisExp.addData('mouse_3.rightButton', mouse_3.rightButton)
    thisExp.addData('mouse_3.time', mouse_3.time)
    thisExp.addData('mouse_3.clicked_name', mouse_3.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof3_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof3_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_20
    mouse_20.x = []
    mouse_20.y = []
    mouse_20.leftButton = []
    mouse_20.midButton = []
    mouse_20.rightButton = []
    mouse_20.time = []
    mouse_20.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof3_enjoy_classComponents = [DidYouEnjoyThisProf_3, imageProf3_2, imageYesButton_20, imageNoButton_20, mouse_20]
    for thisComponent in Prof3_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof3_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_3* updates
        
        # if DidYouEnjoyThisProf_3 is starting this frame...
        if DidYouEnjoyThisProf_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_3.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_3.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_3.started')
            # update status
            DidYouEnjoyThisProf_3.status = STARTED
            DidYouEnjoyThisProf_3.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_3 is active this frame...
        if DidYouEnjoyThisProf_3.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_3 is stopping this frame...
        if DidYouEnjoyThisProf_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_3.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_3.stopped')
                # update status
                DidYouEnjoyThisProf_3.status = FINISHED
                DidYouEnjoyThisProf_3.setAutoDraw(False)
        
        # *imageProf3_2* updates
        
        # if imageProf3_2 is starting this frame...
        if imageProf3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf3_2.frameNStart = frameN  # exact frame index
            imageProf3_2.tStart = t  # local t and not account for scr refresh
            imageProf3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf3_2.started')
            # update status
            imageProf3_2.status = STARTED
            imageProf3_2.setAutoDraw(True)
        
        # if imageProf3_2 is active this frame...
        if imageProf3_2.status == STARTED:
            # update params
            pass
        
        # if imageProf3_2 is stopping this frame...
        if imageProf3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf3_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf3_2.tStop = t  # not accounting for scr refresh
                imageProf3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf3_2.stopped')
                # update status
                imageProf3_2.status = FINISHED
                imageProf3_2.setAutoDraw(False)
        
        # *imageYesButton_20* updates
        
        # if imageYesButton_20 is starting this frame...
        if imageYesButton_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_20.frameNStart = frameN  # exact frame index
            imageYesButton_20.tStart = t  # local t and not account for scr refresh
            imageYesButton_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_20.started')
            # update status
            imageYesButton_20.status = STARTED
            imageYesButton_20.setAutoDraw(True)
        
        # if imageYesButton_20 is active this frame...
        if imageYesButton_20.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_20 is stopping this frame...
        if imageYesButton_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_20.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_20.tStop = t  # not accounting for scr refresh
                imageYesButton_20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_20.stopped')
                # update status
                imageYesButton_20.status = FINISHED
                imageYesButton_20.setAutoDraw(False)
        
        # *imageNoButton_20* updates
        
        # if imageNoButton_20 is starting this frame...
        if imageNoButton_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_20.frameNStart = frameN  # exact frame index
            imageNoButton_20.tStart = t  # local t and not account for scr refresh
            imageNoButton_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_20.started')
            # update status
            imageNoButton_20.status = STARTED
            imageNoButton_20.setAutoDraw(True)
        
        # if imageNoButton_20 is active this frame...
        if imageNoButton_20.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_20 is stopping this frame...
        if imageNoButton_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_20.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_20.tStop = t  # not accounting for scr refresh
                imageNoButton_20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_20.stopped')
                # update status
                imageNoButton_20.status = FINISHED
                imageNoButton_20.setAutoDraw(False)
        # *mouse_20* updates
        
        # if mouse_20 is starting this frame...
        if mouse_20.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_20.frameNStart = frameN  # exact frame index
            mouse_20.tStart = t  # local t and not account for scr refresh
            mouse_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_20.started', t)
            # update status
            mouse_20.status = STARTED
            mouse_20.mouseClock.reset()
            prevButtonState = mouse_20.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_20 is stopping this frame...
        if mouse_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_20.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_20.tStop = t  # not accounting for scr refresh
                mouse_20.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_20.stopped', t)
                # update status
                mouse_20.status = FINISHED
        if mouse_20.status == STARTED:  # only update if started and not finished!
            buttons = mouse_20.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_20):
                            gotValidClick = True
                            mouse_20.clicked_name.append(obj.name)
                    x, y = mouse_20.getPos()
                    mouse_20.x.append(x)
                    mouse_20.y.append(y)
                    buttons = mouse_20.getPressed()
                    mouse_20.leftButton.append(buttons[0])
                    mouse_20.midButton.append(buttons[1])
                    mouse_20.rightButton.append(buttons[2])
                    mouse_20.time.append(mouse_20.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof3_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof3_enjoy_class" ---
    for thisComponent in Prof3_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof3_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_20.x', mouse_20.x)
    thisExp.addData('mouse_20.y', mouse_20.y)
    thisExp.addData('mouse_20.leftButton', mouse_20.leftButton)
    thisExp.addData('mouse_20.midButton', mouse_20.midButton)
    thisExp.addData('mouse_20.rightButton', mouse_20.rightButton)
    thisExp.addData('mouse_20.time', mouse_20.time)
    thisExp.addData('mouse_20.clicked_name', mouse_20.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof4.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_4
    mouse_4.x = []
    mouse_4.y = []
    mouse_4.leftButton = []
    mouse_4.midButton = []
    mouse_4.rightButton = []
    mouse_4.time = []
    mouse_4.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof4Components = [HaveYouTakenThisProf_4, imageProf4, imageYesButton_4, imageNoButton_4, mouse_4]
    for thisComponent in Prof4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_4* updates
        
        # if HaveYouTakenThisProf_4 is starting this frame...
        if HaveYouTakenThisProf_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_4.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_4.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_4.started')
            # update status
            HaveYouTakenThisProf_4.status = STARTED
            HaveYouTakenThisProf_4.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_4 is active this frame...
        if HaveYouTakenThisProf_4.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_4 is stopping this frame...
        if HaveYouTakenThisProf_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_4.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_4.stopped')
                # update status
                HaveYouTakenThisProf_4.status = FINISHED
                HaveYouTakenThisProf_4.setAutoDraw(False)
        
        # *imageProf4* updates
        
        # if imageProf4 is starting this frame...
        if imageProf4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf4.frameNStart = frameN  # exact frame index
            imageProf4.tStart = t  # local t and not account for scr refresh
            imageProf4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf4.started')
            # update status
            imageProf4.status = STARTED
            imageProf4.setAutoDraw(True)
        
        # if imageProf4 is active this frame...
        if imageProf4.status == STARTED:
            # update params
            pass
        
        # if imageProf4 is stopping this frame...
        if imageProf4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf4.tStop = t  # not accounting for scr refresh
                imageProf4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf4.stopped')
                # update status
                imageProf4.status = FINISHED
                imageProf4.setAutoDraw(False)
        
        # *imageYesButton_4* updates
        
        # if imageYesButton_4 is starting this frame...
        if imageYesButton_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_4.frameNStart = frameN  # exact frame index
            imageYesButton_4.tStart = t  # local t and not account for scr refresh
            imageYesButton_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_4.started')
            # update status
            imageYesButton_4.status = STARTED
            imageYesButton_4.setAutoDraw(True)
        
        # if imageYesButton_4 is active this frame...
        if imageYesButton_4.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_4 is stopping this frame...
        if imageYesButton_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_4.tStop = t  # not accounting for scr refresh
                imageYesButton_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_4.stopped')
                # update status
                imageYesButton_4.status = FINISHED
                imageYesButton_4.setAutoDraw(False)
        
        # *imageNoButton_4* updates
        
        # if imageNoButton_4 is starting this frame...
        if imageNoButton_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_4.frameNStart = frameN  # exact frame index
            imageNoButton_4.tStart = t  # local t and not account for scr refresh
            imageNoButton_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_4.started')
            # update status
            imageNoButton_4.status = STARTED
            imageNoButton_4.setAutoDraw(True)
        
        # if imageNoButton_4 is active this frame...
        if imageNoButton_4.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_4 is stopping this frame...
        if imageNoButton_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_4.tStop = t  # not accounting for scr refresh
                imageNoButton_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_4.stopped')
                # update status
                imageNoButton_4.status = FINISHED
                imageNoButton_4.setAutoDraw(False)
        # *mouse_4* updates
        
        # if mouse_4 is starting this frame...
        if mouse_4.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_4.frameNStart = frameN  # exact frame index
            mouse_4.tStart = t  # local t and not account for scr refresh
            mouse_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_4.started', t)
            # update status
            mouse_4.status = STARTED
            mouse_4.mouseClock.reset()
            prevButtonState = mouse_4.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_4 is stopping this frame...
        if mouse_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_4.tStop = t  # not accounting for scr refresh
                mouse_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_4.stopped', t)
                # update status
                mouse_4.status = FINISHED
        if mouse_4.status == STARTED:  # only update if started and not finished!
            buttons = mouse_4.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_4):
                            gotValidClick = True
                            mouse_4.clicked_name.append(obj.name)
                    x, y = mouse_4.getPos()
                    mouse_4.x.append(x)
                    mouse_4.y.append(y)
                    buttons = mouse_4.getPressed()
                    mouse_4.leftButton.append(buttons[0])
                    mouse_4.midButton.append(buttons[1])
                    mouse_4.rightButton.append(buttons[2])
                    mouse_4.time.append(mouse_4.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof4" ---
    for thisComponent in Prof4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof4.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_4.x', mouse_4.x)
    thisExp.addData('mouse_4.y', mouse_4.y)
    thisExp.addData('mouse_4.leftButton', mouse_4.leftButton)
    thisExp.addData('mouse_4.midButton', mouse_4.midButton)
    thisExp.addData('mouse_4.rightButton', mouse_4.rightButton)
    thisExp.addData('mouse_4.time', mouse_4.time)
    thisExp.addData('mouse_4.clicked_name', mouse_4.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof4_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof4_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_21
    mouse_21.x = []
    mouse_21.y = []
    mouse_21.leftButton = []
    mouse_21.midButton = []
    mouse_21.rightButton = []
    mouse_21.time = []
    mouse_21.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof4_enjoy_classComponents = [DidYouEnjoyThisProf_4, imageProf4_2, imageYesButton_21, imageNoButton_21, mouse_21]
    for thisComponent in Prof4_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof4_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_4* updates
        
        # if DidYouEnjoyThisProf_4 is starting this frame...
        if DidYouEnjoyThisProf_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_4.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_4.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_4.started')
            # update status
            DidYouEnjoyThisProf_4.status = STARTED
            DidYouEnjoyThisProf_4.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_4 is active this frame...
        if DidYouEnjoyThisProf_4.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_4 is stopping this frame...
        if DidYouEnjoyThisProf_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_4.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_4.stopped')
                # update status
                DidYouEnjoyThisProf_4.status = FINISHED
                DidYouEnjoyThisProf_4.setAutoDraw(False)
        
        # *imageProf4_2* updates
        
        # if imageProf4_2 is starting this frame...
        if imageProf4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf4_2.frameNStart = frameN  # exact frame index
            imageProf4_2.tStart = t  # local t and not account for scr refresh
            imageProf4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf4_2.started')
            # update status
            imageProf4_2.status = STARTED
            imageProf4_2.setAutoDraw(True)
        
        # if imageProf4_2 is active this frame...
        if imageProf4_2.status == STARTED:
            # update params
            pass
        
        # if imageProf4_2 is stopping this frame...
        if imageProf4_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf4_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf4_2.tStop = t  # not accounting for scr refresh
                imageProf4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf4_2.stopped')
                # update status
                imageProf4_2.status = FINISHED
                imageProf4_2.setAutoDraw(False)
        
        # *imageYesButton_21* updates
        
        # if imageYesButton_21 is starting this frame...
        if imageYesButton_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_21.frameNStart = frameN  # exact frame index
            imageYesButton_21.tStart = t  # local t and not account for scr refresh
            imageYesButton_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_21.started')
            # update status
            imageYesButton_21.status = STARTED
            imageYesButton_21.setAutoDraw(True)
        
        # if imageYesButton_21 is active this frame...
        if imageYesButton_21.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_21 is stopping this frame...
        if imageYesButton_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_21.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_21.tStop = t  # not accounting for scr refresh
                imageYesButton_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_21.stopped')
                # update status
                imageYesButton_21.status = FINISHED
                imageYesButton_21.setAutoDraw(False)
        
        # *imageNoButton_21* updates
        
        # if imageNoButton_21 is starting this frame...
        if imageNoButton_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_21.frameNStart = frameN  # exact frame index
            imageNoButton_21.tStart = t  # local t and not account for scr refresh
            imageNoButton_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_21.started')
            # update status
            imageNoButton_21.status = STARTED
            imageNoButton_21.setAutoDraw(True)
        
        # if imageNoButton_21 is active this frame...
        if imageNoButton_21.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_21 is stopping this frame...
        if imageNoButton_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_21.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_21.tStop = t  # not accounting for scr refresh
                imageNoButton_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_21.stopped')
                # update status
                imageNoButton_21.status = FINISHED
                imageNoButton_21.setAutoDraw(False)
        # *mouse_21* updates
        
        # if mouse_21 is starting this frame...
        if mouse_21.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_21.frameNStart = frameN  # exact frame index
            mouse_21.tStart = t  # local t and not account for scr refresh
            mouse_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_21, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_21.started', t)
            # update status
            mouse_21.status = STARTED
            mouse_21.mouseClock.reset()
            prevButtonState = mouse_21.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_21 is stopping this frame...
        if mouse_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_21.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_21.tStop = t  # not accounting for scr refresh
                mouse_21.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_21.stopped', t)
                # update status
                mouse_21.status = FINISHED
        if mouse_21.status == STARTED:  # only update if started and not finished!
            buttons = mouse_21.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_21):
                            gotValidClick = True
                            mouse_21.clicked_name.append(obj.name)
                    x, y = mouse_21.getPos()
                    mouse_21.x.append(x)
                    mouse_21.y.append(y)
                    buttons = mouse_21.getPressed()
                    mouse_21.leftButton.append(buttons[0])
                    mouse_21.midButton.append(buttons[1])
                    mouse_21.rightButton.append(buttons[2])
                    mouse_21.time.append(mouse_21.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof4_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof4_enjoy_class" ---
    for thisComponent in Prof4_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof4_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_21.x', mouse_21.x)
    thisExp.addData('mouse_21.y', mouse_21.y)
    thisExp.addData('mouse_21.leftButton', mouse_21.leftButton)
    thisExp.addData('mouse_21.midButton', mouse_21.midButton)
    thisExp.addData('mouse_21.rightButton', mouse_21.rightButton)
    thisExp.addData('mouse_21.time', mouse_21.time)
    thisExp.addData('mouse_21.clicked_name', mouse_21.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof5.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_5
    mouse_5.x = []
    mouse_5.y = []
    mouse_5.leftButton = []
    mouse_5.midButton = []
    mouse_5.rightButton = []
    mouse_5.time = []
    mouse_5.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof5Components = [HaveYouTakenThisProf_5, imageProf5, imageYesButton_5, imageNoButton_5, mouse_5]
    for thisComponent in Prof5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_5* updates
        
        # if HaveYouTakenThisProf_5 is starting this frame...
        if HaveYouTakenThisProf_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_5.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_5.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_5.started')
            # update status
            HaveYouTakenThisProf_5.status = STARTED
            HaveYouTakenThisProf_5.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_5 is active this frame...
        if HaveYouTakenThisProf_5.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_5 is stopping this frame...
        if HaveYouTakenThisProf_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_5.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_5.stopped')
                # update status
                HaveYouTakenThisProf_5.status = FINISHED
                HaveYouTakenThisProf_5.setAutoDraw(False)
        
        # *imageProf5* updates
        
        # if imageProf5 is starting this frame...
        if imageProf5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf5.frameNStart = frameN  # exact frame index
            imageProf5.tStart = t  # local t and not account for scr refresh
            imageProf5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf5.started')
            # update status
            imageProf5.status = STARTED
            imageProf5.setAutoDraw(True)
        
        # if imageProf5 is active this frame...
        if imageProf5.status == STARTED:
            # update params
            pass
        
        # if imageProf5 is stopping this frame...
        if imageProf5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf5.tStop = t  # not accounting for scr refresh
                imageProf5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf5.stopped')
                # update status
                imageProf5.status = FINISHED
                imageProf5.setAutoDraw(False)
        
        # *imageYesButton_5* updates
        
        # if imageYesButton_5 is starting this frame...
        if imageYesButton_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_5.frameNStart = frameN  # exact frame index
            imageYesButton_5.tStart = t  # local t and not account for scr refresh
            imageYesButton_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_5.started')
            # update status
            imageYesButton_5.status = STARTED
            imageYesButton_5.setAutoDraw(True)
        
        # if imageYesButton_5 is active this frame...
        if imageYesButton_5.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_5 is stopping this frame...
        if imageYesButton_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_5.tStop = t  # not accounting for scr refresh
                imageYesButton_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_5.stopped')
                # update status
                imageYesButton_5.status = FINISHED
                imageYesButton_5.setAutoDraw(False)
        
        # *imageNoButton_5* updates
        
        # if imageNoButton_5 is starting this frame...
        if imageNoButton_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_5.frameNStart = frameN  # exact frame index
            imageNoButton_5.tStart = t  # local t and not account for scr refresh
            imageNoButton_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_5.started')
            # update status
            imageNoButton_5.status = STARTED
            imageNoButton_5.setAutoDraw(True)
        
        # if imageNoButton_5 is active this frame...
        if imageNoButton_5.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_5 is stopping this frame...
        if imageNoButton_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_5.tStop = t  # not accounting for scr refresh
                imageNoButton_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_5.stopped')
                # update status
                imageNoButton_5.status = FINISHED
                imageNoButton_5.setAutoDraw(False)
        # *mouse_5* updates
        
        # if mouse_5 is starting this frame...
        if mouse_5.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_5.frameNStart = frameN  # exact frame index
            mouse_5.tStart = t  # local t and not account for scr refresh
            mouse_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_5.started', t)
            # update status
            mouse_5.status = STARTED
            mouse_5.mouseClock.reset()
            prevButtonState = mouse_5.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_5 is stopping this frame...
        if mouse_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_5.tStop = t  # not accounting for scr refresh
                mouse_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_5.stopped', t)
                # update status
                mouse_5.status = FINISHED
        if mouse_5.status == STARTED:  # only update if started and not finished!
            buttons = mouse_5.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_5):
                            gotValidClick = True
                            mouse_5.clicked_name.append(obj.name)
                    x, y = mouse_5.getPos()
                    mouse_5.x.append(x)
                    mouse_5.y.append(y)
                    buttons = mouse_5.getPressed()
                    mouse_5.leftButton.append(buttons[0])
                    mouse_5.midButton.append(buttons[1])
                    mouse_5.rightButton.append(buttons[2])
                    mouse_5.time.append(mouse_5.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof5" ---
    for thisComponent in Prof5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof5.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_5.x', mouse_5.x)
    thisExp.addData('mouse_5.y', mouse_5.y)
    thisExp.addData('mouse_5.leftButton', mouse_5.leftButton)
    thisExp.addData('mouse_5.midButton', mouse_5.midButton)
    thisExp.addData('mouse_5.rightButton', mouse_5.rightButton)
    thisExp.addData('mouse_5.time', mouse_5.time)
    thisExp.addData('mouse_5.clicked_name', mouse_5.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof5_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof5_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_22
    mouse_22.x = []
    mouse_22.y = []
    mouse_22.leftButton = []
    mouse_22.midButton = []
    mouse_22.rightButton = []
    mouse_22.time = []
    mouse_22.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof5_enjoy_classComponents = [DidYouEnjoyThisProf_5, imageProf5_2, imageYesButton_22, imageNoButton_22, mouse_22]
    for thisComponent in Prof5_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof5_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_5* updates
        
        # if DidYouEnjoyThisProf_5 is starting this frame...
        if DidYouEnjoyThisProf_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_5.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_5.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_5.started')
            # update status
            DidYouEnjoyThisProf_5.status = STARTED
            DidYouEnjoyThisProf_5.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_5 is active this frame...
        if DidYouEnjoyThisProf_5.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_5 is stopping this frame...
        if DidYouEnjoyThisProf_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_5.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_5.stopped')
                # update status
                DidYouEnjoyThisProf_5.status = FINISHED
                DidYouEnjoyThisProf_5.setAutoDraw(False)
        
        # *imageProf5_2* updates
        
        # if imageProf5_2 is starting this frame...
        if imageProf5_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf5_2.frameNStart = frameN  # exact frame index
            imageProf5_2.tStart = t  # local t and not account for scr refresh
            imageProf5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf5_2.started')
            # update status
            imageProf5_2.status = STARTED
            imageProf5_2.setAutoDraw(True)
        
        # if imageProf5_2 is active this frame...
        if imageProf5_2.status == STARTED:
            # update params
            pass
        
        # if imageProf5_2 is stopping this frame...
        if imageProf5_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf5_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf5_2.tStop = t  # not accounting for scr refresh
                imageProf5_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf5_2.stopped')
                # update status
                imageProf5_2.status = FINISHED
                imageProf5_2.setAutoDraw(False)
        
        # *imageYesButton_22* updates
        
        # if imageYesButton_22 is starting this frame...
        if imageYesButton_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_22.frameNStart = frameN  # exact frame index
            imageYesButton_22.tStart = t  # local t and not account for scr refresh
            imageYesButton_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_22.started')
            # update status
            imageYesButton_22.status = STARTED
            imageYesButton_22.setAutoDraw(True)
        
        # if imageYesButton_22 is active this frame...
        if imageYesButton_22.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_22 is stopping this frame...
        if imageYesButton_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_22.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_22.tStop = t  # not accounting for scr refresh
                imageYesButton_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_22.stopped')
                # update status
                imageYesButton_22.status = FINISHED
                imageYesButton_22.setAutoDraw(False)
        
        # *imageNoButton_22* updates
        
        # if imageNoButton_22 is starting this frame...
        if imageNoButton_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_22.frameNStart = frameN  # exact frame index
            imageNoButton_22.tStart = t  # local t and not account for scr refresh
            imageNoButton_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_22.started')
            # update status
            imageNoButton_22.status = STARTED
            imageNoButton_22.setAutoDraw(True)
        
        # if imageNoButton_22 is active this frame...
        if imageNoButton_22.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_22 is stopping this frame...
        if imageNoButton_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_22.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_22.tStop = t  # not accounting for scr refresh
                imageNoButton_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_22.stopped')
                # update status
                imageNoButton_22.status = FINISHED
                imageNoButton_22.setAutoDraw(False)
        # *mouse_22* updates
        
        # if mouse_22 is starting this frame...
        if mouse_22.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_22.frameNStart = frameN  # exact frame index
            mouse_22.tStart = t  # local t and not account for scr refresh
            mouse_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_22.started', t)
            # update status
            mouse_22.status = STARTED
            mouse_22.mouseClock.reset()
            prevButtonState = mouse_22.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_22 is stopping this frame...
        if mouse_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_22.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_22.tStop = t  # not accounting for scr refresh
                mouse_22.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_22.stopped', t)
                # update status
                mouse_22.status = FINISHED
        if mouse_22.status == STARTED:  # only update if started and not finished!
            buttons = mouse_22.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_22):
                            gotValidClick = True
                            mouse_22.clicked_name.append(obj.name)
                    x, y = mouse_22.getPos()
                    mouse_22.x.append(x)
                    mouse_22.y.append(y)
                    buttons = mouse_22.getPressed()
                    mouse_22.leftButton.append(buttons[0])
                    mouse_22.midButton.append(buttons[1])
                    mouse_22.rightButton.append(buttons[2])
                    mouse_22.time.append(mouse_22.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof5_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof5_enjoy_class" ---
    for thisComponent in Prof5_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof5_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_22.x', mouse_22.x)
    thisExp.addData('mouse_22.y', mouse_22.y)
    thisExp.addData('mouse_22.leftButton', mouse_22.leftButton)
    thisExp.addData('mouse_22.midButton', mouse_22.midButton)
    thisExp.addData('mouse_22.rightButton', mouse_22.rightButton)
    thisExp.addData('mouse_22.time', mouse_22.time)
    thisExp.addData('mouse_22.clicked_name', mouse_22.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof6" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof6.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_6
    mouse_6.x = []
    mouse_6.y = []
    mouse_6.leftButton = []
    mouse_6.midButton = []
    mouse_6.rightButton = []
    mouse_6.time = []
    mouse_6.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof6Components = [HaveYouTakenThisProf_6, imageProf6, imageYesButton_6, imageNoButton_6, mouse_6]
    for thisComponent in Prof6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof6" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_6* updates
        
        # if HaveYouTakenThisProf_6 is starting this frame...
        if HaveYouTakenThisProf_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_6.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_6.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_6.started')
            # update status
            HaveYouTakenThisProf_6.status = STARTED
            HaveYouTakenThisProf_6.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_6 is active this frame...
        if HaveYouTakenThisProf_6.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_6 is stopping this frame...
        if HaveYouTakenThisProf_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_6.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_6.stopped')
                # update status
                HaveYouTakenThisProf_6.status = FINISHED
                HaveYouTakenThisProf_6.setAutoDraw(False)
        
        # *imageProf6* updates
        
        # if imageProf6 is starting this frame...
        if imageProf6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf6.frameNStart = frameN  # exact frame index
            imageProf6.tStart = t  # local t and not account for scr refresh
            imageProf6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf6.started')
            # update status
            imageProf6.status = STARTED
            imageProf6.setAutoDraw(True)
        
        # if imageProf6 is active this frame...
        if imageProf6.status == STARTED:
            # update params
            pass
        
        # if imageProf6 is stopping this frame...
        if imageProf6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf6.tStop = t  # not accounting for scr refresh
                imageProf6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf6.stopped')
                # update status
                imageProf6.status = FINISHED
                imageProf6.setAutoDraw(False)
        
        # *imageYesButton_6* updates
        
        # if imageYesButton_6 is starting this frame...
        if imageYesButton_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_6.frameNStart = frameN  # exact frame index
            imageYesButton_6.tStart = t  # local t and not account for scr refresh
            imageYesButton_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_6.started')
            # update status
            imageYesButton_6.status = STARTED
            imageYesButton_6.setAutoDraw(True)
        
        # if imageYesButton_6 is active this frame...
        if imageYesButton_6.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_6 is stopping this frame...
        if imageYesButton_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_6.tStop = t  # not accounting for scr refresh
                imageYesButton_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_6.stopped')
                # update status
                imageYesButton_6.status = FINISHED
                imageYesButton_6.setAutoDraw(False)
        
        # *imageNoButton_6* updates
        
        # if imageNoButton_6 is starting this frame...
        if imageNoButton_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_6.frameNStart = frameN  # exact frame index
            imageNoButton_6.tStart = t  # local t and not account for scr refresh
            imageNoButton_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_6.started')
            # update status
            imageNoButton_6.status = STARTED
            imageNoButton_6.setAutoDraw(True)
        
        # if imageNoButton_6 is active this frame...
        if imageNoButton_6.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_6 is stopping this frame...
        if imageNoButton_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_6.tStop = t  # not accounting for scr refresh
                imageNoButton_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_6.stopped')
                # update status
                imageNoButton_6.status = FINISHED
                imageNoButton_6.setAutoDraw(False)
        # *mouse_6* updates
        
        # if mouse_6 is starting this frame...
        if mouse_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_6.frameNStart = frameN  # exact frame index
            mouse_6.tStart = t  # local t and not account for scr refresh
            mouse_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_6.started', t)
            # update status
            mouse_6.status = STARTED
            mouse_6.mouseClock.reset()
            prevButtonState = mouse_6.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_6 is stopping this frame...
        if mouse_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_6.tStop = t  # not accounting for scr refresh
                mouse_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_6.stopped', t)
                # update status
                mouse_6.status = FINISHED
        if mouse_6.status == STARTED:  # only update if started and not finished!
            buttons = mouse_6.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_6):
                            gotValidClick = True
                            mouse_6.clicked_name.append(obj.name)
                    x, y = mouse_6.getPos()
                    mouse_6.x.append(x)
                    mouse_6.y.append(y)
                    buttons = mouse_6.getPressed()
                    mouse_6.leftButton.append(buttons[0])
                    mouse_6.midButton.append(buttons[1])
                    mouse_6.rightButton.append(buttons[2])
                    mouse_6.time.append(mouse_6.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof6" ---
    for thisComponent in Prof6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof6.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_6.x', mouse_6.x)
    thisExp.addData('mouse_6.y', mouse_6.y)
    thisExp.addData('mouse_6.leftButton', mouse_6.leftButton)
    thisExp.addData('mouse_6.midButton', mouse_6.midButton)
    thisExp.addData('mouse_6.rightButton', mouse_6.rightButton)
    thisExp.addData('mouse_6.time', mouse_6.time)
    thisExp.addData('mouse_6.clicked_name', mouse_6.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof6_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof6_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_23
    mouse_23.x = []
    mouse_23.y = []
    mouse_23.leftButton = []
    mouse_23.midButton = []
    mouse_23.rightButton = []
    mouse_23.time = []
    mouse_23.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof6_enjoy_classComponents = [DidYouEnjoyThisProf_6, imageProf6_2, imageYesButton_23, imageNoButton_23, mouse_23]
    for thisComponent in Prof6_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof6_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_6* updates
        
        # if DidYouEnjoyThisProf_6 is starting this frame...
        if DidYouEnjoyThisProf_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_6.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_6.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_6.started')
            # update status
            DidYouEnjoyThisProf_6.status = STARTED
            DidYouEnjoyThisProf_6.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_6 is active this frame...
        if DidYouEnjoyThisProf_6.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_6 is stopping this frame...
        if DidYouEnjoyThisProf_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_6.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_6.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_6.stopped')
                # update status
                DidYouEnjoyThisProf_6.status = FINISHED
                DidYouEnjoyThisProf_6.setAutoDraw(False)
        
        # *imageProf6_2* updates
        
        # if imageProf6_2 is starting this frame...
        if imageProf6_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf6_2.frameNStart = frameN  # exact frame index
            imageProf6_2.tStart = t  # local t and not account for scr refresh
            imageProf6_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf6_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf6_2.started')
            # update status
            imageProf6_2.status = STARTED
            imageProf6_2.setAutoDraw(True)
        
        # if imageProf6_2 is active this frame...
        if imageProf6_2.status == STARTED:
            # update params
            pass
        
        # if imageProf6_2 is stopping this frame...
        if imageProf6_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf6_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf6_2.tStop = t  # not accounting for scr refresh
                imageProf6_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf6_2.stopped')
                # update status
                imageProf6_2.status = FINISHED
                imageProf6_2.setAutoDraw(False)
        
        # *imageYesButton_23* updates
        
        # if imageYesButton_23 is starting this frame...
        if imageYesButton_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_23.frameNStart = frameN  # exact frame index
            imageYesButton_23.tStart = t  # local t and not account for scr refresh
            imageYesButton_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_23.started')
            # update status
            imageYesButton_23.status = STARTED
            imageYesButton_23.setAutoDraw(True)
        
        # if imageYesButton_23 is active this frame...
        if imageYesButton_23.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_23 is stopping this frame...
        if imageYesButton_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_23.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_23.tStop = t  # not accounting for scr refresh
                imageYesButton_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_23.stopped')
                # update status
                imageYesButton_23.status = FINISHED
                imageYesButton_23.setAutoDraw(False)
        
        # *imageNoButton_23* updates
        
        # if imageNoButton_23 is starting this frame...
        if imageNoButton_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_23.frameNStart = frameN  # exact frame index
            imageNoButton_23.tStart = t  # local t and not account for scr refresh
            imageNoButton_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_23.started')
            # update status
            imageNoButton_23.status = STARTED
            imageNoButton_23.setAutoDraw(True)
        
        # if imageNoButton_23 is active this frame...
        if imageNoButton_23.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_23 is stopping this frame...
        if imageNoButton_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_23.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_23.tStop = t  # not accounting for scr refresh
                imageNoButton_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_23.stopped')
                # update status
                imageNoButton_23.status = FINISHED
                imageNoButton_23.setAutoDraw(False)
        # *mouse_23* updates
        
        # if mouse_23 is starting this frame...
        if mouse_23.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_23.frameNStart = frameN  # exact frame index
            mouse_23.tStart = t  # local t and not account for scr refresh
            mouse_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_23.started', t)
            # update status
            mouse_23.status = STARTED
            mouse_23.mouseClock.reset()
            prevButtonState = mouse_23.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_23 is stopping this frame...
        if mouse_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_23.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_23.tStop = t  # not accounting for scr refresh
                mouse_23.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_23.stopped', t)
                # update status
                mouse_23.status = FINISHED
        if mouse_23.status == STARTED:  # only update if started and not finished!
            buttons = mouse_23.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_23):
                            gotValidClick = True
                            mouse_23.clicked_name.append(obj.name)
                    x, y = mouse_23.getPos()
                    mouse_23.x.append(x)
                    mouse_23.y.append(y)
                    buttons = mouse_23.getPressed()
                    mouse_23.leftButton.append(buttons[0])
                    mouse_23.midButton.append(buttons[1])
                    mouse_23.rightButton.append(buttons[2])
                    mouse_23.time.append(mouse_23.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof6_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof6_enjoy_class" ---
    for thisComponent in Prof6_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof6_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_23.x', mouse_23.x)
    thisExp.addData('mouse_23.y', mouse_23.y)
    thisExp.addData('mouse_23.leftButton', mouse_23.leftButton)
    thisExp.addData('mouse_23.midButton', mouse_23.midButton)
    thisExp.addData('mouse_23.rightButton', mouse_23.rightButton)
    thisExp.addData('mouse_23.time', mouse_23.time)
    thisExp.addData('mouse_23.clicked_name', mouse_23.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof7" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof7.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_7
    mouse_7.x = []
    mouse_7.y = []
    mouse_7.leftButton = []
    mouse_7.midButton = []
    mouse_7.rightButton = []
    mouse_7.time = []
    mouse_7.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof7Components = [HaveYouTakenThisProf_7, imageProf7, imageYesButton_7, imageNoButton_7, mouse_7]
    for thisComponent in Prof7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof7" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_7* updates
        
        # if HaveYouTakenThisProf_7 is starting this frame...
        if HaveYouTakenThisProf_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_7.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_7.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_7.started')
            # update status
            HaveYouTakenThisProf_7.status = STARTED
            HaveYouTakenThisProf_7.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_7 is active this frame...
        if HaveYouTakenThisProf_7.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_7 is stopping this frame...
        if HaveYouTakenThisProf_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_7.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_7.stopped')
                # update status
                HaveYouTakenThisProf_7.status = FINISHED
                HaveYouTakenThisProf_7.setAutoDraw(False)
        
        # *imageProf7* updates
        
        # if imageProf7 is starting this frame...
        if imageProf7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf7.frameNStart = frameN  # exact frame index
            imageProf7.tStart = t  # local t and not account for scr refresh
            imageProf7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf7.started')
            # update status
            imageProf7.status = STARTED
            imageProf7.setAutoDraw(True)
        
        # if imageProf7 is active this frame...
        if imageProf7.status == STARTED:
            # update params
            pass
        
        # if imageProf7 is stopping this frame...
        if imageProf7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf7.tStop = t  # not accounting for scr refresh
                imageProf7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf7.stopped')
                # update status
                imageProf7.status = FINISHED
                imageProf7.setAutoDraw(False)
        
        # *imageYesButton_7* updates
        
        # if imageYesButton_7 is starting this frame...
        if imageYesButton_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_7.frameNStart = frameN  # exact frame index
            imageYesButton_7.tStart = t  # local t and not account for scr refresh
            imageYesButton_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_7.started')
            # update status
            imageYesButton_7.status = STARTED
            imageYesButton_7.setAutoDraw(True)
        
        # if imageYesButton_7 is active this frame...
        if imageYesButton_7.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_7 is stopping this frame...
        if imageYesButton_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_7.tStop = t  # not accounting for scr refresh
                imageYesButton_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_7.stopped')
                # update status
                imageYesButton_7.status = FINISHED
                imageYesButton_7.setAutoDraw(False)
        
        # *imageNoButton_7* updates
        
        # if imageNoButton_7 is starting this frame...
        if imageNoButton_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_7.frameNStart = frameN  # exact frame index
            imageNoButton_7.tStart = t  # local t and not account for scr refresh
            imageNoButton_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_7.started')
            # update status
            imageNoButton_7.status = STARTED
            imageNoButton_7.setAutoDraw(True)
        
        # if imageNoButton_7 is active this frame...
        if imageNoButton_7.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_7 is stopping this frame...
        if imageNoButton_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_7.tStop = t  # not accounting for scr refresh
                imageNoButton_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_7.stopped')
                # update status
                imageNoButton_7.status = FINISHED
                imageNoButton_7.setAutoDraw(False)
        # *mouse_7* updates
        
        # if mouse_7 is starting this frame...
        if mouse_7.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_7.frameNStart = frameN  # exact frame index
            mouse_7.tStart = t  # local t and not account for scr refresh
            mouse_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_7.started', t)
            # update status
            mouse_7.status = STARTED
            mouse_7.mouseClock.reset()
            prevButtonState = mouse_7.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_7 is stopping this frame...
        if mouse_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_7.tStop = t  # not accounting for scr refresh
                mouse_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_7.stopped', t)
                # update status
                mouse_7.status = FINISHED
        if mouse_7.status == STARTED:  # only update if started and not finished!
            buttons = mouse_7.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_7):
                            gotValidClick = True
                            mouse_7.clicked_name.append(obj.name)
                    x, y = mouse_7.getPos()
                    mouse_7.x.append(x)
                    mouse_7.y.append(y)
                    buttons = mouse_7.getPressed()
                    mouse_7.leftButton.append(buttons[0])
                    mouse_7.midButton.append(buttons[1])
                    mouse_7.rightButton.append(buttons[2])
                    mouse_7.time.append(mouse_7.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof7" ---
    for thisComponent in Prof7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof7.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_7.x', mouse_7.x)
    thisExp.addData('mouse_7.y', mouse_7.y)
    thisExp.addData('mouse_7.leftButton', mouse_7.leftButton)
    thisExp.addData('mouse_7.midButton', mouse_7.midButton)
    thisExp.addData('mouse_7.rightButton', mouse_7.rightButton)
    thisExp.addData('mouse_7.time', mouse_7.time)
    thisExp.addData('mouse_7.clicked_name', mouse_7.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof7_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof7_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_24
    mouse_24.x = []
    mouse_24.y = []
    mouse_24.leftButton = []
    mouse_24.midButton = []
    mouse_24.rightButton = []
    mouse_24.time = []
    mouse_24.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof7_enjoy_classComponents = [DidYouEnjoyThisProf_7, imageProf7_2, imageYesButton_24, imageNoButton_24, mouse_24]
    for thisComponent in Prof7_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof7_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_7* updates
        
        # if DidYouEnjoyThisProf_7 is starting this frame...
        if DidYouEnjoyThisProf_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_7.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_7.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_7.started')
            # update status
            DidYouEnjoyThisProf_7.status = STARTED
            DidYouEnjoyThisProf_7.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_7 is active this frame...
        if DidYouEnjoyThisProf_7.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_7 is stopping this frame...
        if DidYouEnjoyThisProf_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_7.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_7.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_7.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_7.stopped')
                # update status
                DidYouEnjoyThisProf_7.status = FINISHED
                DidYouEnjoyThisProf_7.setAutoDraw(False)
        
        # *imageProf7_2* updates
        
        # if imageProf7_2 is starting this frame...
        if imageProf7_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf7_2.frameNStart = frameN  # exact frame index
            imageProf7_2.tStart = t  # local t and not account for scr refresh
            imageProf7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf7_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf7_2.started')
            # update status
            imageProf7_2.status = STARTED
            imageProf7_2.setAutoDraw(True)
        
        # if imageProf7_2 is active this frame...
        if imageProf7_2.status == STARTED:
            # update params
            pass
        
        # if imageProf7_2 is stopping this frame...
        if imageProf7_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf7_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf7_2.tStop = t  # not accounting for scr refresh
                imageProf7_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf7_2.stopped')
                # update status
                imageProf7_2.status = FINISHED
                imageProf7_2.setAutoDraw(False)
        
        # *imageYesButton_24* updates
        
        # if imageYesButton_24 is starting this frame...
        if imageYesButton_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_24.frameNStart = frameN  # exact frame index
            imageYesButton_24.tStart = t  # local t and not account for scr refresh
            imageYesButton_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_24.started')
            # update status
            imageYesButton_24.status = STARTED
            imageYesButton_24.setAutoDraw(True)
        
        # if imageYesButton_24 is active this frame...
        if imageYesButton_24.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_24 is stopping this frame...
        if imageYesButton_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_24.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_24.tStop = t  # not accounting for scr refresh
                imageYesButton_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_24.stopped')
                # update status
                imageYesButton_24.status = FINISHED
                imageYesButton_24.setAutoDraw(False)
        
        # *imageNoButton_24* updates
        
        # if imageNoButton_24 is starting this frame...
        if imageNoButton_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_24.frameNStart = frameN  # exact frame index
            imageNoButton_24.tStart = t  # local t and not account for scr refresh
            imageNoButton_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_24.started')
            # update status
            imageNoButton_24.status = STARTED
            imageNoButton_24.setAutoDraw(True)
        
        # if imageNoButton_24 is active this frame...
        if imageNoButton_24.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_24 is stopping this frame...
        if imageNoButton_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_24.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_24.tStop = t  # not accounting for scr refresh
                imageNoButton_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_24.stopped')
                # update status
                imageNoButton_24.status = FINISHED
                imageNoButton_24.setAutoDraw(False)
        # *mouse_24* updates
        
        # if mouse_24 is starting this frame...
        if mouse_24.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_24.frameNStart = frameN  # exact frame index
            mouse_24.tStart = t  # local t and not account for scr refresh
            mouse_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_24.started', t)
            # update status
            mouse_24.status = STARTED
            mouse_24.mouseClock.reset()
            prevButtonState = mouse_24.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_24 is stopping this frame...
        if mouse_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_24.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_24.tStop = t  # not accounting for scr refresh
                mouse_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_24.stopped', t)
                # update status
                mouse_24.status = FINISHED
        if mouse_24.status == STARTED:  # only update if started and not finished!
            buttons = mouse_24.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_24):
                            gotValidClick = True
                            mouse_24.clicked_name.append(obj.name)
                    x, y = mouse_24.getPos()
                    mouse_24.x.append(x)
                    mouse_24.y.append(y)
                    buttons = mouse_24.getPressed()
                    mouse_24.leftButton.append(buttons[0])
                    mouse_24.midButton.append(buttons[1])
                    mouse_24.rightButton.append(buttons[2])
                    mouse_24.time.append(mouse_24.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof7_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof7_enjoy_class" ---
    for thisComponent in Prof7_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof7_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_24.x', mouse_24.x)
    thisExp.addData('mouse_24.y', mouse_24.y)
    thisExp.addData('mouse_24.leftButton', mouse_24.leftButton)
    thisExp.addData('mouse_24.midButton', mouse_24.midButton)
    thisExp.addData('mouse_24.rightButton', mouse_24.rightButton)
    thisExp.addData('mouse_24.time', mouse_24.time)
    thisExp.addData('mouse_24.clicked_name', mouse_24.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof8" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof8.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_8
    mouse_8.x = []
    mouse_8.y = []
    mouse_8.leftButton = []
    mouse_8.midButton = []
    mouse_8.rightButton = []
    mouse_8.time = []
    mouse_8.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof8Components = [HaveYouTakenThisProf_8, imageProf8, imageYesButton_8, imageNoButton_8, mouse_8]
    for thisComponent in Prof8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_8* updates
        
        # if HaveYouTakenThisProf_8 is starting this frame...
        if HaveYouTakenThisProf_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_8.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_8.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_8.started')
            # update status
            HaveYouTakenThisProf_8.status = STARTED
            HaveYouTakenThisProf_8.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_8 is active this frame...
        if HaveYouTakenThisProf_8.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_8 is stopping this frame...
        if HaveYouTakenThisProf_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_8.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_8.stopped')
                # update status
                HaveYouTakenThisProf_8.status = FINISHED
                HaveYouTakenThisProf_8.setAutoDraw(False)
        
        # *imageProf8* updates
        
        # if imageProf8 is starting this frame...
        if imageProf8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf8.frameNStart = frameN  # exact frame index
            imageProf8.tStart = t  # local t and not account for scr refresh
            imageProf8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf8.started')
            # update status
            imageProf8.status = STARTED
            imageProf8.setAutoDraw(True)
        
        # if imageProf8 is active this frame...
        if imageProf8.status == STARTED:
            # update params
            pass
        
        # if imageProf8 is stopping this frame...
        if imageProf8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf8.tStop = t  # not accounting for scr refresh
                imageProf8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf8.stopped')
                # update status
                imageProf8.status = FINISHED
                imageProf8.setAutoDraw(False)
        
        # *imageYesButton_8* updates
        
        # if imageYesButton_8 is starting this frame...
        if imageYesButton_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_8.frameNStart = frameN  # exact frame index
            imageYesButton_8.tStart = t  # local t and not account for scr refresh
            imageYesButton_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_8.started')
            # update status
            imageYesButton_8.status = STARTED
            imageYesButton_8.setAutoDraw(True)
        
        # if imageYesButton_8 is active this frame...
        if imageYesButton_8.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_8 is stopping this frame...
        if imageYesButton_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_8.tStop = t  # not accounting for scr refresh
                imageYesButton_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_8.stopped')
                # update status
                imageYesButton_8.status = FINISHED
                imageYesButton_8.setAutoDraw(False)
        
        # *imageNoButton_8* updates
        
        # if imageNoButton_8 is starting this frame...
        if imageNoButton_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_8.frameNStart = frameN  # exact frame index
            imageNoButton_8.tStart = t  # local t and not account for scr refresh
            imageNoButton_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_8.started')
            # update status
            imageNoButton_8.status = STARTED
            imageNoButton_8.setAutoDraw(True)
        
        # if imageNoButton_8 is active this frame...
        if imageNoButton_8.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_8 is stopping this frame...
        if imageNoButton_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_8.tStop = t  # not accounting for scr refresh
                imageNoButton_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_8.stopped')
                # update status
                imageNoButton_8.status = FINISHED
                imageNoButton_8.setAutoDraw(False)
        # *mouse_8* updates
        
        # if mouse_8 is starting this frame...
        if mouse_8.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_8.frameNStart = frameN  # exact frame index
            mouse_8.tStart = t  # local t and not account for scr refresh
            mouse_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_8.started', t)
            # update status
            mouse_8.status = STARTED
            mouse_8.mouseClock.reset()
            prevButtonState = mouse_8.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_8 is stopping this frame...
        if mouse_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_8.tStop = t  # not accounting for scr refresh
                mouse_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_8.stopped', t)
                # update status
                mouse_8.status = FINISHED
        if mouse_8.status == STARTED:  # only update if started and not finished!
            buttons = mouse_8.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_8):
                            gotValidClick = True
                            mouse_8.clicked_name.append(obj.name)
                    x, y = mouse_8.getPos()
                    mouse_8.x.append(x)
                    mouse_8.y.append(y)
                    buttons = mouse_8.getPressed()
                    mouse_8.leftButton.append(buttons[0])
                    mouse_8.midButton.append(buttons[1])
                    mouse_8.rightButton.append(buttons[2])
                    mouse_8.time.append(mouse_8.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof8" ---
    for thisComponent in Prof8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof8.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_8.x', mouse_8.x)
    thisExp.addData('mouse_8.y', mouse_8.y)
    thisExp.addData('mouse_8.leftButton', mouse_8.leftButton)
    thisExp.addData('mouse_8.midButton', mouse_8.midButton)
    thisExp.addData('mouse_8.rightButton', mouse_8.rightButton)
    thisExp.addData('mouse_8.time', mouse_8.time)
    thisExp.addData('mouse_8.clicked_name', mouse_8.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof8_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof8_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_25
    mouse_25.x = []
    mouse_25.y = []
    mouse_25.leftButton = []
    mouse_25.midButton = []
    mouse_25.rightButton = []
    mouse_25.time = []
    mouse_25.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof8_enjoy_classComponents = [DidYouEnjoyThisProf_8, imageProf8_2, imageYesButton_25, imageNoButton_25, mouse_25]
    for thisComponent in Prof8_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof8_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_8* updates
        
        # if DidYouEnjoyThisProf_8 is starting this frame...
        if DidYouEnjoyThisProf_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_8.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_8.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_8, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_8.started')
            # update status
            DidYouEnjoyThisProf_8.status = STARTED
            DidYouEnjoyThisProf_8.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_8 is active this frame...
        if DidYouEnjoyThisProf_8.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_8 is stopping this frame...
        if DidYouEnjoyThisProf_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_8.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_8.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_8.stopped')
                # update status
                DidYouEnjoyThisProf_8.status = FINISHED
                DidYouEnjoyThisProf_8.setAutoDraw(False)
        
        # *imageProf8_2* updates
        
        # if imageProf8_2 is starting this frame...
        if imageProf8_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf8_2.frameNStart = frameN  # exact frame index
            imageProf8_2.tStart = t  # local t and not account for scr refresh
            imageProf8_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf8_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf8_2.started')
            # update status
            imageProf8_2.status = STARTED
            imageProf8_2.setAutoDraw(True)
        
        # if imageProf8_2 is active this frame...
        if imageProf8_2.status == STARTED:
            # update params
            pass
        
        # if imageProf8_2 is stopping this frame...
        if imageProf8_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf8_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf8_2.tStop = t  # not accounting for scr refresh
                imageProf8_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf8_2.stopped')
                # update status
                imageProf8_2.status = FINISHED
                imageProf8_2.setAutoDraw(False)
        
        # *imageYesButton_25* updates
        
        # if imageYesButton_25 is starting this frame...
        if imageYesButton_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_25.frameNStart = frameN  # exact frame index
            imageYesButton_25.tStart = t  # local t and not account for scr refresh
            imageYesButton_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_25.started')
            # update status
            imageYesButton_25.status = STARTED
            imageYesButton_25.setAutoDraw(True)
        
        # if imageYesButton_25 is active this frame...
        if imageYesButton_25.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_25 is stopping this frame...
        if imageYesButton_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_25.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_25.tStop = t  # not accounting for scr refresh
                imageYesButton_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_25.stopped')
                # update status
                imageYesButton_25.status = FINISHED
                imageYesButton_25.setAutoDraw(False)
        
        # *imageNoButton_25* updates
        
        # if imageNoButton_25 is starting this frame...
        if imageNoButton_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_25.frameNStart = frameN  # exact frame index
            imageNoButton_25.tStart = t  # local t and not account for scr refresh
            imageNoButton_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_25.started')
            # update status
            imageNoButton_25.status = STARTED
            imageNoButton_25.setAutoDraw(True)
        
        # if imageNoButton_25 is active this frame...
        if imageNoButton_25.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_25 is stopping this frame...
        if imageNoButton_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_25.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_25.tStop = t  # not accounting for scr refresh
                imageNoButton_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_25.stopped')
                # update status
                imageNoButton_25.status = FINISHED
                imageNoButton_25.setAutoDraw(False)
        # *mouse_25* updates
        
        # if mouse_25 is starting this frame...
        if mouse_25.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_25.frameNStart = frameN  # exact frame index
            mouse_25.tStart = t  # local t and not account for scr refresh
            mouse_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_25.started', t)
            # update status
            mouse_25.status = STARTED
            mouse_25.mouseClock.reset()
            prevButtonState = mouse_25.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_25 is stopping this frame...
        if mouse_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_25.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_25.tStop = t  # not accounting for scr refresh
                mouse_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_25.stopped', t)
                # update status
                mouse_25.status = FINISHED
        if mouse_25.status == STARTED:  # only update if started and not finished!
            buttons = mouse_25.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_25):
                            gotValidClick = True
                            mouse_25.clicked_name.append(obj.name)
                    x, y = mouse_25.getPos()
                    mouse_25.x.append(x)
                    mouse_25.y.append(y)
                    buttons = mouse_25.getPressed()
                    mouse_25.leftButton.append(buttons[0])
                    mouse_25.midButton.append(buttons[1])
                    mouse_25.rightButton.append(buttons[2])
                    mouse_25.time.append(mouse_25.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof8_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof8_enjoy_class" ---
    for thisComponent in Prof8_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof8_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_25.x', mouse_25.x)
    thisExp.addData('mouse_25.y', mouse_25.y)
    thisExp.addData('mouse_25.leftButton', mouse_25.leftButton)
    thisExp.addData('mouse_25.midButton', mouse_25.midButton)
    thisExp.addData('mouse_25.rightButton', mouse_25.rightButton)
    thisExp.addData('mouse_25.time', mouse_25.time)
    thisExp.addData('mouse_25.clicked_name', mouse_25.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof9" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof9.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_9
    mouse_9.x = []
    mouse_9.y = []
    mouse_9.leftButton = []
    mouse_9.midButton = []
    mouse_9.rightButton = []
    mouse_9.time = []
    mouse_9.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof9Components = [HaveYouTakenThisProf_9, imageProf9, imageYesButton_9, imageNoButton_9, mouse_9]
    for thisComponent in Prof9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof9" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_9* updates
        
        # if HaveYouTakenThisProf_9 is starting this frame...
        if HaveYouTakenThisProf_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_9.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_9.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_9.started')
            # update status
            HaveYouTakenThisProf_9.status = STARTED
            HaveYouTakenThisProf_9.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_9 is active this frame...
        if HaveYouTakenThisProf_9.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_9 is stopping this frame...
        if HaveYouTakenThisProf_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_9.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_9.stopped')
                # update status
                HaveYouTakenThisProf_9.status = FINISHED
                HaveYouTakenThisProf_9.setAutoDraw(False)
        
        # *imageProf9* updates
        
        # if imageProf9 is starting this frame...
        if imageProf9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf9.frameNStart = frameN  # exact frame index
            imageProf9.tStart = t  # local t and not account for scr refresh
            imageProf9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf9.started')
            # update status
            imageProf9.status = STARTED
            imageProf9.setAutoDraw(True)
        
        # if imageProf9 is active this frame...
        if imageProf9.status == STARTED:
            # update params
            pass
        
        # if imageProf9 is stopping this frame...
        if imageProf9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf9.tStop = t  # not accounting for scr refresh
                imageProf9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf9.stopped')
                # update status
                imageProf9.status = FINISHED
                imageProf9.setAutoDraw(False)
        
        # *imageYesButton_9* updates
        
        # if imageYesButton_9 is starting this frame...
        if imageYesButton_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_9.frameNStart = frameN  # exact frame index
            imageYesButton_9.tStart = t  # local t and not account for scr refresh
            imageYesButton_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_9.started')
            # update status
            imageYesButton_9.status = STARTED
            imageYesButton_9.setAutoDraw(True)
        
        # if imageYesButton_9 is active this frame...
        if imageYesButton_9.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_9 is stopping this frame...
        if imageYesButton_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_9.tStop = t  # not accounting for scr refresh
                imageYesButton_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_9.stopped')
                # update status
                imageYesButton_9.status = FINISHED
                imageYesButton_9.setAutoDraw(False)
        
        # *imageNoButton_9* updates
        
        # if imageNoButton_9 is starting this frame...
        if imageNoButton_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_9.frameNStart = frameN  # exact frame index
            imageNoButton_9.tStart = t  # local t and not account for scr refresh
            imageNoButton_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_9.started')
            # update status
            imageNoButton_9.status = STARTED
            imageNoButton_9.setAutoDraw(True)
        
        # if imageNoButton_9 is active this frame...
        if imageNoButton_9.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_9 is stopping this frame...
        if imageNoButton_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_9.tStop = t  # not accounting for scr refresh
                imageNoButton_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_9.stopped')
                # update status
                imageNoButton_9.status = FINISHED
                imageNoButton_9.setAutoDraw(False)
        # *mouse_9* updates
        
        # if mouse_9 is starting this frame...
        if mouse_9.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_9.frameNStart = frameN  # exact frame index
            mouse_9.tStart = t  # local t and not account for scr refresh
            mouse_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_9.started', t)
            # update status
            mouse_9.status = STARTED
            mouse_9.mouseClock.reset()
            prevButtonState = mouse_9.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_9 is stopping this frame...
        if mouse_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_9.tStop = t  # not accounting for scr refresh
                mouse_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_9.stopped', t)
                # update status
                mouse_9.status = FINISHED
        if mouse_9.status == STARTED:  # only update if started and not finished!
            buttons = mouse_9.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_9):
                            gotValidClick = True
                            mouse_9.clicked_name.append(obj.name)
                    x, y = mouse_9.getPos()
                    mouse_9.x.append(x)
                    mouse_9.y.append(y)
                    buttons = mouse_9.getPressed()
                    mouse_9.leftButton.append(buttons[0])
                    mouse_9.midButton.append(buttons[1])
                    mouse_9.rightButton.append(buttons[2])
                    mouse_9.time.append(mouse_9.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof9" ---
    for thisComponent in Prof9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof9.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_9.x', mouse_9.x)
    thisExp.addData('mouse_9.y', mouse_9.y)
    thisExp.addData('mouse_9.leftButton', mouse_9.leftButton)
    thisExp.addData('mouse_9.midButton', mouse_9.midButton)
    thisExp.addData('mouse_9.rightButton', mouse_9.rightButton)
    thisExp.addData('mouse_9.time', mouse_9.time)
    thisExp.addData('mouse_9.clicked_name', mouse_9.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof9_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof9_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_26
    mouse_26.x = []
    mouse_26.y = []
    mouse_26.leftButton = []
    mouse_26.midButton = []
    mouse_26.rightButton = []
    mouse_26.time = []
    mouse_26.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof9_enjoy_classComponents = [DidYouEnjoyThisProf_9, imageProf9_2, imageYesButton_26, imageNoButton_26, mouse_26]
    for thisComponent in Prof9_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof9_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_9* updates
        
        # if DidYouEnjoyThisProf_9 is starting this frame...
        if DidYouEnjoyThisProf_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_9.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_9.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_9, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_9.started')
            # update status
            DidYouEnjoyThisProf_9.status = STARTED
            DidYouEnjoyThisProf_9.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_9 is active this frame...
        if DidYouEnjoyThisProf_9.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_9 is stopping this frame...
        if DidYouEnjoyThisProf_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_9.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_9.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_9.stopped')
                # update status
                DidYouEnjoyThisProf_9.status = FINISHED
                DidYouEnjoyThisProf_9.setAutoDraw(False)
        
        # *imageProf9_2* updates
        
        # if imageProf9_2 is starting this frame...
        if imageProf9_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf9_2.frameNStart = frameN  # exact frame index
            imageProf9_2.tStart = t  # local t and not account for scr refresh
            imageProf9_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf9_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf9_2.started')
            # update status
            imageProf9_2.status = STARTED
            imageProf9_2.setAutoDraw(True)
        
        # if imageProf9_2 is active this frame...
        if imageProf9_2.status == STARTED:
            # update params
            pass
        
        # if imageProf9_2 is stopping this frame...
        if imageProf9_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf9_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf9_2.tStop = t  # not accounting for scr refresh
                imageProf9_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf9_2.stopped')
                # update status
                imageProf9_2.status = FINISHED
                imageProf9_2.setAutoDraw(False)
        
        # *imageYesButton_26* updates
        
        # if imageYesButton_26 is starting this frame...
        if imageYesButton_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_26.frameNStart = frameN  # exact frame index
            imageYesButton_26.tStart = t  # local t and not account for scr refresh
            imageYesButton_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_26.started')
            # update status
            imageYesButton_26.status = STARTED
            imageYesButton_26.setAutoDraw(True)
        
        # if imageYesButton_26 is active this frame...
        if imageYesButton_26.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_26 is stopping this frame...
        if imageYesButton_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_26.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_26.tStop = t  # not accounting for scr refresh
                imageYesButton_26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_26.stopped')
                # update status
                imageYesButton_26.status = FINISHED
                imageYesButton_26.setAutoDraw(False)
        
        # *imageNoButton_26* updates
        
        # if imageNoButton_26 is starting this frame...
        if imageNoButton_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_26.frameNStart = frameN  # exact frame index
            imageNoButton_26.tStart = t  # local t and not account for scr refresh
            imageNoButton_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_26.started')
            # update status
            imageNoButton_26.status = STARTED
            imageNoButton_26.setAutoDraw(True)
        
        # if imageNoButton_26 is active this frame...
        if imageNoButton_26.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_26 is stopping this frame...
        if imageNoButton_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_26.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_26.tStop = t  # not accounting for scr refresh
                imageNoButton_26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_26.stopped')
                # update status
                imageNoButton_26.status = FINISHED
                imageNoButton_26.setAutoDraw(False)
        # *mouse_26* updates
        
        # if mouse_26 is starting this frame...
        if mouse_26.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_26.frameNStart = frameN  # exact frame index
            mouse_26.tStart = t  # local t and not account for scr refresh
            mouse_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_26, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_26.started', t)
            # update status
            mouse_26.status = STARTED
            mouse_26.mouseClock.reset()
            prevButtonState = mouse_26.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_26 is stopping this frame...
        if mouse_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_26.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_26.tStop = t  # not accounting for scr refresh
                mouse_26.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_26.stopped', t)
                # update status
                mouse_26.status = FINISHED
        if mouse_26.status == STARTED:  # only update if started and not finished!
            buttons = mouse_26.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_26):
                            gotValidClick = True
                            mouse_26.clicked_name.append(obj.name)
                    x, y = mouse_26.getPos()
                    mouse_26.x.append(x)
                    mouse_26.y.append(y)
                    buttons = mouse_26.getPressed()
                    mouse_26.leftButton.append(buttons[0])
                    mouse_26.midButton.append(buttons[1])
                    mouse_26.rightButton.append(buttons[2])
                    mouse_26.time.append(mouse_26.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof9_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof9_enjoy_class" ---
    for thisComponent in Prof9_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof9_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_26.x', mouse_26.x)
    thisExp.addData('mouse_26.y', mouse_26.y)
    thisExp.addData('mouse_26.leftButton', mouse_26.leftButton)
    thisExp.addData('mouse_26.midButton', mouse_26.midButton)
    thisExp.addData('mouse_26.rightButton', mouse_26.rightButton)
    thisExp.addData('mouse_26.time', mouse_26.time)
    thisExp.addData('mouse_26.clicked_name', mouse_26.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof10" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof10.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_10
    mouse_10.x = []
    mouse_10.y = []
    mouse_10.leftButton = []
    mouse_10.midButton = []
    mouse_10.rightButton = []
    mouse_10.time = []
    mouse_10.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof10Components = [HaveYouTakenThisProf_10, imageProf10, imageYesButton_10, imageNoButton_10, mouse_10]
    for thisComponent in Prof10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof10" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_10* updates
        
        # if HaveYouTakenThisProf_10 is starting this frame...
        if HaveYouTakenThisProf_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_10.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_10.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_10.started')
            # update status
            HaveYouTakenThisProf_10.status = STARTED
            HaveYouTakenThisProf_10.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_10 is active this frame...
        if HaveYouTakenThisProf_10.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_10 is stopping this frame...
        if HaveYouTakenThisProf_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_10.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_10.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_10.stopped')
                # update status
                HaveYouTakenThisProf_10.status = FINISHED
                HaveYouTakenThisProf_10.setAutoDraw(False)
        
        # *imageProf10* updates
        
        # if imageProf10 is starting this frame...
        if imageProf10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf10.frameNStart = frameN  # exact frame index
            imageProf10.tStart = t  # local t and not account for scr refresh
            imageProf10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf10.started')
            # update status
            imageProf10.status = STARTED
            imageProf10.setAutoDraw(True)
        
        # if imageProf10 is active this frame...
        if imageProf10.status == STARTED:
            # update params
            pass
        
        # if imageProf10 is stopping this frame...
        if imageProf10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf10.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf10.tStop = t  # not accounting for scr refresh
                imageProf10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf10.stopped')
                # update status
                imageProf10.status = FINISHED
                imageProf10.setAutoDraw(False)
        
        # *imageYesButton_10* updates
        
        # if imageYesButton_10 is starting this frame...
        if imageYesButton_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_10.frameNStart = frameN  # exact frame index
            imageYesButton_10.tStart = t  # local t and not account for scr refresh
            imageYesButton_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_10.started')
            # update status
            imageYesButton_10.status = STARTED
            imageYesButton_10.setAutoDraw(True)
        
        # if imageYesButton_10 is active this frame...
        if imageYesButton_10.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_10 is stopping this frame...
        if imageYesButton_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_10.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_10.tStop = t  # not accounting for scr refresh
                imageYesButton_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_10.stopped')
                # update status
                imageYesButton_10.status = FINISHED
                imageYesButton_10.setAutoDraw(False)
        
        # *imageNoButton_10* updates
        
        # if imageNoButton_10 is starting this frame...
        if imageNoButton_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_10.frameNStart = frameN  # exact frame index
            imageNoButton_10.tStart = t  # local t and not account for scr refresh
            imageNoButton_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_10.started')
            # update status
            imageNoButton_10.status = STARTED
            imageNoButton_10.setAutoDraw(True)
        
        # if imageNoButton_10 is active this frame...
        if imageNoButton_10.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_10 is stopping this frame...
        if imageNoButton_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_10.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_10.tStop = t  # not accounting for scr refresh
                imageNoButton_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_10.stopped')
                # update status
                imageNoButton_10.status = FINISHED
                imageNoButton_10.setAutoDraw(False)
        # *mouse_10* updates
        
        # if mouse_10 is starting this frame...
        if mouse_10.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_10.frameNStart = frameN  # exact frame index
            mouse_10.tStart = t  # local t and not account for scr refresh
            mouse_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_10.started', t)
            # update status
            mouse_10.status = STARTED
            mouse_10.mouseClock.reset()
            prevButtonState = mouse_10.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_10 is stopping this frame...
        if mouse_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_10.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_10.tStop = t  # not accounting for scr refresh
                mouse_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_10.stopped', t)
                # update status
                mouse_10.status = FINISHED
        if mouse_10.status == STARTED:  # only update if started and not finished!
            buttons = mouse_10.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_10):
                            gotValidClick = True
                            mouse_10.clicked_name.append(obj.name)
                    x, y = mouse_10.getPos()
                    mouse_10.x.append(x)
                    mouse_10.y.append(y)
                    buttons = mouse_10.getPressed()
                    mouse_10.leftButton.append(buttons[0])
                    mouse_10.midButton.append(buttons[1])
                    mouse_10.rightButton.append(buttons[2])
                    mouse_10.time.append(mouse_10.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof10" ---
    for thisComponent in Prof10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof10.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_10.x', mouse_10.x)
    thisExp.addData('mouse_10.y', mouse_10.y)
    thisExp.addData('mouse_10.leftButton', mouse_10.leftButton)
    thisExp.addData('mouse_10.midButton', mouse_10.midButton)
    thisExp.addData('mouse_10.rightButton', mouse_10.rightButton)
    thisExp.addData('mouse_10.time', mouse_10.time)
    thisExp.addData('mouse_10.clicked_name', mouse_10.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof10_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof10_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_27
    mouse_27.x = []
    mouse_27.y = []
    mouse_27.leftButton = []
    mouse_27.midButton = []
    mouse_27.rightButton = []
    mouse_27.time = []
    mouse_27.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof10_enjoy_classComponents = [DidYouEnjoyThisProf_10, imageProf10_2, imageYesButton_27, imageNoButton_27, mouse_27]
    for thisComponent in Prof10_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof10_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_10* updates
        
        # if DidYouEnjoyThisProf_10 is starting this frame...
        if DidYouEnjoyThisProf_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_10.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_10.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_10, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_10.started')
            # update status
            DidYouEnjoyThisProf_10.status = STARTED
            DidYouEnjoyThisProf_10.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_10 is active this frame...
        if DidYouEnjoyThisProf_10.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_10 is stopping this frame...
        if DidYouEnjoyThisProf_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_10.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_10.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_10.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_10.stopped')
                # update status
                DidYouEnjoyThisProf_10.status = FINISHED
                DidYouEnjoyThisProf_10.setAutoDraw(False)
        
        # *imageProf10_2* updates
        
        # if imageProf10_2 is starting this frame...
        if imageProf10_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf10_2.frameNStart = frameN  # exact frame index
            imageProf10_2.tStart = t  # local t and not account for scr refresh
            imageProf10_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf10_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf10_2.started')
            # update status
            imageProf10_2.status = STARTED
            imageProf10_2.setAutoDraw(True)
        
        # if imageProf10_2 is active this frame...
        if imageProf10_2.status == STARTED:
            # update params
            pass
        
        # if imageProf10_2 is stopping this frame...
        if imageProf10_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf10_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf10_2.tStop = t  # not accounting for scr refresh
                imageProf10_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf10_2.stopped')
                # update status
                imageProf10_2.status = FINISHED
                imageProf10_2.setAutoDraw(False)
        
        # *imageYesButton_27* updates
        
        # if imageYesButton_27 is starting this frame...
        if imageYesButton_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_27.frameNStart = frameN  # exact frame index
            imageYesButton_27.tStart = t  # local t and not account for scr refresh
            imageYesButton_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_27.started')
            # update status
            imageYesButton_27.status = STARTED
            imageYesButton_27.setAutoDraw(True)
        
        # if imageYesButton_27 is active this frame...
        if imageYesButton_27.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_27 is stopping this frame...
        if imageYesButton_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_27.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_27.tStop = t  # not accounting for scr refresh
                imageYesButton_27.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_27.stopped')
                # update status
                imageYesButton_27.status = FINISHED
                imageYesButton_27.setAutoDraw(False)
        
        # *imageNoButton_27* updates
        
        # if imageNoButton_27 is starting this frame...
        if imageNoButton_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_27.frameNStart = frameN  # exact frame index
            imageNoButton_27.tStart = t  # local t and not account for scr refresh
            imageNoButton_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_27.started')
            # update status
            imageNoButton_27.status = STARTED
            imageNoButton_27.setAutoDraw(True)
        
        # if imageNoButton_27 is active this frame...
        if imageNoButton_27.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_27 is stopping this frame...
        if imageNoButton_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_27.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_27.tStop = t  # not accounting for scr refresh
                imageNoButton_27.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_27.stopped')
                # update status
                imageNoButton_27.status = FINISHED
                imageNoButton_27.setAutoDraw(False)
        # *mouse_27* updates
        
        # if mouse_27 is starting this frame...
        if mouse_27.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_27.frameNStart = frameN  # exact frame index
            mouse_27.tStart = t  # local t and not account for scr refresh
            mouse_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_27, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_27.started', t)
            # update status
            mouse_27.status = STARTED
            mouse_27.mouseClock.reset()
            prevButtonState = mouse_27.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_27 is stopping this frame...
        if mouse_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_27.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_27.tStop = t  # not accounting for scr refresh
                mouse_27.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_27.stopped', t)
                # update status
                mouse_27.status = FINISHED
        if mouse_27.status == STARTED:  # only update if started and not finished!
            buttons = mouse_27.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_27):
                            gotValidClick = True
                            mouse_27.clicked_name.append(obj.name)
                    x, y = mouse_27.getPos()
                    mouse_27.x.append(x)
                    mouse_27.y.append(y)
                    buttons = mouse_27.getPressed()
                    mouse_27.leftButton.append(buttons[0])
                    mouse_27.midButton.append(buttons[1])
                    mouse_27.rightButton.append(buttons[2])
                    mouse_27.time.append(mouse_27.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof10_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof10_enjoy_class" ---
    for thisComponent in Prof10_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof10_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_27.x', mouse_27.x)
    thisExp.addData('mouse_27.y', mouse_27.y)
    thisExp.addData('mouse_27.leftButton', mouse_27.leftButton)
    thisExp.addData('mouse_27.midButton', mouse_27.midButton)
    thisExp.addData('mouse_27.rightButton', mouse_27.rightButton)
    thisExp.addData('mouse_27.time', mouse_27.time)
    thisExp.addData('mouse_27.clicked_name', mouse_27.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof11" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof11.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_11
    mouse_11.x = []
    mouse_11.y = []
    mouse_11.leftButton = []
    mouse_11.midButton = []
    mouse_11.rightButton = []
    mouse_11.time = []
    mouse_11.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof11Components = [HaveYouTakenThisProf_11, imageProf11, imageYesButton_11, imageNoButton_11, mouse_11]
    for thisComponent in Prof11Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof11" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_11* updates
        
        # if HaveYouTakenThisProf_11 is starting this frame...
        if HaveYouTakenThisProf_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_11.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_11.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_11.started')
            # update status
            HaveYouTakenThisProf_11.status = STARTED
            HaveYouTakenThisProf_11.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_11 is active this frame...
        if HaveYouTakenThisProf_11.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_11 is stopping this frame...
        if HaveYouTakenThisProf_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_11.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_11.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_11.stopped')
                # update status
                HaveYouTakenThisProf_11.status = FINISHED
                HaveYouTakenThisProf_11.setAutoDraw(False)
        
        # *imageProf11* updates
        
        # if imageProf11 is starting this frame...
        if imageProf11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf11.frameNStart = frameN  # exact frame index
            imageProf11.tStart = t  # local t and not account for scr refresh
            imageProf11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf11.started')
            # update status
            imageProf11.status = STARTED
            imageProf11.setAutoDraw(True)
        
        # if imageProf11 is active this frame...
        if imageProf11.status == STARTED:
            # update params
            pass
        
        # if imageProf11 is stopping this frame...
        if imageProf11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf11.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf11.tStop = t  # not accounting for scr refresh
                imageProf11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf11.stopped')
                # update status
                imageProf11.status = FINISHED
                imageProf11.setAutoDraw(False)
        
        # *imageYesButton_11* updates
        
        # if imageYesButton_11 is starting this frame...
        if imageYesButton_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_11.frameNStart = frameN  # exact frame index
            imageYesButton_11.tStart = t  # local t and not account for scr refresh
            imageYesButton_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_11.started')
            # update status
            imageYesButton_11.status = STARTED
            imageYesButton_11.setAutoDraw(True)
        
        # if imageYesButton_11 is active this frame...
        if imageYesButton_11.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_11 is stopping this frame...
        if imageYesButton_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_11.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_11.tStop = t  # not accounting for scr refresh
                imageYesButton_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_11.stopped')
                # update status
                imageYesButton_11.status = FINISHED
                imageYesButton_11.setAutoDraw(False)
        
        # *imageNoButton_11* updates
        
        # if imageNoButton_11 is starting this frame...
        if imageNoButton_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_11.frameNStart = frameN  # exact frame index
            imageNoButton_11.tStart = t  # local t and not account for scr refresh
            imageNoButton_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_11.started')
            # update status
            imageNoButton_11.status = STARTED
            imageNoButton_11.setAutoDraw(True)
        
        # if imageNoButton_11 is active this frame...
        if imageNoButton_11.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_11 is stopping this frame...
        if imageNoButton_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_11.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_11.tStop = t  # not accounting for scr refresh
                imageNoButton_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_11.stopped')
                # update status
                imageNoButton_11.status = FINISHED
                imageNoButton_11.setAutoDraw(False)
        # *mouse_11* updates
        
        # if mouse_11 is starting this frame...
        if mouse_11.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_11.frameNStart = frameN  # exact frame index
            mouse_11.tStart = t  # local t and not account for scr refresh
            mouse_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_11.started', t)
            # update status
            mouse_11.status = STARTED
            mouse_11.mouseClock.reset()
            prevButtonState = mouse_11.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_11 is stopping this frame...
        if mouse_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_11.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_11.tStop = t  # not accounting for scr refresh
                mouse_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_11.stopped', t)
                # update status
                mouse_11.status = FINISHED
        if mouse_11.status == STARTED:  # only update if started and not finished!
            buttons = mouse_11.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_11):
                            gotValidClick = True
                            mouse_11.clicked_name.append(obj.name)
                    x, y = mouse_11.getPos()
                    mouse_11.x.append(x)
                    mouse_11.y.append(y)
                    buttons = mouse_11.getPressed()
                    mouse_11.leftButton.append(buttons[0])
                    mouse_11.midButton.append(buttons[1])
                    mouse_11.rightButton.append(buttons[2])
                    mouse_11.time.append(mouse_11.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof11" ---
    for thisComponent in Prof11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof11.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_11.x', mouse_11.x)
    thisExp.addData('mouse_11.y', mouse_11.y)
    thisExp.addData('mouse_11.leftButton', mouse_11.leftButton)
    thisExp.addData('mouse_11.midButton', mouse_11.midButton)
    thisExp.addData('mouse_11.rightButton', mouse_11.rightButton)
    thisExp.addData('mouse_11.time', mouse_11.time)
    thisExp.addData('mouse_11.clicked_name', mouse_11.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof11_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof11_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_28
    mouse_28.x = []
    mouse_28.y = []
    mouse_28.leftButton = []
    mouse_28.midButton = []
    mouse_28.rightButton = []
    mouse_28.time = []
    mouse_28.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof11_enjoy_classComponents = [DidYouEnjoyThisProf_11, imageProf11_2, imageYesButton_28, imageNoButton_28, mouse_28]
    for thisComponent in Prof11_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof11_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_11* updates
        
        # if DidYouEnjoyThisProf_11 is starting this frame...
        if DidYouEnjoyThisProf_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_11.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_11.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_11.started')
            # update status
            DidYouEnjoyThisProf_11.status = STARTED
            DidYouEnjoyThisProf_11.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_11 is active this frame...
        if DidYouEnjoyThisProf_11.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_11 is stopping this frame...
        if DidYouEnjoyThisProf_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_11.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_11.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_11.stopped')
                # update status
                DidYouEnjoyThisProf_11.status = FINISHED
                DidYouEnjoyThisProf_11.setAutoDraw(False)
        
        # *imageProf11_2* updates
        
        # if imageProf11_2 is starting this frame...
        if imageProf11_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf11_2.frameNStart = frameN  # exact frame index
            imageProf11_2.tStart = t  # local t and not account for scr refresh
            imageProf11_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf11_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf11_2.started')
            # update status
            imageProf11_2.status = STARTED
            imageProf11_2.setAutoDraw(True)
        
        # if imageProf11_2 is active this frame...
        if imageProf11_2.status == STARTED:
            # update params
            pass
        
        # if imageProf11_2 is stopping this frame...
        if imageProf11_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf11_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf11_2.tStop = t  # not accounting for scr refresh
                imageProf11_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf11_2.stopped')
                # update status
                imageProf11_2.status = FINISHED
                imageProf11_2.setAutoDraw(False)
        
        # *imageYesButton_28* updates
        
        # if imageYesButton_28 is starting this frame...
        if imageYesButton_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_28.frameNStart = frameN  # exact frame index
            imageYesButton_28.tStart = t  # local t and not account for scr refresh
            imageYesButton_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_28.started')
            # update status
            imageYesButton_28.status = STARTED
            imageYesButton_28.setAutoDraw(True)
        
        # if imageYesButton_28 is active this frame...
        if imageYesButton_28.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_28 is stopping this frame...
        if imageYesButton_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_28.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_28.tStop = t  # not accounting for scr refresh
                imageYesButton_28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_28.stopped')
                # update status
                imageYesButton_28.status = FINISHED
                imageYesButton_28.setAutoDraw(False)
        
        # *imageNoButton_28* updates
        
        # if imageNoButton_28 is starting this frame...
        if imageNoButton_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_28.frameNStart = frameN  # exact frame index
            imageNoButton_28.tStart = t  # local t and not account for scr refresh
            imageNoButton_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_28.started')
            # update status
            imageNoButton_28.status = STARTED
            imageNoButton_28.setAutoDraw(True)
        
        # if imageNoButton_28 is active this frame...
        if imageNoButton_28.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_28 is stopping this frame...
        if imageNoButton_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_28.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_28.tStop = t  # not accounting for scr refresh
                imageNoButton_28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_28.stopped')
                # update status
                imageNoButton_28.status = FINISHED
                imageNoButton_28.setAutoDraw(False)
        # *mouse_28* updates
        
        # if mouse_28 is starting this frame...
        if mouse_28.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_28.frameNStart = frameN  # exact frame index
            mouse_28.tStart = t  # local t and not account for scr refresh
            mouse_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_28, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_28.started', t)
            # update status
            mouse_28.status = STARTED
            mouse_28.mouseClock.reset()
            prevButtonState = mouse_28.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_28 is stopping this frame...
        if mouse_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_28.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_28.tStop = t  # not accounting for scr refresh
                mouse_28.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_28.stopped', t)
                # update status
                mouse_28.status = FINISHED
        if mouse_28.status == STARTED:  # only update if started and not finished!
            buttons = mouse_28.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_28):
                            gotValidClick = True
                            mouse_28.clicked_name.append(obj.name)
                    x, y = mouse_28.getPos()
                    mouse_28.x.append(x)
                    mouse_28.y.append(y)
                    buttons = mouse_28.getPressed()
                    mouse_28.leftButton.append(buttons[0])
                    mouse_28.midButton.append(buttons[1])
                    mouse_28.rightButton.append(buttons[2])
                    mouse_28.time.append(mouse_28.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof11_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof11_enjoy_class" ---
    for thisComponent in Prof11_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof11_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_28.x', mouse_28.x)
    thisExp.addData('mouse_28.y', mouse_28.y)
    thisExp.addData('mouse_28.leftButton', mouse_28.leftButton)
    thisExp.addData('mouse_28.midButton', mouse_28.midButton)
    thisExp.addData('mouse_28.rightButton', mouse_28.rightButton)
    thisExp.addData('mouse_28.time', mouse_28.time)
    thisExp.addData('mouse_28.clicked_name', mouse_28.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof12" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof12.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_12
    mouse_12.x = []
    mouse_12.y = []
    mouse_12.leftButton = []
    mouse_12.midButton = []
    mouse_12.rightButton = []
    mouse_12.time = []
    mouse_12.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof12Components = [HaveYouTakenThisProf_12, imageProf12, imageYesButton_12, imageNoButton_12, mouse_12]
    for thisComponent in Prof12Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof12" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_12* updates
        
        # if HaveYouTakenThisProf_12 is starting this frame...
        if HaveYouTakenThisProf_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_12.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_12.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_12.started')
            # update status
            HaveYouTakenThisProf_12.status = STARTED
            HaveYouTakenThisProf_12.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_12 is active this frame...
        if HaveYouTakenThisProf_12.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_12 is stopping this frame...
        if HaveYouTakenThisProf_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_12.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_12.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_12.stopped')
                # update status
                HaveYouTakenThisProf_12.status = FINISHED
                HaveYouTakenThisProf_12.setAutoDraw(False)
        
        # *imageProf12* updates
        
        # if imageProf12 is starting this frame...
        if imageProf12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf12.frameNStart = frameN  # exact frame index
            imageProf12.tStart = t  # local t and not account for scr refresh
            imageProf12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf12.started')
            # update status
            imageProf12.status = STARTED
            imageProf12.setAutoDraw(True)
        
        # if imageProf12 is active this frame...
        if imageProf12.status == STARTED:
            # update params
            pass
        
        # if imageProf12 is stopping this frame...
        if imageProf12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf12.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf12.tStop = t  # not accounting for scr refresh
                imageProf12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf12.stopped')
                # update status
                imageProf12.status = FINISHED
                imageProf12.setAutoDraw(False)
        
        # *imageYesButton_12* updates
        
        # if imageYesButton_12 is starting this frame...
        if imageYesButton_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_12.frameNStart = frameN  # exact frame index
            imageYesButton_12.tStart = t  # local t and not account for scr refresh
            imageYesButton_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_12.started')
            # update status
            imageYesButton_12.status = STARTED
            imageYesButton_12.setAutoDraw(True)
        
        # if imageYesButton_12 is active this frame...
        if imageYesButton_12.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_12 is stopping this frame...
        if imageYesButton_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_12.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_12.tStop = t  # not accounting for scr refresh
                imageYesButton_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_12.stopped')
                # update status
                imageYesButton_12.status = FINISHED
                imageYesButton_12.setAutoDraw(False)
        
        # *imageNoButton_12* updates
        
        # if imageNoButton_12 is starting this frame...
        if imageNoButton_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_12.frameNStart = frameN  # exact frame index
            imageNoButton_12.tStart = t  # local t and not account for scr refresh
            imageNoButton_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_12.started')
            # update status
            imageNoButton_12.status = STARTED
            imageNoButton_12.setAutoDraw(True)
        
        # if imageNoButton_12 is active this frame...
        if imageNoButton_12.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_12 is stopping this frame...
        if imageNoButton_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_12.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_12.tStop = t  # not accounting for scr refresh
                imageNoButton_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_12.stopped')
                # update status
                imageNoButton_12.status = FINISHED
                imageNoButton_12.setAutoDraw(False)
        # *mouse_12* updates
        
        # if mouse_12 is starting this frame...
        if mouse_12.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_12.frameNStart = frameN  # exact frame index
            mouse_12.tStart = t  # local t and not account for scr refresh
            mouse_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_12.started', t)
            # update status
            mouse_12.status = STARTED
            mouse_12.mouseClock.reset()
            prevButtonState = mouse_12.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_12 is stopping this frame...
        if mouse_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_12.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_12.tStop = t  # not accounting for scr refresh
                mouse_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_12.stopped', t)
                # update status
                mouse_12.status = FINISHED
        if mouse_12.status == STARTED:  # only update if started and not finished!
            buttons = mouse_12.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_12):
                            gotValidClick = True
                            mouse_12.clicked_name.append(obj.name)
                    x, y = mouse_12.getPos()
                    mouse_12.x.append(x)
                    mouse_12.y.append(y)
                    buttons = mouse_12.getPressed()
                    mouse_12.leftButton.append(buttons[0])
                    mouse_12.midButton.append(buttons[1])
                    mouse_12.rightButton.append(buttons[2])
                    mouse_12.time.append(mouse_12.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof12" ---
    for thisComponent in Prof12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof12.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_12.x', mouse_12.x)
    thisExp.addData('mouse_12.y', mouse_12.y)
    thisExp.addData('mouse_12.leftButton', mouse_12.leftButton)
    thisExp.addData('mouse_12.midButton', mouse_12.midButton)
    thisExp.addData('mouse_12.rightButton', mouse_12.rightButton)
    thisExp.addData('mouse_12.time', mouse_12.time)
    thisExp.addData('mouse_12.clicked_name', mouse_12.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof12_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof12_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_29
    mouse_29.x = []
    mouse_29.y = []
    mouse_29.leftButton = []
    mouse_29.midButton = []
    mouse_29.rightButton = []
    mouse_29.time = []
    mouse_29.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof12_enjoy_classComponents = [DidYouEnjoyThisProf_12, imageProf12_2, imageYesButton_29, imageNoButton_29, mouse_29]
    for thisComponent in Prof12_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof12_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_12* updates
        
        # if DidYouEnjoyThisProf_12 is starting this frame...
        if DidYouEnjoyThisProf_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_12.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_12.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_12.started')
            # update status
            DidYouEnjoyThisProf_12.status = STARTED
            DidYouEnjoyThisProf_12.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_12 is active this frame...
        if DidYouEnjoyThisProf_12.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_12 is stopping this frame...
        if DidYouEnjoyThisProf_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_12.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_12.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_12.stopped')
                # update status
                DidYouEnjoyThisProf_12.status = FINISHED
                DidYouEnjoyThisProf_12.setAutoDraw(False)
        
        # *imageProf12_2* updates
        
        # if imageProf12_2 is starting this frame...
        if imageProf12_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf12_2.frameNStart = frameN  # exact frame index
            imageProf12_2.tStart = t  # local t and not account for scr refresh
            imageProf12_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf12_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf12_2.started')
            # update status
            imageProf12_2.status = STARTED
            imageProf12_2.setAutoDraw(True)
        
        # if imageProf12_2 is active this frame...
        if imageProf12_2.status == STARTED:
            # update params
            pass
        
        # if imageProf12_2 is stopping this frame...
        if imageProf12_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf12_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf12_2.tStop = t  # not accounting for scr refresh
                imageProf12_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf12_2.stopped')
                # update status
                imageProf12_2.status = FINISHED
                imageProf12_2.setAutoDraw(False)
        
        # *imageYesButton_29* updates
        
        # if imageYesButton_29 is starting this frame...
        if imageYesButton_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_29.frameNStart = frameN  # exact frame index
            imageYesButton_29.tStart = t  # local t and not account for scr refresh
            imageYesButton_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_29.started')
            # update status
            imageYesButton_29.status = STARTED
            imageYesButton_29.setAutoDraw(True)
        
        # if imageYesButton_29 is active this frame...
        if imageYesButton_29.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_29 is stopping this frame...
        if imageYesButton_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_29.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_29.tStop = t  # not accounting for scr refresh
                imageYesButton_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_29.stopped')
                # update status
                imageYesButton_29.status = FINISHED
                imageYesButton_29.setAutoDraw(False)
        
        # *imageNoButton_29* updates
        
        # if imageNoButton_29 is starting this frame...
        if imageNoButton_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_29.frameNStart = frameN  # exact frame index
            imageNoButton_29.tStart = t  # local t and not account for scr refresh
            imageNoButton_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_29.started')
            # update status
            imageNoButton_29.status = STARTED
            imageNoButton_29.setAutoDraw(True)
        
        # if imageNoButton_29 is active this frame...
        if imageNoButton_29.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_29 is stopping this frame...
        if imageNoButton_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_29.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_29.tStop = t  # not accounting for scr refresh
                imageNoButton_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_29.stopped')
                # update status
                imageNoButton_29.status = FINISHED
                imageNoButton_29.setAutoDraw(False)
        # *mouse_29* updates
        
        # if mouse_29 is starting this frame...
        if mouse_29.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_29.frameNStart = frameN  # exact frame index
            mouse_29.tStart = t  # local t and not account for scr refresh
            mouse_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_29.started', t)
            # update status
            mouse_29.status = STARTED
            mouse_29.mouseClock.reset()
            prevButtonState = mouse_29.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_29 is stopping this frame...
        if mouse_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_29.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_29.tStop = t  # not accounting for scr refresh
                mouse_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_29.stopped', t)
                # update status
                mouse_29.status = FINISHED
        if mouse_29.status == STARTED:  # only update if started and not finished!
            buttons = mouse_29.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_29):
                            gotValidClick = True
                            mouse_29.clicked_name.append(obj.name)
                    x, y = mouse_29.getPos()
                    mouse_29.x.append(x)
                    mouse_29.y.append(y)
                    buttons = mouse_29.getPressed()
                    mouse_29.leftButton.append(buttons[0])
                    mouse_29.midButton.append(buttons[1])
                    mouse_29.rightButton.append(buttons[2])
                    mouse_29.time.append(mouse_29.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof12_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof12_enjoy_class" ---
    for thisComponent in Prof12_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof12_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_29.x', mouse_29.x)
    thisExp.addData('mouse_29.y', mouse_29.y)
    thisExp.addData('mouse_29.leftButton', mouse_29.leftButton)
    thisExp.addData('mouse_29.midButton', mouse_29.midButton)
    thisExp.addData('mouse_29.rightButton', mouse_29.rightButton)
    thisExp.addData('mouse_29.time', mouse_29.time)
    thisExp.addData('mouse_29.clicked_name', mouse_29.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof13" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof13.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_13
    mouse_13.x = []
    mouse_13.y = []
    mouse_13.leftButton = []
    mouse_13.midButton = []
    mouse_13.rightButton = []
    mouse_13.time = []
    mouse_13.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof13Components = [HaveYouTakenThisProf_13, imageProf13, imageYesButton_13, imageNoButton_13, mouse_13]
    for thisComponent in Prof13Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof13" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_13* updates
        
        # if HaveYouTakenThisProf_13 is starting this frame...
        if HaveYouTakenThisProf_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_13.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_13.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_13.started')
            # update status
            HaveYouTakenThisProf_13.status = STARTED
            HaveYouTakenThisProf_13.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_13 is active this frame...
        if HaveYouTakenThisProf_13.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_13 is stopping this frame...
        if HaveYouTakenThisProf_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_13.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_13.stopped')
                # update status
                HaveYouTakenThisProf_13.status = FINISHED
                HaveYouTakenThisProf_13.setAutoDraw(False)
        
        # *imageProf13* updates
        
        # if imageProf13 is starting this frame...
        if imageProf13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf13.frameNStart = frameN  # exact frame index
            imageProf13.tStart = t  # local t and not account for scr refresh
            imageProf13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf13.started')
            # update status
            imageProf13.status = STARTED
            imageProf13.setAutoDraw(True)
        
        # if imageProf13 is active this frame...
        if imageProf13.status == STARTED:
            # update params
            pass
        
        # if imageProf13 is stopping this frame...
        if imageProf13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf13.tStop = t  # not accounting for scr refresh
                imageProf13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf13.stopped')
                # update status
                imageProf13.status = FINISHED
                imageProf13.setAutoDraw(False)
        
        # *imageYesButton_13* updates
        
        # if imageYesButton_13 is starting this frame...
        if imageYesButton_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_13.frameNStart = frameN  # exact frame index
            imageYesButton_13.tStart = t  # local t and not account for scr refresh
            imageYesButton_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_13.started')
            # update status
            imageYesButton_13.status = STARTED
            imageYesButton_13.setAutoDraw(True)
        
        # if imageYesButton_13 is active this frame...
        if imageYesButton_13.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_13 is stopping this frame...
        if imageYesButton_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_13.tStop = t  # not accounting for scr refresh
                imageYesButton_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_13.stopped')
                # update status
                imageYesButton_13.status = FINISHED
                imageYesButton_13.setAutoDraw(False)
        
        # *imageNoButton_13* updates
        
        # if imageNoButton_13 is starting this frame...
        if imageNoButton_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_13.frameNStart = frameN  # exact frame index
            imageNoButton_13.tStart = t  # local t and not account for scr refresh
            imageNoButton_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_13.started')
            # update status
            imageNoButton_13.status = STARTED
            imageNoButton_13.setAutoDraw(True)
        
        # if imageNoButton_13 is active this frame...
        if imageNoButton_13.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_13 is stopping this frame...
        if imageNoButton_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_13.tStop = t  # not accounting for scr refresh
                imageNoButton_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_13.stopped')
                # update status
                imageNoButton_13.status = FINISHED
                imageNoButton_13.setAutoDraw(False)
        # *mouse_13* updates
        
        # if mouse_13 is starting this frame...
        if mouse_13.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_13.frameNStart = frameN  # exact frame index
            mouse_13.tStart = t  # local t and not account for scr refresh
            mouse_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_13.started', t)
            # update status
            mouse_13.status = STARTED
            mouse_13.mouseClock.reset()
            prevButtonState = mouse_13.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_13 is stopping this frame...
        if mouse_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_13.tStop = t  # not accounting for scr refresh
                mouse_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_13.stopped', t)
                # update status
                mouse_13.status = FINISHED
        if mouse_13.status == STARTED:  # only update if started and not finished!
            buttons = mouse_13.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_13):
                            gotValidClick = True
                            mouse_13.clicked_name.append(obj.name)
                    x, y = mouse_13.getPos()
                    mouse_13.x.append(x)
                    mouse_13.y.append(y)
                    buttons = mouse_13.getPressed()
                    mouse_13.leftButton.append(buttons[0])
                    mouse_13.midButton.append(buttons[1])
                    mouse_13.rightButton.append(buttons[2])
                    mouse_13.time.append(mouse_13.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof13Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof13" ---
    for thisComponent in Prof13Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof13.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_13.x', mouse_13.x)
    thisExp.addData('mouse_13.y', mouse_13.y)
    thisExp.addData('mouse_13.leftButton', mouse_13.leftButton)
    thisExp.addData('mouse_13.midButton', mouse_13.midButton)
    thisExp.addData('mouse_13.rightButton', mouse_13.rightButton)
    thisExp.addData('mouse_13.time', mouse_13.time)
    thisExp.addData('mouse_13.clicked_name', mouse_13.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof13_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof13_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_30
    mouse_30.x = []
    mouse_30.y = []
    mouse_30.leftButton = []
    mouse_30.midButton = []
    mouse_30.rightButton = []
    mouse_30.time = []
    mouse_30.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof13_enjoy_classComponents = [DidYouEnjoyThisProf_13, imageProf13_2, imageYesButton_30, imageNoButton_30, mouse_30]
    for thisComponent in Prof13_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof13_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_13* updates
        
        # if DidYouEnjoyThisProf_13 is starting this frame...
        if DidYouEnjoyThisProf_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_13.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_13.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_13.started')
            # update status
            DidYouEnjoyThisProf_13.status = STARTED
            DidYouEnjoyThisProf_13.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_13 is active this frame...
        if DidYouEnjoyThisProf_13.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_13 is stopping this frame...
        if DidYouEnjoyThisProf_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_13.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_13.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_13.stopped')
                # update status
                DidYouEnjoyThisProf_13.status = FINISHED
                DidYouEnjoyThisProf_13.setAutoDraw(False)
        
        # *imageProf13_2* updates
        
        # if imageProf13_2 is starting this frame...
        if imageProf13_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf13_2.frameNStart = frameN  # exact frame index
            imageProf13_2.tStart = t  # local t and not account for scr refresh
            imageProf13_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf13_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf13_2.started')
            # update status
            imageProf13_2.status = STARTED
            imageProf13_2.setAutoDraw(True)
        
        # if imageProf13_2 is active this frame...
        if imageProf13_2.status == STARTED:
            # update params
            pass
        
        # if imageProf13_2 is stopping this frame...
        if imageProf13_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf13_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf13_2.tStop = t  # not accounting for scr refresh
                imageProf13_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf13_2.stopped')
                # update status
                imageProf13_2.status = FINISHED
                imageProf13_2.setAutoDraw(False)
        
        # *imageYesButton_30* updates
        
        # if imageYesButton_30 is starting this frame...
        if imageYesButton_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_30.frameNStart = frameN  # exact frame index
            imageYesButton_30.tStart = t  # local t and not account for scr refresh
            imageYesButton_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_30.started')
            # update status
            imageYesButton_30.status = STARTED
            imageYesButton_30.setAutoDraw(True)
        
        # if imageYesButton_30 is active this frame...
        if imageYesButton_30.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_30 is stopping this frame...
        if imageYesButton_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_30.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_30.tStop = t  # not accounting for scr refresh
                imageYesButton_30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_30.stopped')
                # update status
                imageYesButton_30.status = FINISHED
                imageYesButton_30.setAutoDraw(False)
        
        # *imageNoButton_30* updates
        
        # if imageNoButton_30 is starting this frame...
        if imageNoButton_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_30.frameNStart = frameN  # exact frame index
            imageNoButton_30.tStart = t  # local t and not account for scr refresh
            imageNoButton_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_30.started')
            # update status
            imageNoButton_30.status = STARTED
            imageNoButton_30.setAutoDraw(True)
        
        # if imageNoButton_30 is active this frame...
        if imageNoButton_30.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_30 is stopping this frame...
        if imageNoButton_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_30.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_30.tStop = t  # not accounting for scr refresh
                imageNoButton_30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_30.stopped')
                # update status
                imageNoButton_30.status = FINISHED
                imageNoButton_30.setAutoDraw(False)
        # *mouse_30* updates
        
        # if mouse_30 is starting this frame...
        if mouse_30.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_30.frameNStart = frameN  # exact frame index
            mouse_30.tStart = t  # local t and not account for scr refresh
            mouse_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_30.started', t)
            # update status
            mouse_30.status = STARTED
            mouse_30.mouseClock.reset()
            prevButtonState = mouse_30.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_30 is stopping this frame...
        if mouse_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_30.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_30.tStop = t  # not accounting for scr refresh
                mouse_30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_30.stopped', t)
                # update status
                mouse_30.status = FINISHED
        if mouse_30.status == STARTED:  # only update if started and not finished!
            buttons = mouse_30.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_30):
                            gotValidClick = True
                            mouse_30.clicked_name.append(obj.name)
                    x, y = mouse_30.getPos()
                    mouse_30.x.append(x)
                    mouse_30.y.append(y)
                    buttons = mouse_30.getPressed()
                    mouse_30.leftButton.append(buttons[0])
                    mouse_30.midButton.append(buttons[1])
                    mouse_30.rightButton.append(buttons[2])
                    mouse_30.time.append(mouse_30.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof13_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof13_enjoy_class" ---
    for thisComponent in Prof13_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof13_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_30.x', mouse_30.x)
    thisExp.addData('mouse_30.y', mouse_30.y)
    thisExp.addData('mouse_30.leftButton', mouse_30.leftButton)
    thisExp.addData('mouse_30.midButton', mouse_30.midButton)
    thisExp.addData('mouse_30.rightButton', mouse_30.rightButton)
    thisExp.addData('mouse_30.time', mouse_30.time)
    thisExp.addData('mouse_30.clicked_name', mouse_30.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof14" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof14.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_14
    mouse_14.x = []
    mouse_14.y = []
    mouse_14.leftButton = []
    mouse_14.midButton = []
    mouse_14.rightButton = []
    mouse_14.time = []
    mouse_14.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof14Components = [HaveYouTakenThisProf_14, imageProf14, imageYesButton_14, imageNoButton_14, mouse_14]
    for thisComponent in Prof14Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof14" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_14* updates
        
        # if HaveYouTakenThisProf_14 is starting this frame...
        if HaveYouTakenThisProf_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_14.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_14.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_14.started')
            # update status
            HaveYouTakenThisProf_14.status = STARTED
            HaveYouTakenThisProf_14.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_14 is active this frame...
        if HaveYouTakenThisProf_14.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_14 is stopping this frame...
        if HaveYouTakenThisProf_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_14.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_14.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_14.stopped')
                # update status
                HaveYouTakenThisProf_14.status = FINISHED
                HaveYouTakenThisProf_14.setAutoDraw(False)
        
        # *imageProf14* updates
        
        # if imageProf14 is starting this frame...
        if imageProf14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf14.frameNStart = frameN  # exact frame index
            imageProf14.tStart = t  # local t and not account for scr refresh
            imageProf14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf14.started')
            # update status
            imageProf14.status = STARTED
            imageProf14.setAutoDraw(True)
        
        # if imageProf14 is active this frame...
        if imageProf14.status == STARTED:
            # update params
            pass
        
        # if imageProf14 is stopping this frame...
        if imageProf14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf14.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf14.tStop = t  # not accounting for scr refresh
                imageProf14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf14.stopped')
                # update status
                imageProf14.status = FINISHED
                imageProf14.setAutoDraw(False)
        
        # *imageYesButton_14* updates
        
        # if imageYesButton_14 is starting this frame...
        if imageYesButton_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_14.frameNStart = frameN  # exact frame index
            imageYesButton_14.tStart = t  # local t and not account for scr refresh
            imageYesButton_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_14.started')
            # update status
            imageYesButton_14.status = STARTED
            imageYesButton_14.setAutoDraw(True)
        
        # if imageYesButton_14 is active this frame...
        if imageYesButton_14.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_14 is stopping this frame...
        if imageYesButton_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_14.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_14.tStop = t  # not accounting for scr refresh
                imageYesButton_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_14.stopped')
                # update status
                imageYesButton_14.status = FINISHED
                imageYesButton_14.setAutoDraw(False)
        
        # *imageNoButton_14* updates
        
        # if imageNoButton_14 is starting this frame...
        if imageNoButton_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_14.frameNStart = frameN  # exact frame index
            imageNoButton_14.tStart = t  # local t and not account for scr refresh
            imageNoButton_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_14.started')
            # update status
            imageNoButton_14.status = STARTED
            imageNoButton_14.setAutoDraw(True)
        
        # if imageNoButton_14 is active this frame...
        if imageNoButton_14.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_14 is stopping this frame...
        if imageNoButton_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_14.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_14.tStop = t  # not accounting for scr refresh
                imageNoButton_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_14.stopped')
                # update status
                imageNoButton_14.status = FINISHED
                imageNoButton_14.setAutoDraw(False)
        # *mouse_14* updates
        
        # if mouse_14 is starting this frame...
        if mouse_14.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_14.frameNStart = frameN  # exact frame index
            mouse_14.tStart = t  # local t and not account for scr refresh
            mouse_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_14.started', t)
            # update status
            mouse_14.status = STARTED
            mouse_14.mouseClock.reset()
            prevButtonState = mouse_14.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_14 is stopping this frame...
        if mouse_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_14.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_14.tStop = t  # not accounting for scr refresh
                mouse_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_14.stopped', t)
                # update status
                mouse_14.status = FINISHED
        if mouse_14.status == STARTED:  # only update if started and not finished!
            buttons = mouse_14.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_14):
                            gotValidClick = True
                            mouse_14.clicked_name.append(obj.name)
                    x, y = mouse_14.getPos()
                    mouse_14.x.append(x)
                    mouse_14.y.append(y)
                    buttons = mouse_14.getPressed()
                    mouse_14.leftButton.append(buttons[0])
                    mouse_14.midButton.append(buttons[1])
                    mouse_14.rightButton.append(buttons[2])
                    mouse_14.time.append(mouse_14.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof14Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof14" ---
    for thisComponent in Prof14Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof14.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_14.x', mouse_14.x)
    thisExp.addData('mouse_14.y', mouse_14.y)
    thisExp.addData('mouse_14.leftButton', mouse_14.leftButton)
    thisExp.addData('mouse_14.midButton', mouse_14.midButton)
    thisExp.addData('mouse_14.rightButton', mouse_14.rightButton)
    thisExp.addData('mouse_14.time', mouse_14.time)
    thisExp.addData('mouse_14.clicked_name', mouse_14.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof14_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof14_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_31
    mouse_31.x = []
    mouse_31.y = []
    mouse_31.leftButton = []
    mouse_31.midButton = []
    mouse_31.rightButton = []
    mouse_31.time = []
    mouse_31.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof14_enjoy_classComponents = [DidYouEnjoyThisProf_14, imageProf14_2, imageYesButton_31, imageNoButton_31, mouse_31]
    for thisComponent in Prof14_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof14_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_14* updates
        
        # if DidYouEnjoyThisProf_14 is starting this frame...
        if DidYouEnjoyThisProf_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_14.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_14.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_14.started')
            # update status
            DidYouEnjoyThisProf_14.status = STARTED
            DidYouEnjoyThisProf_14.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_14 is active this frame...
        if DidYouEnjoyThisProf_14.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_14 is stopping this frame...
        if DidYouEnjoyThisProf_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_14.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_14.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_14.stopped')
                # update status
                DidYouEnjoyThisProf_14.status = FINISHED
                DidYouEnjoyThisProf_14.setAutoDraw(False)
        
        # *imageProf14_2* updates
        
        # if imageProf14_2 is starting this frame...
        if imageProf14_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf14_2.frameNStart = frameN  # exact frame index
            imageProf14_2.tStart = t  # local t and not account for scr refresh
            imageProf14_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf14_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf14_2.started')
            # update status
            imageProf14_2.status = STARTED
            imageProf14_2.setAutoDraw(True)
        
        # if imageProf14_2 is active this frame...
        if imageProf14_2.status == STARTED:
            # update params
            pass
        
        # if imageProf14_2 is stopping this frame...
        if imageProf14_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf14_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf14_2.tStop = t  # not accounting for scr refresh
                imageProf14_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf14_2.stopped')
                # update status
                imageProf14_2.status = FINISHED
                imageProf14_2.setAutoDraw(False)
        
        # *imageYesButton_31* updates
        
        # if imageYesButton_31 is starting this frame...
        if imageYesButton_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_31.frameNStart = frameN  # exact frame index
            imageYesButton_31.tStart = t  # local t and not account for scr refresh
            imageYesButton_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_31.started')
            # update status
            imageYesButton_31.status = STARTED
            imageYesButton_31.setAutoDraw(True)
        
        # if imageYesButton_31 is active this frame...
        if imageYesButton_31.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_31 is stopping this frame...
        if imageYesButton_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_31.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_31.tStop = t  # not accounting for scr refresh
                imageYesButton_31.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_31.stopped')
                # update status
                imageYesButton_31.status = FINISHED
                imageYesButton_31.setAutoDraw(False)
        
        # *imageNoButton_31* updates
        
        # if imageNoButton_31 is starting this frame...
        if imageNoButton_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_31.frameNStart = frameN  # exact frame index
            imageNoButton_31.tStart = t  # local t and not account for scr refresh
            imageNoButton_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_31.started')
            # update status
            imageNoButton_31.status = STARTED
            imageNoButton_31.setAutoDraw(True)
        
        # if imageNoButton_31 is active this frame...
        if imageNoButton_31.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_31 is stopping this frame...
        if imageNoButton_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_31.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_31.tStop = t  # not accounting for scr refresh
                imageNoButton_31.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_31.stopped')
                # update status
                imageNoButton_31.status = FINISHED
                imageNoButton_31.setAutoDraw(False)
        # *mouse_31* updates
        
        # if mouse_31 is starting this frame...
        if mouse_31.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_31.frameNStart = frameN  # exact frame index
            mouse_31.tStart = t  # local t and not account for scr refresh
            mouse_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_31, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_31.started', t)
            # update status
            mouse_31.status = STARTED
            mouse_31.mouseClock.reset()
            prevButtonState = mouse_31.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_31 is stopping this frame...
        if mouse_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_31.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_31.tStop = t  # not accounting for scr refresh
                mouse_31.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_31.stopped', t)
                # update status
                mouse_31.status = FINISHED
        if mouse_31.status == STARTED:  # only update if started and not finished!
            buttons = mouse_31.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_31):
                            gotValidClick = True
                            mouse_31.clicked_name.append(obj.name)
                    x, y = mouse_31.getPos()
                    mouse_31.x.append(x)
                    mouse_31.y.append(y)
                    buttons = mouse_31.getPressed()
                    mouse_31.leftButton.append(buttons[0])
                    mouse_31.midButton.append(buttons[1])
                    mouse_31.rightButton.append(buttons[2])
                    mouse_31.time.append(mouse_31.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof14_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof14_enjoy_class" ---
    for thisComponent in Prof14_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof14_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_31.x', mouse_31.x)
    thisExp.addData('mouse_31.y', mouse_31.y)
    thisExp.addData('mouse_31.leftButton', mouse_31.leftButton)
    thisExp.addData('mouse_31.midButton', mouse_31.midButton)
    thisExp.addData('mouse_31.rightButton', mouse_31.rightButton)
    thisExp.addData('mouse_31.time', mouse_31.time)
    thisExp.addData('mouse_31.clicked_name', mouse_31.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof15" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof15.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_15
    mouse_15.x = []
    mouse_15.y = []
    mouse_15.leftButton = []
    mouse_15.midButton = []
    mouse_15.rightButton = []
    mouse_15.time = []
    mouse_15.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof15Components = [HaveYouTakenThisProf_15, imageProf15, imageYesButton_15, imageNoButton_15, mouse_15]
    for thisComponent in Prof15Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof15" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_15* updates
        
        # if HaveYouTakenThisProf_15 is starting this frame...
        if HaveYouTakenThisProf_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_15.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_15.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_15.started')
            # update status
            HaveYouTakenThisProf_15.status = STARTED
            HaveYouTakenThisProf_15.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_15 is active this frame...
        if HaveYouTakenThisProf_15.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_15 is stopping this frame...
        if HaveYouTakenThisProf_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_15.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_15.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_15.stopped')
                # update status
                HaveYouTakenThisProf_15.status = FINISHED
                HaveYouTakenThisProf_15.setAutoDraw(False)
        
        # *imageProf15* updates
        
        # if imageProf15 is starting this frame...
        if imageProf15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf15.frameNStart = frameN  # exact frame index
            imageProf15.tStart = t  # local t and not account for scr refresh
            imageProf15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf15.started')
            # update status
            imageProf15.status = STARTED
            imageProf15.setAutoDraw(True)
        
        # if imageProf15 is active this frame...
        if imageProf15.status == STARTED:
            # update params
            pass
        
        # if imageProf15 is stopping this frame...
        if imageProf15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf15.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf15.tStop = t  # not accounting for scr refresh
                imageProf15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf15.stopped')
                # update status
                imageProf15.status = FINISHED
                imageProf15.setAutoDraw(False)
        
        # *imageYesButton_15* updates
        
        # if imageYesButton_15 is starting this frame...
        if imageYesButton_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_15.frameNStart = frameN  # exact frame index
            imageYesButton_15.tStart = t  # local t and not account for scr refresh
            imageYesButton_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_15.started')
            # update status
            imageYesButton_15.status = STARTED
            imageYesButton_15.setAutoDraw(True)
        
        # if imageYesButton_15 is active this frame...
        if imageYesButton_15.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_15 is stopping this frame...
        if imageYesButton_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_15.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_15.tStop = t  # not accounting for scr refresh
                imageYesButton_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_15.stopped')
                # update status
                imageYesButton_15.status = FINISHED
                imageYesButton_15.setAutoDraw(False)
        
        # *imageNoButton_15* updates
        
        # if imageNoButton_15 is starting this frame...
        if imageNoButton_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_15.frameNStart = frameN  # exact frame index
            imageNoButton_15.tStart = t  # local t and not account for scr refresh
            imageNoButton_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_15.started')
            # update status
            imageNoButton_15.status = STARTED
            imageNoButton_15.setAutoDraw(True)
        
        # if imageNoButton_15 is active this frame...
        if imageNoButton_15.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_15 is stopping this frame...
        if imageNoButton_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_15.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_15.tStop = t  # not accounting for scr refresh
                imageNoButton_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_15.stopped')
                # update status
                imageNoButton_15.status = FINISHED
                imageNoButton_15.setAutoDraw(False)
        # *mouse_15* updates
        
        # if mouse_15 is starting this frame...
        if mouse_15.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_15.frameNStart = frameN  # exact frame index
            mouse_15.tStart = t  # local t and not account for scr refresh
            mouse_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_15.started', t)
            # update status
            mouse_15.status = STARTED
            mouse_15.mouseClock.reset()
            prevButtonState = mouse_15.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_15 is stopping this frame...
        if mouse_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_15.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_15.tStop = t  # not accounting for scr refresh
                mouse_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_15.stopped', t)
                # update status
                mouse_15.status = FINISHED
        if mouse_15.status == STARTED:  # only update if started and not finished!
            buttons = mouse_15.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_15):
                            gotValidClick = True
                            mouse_15.clicked_name.append(obj.name)
                    x, y = mouse_15.getPos()
                    mouse_15.x.append(x)
                    mouse_15.y.append(y)
                    buttons = mouse_15.getPressed()
                    mouse_15.leftButton.append(buttons[0])
                    mouse_15.midButton.append(buttons[1])
                    mouse_15.rightButton.append(buttons[2])
                    mouse_15.time.append(mouse_15.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof15Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof15" ---
    for thisComponent in Prof15Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof15.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_15.x', mouse_15.x)
    thisExp.addData('mouse_15.y', mouse_15.y)
    thisExp.addData('mouse_15.leftButton', mouse_15.leftButton)
    thisExp.addData('mouse_15.midButton', mouse_15.midButton)
    thisExp.addData('mouse_15.rightButton', mouse_15.rightButton)
    thisExp.addData('mouse_15.time', mouse_15.time)
    thisExp.addData('mouse_15.clicked_name', mouse_15.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof15_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof15_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_32
    mouse_32.x = []
    mouse_32.y = []
    mouse_32.leftButton = []
    mouse_32.midButton = []
    mouse_32.rightButton = []
    mouse_32.time = []
    mouse_32.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof15_enjoy_classComponents = [DidYouEnjoyThisProf_15, imageProf15_2, imageYesButton_33, imageNoButton_32, mouse_32]
    for thisComponent in Prof15_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof15_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_15* updates
        
        # if DidYouEnjoyThisProf_15 is starting this frame...
        if DidYouEnjoyThisProf_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_15.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_15.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_15.started')
            # update status
            DidYouEnjoyThisProf_15.status = STARTED
            DidYouEnjoyThisProf_15.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_15 is active this frame...
        if DidYouEnjoyThisProf_15.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_15 is stopping this frame...
        if DidYouEnjoyThisProf_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_15.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_15.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_15.stopped')
                # update status
                DidYouEnjoyThisProf_15.status = FINISHED
                DidYouEnjoyThisProf_15.setAutoDraw(False)
        
        # *imageProf15_2* updates
        
        # if imageProf15_2 is starting this frame...
        if imageProf15_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf15_2.frameNStart = frameN  # exact frame index
            imageProf15_2.tStart = t  # local t and not account for scr refresh
            imageProf15_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf15_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf15_2.started')
            # update status
            imageProf15_2.status = STARTED
            imageProf15_2.setAutoDraw(True)
        
        # if imageProf15_2 is active this frame...
        if imageProf15_2.status == STARTED:
            # update params
            pass
        
        # if imageProf15_2 is stopping this frame...
        if imageProf15_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf15_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf15_2.tStop = t  # not accounting for scr refresh
                imageProf15_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf15_2.stopped')
                # update status
                imageProf15_2.status = FINISHED
                imageProf15_2.setAutoDraw(False)
        
        # *imageYesButton_33* updates
        
        # if imageYesButton_33 is starting this frame...
        if imageYesButton_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_33.frameNStart = frameN  # exact frame index
            imageYesButton_33.tStart = t  # local t and not account for scr refresh
            imageYesButton_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_33.started')
            # update status
            imageYesButton_33.status = STARTED
            imageYesButton_33.setAutoDraw(True)
        
        # if imageYesButton_33 is active this frame...
        if imageYesButton_33.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_33 is stopping this frame...
        if imageYesButton_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_33.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_33.tStop = t  # not accounting for scr refresh
                imageYesButton_33.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_33.stopped')
                # update status
                imageYesButton_33.status = FINISHED
                imageYesButton_33.setAutoDraw(False)
        
        # *imageNoButton_32* updates
        
        # if imageNoButton_32 is starting this frame...
        if imageNoButton_32.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_32.frameNStart = frameN  # exact frame index
            imageNoButton_32.tStart = t  # local t and not account for scr refresh
            imageNoButton_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_32.started')
            # update status
            imageNoButton_32.status = STARTED
            imageNoButton_32.setAutoDraw(True)
        
        # if imageNoButton_32 is active this frame...
        if imageNoButton_32.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_32 is stopping this frame...
        if imageNoButton_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_32.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_32.tStop = t  # not accounting for scr refresh
                imageNoButton_32.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_32.stopped')
                # update status
                imageNoButton_32.status = FINISHED
                imageNoButton_32.setAutoDraw(False)
        # *mouse_32* updates
        
        # if mouse_32 is starting this frame...
        if mouse_32.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_32.frameNStart = frameN  # exact frame index
            mouse_32.tStart = t  # local t and not account for scr refresh
            mouse_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_32, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_32.started', t)
            # update status
            mouse_32.status = STARTED
            mouse_32.mouseClock.reset()
            prevButtonState = mouse_32.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_32 is stopping this frame...
        if mouse_32.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_32.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_32.tStop = t  # not accounting for scr refresh
                mouse_32.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_32.stopped', t)
                # update status
                mouse_32.status = FINISHED
        if mouse_32.status == STARTED:  # only update if started and not finished!
            buttons = mouse_32.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_32):
                            gotValidClick = True
                            mouse_32.clicked_name.append(obj.name)
                    x, y = mouse_32.getPos()
                    mouse_32.x.append(x)
                    mouse_32.y.append(y)
                    buttons = mouse_32.getPressed()
                    mouse_32.leftButton.append(buttons[0])
                    mouse_32.midButton.append(buttons[1])
                    mouse_32.rightButton.append(buttons[2])
                    mouse_32.time.append(mouse_32.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof15_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof15_enjoy_class" ---
    for thisComponent in Prof15_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof15_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_32.x', mouse_32.x)
    thisExp.addData('mouse_32.y', mouse_32.y)
    thisExp.addData('mouse_32.leftButton', mouse_32.leftButton)
    thisExp.addData('mouse_32.midButton', mouse_32.midButton)
    thisExp.addData('mouse_32.rightButton', mouse_32.rightButton)
    thisExp.addData('mouse_32.time', mouse_32.time)
    thisExp.addData('mouse_32.clicked_name', mouse_32.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof16" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof16.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_16
    mouse_16.x = []
    mouse_16.y = []
    mouse_16.leftButton = []
    mouse_16.midButton = []
    mouse_16.rightButton = []
    mouse_16.time = []
    mouse_16.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof16Components = [HaveYouTakenThisProf_16, imageProf16, imageYesButton_16, imageNoButton_16, mouse_16]
    for thisComponent in Prof16Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof16" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_16* updates
        
        # if HaveYouTakenThisProf_16 is starting this frame...
        if HaveYouTakenThisProf_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_16.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_16.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_16.started')
            # update status
            HaveYouTakenThisProf_16.status = STARTED
            HaveYouTakenThisProf_16.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_16 is active this frame...
        if HaveYouTakenThisProf_16.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_16 is stopping this frame...
        if HaveYouTakenThisProf_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_16.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_16.stopped')
                # update status
                HaveYouTakenThisProf_16.status = FINISHED
                HaveYouTakenThisProf_16.setAutoDraw(False)
        
        # *imageProf16* updates
        
        # if imageProf16 is starting this frame...
        if imageProf16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf16.frameNStart = frameN  # exact frame index
            imageProf16.tStart = t  # local t and not account for scr refresh
            imageProf16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf16.started')
            # update status
            imageProf16.status = STARTED
            imageProf16.setAutoDraw(True)
        
        # if imageProf16 is active this frame...
        if imageProf16.status == STARTED:
            # update params
            pass
        
        # if imageProf16 is stopping this frame...
        if imageProf16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf16.tStop = t  # not accounting for scr refresh
                imageProf16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf16.stopped')
                # update status
                imageProf16.status = FINISHED
                imageProf16.setAutoDraw(False)
        
        # *imageYesButton_16* updates
        
        # if imageYesButton_16 is starting this frame...
        if imageYesButton_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_16.frameNStart = frameN  # exact frame index
            imageYesButton_16.tStart = t  # local t and not account for scr refresh
            imageYesButton_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_16.started')
            # update status
            imageYesButton_16.status = STARTED
            imageYesButton_16.setAutoDraw(True)
        
        # if imageYesButton_16 is active this frame...
        if imageYesButton_16.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_16 is stopping this frame...
        if imageYesButton_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_16.tStop = t  # not accounting for scr refresh
                imageYesButton_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_16.stopped')
                # update status
                imageYesButton_16.status = FINISHED
                imageYesButton_16.setAutoDraw(False)
        
        # *imageNoButton_16* updates
        
        # if imageNoButton_16 is starting this frame...
        if imageNoButton_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_16.frameNStart = frameN  # exact frame index
            imageNoButton_16.tStart = t  # local t and not account for scr refresh
            imageNoButton_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_16.started')
            # update status
            imageNoButton_16.status = STARTED
            imageNoButton_16.setAutoDraw(True)
        
        # if imageNoButton_16 is active this frame...
        if imageNoButton_16.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_16 is stopping this frame...
        if imageNoButton_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_16.tStop = t  # not accounting for scr refresh
                imageNoButton_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_16.stopped')
                # update status
                imageNoButton_16.status = FINISHED
                imageNoButton_16.setAutoDraw(False)
        # *mouse_16* updates
        
        # if mouse_16 is starting this frame...
        if mouse_16.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_16.frameNStart = frameN  # exact frame index
            mouse_16.tStart = t  # local t and not account for scr refresh
            mouse_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_16.started', t)
            # update status
            mouse_16.status = STARTED
            mouse_16.mouseClock.reset()
            prevButtonState = mouse_16.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_16 is stopping this frame...
        if mouse_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_16.tStop = t  # not accounting for scr refresh
                mouse_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_16.stopped', t)
                # update status
                mouse_16.status = FINISHED
        if mouse_16.status == STARTED:  # only update if started and not finished!
            buttons = mouse_16.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_16):
                            gotValidClick = True
                            mouse_16.clicked_name.append(obj.name)
                    x, y = mouse_16.getPos()
                    mouse_16.x.append(x)
                    mouse_16.y.append(y)
                    buttons = mouse_16.getPressed()
                    mouse_16.leftButton.append(buttons[0])
                    mouse_16.midButton.append(buttons[1])
                    mouse_16.rightButton.append(buttons[2])
                    mouse_16.time.append(mouse_16.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof16Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof16" ---
    for thisComponent in Prof16Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof16.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_16.x', mouse_16.x)
    thisExp.addData('mouse_16.y', mouse_16.y)
    thisExp.addData('mouse_16.leftButton', mouse_16.leftButton)
    thisExp.addData('mouse_16.midButton', mouse_16.midButton)
    thisExp.addData('mouse_16.rightButton', mouse_16.rightButton)
    thisExp.addData('mouse_16.time', mouse_16.time)
    thisExp.addData('mouse_16.clicked_name', mouse_16.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof16_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof16_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_33
    mouse_33.x = []
    mouse_33.y = []
    mouse_33.leftButton = []
    mouse_33.midButton = []
    mouse_33.rightButton = []
    mouse_33.time = []
    mouse_33.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof16_enjoy_classComponents = [DidYouEnjoyThisProf_16, imageProf16_2, imageYesButton_34, imageNoButton_33, mouse_33]
    for thisComponent in Prof16_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof16_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_16* updates
        
        # if DidYouEnjoyThisProf_16 is starting this frame...
        if DidYouEnjoyThisProf_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_16.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_16.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_16.started')
            # update status
            DidYouEnjoyThisProf_16.status = STARTED
            DidYouEnjoyThisProf_16.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_16 is active this frame...
        if DidYouEnjoyThisProf_16.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_16 is stopping this frame...
        if DidYouEnjoyThisProf_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_16.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_16.stopped')
                # update status
                DidYouEnjoyThisProf_16.status = FINISHED
                DidYouEnjoyThisProf_16.setAutoDraw(False)
        
        # *imageProf16_2* updates
        
        # if imageProf16_2 is starting this frame...
        if imageProf16_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf16_2.frameNStart = frameN  # exact frame index
            imageProf16_2.tStart = t  # local t and not account for scr refresh
            imageProf16_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf16_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf16_2.started')
            # update status
            imageProf16_2.status = STARTED
            imageProf16_2.setAutoDraw(True)
        
        # if imageProf16_2 is active this frame...
        if imageProf16_2.status == STARTED:
            # update params
            pass
        
        # if imageProf16_2 is stopping this frame...
        if imageProf16_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf16_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf16_2.tStop = t  # not accounting for scr refresh
                imageProf16_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf16_2.stopped')
                # update status
                imageProf16_2.status = FINISHED
                imageProf16_2.setAutoDraw(False)
        
        # *imageYesButton_34* updates
        
        # if imageYesButton_34 is starting this frame...
        if imageYesButton_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_34.frameNStart = frameN  # exact frame index
            imageYesButton_34.tStart = t  # local t and not account for scr refresh
            imageYesButton_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_34.started')
            # update status
            imageYesButton_34.status = STARTED
            imageYesButton_34.setAutoDraw(True)
        
        # if imageYesButton_34 is active this frame...
        if imageYesButton_34.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_34 is stopping this frame...
        if imageYesButton_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_34.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_34.tStop = t  # not accounting for scr refresh
                imageYesButton_34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_34.stopped')
                # update status
                imageYesButton_34.status = FINISHED
                imageYesButton_34.setAutoDraw(False)
        
        # *imageNoButton_33* updates
        
        # if imageNoButton_33 is starting this frame...
        if imageNoButton_33.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_33.frameNStart = frameN  # exact frame index
            imageNoButton_33.tStart = t  # local t and not account for scr refresh
            imageNoButton_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_33.started')
            # update status
            imageNoButton_33.status = STARTED
            imageNoButton_33.setAutoDraw(True)
        
        # if imageNoButton_33 is active this frame...
        if imageNoButton_33.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_33 is stopping this frame...
        if imageNoButton_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_33.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_33.tStop = t  # not accounting for scr refresh
                imageNoButton_33.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_33.stopped')
                # update status
                imageNoButton_33.status = FINISHED
                imageNoButton_33.setAutoDraw(False)
        # *mouse_33* updates
        
        # if mouse_33 is starting this frame...
        if mouse_33.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_33.frameNStart = frameN  # exact frame index
            mouse_33.tStart = t  # local t and not account for scr refresh
            mouse_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_33, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_33.started', t)
            # update status
            mouse_33.status = STARTED
            mouse_33.mouseClock.reset()
            prevButtonState = mouse_33.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_33 is stopping this frame...
        if mouse_33.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_33.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_33.tStop = t  # not accounting for scr refresh
                mouse_33.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_33.stopped', t)
                # update status
                mouse_33.status = FINISHED
        if mouse_33.status == STARTED:  # only update if started and not finished!
            buttons = mouse_33.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_33):
                            gotValidClick = True
                            mouse_33.clicked_name.append(obj.name)
                    x, y = mouse_33.getPos()
                    mouse_33.x.append(x)
                    mouse_33.y.append(y)
                    buttons = mouse_33.getPressed()
                    mouse_33.leftButton.append(buttons[0])
                    mouse_33.midButton.append(buttons[1])
                    mouse_33.rightButton.append(buttons[2])
                    mouse_33.time.append(mouse_33.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof16_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof16_enjoy_class" ---
    for thisComponent in Prof16_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof16_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_33.x', mouse_33.x)
    thisExp.addData('mouse_33.y', mouse_33.y)
    thisExp.addData('mouse_33.leftButton', mouse_33.leftButton)
    thisExp.addData('mouse_33.midButton', mouse_33.midButton)
    thisExp.addData('mouse_33.rightButton', mouse_33.rightButton)
    thisExp.addData('mouse_33.time', mouse_33.time)
    thisExp.addData('mouse_33.clicked_name', mouse_33.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof17" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof17.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_17
    mouse_17.x = []
    mouse_17.y = []
    mouse_17.leftButton = []
    mouse_17.midButton = []
    mouse_17.rightButton = []
    mouse_17.time = []
    mouse_17.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof17Components = [HaveYouTakenThisProf_17, imageProf17, imageYesButton_17, imageNoButton_17, mouse_17]
    for thisComponent in Prof17Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof17" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *HaveYouTakenThisProf_17* updates
        
        # if HaveYouTakenThisProf_17 is starting this frame...
        if HaveYouTakenThisProf_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            HaveYouTakenThisProf_17.frameNStart = frameN  # exact frame index
            HaveYouTakenThisProf_17.tStart = t  # local t and not account for scr refresh
            HaveYouTakenThisProf_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(HaveYouTakenThisProf_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_17.started')
            # update status
            HaveYouTakenThisProf_17.status = STARTED
            HaveYouTakenThisProf_17.setAutoDraw(True)
        
        # if HaveYouTakenThisProf_17 is active this frame...
        if HaveYouTakenThisProf_17.status == STARTED:
            # update params
            pass
        
        # if HaveYouTakenThisProf_17 is stopping this frame...
        if HaveYouTakenThisProf_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > HaveYouTakenThisProf_17.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                HaveYouTakenThisProf_17.tStop = t  # not accounting for scr refresh
                HaveYouTakenThisProf_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HaveYouTakenThisProf_17.stopped')
                # update status
                HaveYouTakenThisProf_17.status = FINISHED
                HaveYouTakenThisProf_17.setAutoDraw(False)
        
        # *imageProf17* updates
        
        # if imageProf17 is starting this frame...
        if imageProf17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf17.frameNStart = frameN  # exact frame index
            imageProf17.tStart = t  # local t and not account for scr refresh
            imageProf17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf17.started')
            # update status
            imageProf17.status = STARTED
            imageProf17.setAutoDraw(True)
        
        # if imageProf17 is active this frame...
        if imageProf17.status == STARTED:
            # update params
            pass
        
        # if imageProf17 is stopping this frame...
        if imageProf17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf17.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf17.tStop = t  # not accounting for scr refresh
                imageProf17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf17.stopped')
                # update status
                imageProf17.status = FINISHED
                imageProf17.setAutoDraw(False)
        
        # *imageYesButton_17* updates
        
        # if imageYesButton_17 is starting this frame...
        if imageYesButton_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_17.frameNStart = frameN  # exact frame index
            imageYesButton_17.tStart = t  # local t and not account for scr refresh
            imageYesButton_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_17.started')
            # update status
            imageYesButton_17.status = STARTED
            imageYesButton_17.setAutoDraw(True)
        
        # if imageYesButton_17 is active this frame...
        if imageYesButton_17.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_17 is stopping this frame...
        if imageYesButton_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_17.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_17.tStop = t  # not accounting for scr refresh
                imageYesButton_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_17.stopped')
                # update status
                imageYesButton_17.status = FINISHED
                imageYesButton_17.setAutoDraw(False)
        
        # *imageNoButton_17* updates
        
        # if imageNoButton_17 is starting this frame...
        if imageNoButton_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_17.frameNStart = frameN  # exact frame index
            imageNoButton_17.tStart = t  # local t and not account for scr refresh
            imageNoButton_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_17.started')
            # update status
            imageNoButton_17.status = STARTED
            imageNoButton_17.setAutoDraw(True)
        
        # if imageNoButton_17 is active this frame...
        if imageNoButton_17.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_17 is stopping this frame...
        if imageNoButton_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_17.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_17.tStop = t  # not accounting for scr refresh
                imageNoButton_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_17.stopped')
                # update status
                imageNoButton_17.status = FINISHED
                imageNoButton_17.setAutoDraw(False)
        # *mouse_17* updates
        
        # if mouse_17 is starting this frame...
        if mouse_17.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_17.frameNStart = frameN  # exact frame index
            mouse_17.tStart = t  # local t and not account for scr refresh
            mouse_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_17.started', t)
            # update status
            mouse_17.status = STARTED
            mouse_17.mouseClock.reset()
            prevButtonState = mouse_17.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_17 is stopping this frame...
        if mouse_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_17.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_17.tStop = t  # not accounting for scr refresh
                mouse_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_17.stopped', t)
                # update status
                mouse_17.status = FINISHED
        if mouse_17.status == STARTED:  # only update if started and not finished!
            buttons = mouse_17.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_17):
                            gotValidClick = True
                            mouse_17.clicked_name.append(obj.name)
                    x, y = mouse_17.getPos()
                    mouse_17.x.append(x)
                    mouse_17.y.append(y)
                    buttons = mouse_17.getPressed()
                    mouse_17.leftButton.append(buttons[0])
                    mouse_17.midButton.append(buttons[1])
                    mouse_17.rightButton.append(buttons[2])
                    mouse_17.time.append(mouse_17.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof17Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof17" ---
    for thisComponent in Prof17Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof17.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_17.x', mouse_17.x)
    thisExp.addData('mouse_17.y', mouse_17.y)
    thisExp.addData('mouse_17.leftButton', mouse_17.leftButton)
    thisExp.addData('mouse_17.midButton', mouse_17.midButton)
    thisExp.addData('mouse_17.rightButton', mouse_17.rightButton)
    thisExp.addData('mouse_17.time', mouse_17.time)
    thisExp.addData('mouse_17.clicked_name', mouse_17.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "BlankScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('BlankScreen.started', globalClock.getTime())
    # keep track of which components have finished
    BlankScreenComponents = [Next_prof]
    for thisComponent in BlankScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "BlankScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Next_prof* updates
        
        # if Next_prof is starting this frame...
        if Next_prof.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Next_prof.frameNStart = frameN  # exact frame index
            Next_prof.tStart = t  # local t and not account for scr refresh
            Next_prof.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Next_prof, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Next_prof.started')
            # update status
            Next_prof.status = STARTED
            Next_prof.setAutoDraw(True)
        
        # if Next_prof is active this frame...
        if Next_prof.status == STARTED:
            # update params
            pass
        
        # if Next_prof is stopping this frame...
        if Next_prof.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Next_prof.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Next_prof.tStop = t  # not accounting for scr refresh
                Next_prof.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Next_prof.stopped')
                # update status
                Next_prof.status = FINISHED
                Next_prof.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BlankScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BlankScreen" ---
    for thisComponent in BlankScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('BlankScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "Prof17_enjoy_class" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Prof17_enjoy_class.started', globalClock.getTime())
    # setup some python lists for storing info about the mouse_34
    mouse_34.x = []
    mouse_34.y = []
    mouse_34.leftButton = []
    mouse_34.midButton = []
    mouse_34.rightButton = []
    mouse_34.time = []
    mouse_34.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    Prof17_enjoy_classComponents = [DidYouEnjoyThisProf_17, imageProf17_2, imageYesButton_35, imageNoButton_34, mouse_34]
    for thisComponent in Prof17_enjoy_classComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Prof17_enjoy_class" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 5.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *DidYouEnjoyThisProf_17* updates
        
        # if DidYouEnjoyThisProf_17 is starting this frame...
        if DidYouEnjoyThisProf_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            DidYouEnjoyThisProf_17.frameNStart = frameN  # exact frame index
            DidYouEnjoyThisProf_17.tStart = t  # local t and not account for scr refresh
            DidYouEnjoyThisProf_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(DidYouEnjoyThisProf_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_17.started')
            # update status
            DidYouEnjoyThisProf_17.status = STARTED
            DidYouEnjoyThisProf_17.setAutoDraw(True)
        
        # if DidYouEnjoyThisProf_17 is active this frame...
        if DidYouEnjoyThisProf_17.status == STARTED:
            # update params
            pass
        
        # if DidYouEnjoyThisProf_17 is stopping this frame...
        if DidYouEnjoyThisProf_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > DidYouEnjoyThisProf_17.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                DidYouEnjoyThisProf_17.tStop = t  # not accounting for scr refresh
                DidYouEnjoyThisProf_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'DidYouEnjoyThisProf_17.stopped')
                # update status
                DidYouEnjoyThisProf_17.status = FINISHED
                DidYouEnjoyThisProf_17.setAutoDraw(False)
        
        # *imageProf17_2* updates
        
        # if imageProf17_2 is starting this frame...
        if imageProf17_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageProf17_2.frameNStart = frameN  # exact frame index
            imageProf17_2.tStart = t  # local t and not account for scr refresh
            imageProf17_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageProf17_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageProf17_2.started')
            # update status
            imageProf17_2.status = STARTED
            imageProf17_2.setAutoDraw(True)
        
        # if imageProf17_2 is active this frame...
        if imageProf17_2.status == STARTED:
            # update params
            pass
        
        # if imageProf17_2 is stopping this frame...
        if imageProf17_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageProf17_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageProf17_2.tStop = t  # not accounting for scr refresh
                imageProf17_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageProf17_2.stopped')
                # update status
                imageProf17_2.status = FINISHED
                imageProf17_2.setAutoDraw(False)
        
        # *imageYesButton_35* updates
        
        # if imageYesButton_35 is starting this frame...
        if imageYesButton_35.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageYesButton_35.frameNStart = frameN  # exact frame index
            imageYesButton_35.tStart = t  # local t and not account for scr refresh
            imageYesButton_35.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageYesButton_35, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageYesButton_35.started')
            # update status
            imageYesButton_35.status = STARTED
            imageYesButton_35.setAutoDraw(True)
        
        # if imageYesButton_35 is active this frame...
        if imageYesButton_35.status == STARTED:
            # update params
            pass
        
        # if imageYesButton_35 is stopping this frame...
        if imageYesButton_35.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageYesButton_35.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageYesButton_35.tStop = t  # not accounting for scr refresh
                imageYesButton_35.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageYesButton_35.stopped')
                # update status
                imageYesButton_35.status = FINISHED
                imageYesButton_35.setAutoDraw(False)
        
        # *imageNoButton_34* updates
        
        # if imageNoButton_34 is starting this frame...
        if imageNoButton_34.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imageNoButton_34.frameNStart = frameN  # exact frame index
            imageNoButton_34.tStart = t  # local t and not account for scr refresh
            imageNoButton_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imageNoButton_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'imageNoButton_34.started')
            # update status
            imageNoButton_34.status = STARTED
            imageNoButton_34.setAutoDraw(True)
        
        # if imageNoButton_34 is active this frame...
        if imageNoButton_34.status == STARTED:
            # update params
            pass
        
        # if imageNoButton_34 is stopping this frame...
        if imageNoButton_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imageNoButton_34.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                imageNoButton_34.tStop = t  # not accounting for scr refresh
                imageNoButton_34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'imageNoButton_34.stopped')
                # update status
                imageNoButton_34.status = FINISHED
                imageNoButton_34.setAutoDraw(False)
        # *mouse_34* updates
        
        # if mouse_34 is starting this frame...
        if mouse_34.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            mouse_34.frameNStart = frameN  # exact frame index
            mouse_34.tStart = t  # local t and not account for scr refresh
            mouse_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('mouse_34.started', t)
            # update status
            mouse_34.status = STARTED
            mouse_34.mouseClock.reset()
            prevButtonState = mouse_34.getPressed()  # if button is down already this ISN'T a new click
        
        # if mouse_34 is stopping this frame...
        if mouse_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > mouse_34.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                mouse_34.tStop = t  # not accounting for scr refresh
                mouse_34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('mouse_34.stopped', t)
                # update status
                mouse_34.status = FINISHED
        if mouse_34.status == STARTED:  # only update if started and not finished!
            buttons = mouse_34.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    clickableList = environmenttools.getFromNames(['imageYesButton', 'imageNoButton'], namespace=locals())
                    for obj in clickableList:
                        # is this object clicked on?
                        if obj.contains(mouse_34):
                            gotValidClick = True
                            mouse_34.clicked_name.append(obj.name)
                    x, y = mouse_34.getPos()
                    mouse_34.x.append(x)
                    mouse_34.y.append(y)
                    buttons = mouse_34.getPressed()
                    mouse_34.leftButton.append(buttons[0])
                    mouse_34.midButton.append(buttons[1])
                    mouse_34.rightButton.append(buttons[2])
                    mouse_34.time.append(mouse_34.mouseClock.getTime())
                    if gotValidClick:
                        continueRoutine = False  # end routine on response
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prof17_enjoy_classComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Prof17_enjoy_class" ---
    for thisComponent in Prof17_enjoy_classComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Prof17_enjoy_class.stopped', globalClock.getTime())
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_34.x', mouse_34.x)
    thisExp.addData('mouse_34.y', mouse_34.y)
    thisExp.addData('mouse_34.leftButton', mouse_34.leftButton)
    thisExp.addData('mouse_34.midButton', mouse_34.midButton)
    thisExp.addData('mouse_34.rightButton', mouse_34.rightButton)
    thisExp.addData('mouse_34.time', mouse_34.time)
    thisExp.addData('mouse_34.clicked_name', mouse_34.clicked_name)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-5.000000)
    
    # --- Prepare to start Routine "ThankYouScreen" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('ThankYouScreen.started', globalClock.getTime())
    # keep track of which components have finished
    ThankYouScreenComponents = [textThankYouMessage]
    for thisComponent in ThankYouScreenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ThankYouScreen" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 3.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *textThankYouMessage* updates
        
        # if textThankYouMessage is starting this frame...
        if textThankYouMessage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            textThankYouMessage.frameNStart = frameN  # exact frame index
            textThankYouMessage.tStart = t  # local t and not account for scr refresh
            textThankYouMessage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textThankYouMessage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'textThankYouMessage.started')
            # update status
            textThankYouMessage.status = STARTED
            textThankYouMessage.setAutoDraw(True)
        
        # if textThankYouMessage is active this frame...
        if textThankYouMessage.status == STARTED:
            # update params
            pass
        
        # if textThankYouMessage is stopping this frame...
        if textThankYouMessage.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textThankYouMessage.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                textThankYouMessage.tStop = t  # not accounting for scr refresh
                textThankYouMessage.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textThankYouMessage.stopped')
                # update status
                textThankYouMessage.status = FINISHED
                textThankYouMessage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ThankYouScreenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ThankYouScreen" ---
    for thisComponent in ThankYouScreenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('ThankYouScreen.stopped', globalClock.getTime())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.000000)
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
