import pygame
import random

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((760,650))

x=300
y=550
x_change=0
y_change=0

#adding player
player = pygame.image.load("upward-arrow.png")


#setting images for enemey
enemey = pygame.image.load("downward-arrow.png")
bh = pygame.image.load("black-hole.png")
list1 = [42, 212, 382, 552, 700]
enemey_x = random.choice(list1)
enemey_y=0
enemey_speed = 10




#loading player on screen
def playerimg():
    screen.blit(player,(x,y))

# def bhimg():
#     screen.blit(bh,(10,0))
#     screen.blit(bh,(180,0))
#     screen.blit(bh,(350,0))
#     screen.blit(bh,(520,0))
#     screen.blit(bh,(690,0))
#     # screen.blit(bh,(10,0))


def enemeyimg_fire(x,y):
    screen.blit(enemey,(x,y))



running = True
while running:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += 10
            elif event.key == pygame.K_RIGHT:
                x_change -= 10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x = x - x_change
    if x<=0:
         x=0
    if x>=696:
        x=696

    enemeyimg_fire(enemey_x,enemey_y)
    enemey_y += enemey_speed
    if enemey_y > 650:
        enemey_y = 0
        enemey_x = random.choice(list1)
    playerimg()

    clock.tick(30)
    pygame.display.update()