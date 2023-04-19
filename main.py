import pygame
clock=pygame.time.Clock()
pygame.init()
size_x=600
size_y=600
screen=pygame.display.set_mode((size_x,size_y))
pygame.display.set_caption("KostikTemik")
icon=pygame.image.load('venv/images/programkot.png')
pygame.display.set_icon(icon)
screen.fill((80,79,79))
running=True
player=pygame.image.load('venv/images/sprite1.png')
pl_x=0
pl_y=0
speed=3
move_up = False
move_down = False
move_left = False
move_right = False
walk_down=[pygame.image.load('venv/images/sprite1.png'),
           pygame.image.load('venv/images/sprite2.png'),
           pygame.image.load('venv/images/sprite3.png'),
           pygame.image.load('venv/images/sprite4.png'),
           pygame.image.load('venv/images/sprite5.png')
           ]
index_anim=0


while running:
    clock.tick(10)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up=True
                index_anim=4
            if event.key == pygame.K_s:
                move_down=True
                index_anim=1

            if event.key == pygame.K_a:
                move_left=True
                index_anim=3

            if event.key == pygame.K_d:
                move_right=True
                index_anim=2
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_w:
               move_up=False
               index_anim=0

            if event.key == pygame.K_s:
                move_down=False
                index_anim=0

            if event.key == pygame.K_a:
                move_left=False
                index_anim=0

            if event.key == pygame.K_d:
                move_right=False
                index_anim=0
    if move_up == True:
        if (pl_y - speed >=0):
            pl_y -= speed
    if move_down == True:
            if (pl_y + speed +100<= size_y):
                pl_y += speed
    if move_right == True:
            if (pl_x + speed +100 <= size_x):
                pl_x += speed
    if move_left == True:
            if (pl_x - speed >= 0):
                pl_x -= speed
    screen.fill((80, 79, 79))
    screen.blit(walk_down[index_anim], (pl_x, pl_y))
    pygame.display.flip()

