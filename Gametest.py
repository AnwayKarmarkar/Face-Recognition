import pygame
import time
import random

displayHeight = 600
displayWidth = 800

carWidth = 72
carHeight = 42

grey = (150,150,150)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,30)

pygame.init()
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('testGame')
clock = pygame.time.Clock()

carImg = pygame.image.load('plane.png')

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(10,10))

def building(buildingX, buildingY, buildingW, buildingH, buildingCol):
    pygame.draw.rect(gameDisplay , buildingCol , [buildingX, buildingY, buildingW, buildingH])

def text_objects(text , font):
    TextSurface = font.render(text , True , yellow)
    return TextSurface, TextSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('C:\Windows\Fonts\cour.ttf',70)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((displayWidth/2),(displayHeight/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)

    gameLoop()

def crash():
    message_display('YOU DIED. RIP')

def plane(x,y):
    gameDisplay.blit(carImg,(x,y))

def gameLoop():
    
    x = displayWidth * 0.45
    y = displayHeight * 0.8

    #building_StartX = random.randrange(0, displayWidth)
    building_StartX = x-115
    building_StartY = -600
    building_Speed = 8
    building_Width = 300
    building_Height = 70

    building_Dodged = 0

    x_change = 0
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x >= 0:
                    x_change = -10
                if event.key ==pygame.K_RIGHT and x+carWidth <= displayWidth:
                    x_change = 10

            if event.type == pygame.KEYUP:
                if event.key ==pygame.K_LEFT or event.key ==pygame.K_RIGHT:
                    x_change = 0
        x += x_change

        gameDisplay.fill(grey)

        building(building_StartX, building_StartY, building_Width, building_Height, black)
        building_StartY += building_Speed

        plane(x,y)    

        things_dodged(building_Dodged)

        if x > displayWidth-carWidth or x < 0:
            crash()

        if building_StartY > displayHeight:
            building_StartY = 0 - building_Height
            #building_StartX = random.randrange(0, (displayWidth-building_Width))
            building_StartX = x-115
            building_Dodged +=1
            building_Speed += 0.7

        if y < building_StartY+building_Height and y + carHeight >= building_StartY:
            if x > building_StartX and x < building_StartX+building_Width or x+carWidth > building_StartX and x+carWidth < building_StartX+building_Width:
                crash()

        pygame.display.update()
        clock.tick(60)

gameLoop()