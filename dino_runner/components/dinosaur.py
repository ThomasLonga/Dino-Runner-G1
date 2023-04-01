import pygame
from pygame import Surface
from pygame.sprite import Sprite
from pygame.rect import Rect

from dino_runner.utils.constants import JUMPING, RUNNING, DUCKING 

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

class Dinosaur(Sprite):
    JUMP_VELOCITY = 8.5
    DUCK_POS_X = 40
    DUCK_POS_Y = 350

   

    def __init__(self):
        self.image = RUNNING[0]
        self.rect = self.image.get_rect()
        self.POS_X = 80
        self.POS_Y = 310
        self.step = 0
        self.action = DINO_RUNNING 
        self.jump_velocity = self.JUMP_VELOCITY
        self.dinoDuck = DINO_DUCKING

   

    def get_pos_x(self):
         return  self.POS_X
    
    def get_pos_y(self):
        return  self.POS_Y
        

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()

        if self.action != DINO_JUMPING: #imagen
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING

            elif user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING

            else:
                self.action = DINO_RUNNING

        if self.step >= 10:
            self.step = 0

    def run(self):
        self.image = RUNNING[self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.get_pos_x()
        self.rect.y = self.get_pos_y()
        self.step += 1

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.get_pos_y()
            self.jump_velocity = self.JUMP_VELOCITY

    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.DUCK_POS_X
        self.rect.y = self.DUCK_POS_Y
        self.step +=1

    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))