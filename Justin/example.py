import pygame
import pygbutton

pygame.init()

displayWidth = 800
displayHeight = 600

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Cubulicious')
clock = pygame.time.Clock()

backgroundImg = pygame.image.load('Images/background.png')
backgroundImg = pygame.transform.scale(backgroundImg, (displayWidth,displayHeight))

cubeImg = pygame.image.load('Images/cube.png')
cubeImg = pygame.transform.scale(cubeImg, ((displayWidth / 2), (displayHeight / 2)))

pygame.mixer.music.load('Audio/main.mp3')
pygame.mixer.music.play(-1)

playButton = pygbutton.PygButton((displayWidth / 13, displayHeight / 1.125, 120, 60),'Play')
feedButton = pygbutton.PygButton((displayWidth / 2.35, displayHeight / 1.125, 120, 60),'Feed')
cleanButton = pygbutton.PygButton((displayWidth / 1.3, displayHeight / 1.125, 120, 60),'Clean')

def cube(x,y):
    gameDisplay.blit(cubeImg,(x,y))

cubeX = (displayWidth * 0.25)
cubeY = (displayHeight * 0.4)

cubeXChange = 0
cubeYChange = 0

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
        playButton.handleEvent(event)
        feedButton.handleEvent(event)
        cleanButton.handleEvent(event)

    gameDisplay.blit(backgroundImg,(0,0))
    cube(cubeX,cubeY)
    
    playButton.draw(gameDisplay)
    feedButton.draw(gameDisplay)
    cleanButton.draw(gameDisplay)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
