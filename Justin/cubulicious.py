import pygame
import pygbutton

pygame.init()

# Create variables for the width and height of the game window.
displayWidth = 800
displayHeight = 600

# Sets the game's window size, name, and update speed.
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight),pygame.RESIZABLE)
pygame.display.set_caption('Cubulicious')
clock = pygame.time.Clock()

# Sets the background image for the game.
backgroundImg = pygame.image.load('Images/background.png')
backgroundImg = pygame.transform.scale(backgroundImg, (displayWidth,displayHeight))

# Sets the creature for the game.
creatureImg = pygame.image.load('Images/cube.png')
creatureImg = pygame.transform.scale(creatureImg, ((displayWidth / 2), (displayHeight / 2)))

# Sets the main song to a continuous loop.
pygame.mixer.music.load('Audio/main.ogg')
pygame.mixer.music.play(-1)

# Sets the three buttons Play, Feed, and Clean.
playButton = pygbutton.PygButton((displayWidth / 13, displayHeight / 1.125, 120, 60),'Play')
feedButton = pygbutton.PygButton((displayWidth / 2.35, displayHeight / 1.125, 120, 60),'Feed')
cleanButton = pygbutton.PygButton((displayWidth / 1.3, displayHeight / 1.125, 120, 60),'Clean')

# Function for redrawing the game window's contents to scale.
def resize(e):
    # Need to reference the global variables instead of creating new ones.
    global gameDisplay, displayWidth, displayHeight, backgroundImg, creatureImg, playButton, feedButton, cleanButton

    # Update game window's size.
    gameDisplay = pygame.display.set_mode(event.dict['size'],pygame.RESIZABLE)
    displayWidth = event.dict['size'][0]
    displayHeight = event.dict['size'][1]

    # Update background and creature size. (Picture needs to be set again because of resizing issues.)
    backgroundImg = pygame.image.load('Images/background.png')
    backgroundImg = pygame.transform.scale(backgroundImg, (displayWidth,displayHeight))
    creatureImg = pygame.image.load('Images/cube.png')
    creatureImg = pygame.transform.scale(creatureImg, ((displayWidth / 2), (displayHeight / 2)))

    # Update the sizes and positions of the buttons.
    playButton = pygbutton.PygButton((displayWidth / 13, displayHeight / 1.125, displayWidth / 6, displayHeight / 10),'Play')
    feedButton = pygbutton.PygButton((displayWidth / 2.35, displayHeight / 1.125, displayWidth / 6, displayHeight / 10),'Feed')
    cleanButton = pygbutton.PygButton((displayWidth / 1.3, displayHeight / 1.125, displayWidth / 6, displayHeight / 10),'Clean')

# Function for drawing where the creature is.
def creaturePos(x,y):
    gameDisplay.blit(creatureImg,(x,y))

# Variable for game close/crash.
crashed = False

# Main loop for game. Checks events and draws/updates images and buttons.
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.VIDEORESIZE:
            resize(event)
        if 'click' in playButton.handleEvent(event):
            pass # Replace pass for code that handles play button's action.
        if 'click' in feedButton.handleEvent(event):
            pass # Replace pass for code that handles feed button's action.
        if 'click' in cleanButton.handleEvent(event):
            pass # Replace pass for code that handles clean button's action.

    gameDisplay.blit(backgroundImg,(0,0))
    creaturePos(displayWidth * 0.25,displayHeight * 0.4)
    
    playButton.draw(gameDisplay)
    feedButton.draw(gameDisplay)
    cleanButton.draw(gameDisplay)
    
    pygame.display.update()
    clock.tick(60) # FPS = 60

pygame.quit()
quit()
sys.exit()
