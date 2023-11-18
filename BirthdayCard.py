import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("BIRTHDAY GREETING CARD")

img=pygame.image.load("backgroundone.jpg")
image=pygame.transform.scale(img,(WIDTH,HEIGHT))

while True:
    for event in pygame.event.get():
        #check if a user wants to exit the game or not
        if event.type==pygame.QUIT:
            exit()
    font=pygame.font.SysFont("Times New Roman", 50)
    text=font.render("Happy", False, (0,0,0))
    text2=font.render("Birthday", True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text,(210,180))
    screen.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)
    img1=pygame.image.load("backgroundtwo.jpg")
    image1=pygame.transform.scale(img1,(WIDTH,HEIGHT))

    font1=pygame.font.SysFont("Times New Roman", 50)
    text1=font1.render("Wish you a", False, (0,0,0))
    text3=font1.render("bright future", True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image1,(0,0))
    screen.blit(text1,(210,180))
    screen.blit(text3,(180,264))
    pygame.display.update()
    time.sleep(2)

    img2=pygame.image.load("backgroundthree.jpg")
    image2=pygame.transform.scale(img2,(WIDTH,HEIGHT))

    font2=pygame.font.SysFont("Times New Roman", 50)
    text2=font2.render("Have a wonderful Bday!!!", False, (0,0,0))
    screen.fill((255,255,255))
    screen.blit(image2,(0,0))
    screen.blit(text2,(123,180))
    pygame.display.update()
    time.sleep(2)