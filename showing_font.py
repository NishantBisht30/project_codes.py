import pygame

pygame.init()

width = 500
hieght = 400
screen = pygame.display.set_mode((width,hieght))

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
text_x = 10
text_y = 285

def show_score(x,y):
    score = font.render("Score : " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    show_score(text_x,text_y)
    pygame.display.update()
