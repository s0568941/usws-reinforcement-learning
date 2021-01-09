#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

from usws_jump_and_run_game.environment.obstacles.obstacle import Obstacle

img = pygame.image.load('environment/obstacles/pictures/spike.png')

class Coin(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)
        # screen.blit(pygame.transform.scale(img, (self.width + 10, self.height)), (self.x-5, self.y))
#        screen.blit(pygame.transform.scale(pygame.transform.rotate(img, 180), (self.width + 10, self.height)), (self.x-5, self.y))
