import sys, os
import pygame
from pygame.locals import *
import music_player
from handle_input import *

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

TITLE_WIDTH = 400
BUTTON_HEIGHT = 46
PADDING = 10

WHITE =     pygame.Color(255, 255, 255)
LITEWHITE = pygame.Color(255, 255, 255, 127)
GREEN =     pygame.Color( 10, 200,  90)

tracknames = [
                "Title",
                "Begin",
                "Level 1",
                "Victory",
                "Game Over",
                "Timed Level",
                "Level 2",
                "High Score",
                "Options",
                "Bonus Level",
                ]

def drawPlaylist(display, tracks, font):
        list_x = TITLE_WIDTH + BUTTON_HEIGHT + PADDING
        list_y = (
                        BUTTON_HEIGHT * len(tracknames) +
                        PADDING * (len(tracknames)+1)
                        )
        screen_space_x = SCREEN_WIDTH - list_x
        screen_space_y = SCREEN_HEIGHT - list_y
        trackrects = []
        buttonrects = []
        for i in range(0, len(tracks)):
                text_start_x = int(screen_space_x/2)
                text_start_y = int(screen_space_y/2) + \
                               i * BUTTON_HEIGHT + \
                               (i+1) * PADDING
                text_center = (
                    text_start_x + int(TITLE_WIDTH/2),
                    text_start_y + int(BUTTON_HEIGHT/2)
                    )
                button_start_x = \
                       int(screen_space_x/2) + \
                       TITLE_WIDTH + PADDING
                button_start_y = \
                       int(screen_space_y/2) + \
                       i * BUTTON_HEIGHT + \
                       (i+1) * PADDING
                trackrect = pygame.Rect(
                               text_start_x,
                               text_start_y,
                               TITLE_WIDTH,
                               BUTTON_HEIGHT
                       )
                pygame.draw.rect(
                    display,
                    GREEN,
                    trackrect,
                    1
                    )
                buttonrect = pygame.Rect(
                       button_start_x,
                       button_start_y,
                       BUTTON_HEIGHT,
                       BUTTON_HEIGHT,
                        )
                pygame.draw.rect(
                    display,
                    GREEN,
                    buttonrect,
                    1
                    )
                drawPlayButton(
                     button_start_x,
                     button_start_y,
                     GREEN,
                     display
                     )
                trackname = font.render(tracks[i], 0, WHITE)
                tracknamerect = trackname.get_rect()
                tracknamerect.center = text_center
                trackrects.append(trackrect)
                buttonrects.append(buttonrect)
                display.blit(trackname, tracknamerect)
        return trackrects, buttonrects


                
def drawPlayButton(x, y, color, display):
        pygame.draw.polygon(
                display,
                color,
                [
                    (x + PADDING, y + PADDING),
                    (
                            x + BUTTON_HEIGHT - PADDING,
                            y + int(BUTTON_HEIGHT)/2
                            ),
                    (x + PADDING, y + BUTTON_HEIGHT - PADDING),
                ],
                0
                )

pygame.init()
player = music_player.init(os.path.join('soundtest','tracks.txt'),0)
tracknames = []
for track in player.tracks_ordered:
        tracknames.append(track.title)
disp = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont('Helvetica', 18)
tracks, buttons = drawPlaylist(disp, tracknames, font)

def mouseInTrackButtons(coords, buttonrects):
        for i in range(0,len(buttonrects)):
                if buttonrects[i].collidepoint(coords):
                        return i
        return None

def buttonClicked(event):
        i = mouseInTrackButtons(event.pos, buttons)
        if i is not None:
                player.change_track(i)

player_commands = {
        'quit':quit,
        'mousebuttondown':buttonClicked
        }


while True:
        handleInput(pygame.event.get(), player_commands)
        pygame.display.update()

