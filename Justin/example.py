import pygame

pygame.init()

displayWidth = 800
displayHeight = 600

black = (0,0,0)
white = (255,255,255)

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Zoom')
clock = pygame.time.Clock()

boltImg = pygame.image.load('Images/bolt.png')

def bolt(x,y):
    gameDisplay.blit(boltImg,(x,y))

boltX = (displayWidth * 0.45)
boltY = (displayHeight * 0.8)

boltXChange = 0
boltYChange = 0

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boltXChange = -5
            elif event.key == pygame.K_RIGHT:
                boltXChange = 5
            elif event.key == pygame.K_UP:
                boltYChange = -5
            elif event.key == pygame.K_DOWN:
                boltYChange = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                boltXChange = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                boltYChange = 0

    gameDisplay.fill(white)

    boltX += boltXChange
    boltY += boltYChange
    bolt(boltX,boltY)    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
