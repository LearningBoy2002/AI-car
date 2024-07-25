import pygame
import os
import math
import sys
import neat 


SCREEN_WIDTH = 1244
SCREEN_HEIGHT = 1016
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
TRACK = pygame.image.load(os.path.join("Assets", "track.png"))

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load(os.path.join("Assets", "Car1.png"))
        self.original_image = pygame.transform.rotate(self.original_image, -90)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(490, 820))
        self.drive_state = False
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0

    def update(self):
        self.drive()
        self.rotate()

    def drive(self):
        if self.drive_state:
               self.rect.center += self.vel_vector * 6
    
    def rotate(self):
         self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.05)

car = pygame.sprite.GroupSingle(Car())


def eval_genomes():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 

        SCREEN.blit(TRACK, (0, 0)) 


        user_input = pygame.key.get_pressed()
        if (sum(pygame.key.get_pressed()) <= 1):
            car.sprite.drive_state = False
        
        if user_input[pygame.K_UP]:
            car.sprite.drive_state = True
            

        car.draw(SCREEN)
        car.update()
        pygame.display.update()
        clock.tick(60)





eval_genomes()
    
        
    
