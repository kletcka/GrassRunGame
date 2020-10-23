import pygame
import random
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
class Hero(pygame.sprite.Sprite):
    def __init__(self):
        self.image_adress = os.path.join('Game', 'grass.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (50, 50))
        self.x = 300
        self.y = 20
        self.rect = pygame.Rect(self.x+14, self.y+37, 20, 15)

    def draw(self, screen):
        #test-function pygame.draw.rect(screen,(255, 255, 255),self.rect)
        screen.blit(self.my_image,(self.x, self.y))
    

class Over(pygame.sprite.Sprite):
    def __init__(self):
        self.image_adress = os.path.join('Game', 'over.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (600, 600))
        self.x = 0
        self.y = 0
    def draw(self, screen):
        screen.blit(self.my_image,(self.x, self.y))
    
class Space(pygame.sprite.Sprite):
    def __init__(self):
        self.image_adress = os.path.join('Game', 'space.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (250, 250))
        self.x = 125
        self.y = 400
        self.rect = pygame.Rect(self.x+75, self.y+100, 110, 40) 
    def draw(self, screen):
        #test-function pygame.draw.rect(screen,(255, 255, 255),self.rect)
        screen.blit(self.my_image,(self.x, self.y))
    

class Field(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image_adress = os.path.join('Game', 'field.png')
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (200, 200))
        self.x = x
        self.y = y

    def move(self, vector, step):
        if vector == 'X':
            self.x += step
        if vector == 'Y': 
            self.y += step
        if self.x>=605:
            self.x = -200
        if self.x<=-205:
            self.x = 600
        if self.y>=601:
            self.y = -200
        if self.y<=-201:
            self.y = 600
    def draw(self, screen):
        screen.blit(self.my_image,(self.x, self.y))


class Car(pygame.sprite.Sprite):
    def __init__(self, y):
        self.v = random.randint(0,1)
        self.color = random.randint(0,3)
        self.way = 'Car' + list(['R', 'L'])[self.v] + list(['B', 'G', 'R', 'Y'])[self.color] + '.png'
        self.image_adress = os.path.join('Game', self.way)
        self.my_image = pygame.image.load(self.image_adress).convert_alpha()
        self.my_image = pygame.transform.scale(self.my_image, (200, 200))
        self.y = y
        self.x = random.randint(-180, 720)
        self.rect = pygame.Rect(self.x+14, self.y+37, 20, 15)


    def draw(self, screen):
        self.rect = pygame.Rect(self.x+60, self.y+135, 80, 30)
        
        screen.blit(self.my_image,(self.x, self.y))
        #test-function pygame.draw.rect(screen,(255, 255, 255),self.rect)

    def move(self, step):
        if self.v == 1:
            self.x -= step
        else:
            self.x += step
        if self.x>=800:
            self.x = -100
        if self.x<=-200:
            self.x = 700
        if self.y>=800:
            self.y = -100
            self.v = random.randint(0,1)
            self.color = random.randint(0,3)
            self.way = 'Car' + list(['R', 'L'])[self.v] + list(['B', 'G', 'R', 'Y'])[self.color] + '.png'
            self.image_adress = os.path.join('Game', self.way)
            self.my_image = pygame.image.load(self.image_adress).convert_alpha()
            self.my_image = pygame.transform.scale(self.my_image, (200, 200))
            self.x = random.randint(-180, 720)
        if self.y<=-200:
            self.y = 700
            self.v = random.randint(0,1)
            self.color = random.randint(0,3)
            self.way = 'Car' + list(['R', 'L'])[self.v] + list(['B', 'G', 'R', 'Y'])[self.color] + '.png'
            self.image_adress = os.path.join('Game', self.way)
            self.my_image = pygame.image.load(self.image_adress).convert_alpha()
            self.my_image = pygame.transform.scale(self.my_image, (200, 200))
            self.x = random.randint(-180, 720)

    def gmove(self, step, ystep):
        self.x += step
        self.y += ystep

