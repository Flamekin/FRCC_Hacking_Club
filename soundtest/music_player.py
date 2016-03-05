import os, sys, pygame
from pygame.locals import *

from handle_input import handleInput, quit

TRACKFILE = os.path.join('soundtest','tracks.txt')
FIRSTTRACK = 0

class Track(object):
        def __init__(self, title, name, path, 
                        firstloop, looplen, looppoint):
                self.title = title
                self.name = name
                self.path = path
                self.firstloop = firstloop
                self.looplen = looplen
                self.looppoint = looppoint

class MusicPlayer(object):
        '''MusicPlayer:
        A wrapper for the singleton mixer object that also includes
        data about the tracks.

        Has two different mutable sequences that contain the Track objects:
        self.tracks is a dict, indexed by each track's unique name (a string
        without spaces). This index is used to call a specific track
        regardless of its place in the playlist, e.g. call a specific track
        before the track list is finalized.
        self.tracks_ordered is a list of references to the same Track objects
        that are in the dict in the order they were read from the file (and
        the same order they should be displayed in sound tests).

        self.curtrack is a string, the index for self.tracks of the track
        the mixer is currently handling.

        nextloop is a number in milleseconds. It is the argument for 
        pygame.mixer.get_pos(), the point in the audio file when the mixer
        is supposed to loop back to the track's starting point.

        self.mixer is a reference to the pygame.mixer.music module. Because
        it is passed by reference during initiation, importing that module
        is unnecessary.
        '''
        tracks = {} # dict of track objects, indexed by track.name
        tracks_ordered = [] # list of track objects in play order
        curtrack = None # currently loaded track
        nextloop = 0

        def __init__(self, mixer):
                self.mixer = mixer # the pygame mixer.music module

        def load(self, track):
                """MusicPlayer.load():

                Tell the Pygame mixer object to load the specified
                track by its name (a string argument).
                """
                self.curtrack = track
                self.mixer.load(self.tracks[self.curtrack].path)
                self.nextloop = self.tracks[self.curtrack].firstloop
                self.looplen = self.tracks[self.curtrack].looplen
                self.looppoint = self.tracks[self.curtrack].looppoint

        def loadTracks(self, track_data):
                """MusicPlayer.loadTracks():
                
                Open a text file with data about the tracks, create
                the track objects, and fill the dict and list with their
                data. track_data is a string, a path to the object.

                The text file thus referred to should be in the following
                format:

                Track Title trackname path firstloop looplen looppoint

                Track Title: A human-readable title for the track. Can be
                as many words as needed. Special characters should be escaped.

                trackname: a string without spaces or punctuation. Used as the
                index for this track in self.tracks.

                path: a string that is a filesystem path for the location of
                the track.

                firstloop: a number in milleseconds that marks the point of
                the track in which the mixer should loop back to the starting
                point.

                looplen: a number in milleseconds that denotes how long each
                loop (after the first) the track should loop.

                looppoint: a number in seconds (not milliseconds) that marks
                the point in the track that the mixer should return to after
                each loop. For some tracks, it may be 0. For others, with
                intros, it may be different. Should be equivalent to
                firstloop - looplen.
                """

                with open(track_data, mode='r') as data:
                        for trackline in data:
                                trackdata = trackline.rstrip("\n\r").split()
                                looppoint = float(trackdata.pop(-1))
                                looplen = int(trackdata.pop(-1))
                                firstloop = int(trackdata.pop(-1))
                                path = trackdata.pop(-1)
                                name = trackdata.pop(-1)
                                title = ' '.join(trackdata)

                                nexttrack = Track(title, name, path,
                                        firstloop, looplen, looppoint)
                                self.tracks_ordered.append(nexttrack)
                                self.tracks[nexttrack.name] = nexttrack

        def play(self):
                """
                MusicPlayer.play():

                """
                self.nextloop = self.tracks[self.curtrack].firstloop
                self.looplen = self.tracks[self.curtrack].looplen
                self.mixer.play()

        def update(self):
                # While the music player is active, this should be called
                # once in each iteration of the main loop, wherever
                # that is.
                if self.mixer.get_pos() >= self.nextloop:
                        self.mixer.play(-1,self.looppoint)
                        self.nextloop += self.looplen

        def change_track(self, tracknum):
                try:
                        next_track = self.tracks_ordered[tracknum].name
                        pygame.mixer.music.stop()
                        self.load(next_track)
                        self.play()
                except IndexError:
                        # log this later when logging is implemented.
                        # for now we want the program to do nothing
                        # rather than freak out from bad user input.
                        print("Attempted to load a track that does not exist.")
                        return

def init(trackfile, firsttrack):
        pygame.mixer.init()
        player = MusicPlayer(pygame.mixer.music)
        player.loadTracks(trackfile)
        player.load(player.tracks_ordered[firsttrack].name)
        player.play()

        return player

def changeTrackKbd(event):
        try:
                player.change_track(int(chr(event.key))-1)
        except ValueError:
                # log this later when logging is implemented.
                # for now we want the program to do nothing
                # rather than freak out from bad user input.
                print("Change tracks by typing numbers.")

def pauseMouse(event):
        pygame.mixer.music.pause()

def unpauseMouse(event):
        pygame.mixer.music.unpause()

kbd_player_cmds = {
                'mousebuttondown':pauseMouse,
                'mousebuttonup':unpauseMouse,
                'keydown':changeTrackKbd,
                'quit':quit
}

def main():
        global player
        player = init(TRACKFILE, FIRSTTRACK)

        pygame.init()
        disp = pygame.display.set_mode((800, 600))

        while True:
                handleInput(pygame.event.get(), kbd_player_cmds)
                player.update()

if __name__ == '__main__':
        main()
