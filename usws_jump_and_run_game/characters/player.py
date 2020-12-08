#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
pygame.init()

# Array mit Bildern des Characters
walk_right = [pygame.image.load('characters/pictures/run/right1.png'), pygame.image.load('characters/pictures/run/right2.png'), pygame.image.load('characters/pictures/run/right3.png'), pygame.image.load('characters/pictures/run/right4.png'), pygame.image.load('characters/pictures/run/right5.png'), pygame.image.load('characters/pictures/run/right6.png')]
walk_left = [pygame.image.load('characters/pictures/run/left1.png'), pygame.image.load('characters/pictures/run/left2.png'), pygame.image.load('characters/pictures/run/left3.png'), pygame.image.load('characters/pictures/run/left4.png'), pygame.image.load('characters/pictures/run/left5.png'), pygame.image.load('characters/pictures/run/left6.png')]
idle_left_p = [pygame.image.load('characters/pictures/idle/idleL1.png'), pygame.image.load('characters/pictures/idle/idleL2.png'), pygame.image.load('characters/pictures/idle/idleL3.png')]
idle_right_p = [pygame.image.load('characters/pictures/idle/idleR1.png'), pygame.image.load('characters/pictures/idle/idleR2.png'), pygame.image.load('characters/pictures/idle/idleR3.png')]

class Player:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = 5
        self.is_jump = False
        self.left = False
        self.right = False
        # Walk count wird als index in einem array von Bildern genutzt, um den Char animieren zu koennen
        self.walk_count = 0
        self.jump_velocity = 8
        self.idle_left = False
        self.idle_right = False
        self.idle_count = 0

    def draw(self, screen):
        # Mithilfe von walk_count wird ein Bild aus dem Array ausgesucht, was die Bewegung animiert
        if (self.walk_count + 1) >= 18:
            self.walk_count = 0

        if (self.idle_count + 1) >= 18:
            self.idle_count = 0

        if self.left:
            screen.blit(walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1

        else:
            if self.idle_left:
                screen.blit(idle_left_p[self.idle_count // 6], (self.x, self.y))
                self.idle_count += 1

            else:
                screen.blit(idle_right_p[self.idle_count // 6], (self.x, self.y))
                self.idle_count += 1
