import pygame
import random

width,height=1024,800
font_width=15

pygame.init()
screen = pygame.display.set_mode((width,height))
font=pygame.font.SysFont("font.ttf",25)
bg_surface=pygame.Surface((width,height),flags=pygame.SRCALPHA)
pygame.Surface.convert(bg_surface)
bg_surface.fill(pygame.Color(0,0,0,28))
screen.fill((0,0,0))

letter=['I','L','O','V','E','Y','C','Y']
texts=[]
for i in range(8):
    text=font.render(str(letter[i]),True,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    texts.append(text)

column=int(width/font_width)

drops=[]
for i in range(column):
    drops.append(0)


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    screen.blit(bg_surface,(0,0))

    for i in range(column):
        text=random.choice(texts)
        screen.blit(text,(i*font_width,drops[i]*font_width))

        drops[i]+=1

        if drops[i]*font_width>height or random.random()>0.95:
            drops[i]=0

    pygame.display.flip()
    pygame.time.delay(30)