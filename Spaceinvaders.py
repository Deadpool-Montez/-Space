import pygame
pygame.init()
WIDTH,HEIGHT=900,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SPACE INVADERS")
BORDER=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
FONT=pygame.font.SysFont("comicsans",70)
FPS=60
VEL=5
BULLETVEL=7
SSWIDTH,SSHEIGHT=55,40
#Creating events
Yellowhit=pygame.USEREVENT+1
Redhit=pygame.USEREVENT+2
Yellowspaceshipimg=pygame.image.load("YellowSpaceship.png")
Yellowspaceship=pygame.transform.rotate(pygame.transform.scale(Yellowspaceshipimg,(SSWIDTH,SSHEIGHT)),90)
Redspaceshipimg=pygame.image.load("RedSpaceship.png")
Redspaceship=pygame.transform.rotate(pygame.transform.scale(Redspaceshipimg,(SSWIDTH,SSHEIGHT)),270)
Space=pygame.transform.scale(pygame.image.load("STARS.png"),(WIDTH,HEIGHT))

def drawscreen(red,yellow,redbullets,yellowbullets,redhealth,yellowhealth):
    screen.blit(Space,(0,0))
    pygame.draw.rect(screen,"black",BORDER)
    Red_health_text=FONT.render("HEALTH: "+str(redhealth),1,"white")
    Yellow_health_text=FONT.render("HEALTH: "+str(yellowhealth),1,"white")
    screen.blit(Red_health_text,(WIDTH-20,10))
    screen.blit(Yellow_health_text,(10,10))
    screen.blit(Yellowspaceship,(yellow.x,yellow.y))
    screen.blit(Redspaceship,(red.x,red.y))
    for bullet in yellowbullets:
        pygame.draw.rect(screen,"yellow",bullet)
    for bullet in redbullets:
        pygame.draw.rect(screen,"red",bullet)
    pygame.display.update()

def yellow_movement(keys_pressed,yellow):
    if keys_pressed[pygame.K_a] and yellow.x-VEL>0:
        yellow.x-=VEL
    if keys_pressed[pygame.K_d] and yellow.x+VEL<BORDER.x:
        yellow.x+=VEL
    if keys_pressed[pygame.K_w] and yellow.y-VEL>0:
        yellow.y-=VEL
    if keys_pressed[pygame.K_s] and yellow.y+VEL<HEIGHT:
        yellow.y+=VEL

def red_movement(keys_pressed,red):
    if keys_pressed[pygame.K_LEFT] and red.x-VEL>BORDER.x+BORDER.width:
        red.x-=VEL
    if keys_pressed[pygame.K_RIGHT] and red.x+VEL<WIDTH:
        red.x+=VEL
    if keys_pressed[pygame.K_UP] and red.y-VEL>0:
        red.y-=VEL
    if keys_pressed[pygame.K_DOWN] and red.y+VEL<HEIGHT:
        red.y+=VEL
def handle_bullets(yellowbullets,redbullets,yellow,red):
    for bullet in yellowbullets:
        bullet.x+=BULLETVEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Redhit))
            yellowbullets.remove(bullet)
        elif bullet.x>WIDTH:
            yellowbullets.remove(bullet)
            
    for bullet in redbullets:
        bullet.x+=BULLETVEL
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellowhit))
            redbullets.remove(bullet)
        elif bullet.x>WIDTH<0:
            redbullets.remove(bullet)
def draw_winner(text):
    draw_text=FONT.render(text,1,"white")
    screen.blit(draw_text,(WIDTH/2-draw_text.get_width()/2,HEIGHT/2-draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)
def main():
    red=pygame.Rect(700,300,SSWIDTH,SSHEIGHT)
    yellow=pygame.Rect(100,300,SSWIDTH,SSHEIGHT)
    redbullets=[]
    yellowbullets=[]
    redhealth=10
    yellowhealth=10

    clock=pygame.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
main()

        