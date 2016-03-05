import sys, pygame
from pygame.locals import *

def hashableEvent(event):
        # turn a pygame event into a string that can be a key for a dict
        # of callables
        if event.type == MOUSEBUTTONDOWN:
                return 'mousebuttondown'
        elif event.type == MOUSEBUTTONUP:
                return 'mousebuttonup'
        elif event.type == KEYDOWN:
                return 'keydown'
        elif event.type == QUIT:
                return 'quit'
        elif event.type == MOUSEMOTION:
                return 'mousemotion'
        elif event.type == VIDEORESIZE:
                return 'videoresize'
        elif event.type == VIDEOEXPOSE:
                return 'videoexpose'
        elif event.type == ACTIVEEVENT:
                return 'activeevent'
        elif event.type == USEREVENT:
                return 'userevent'
 
def handleInput(events, commands):
        # pass pygame.event.get() as events
        # and a dictionary of callables as commands
        for event in events:
               eventtype = hashableEvent(event)
               if eventtype in commands:
                        # only execute if there is a command to handle
                        commands[eventtype](event)

def quit(event):
        # this is going to be used in virtually every screen.
        # deinitialize pygame and python when the window is closed.
        pygame.quit()
        sys.exit()
