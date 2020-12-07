#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
pygame.init()

# Array mit Bildern des Characters
walk_right = [pygame.image.load('characters/pictures/run/right1.png'), pygame.image.load('characters/pictures/run/right2.png'), pygame.image.load('characters/pictures/run/right3.png'), pygame.image.load('characters/pictures/run/right4.png'), pygame.image.load('characters/pictures/run/right5.png'), pygame.image.load('characters/pictures/run/right6.png')]
walk_left = [pygame.image.load('characters/pictures/run/left1.png'), pygame.image.load('characters/pictures/run/left2.png'), pygame.image.load('characters/pictures/run/left3.png'), pygame.image.load('characters/pictures/run/left4.png'), pygame.image.load('characters/pictures/run/left5.png'), pygame.image.load('characters/pictures/run/left6.png')]

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
        # values sind 'r' oder 'l' (right, left) - wird benoetigt um die Richtung im Stand festzulegen
        self.last_direction = ''
        self.jump_velocity = 8

    def draw(self, screen):
        # Mithilfe von walk_count wird ein Bild aus dem Array ausgesucht, was die Bewegung animiert
        if (self.walk_count + 1) >= 18:
            self.walk_count = 0

        if self.left:
            screen.blit(walk_left[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right[self.walk_count // 3], (self.x, self.y))
            self.walk_count += 1
        else:
            standing_char = walk_left[0] if self.last_direction.lower() == 'l' else walk_right[0]
            screen.blit(standing_char, (self.x, self.y))
