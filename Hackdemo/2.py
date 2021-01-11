import pygame

width,height=600,400
rgb=(0,0,0)
pygame.init()
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("hello")
screen.fill(rgb)
font=pygame.font.SysFont("font.ttf",500)
text = font.render("a",True,(255,255,255))
screen.blit(text,(10,10))
# screen.fill(pygame.Color(0,0,0,28))
# yang=pygame.image.load("1.jpg")
# screen.blit(yang,(0,0))
# screen.blit(yang,(100,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    pygame.time.delay(10)