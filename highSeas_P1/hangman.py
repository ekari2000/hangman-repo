import pygame
import sys
import random as r
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)

font = pygame.font.SysFont('Comic Sans MS', 75)
font2 = pygame.font.SysFont('Comic Sans MS', 25)
position=(400,100)

mainScreen= pygame.display.set_mode((800,600))
mainScreen.fill(white)


gallow=pygame.image.load('hangman_1.png')
gallowRect=gallow.get_rect(center=(500,300))
hangmanImages = [
    pygame.image.load('hangman_2.png'),
    pygame.image.load('hangman_3.png'),
    pygame.image.load('hangman_4.png'),
    pygame.image.load('hangman_5.png'),
    pygame.image.load('hangman_6.png'),
    pygame.image.load('hangman_full.png')
]
hangmanRects=[]
for i in hangmanImages:
    x=i.get_rect(center=(500, 300))
    hangmanRects.append(x)

def displayText(screen, text, font, color, position):
    textSurface= font.render(text,True, color)
    textRect= textSurface.get_rect(center=position)
    screen.blit(textSurface, textRect)

def allIndex(s,cha):
   return [i for i, c in enumerate(s) if c == cha]

with open('wordList.txt','r') as file:
    lines = file.readlines()
word=(r.choice(lines)).strip()
letters=list(word)
correctWord = ['___'] * len(letters)
incorrectLetters =[]

count=0
gameOver= False

print(word)

while True:
    mainScreen.fill(white)
    displayText(mainScreen,'HANGMAN',font,black,position)
    mainScreen.blit(gallow,gallowRect)
    displayText(mainScreen, ' '.join(correctWord), font2, black, (400, 450))


    displayText(mainScreen, 'Incorrect Letters: ' + ', '.join(incorrectLetters), font2, red, (400,550))

    if count > 0:
        mainScreen.blit(hangmanImages[count-1], hangmanRects[count-1])

    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            letter=pygame.key.name(event.key)
            if letter in letters:
                I=allIndex(word,letter)
                for i in I:
                    correctWord[i]=letter
                displayText(mainScreen,' '.join(correctWord), font2, black,(400,500))
                pygame.display.flip()
                
            else:
                if letter not in incorrectLetters:
                    incorrectLetters.append(letter)
                    count+=1
   
    if count>= len(hangmanImages):
        mainScreen.fill(white)
        displayText(mainScreen,'YOU LOST!',font,black,(400,300))
        displayText(mainScreen,f'The word was {word}',font2,black,(400,350))
        pygame.display.flip()
        pygame.time.delay(3000)
        break
                   
    if '___' not in correctWord:
        mainScreen.fill(white)
        displayText(mainScreen,'YOU WON!',font,black,(400,300))
        pygame.display.flip()
        pygame.time.delay(3000)
        break
                    