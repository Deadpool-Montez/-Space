import pygame

pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill("white")
img=pygame.image.load("bulbone.jpg")
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
    event=pygame.event.poll()
    if event.type==pygame.MOUSEBUTTONDOWN:
        img=pygame.image.load("bulbtwo.jpg")
        screen.blit(img, (0,0))
        pygame.display.update()
    elif event.type==pygame.MOUSEBUTTONUP:
        img=pygame.image.load("bulbone.jpg")
        screen.blit(img, (0,0))
        pygame.display.update()