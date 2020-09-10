#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
#import tensorflow as tf
#from tensorflow import keras
#from tensorflow.keras import layers
import math

lastdashright = True
# In[ ]:


def model():
    model = keras.Sequential([
        layers.Dense(2, activation="relu", name="input"),
        layers.Dense(3, activation="relu"),
        layers.Dense(48, name="output"),
    ])


# In[20]:


# every possible move the AI can make
def right():
    controller.tilt_analog(melee.Button.BUTTON_MAIN,1,.5)
    console.step()
    controller.release_all()
def left():
    controller.tilt_analog(melee.Button.BUTTON_MAIN,0,.5)
    console.step()
    controller.release_all()
def jump():
    controller.press_button(melee.Button.BUTTON_X)
    console.step()
    console.step()
    console.step()
    controller.release_all()
def jab():
    controller.press_button(melee.Button.BUTTON_A)
def shorthop():
    if gamestate.player[2].jumps_left == 2 and gamestate.player[2].action != melee.Action.KNEE_BEND:
                controller.press_button(melee.Button.BUTTON_X)
                console.step()
                controller.release_all()
                console.step()
                console.step()
def crouch():
    controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.5)
    console.step()
    controller.release_all()
def fastfall():
        controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,0)
        console.step()
        controller.release_all()
def pivot():
    global gamestate
    global lastdashright
    
    if lastdashright:
        controller.tilt_analog(melee.Button.BUTTON_MAIN,0,.5)
        console.step()
        controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.5)
        gamestate=console.step()
        print("turn left")
        if gamestate.player[2].facing:
            print("failed pivot")
    else:
        controller.tilt_analog(melee.Button.BUTTON_MAIN,1,.5)
        gamestate=console.step()
        controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.5)
        gamestate=console.step()
        print("turn right")
        if gamestate.player[2].facing ==False:
            print("failed pivot")
    print(controller.current.main_stick[0])
def dash(Right,Percent):
    global gamestate
    global lastdashright
    lastdashright = Right
    if Right:
        controller.tilt_analog(melee.Button.BUTTON_MAIN,1,.5)
    else:
        controller.tilt_analog(melee.Button.BUTTON_MAIN,0,.5)
    for x in range(math.floor(Percent*dashframes[str(gamestate.player[2].character)])):
        gamestate = console.step()
    #controller.release_all()
def tilt(up,foward):
    if up:
        controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.75)
        controller.press_button(melee.Button.BUTTON_A)
        for x in range(melee.framedata.frame_count(Melee.enums.Action.UPTILT)):
            console.step()
    if foward:
        if gamestate.player[2].facing:
            controller.tilt_analog(melee.Button.BUTTON_MAIN,.75,.5)
        else:
            controller.tilt_analog(melee.Button.BUTTON_MAIN,.25,.5)
        controller.press_button(melee.Button.BUTTON_A)
        for x in range(10):#(melee.framedata.frame_count(melee.enums.Action.FTILT_MID)):
            console.step()
    else:
        controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.25)
        controller.press_button(melee.Button.BUTTON_A)
        for x in range(10):#Melee.framedata.frame_count(Melee.enums.Action.DOWNTILT)):
            console.step()
    controller.release_all()


# In[2]:


dashframes =  {"Mewtwo":18,"Character.CPTFALCON":15,"Marth":15,"Roy":15,"Donkey Kong":15, "Ganondorf":15,"Peach":15,"Zelda":15,"Pikachu":13,"Pichu":13,"Young Link":13,"Yoshi":13,"Bowser":13,"Ice Climbers":13,"Ness":13,"Jigglypuff": 13,"Kirby":12,"Link":12,"Fox":11,"Falco":11,"Mario":10,"Dr.Mario":10,"Luigi":10,"Mr.Game & Watch":8,"Samus":8,"Sheik":7}


# In[3]:


dashframes["Fox"]


# In[18]:


#model
def nextAction(gamestate):
    inputarr = [gamestate.player[1].x,gamestate.player[1].y,gamestate.player[2].x,gamestate.player[2].y]
    prediction = model.predict(inputarr)
    if prediction == 0:
        return right()# right,
    elif prediction == 1: 
        return left()# left,
    elif prediction ==2: 
        return # jump,
    elif prediction == 3: 
        return # short hop .5,
    elif prediction == 4: 
        return # short hop forward 1,
    elif prediction == 5: 
        return # short hop forward .75,
    elif prediction == 6: 
        return # short hop backward .25,
    elif prediction == 7: 
        return # short hop backward 0,
    elif prediction == 8: 
        return # standing grab,
    elif prediction == 9: 
        return # jump cancel grab,
    elif prediction == 10: 
        return # spot dodge,
    elif prediction == 11: 
        return # shield,
    elif prediction == 12: 
        return # wave dash left 0,
    elif prediction == 13: 
        return # wave dash left .25,
    elif prediction == 14: 
        return # wave dash right 1,
    elif prediction == 15: 
        return # wave dash right .75,
    elif prediction == 16: 
        return # wave dash in-place,
    elif prediction == 17: 
        return # up air,
    elif prediction == 18: 
        return # down air,
    elif prediction == 19: 
        return # forward air, 
    elif prediction == 20: 
        return # back air,
    elif prediction == 21: 
        return # neutral air,
    elif prediction == 22: 
        return #neutral b,
    elif prediction == 23: 
        return #side b,
    elif prediction == 24: 
        return #down b,
    elif prediction == 25: 
        return #up b,
    elif prediction == 26: 
        return # amsa teq left,
    elif prediction == 27: 
        return # amsa teq right,
    elif prediction == 28: 
        return # amsa teq neutral,
    elif prediction == 29: 
        return # slide off di,
    elif prediction == 30: 
        return # di down away,
    elif prediction == 31: 
        return # survival di,
    elif prediction == 32: 
        return # combo di,
    elif prediction == 33: 
        fastfall()
        return #fast fall,
    elif prediction == 34:
        jab()
        return #jab,
    elif prediction == 35: 
        tilt(False,True)
        return #forward tilt,
    elif prediction == 36:
        tilt(False,False)
        return #down tilt,
    elif prediction == 37: 
        tilt(True,False)
        return #up tilt,
    elif prediction == 38:
        dash(True,1)
        return # dash right 1,
    elif prediction == 39:
        dash(True,.75)
        return # dash right .75,
    elif prediction == 40:
        dash(True,.25)
        return # dash right .25,
    elif prediction == 41:
        dash(True,.15)
        return # dash right .15,
    elif prediction == 42:
        dash(False,1)
        return # dash left 1,
    elif prediction == 43:
        dash(False,.75)
        return # dash left .75,
    elif prediction == 44:
        dash(False,.25)
        return # dash left .25,
    elif prediction == 45:
        dash(False,.15)
        return # dash left .15,
    elif prediction == 46:
        pivot()
        return # pivot,
    elif prediction == 47: 
        crouch()
        return # crouch,
    elif prediction == 48: 
        return # c stick down
    elif prediction == 49:
        return #head empty; no thoughts


# In[2]:


#model interface

import argparse
import signal
import sys
import melee
# This example program demonstrates how to use the Melee API to run a console,
#   setup controllers, and send button presses over to a console (dolphin or Slippi/Wii)

def check_port(value):
    ivalue = int(value)
    if ivalue < 1 or ivalue > 4:
        raise argparse.ArgumentTypeError("%s is an invalid controller port.                                          Must be 1, 2, 3, or 4." % value)
    return ivalue

parser = argparse.ArgumentParser(description='Example of libmelee in action')
parser.add_argument('--port', '-p', type=check_port,
                    help='The controller port (1-4) your AI will play on',
                    default=2)
parser.add_argument('--opponent', '-o', type=check_port,
                    help='The controller port (1-4) the opponent will play on',
                    default=1)
parser.add_argument('--debug', '-d', action='store_true',
                    help='Debug mode. Creates a CSV of all game states')
parser.add_argument('--framerecord', '-r', default=False, action='store_true',
                    help='(DEVELOPMENT ONLY) Records frame data from the match,' \
                    'stores into framedata.csv.')
parser.add_argument('--address', '-a', default="127.0.0.1",
                    help='IP address of Slippi/Wii')
parser.add_argument('--dolphin_executable_path', '-e', default="C:/Users/colem/Downloads/Ishiiruka-gamma/Ishiiruka-gamma/Binary/x64",
                    help='Manually specify the non-installed directory where dolphin is')
parser.add_argument('--connect_code', '-t', default="",
                    help='Direct connect code to connect to in Slippi Online')

args = parser.parse_args()

# This logger object is useful for retroactively debugging issues in your bot
#   You can write things to it each frame, and it will create a CSV file describing the match
log = None
if args.debug:
    log = melee.Logger()

# This frame data object contains lots of helper functions and values for looking up
#   various Melee stats, hitboxes, and physics calculations
framedata = melee.FrameData(args.framerecord)

# Create our Console object.
#   This will be one of the primary objects that we will interface with.
#   The Console represents the virtual or hardware system Melee is playing on.
#   Through this object, we can get "GameState" objects per-frame so that your
#       bot can actually "see" what's happening in the game
console = melee.Console(path=args.dolphin_executable_path,
                        slippi_address=args.address,
                        slippi_port=51441,
                        blocking_input=False,
                        logger=log)

# Dolphin has an optional mode to not render the game's visuals
#   This is useful for BotvBot matches
console.render = True

# Create our Controller object
#   The controller is the second primary object your bot will interact with
#   Your controller is your way of sending button presses to the game, whether
#   virtual or physical.
controller = melee.Controller(console=console,
                              port=args.port,
                              type=melee.ControllerType.STANDARD)

controller_opponent = melee.Controller(console=console,
                                       port=args.opponent,
                                       type=melee.ControllerType.GCN_ADAPTER)

# This isn't necessary, but makes it so that Dolphin will get killed when you ^C
def signal_handler(sig, frame):
    console.stop()
    if args.debug:
        log.writelog()
        print("") #because the ^C will be on the terminal
        print("Log file created: " + log.filename)
    print("Shutting down cleanly...")
    if args.framerecord:
        framedata.save_recording()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Run the console
console.run()

# Connect to the console
print("Connecting to console...")
if not console.connect():
    print("ERROR: Failed to connect to the console.")
    print("\tIf you're trying to autodiscover, local firewall settings can " +
          "get in the way. Try specifying the address manually.")
    sys.exit(-1)

# Plug our controller in
#   Due to how named pipes work, this has to come AFTER running dolphin
#   NOTE: If you're loading a movie file, don't connect the controller,
#   dolphin will hang waiting for input and never receive it
print("Connecting controller to console...")
if not controller.connect():
    print("ERROR: Failed to connect the controller.")
    sys.exit(-1)
print("Controller connected")
loop=1
x=6
# Main loop
while True:
    # "step" to the next frame
    gamestate = console.step()
    #print(gamestate.player[2].character)

    # The console object keeps track of how long your bot is taking to process frames
    #   And can warn you if it's taking too long
    if console.processingtime * 1000 > 12:
        print("WARNING: Last frame took " + str(console.processingtime*1000) + "ms to process.")

    # What menu are we in?
    if gamestate.menu_state in [melee.Menu.IN_GAME, melee.Menu.SUDDEN_DEATH]:

        # Slippi Online matches assign you a random port once you're in game that's different
        #   than the one you're physically plugged into. This helper will autodiscover what
        #   port we actually are.
        discovered_port = melee.gamestate.port_detector(gamestate, controller, melee.Character.FOX)

        if discovered_port > 0:
            if args.framerecord:
                framedata._record_frame(gamestate)
                
            # NOTE: This is where your AI does all of its stuff!
            # This line will get hit once per frame, so here is where you read
            #   in the gamestate and decide what buttons to push on the controller
            #for x in range(15):
            #    dash(True,x/15)
            #    dash(False,x/15)
            #Pivot Deminstration
            #loop+=1

            if loop == 100:
                x=15
                print(x)
                dash(False,x/15)
                #controller.tilt_analog(melee.Button.BUTTON_MAIN,0,.5)
                #for b in range(x-1):
                #    gamestate= console.step()
                #controller.tilt_analog(melee.Button.BUTTON_MAIN,1,.5)
                #gamestate= console.step()
                #controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.5)
                #dash(False,x/15)
                #print("after Dash stick")
                #print(controller.current.main_stick)
                pivot()
                tilt(False,True)
                #print("after pivot stick")
                #print(controller.current.main_stick)
            elif loop == 200:
                print(x)
                dash(True,x/15)
                #controller.tilt_analog(melee.Button.BUTTON_MAIN,1,.5)
                #for b in range(x-1):
                #    gamestate= console.step()
                #controller.tilt_analog(melee.Button.BUTTON_MAIN,0,.5)
                #gamestate= console.step()
                #controller.tilt_analog(melee.Button.BUTTON_MAIN,.5,.5)
                #print("after Dash stick")
                #print(controller.current.main_stick)
                pivot()
                #tilt(up,foward)
                tilt(False,True)
                #MoonWalk()
                if x >= 15:
                    x=6
                else:
                    x+=1
                #print("after pivot stick")
                #print(controller.current.main_stick)
                loop=0
            loop+=1
            
    else:
        melee.MenuHelper.menu_helper_simple(gamestate,
                                            controller,
                                            args.port,
                                            melee.Character.GAMEANDWATCH,
                                            melee.Stage.FINAL_DESTINATION,
                                            args.connect_code,
                                            autostart=False,
                                            swag=False)
    if log:
        log.logframe(gamestate)
        log.writeframe()


# In[ ]:




