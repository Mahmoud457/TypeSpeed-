import textwrap
import time
import pygame

global run

textType = 'freesansbold.ttf'
textSize = 32


bg = (0, 0 ,0)
pygame.init()
screenWidth = 1200
screenHeight = 800
screen = pygame.display.set_mode([screenWidth, screenHeight])

startTime = 0


pygame.display.update()
textColour = (255, 255, 255)
textBGcolour = bg


def endGame():
    endTime = time.time()
    print(endTime-startTime)
    print((textLen//(endTime-startTime)*60, "characters per minute"))
    global run
    run = False
def grabText(filename="default.txt"):
    f = open(filename, "r")
    passage = list(f.read())
    return passage

def checkText(pressedKey):

    if pressedKey == "space":
        pressedKey = " "

    if pressedKey == text[0].lower():
        text.pop(0)
    if len(text) <= 0:
        endGame()

def drawText():
    font = pygame.font.Font(textType, textSize)
    wrapped = textwrap.wrap(''.join(text))
    count = 0
    for x in wrapped:
        drawn = font.render(x, True, textColour, textBGcolour)
        textRect = drawn.get_rect()
        textRect.center = (screenWidth//2, screenHeight//3 + 50*count)
        screen.blit(drawn, textRect)
        count+=1
        if count > 2:
            break


text = grabText()
textLen = len(text)


run = True
while run:
    screen.fill(bg)

    drawText()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            checkText(pygame.key.name(event.key))
            if startTime == 0:
                startTime = time.time()
    pygame.display.update()
