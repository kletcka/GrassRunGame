import pygame
import random
import objects
import os.path
pygame.init()

#настройки экрана
WIDTH = 600
HEIGHT = 600
pygame.display.set_caption("GrassRun")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

#переменные
done = False
mode = True
score = 0
max_x = 0
cur_x = 0

#объекты и списки объектов
hero = objects.Hero()
g_o = objects.Over()
space = objects.Space()
fields = []
cars = []
def up_list():
    global fields, cars
    fields = []
    cars = []
    for i in range(1,9):
        cars.append(objects.Car(i*100-100))

    for i in [-200,0,200,400,600,800]:
        for j in [-200,0,200,400,600,800]:
            fields.append(objects.Field(i,j))


up_list()
while not done:
    screen.fill((0,0,0))   
    if mode == True:
        clock.tick(60)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                done = True


        if pygame.key.get_pressed()[pygame.K_UP]:
            for i in fields:
                i.move('Y', 2)
            for i in cars:
                i.gmove(0, 2)
            cur_x-=1
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            for i in fields:
                i.move('Y', -2)
            for i in cars:
                i.gmove(0, -2)
            if cur_x==max_x:
                max_x +=1
            cur_x +=1
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            for i in fields:
                i.move('X', -2)
            for i in cars:
                i.gmove(-2, 0)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            for i in fields:
                i.move('X', 2)
            for i in cars:
                i.gmove(2, 0)



        for i in fields:
            i.draw(screen)

        for i in cars:
            i.draw(screen)
            i.move(6)
            if hero.rect.colliderect(i.rect):
                mode = False

        hero.draw(screen)

        font = pygame.font.Font(pygame.font.match_font('arial'), 30)
        text_surface = font.render(f'Score:{max_x//100}', True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (300, 0)
        screen.blit(text_surface, text_rect)
            
    if mode == False:
        clock.tick(30)



        g_o.draw(screen)
        font = pygame.font.Font(pygame.font.match_font('arial'), 30)
        text_surface = font.render(f'Нажмите                       чтобы продожить', True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (300, 500)
        screen.blit(text_surface, text_rect)
        space.draw(screen)


        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                done = True
            if pygame.mouse.get_pressed()[0] == 1 and space.rect.collidepoint(pygame.mouse.get_pos()):
                mode = True
                cars = []
                up_list()

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            mode = True
            up_list()
    pygame.display.flip()
    



pygame.quit()