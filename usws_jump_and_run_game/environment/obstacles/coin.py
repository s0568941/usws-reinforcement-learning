#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

from usws_jump_and_run_game.environment.obstacles.obstacle import Obstacle

img = [
    pygame.transform.scale(pygame.image.load('environment/obstacles/pictures/coin/C1011.png'), (int(0.40 * 128), int(0.40 * 128))),
    pygame.transform.scale(pygame.image.load('environment/obstacles/pictures/coin/C1012.png'), (int(0.40 * 128), int(0.40 * 128))),
    pygame.transform.scale(pygame.image.load('environment/obstacles/pictures/coin/C1013.png'), (int(0.40 * 128), int(0.40 * 128))),
    pygame.transform.scale(pygame.image.load('environment/obstacles/pictures/coin/C1014.png'), (int(0.40 * 128), int(0.40 * 128)))]

class Coin(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.spin_count = 0

    def draw(self, screen):
        if (self.spin_count + 1) >= 12:
            self.spin_count = 0
        screen.blit(img[self.spin_count // 3], (self.x, self.y))
        self.spin_count += 1
