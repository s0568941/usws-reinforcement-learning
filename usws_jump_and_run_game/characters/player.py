#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

from usws_jump_and_run_game.utils.constants import *

# Array mit Bildern des Characters
walk_right_p = [pygame.image.load('characters/pictures/run/right1.png'),
                pygame.image.load('characters/pictures/run/right2.png'),
                pygame.image.load('characters/pictures/run/right3.png'),
                pygame.image.load('characters/pictures/run/right4.png'),
                pygame.image.load('characters/pictures/run/right5.png'),
                pygame.image.load('characters/pictures/run/right6.png')]
walk_left_p = [pygame.image.load('characters/pictures/run/left1.png'),
               pygame.image.load('characters/pictures/run/left2.png'),
               pygame.image.load('characters/pictures/run/left3.png'),
               pygame.image.load('characters/pictures/run/left4.png'),
               pygame.image.load('characters/pictures/run/left5.png'),
               pygame.image.load('characters/pictures/run/left6.png')]
idle_left_p = [pygame.image.load('characters/pictures/idle/idleL1.png'),
               pygame.image.load('characters/pictures/idle/idleL2.png'),
               pygame.image.load('characters/pictures/idle/idleL3.png')]
idle_right_p = [pygame.image.load('characters/pictures/idle/idleR1.png'),
                pygame.image.load('characters/pictures/idle/idleR2.png'),
                pygame.image.load('characters/pictures/idle/idleR3.png')]
jump_left_p = [pygame.image.load('characters/pictures/jump/jumpL1.png'),
               pygame.image.load('characters/pictures/jump/jumpL2.png'),
               pygame.image.load('characters/pictures/jump/jumpL3.png'),
               pygame.image.load('characters/pictures/jump/jumpL4.png')]
jump_right_p = [pygame.image.load('characters/pictures/jump/jumpR1.png'),
                pygame.image.load('characters/pictures/jump/jumpR2.png'),
                pygame.image.load('characters/pictures/jump/jumpR3.png'),
                pygame.image.load('characters/pictures/jump/jumpR4.png')]


class Player:
    def __init__(self, x, y, height, width):
        # static_x and static_y keep the player at the same spot while x and y track his movement in the environment
        self.x = x
        self.static_x = x
        self.y = y
        self.static_y = y
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
        self.jump_count = 0
        self.last_dir = ''
        self.hitbox = (self.x + 17, self.y + 7, self.height, self.width)

    def draw(self, screen):
        # Mithilfe von walk_count wird ein Bild aus dem Array ausgesucht, was die Bewegung animiert
        if (self.walk_count + 1) >= 18:
            self.walk_count = 0

        if (self.idle_count + 1) >= 18:
            self.idle_count = 0

        if (self.jump_count + 1) >= 8:
            self.jump_count = 0

        if self.left:
            screen.blit(walk_left_p[self.walk_count // 3], (self.static_x, self.static_y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right_p[self.walk_count // 3], (self.static_x, self.static_y))
            self.walk_count += 1
        elif self.is_jump:
            if self.last_dir == 'r':
                screen.blit(jump_right_p[self.jump_count // 2], (self.static_x, self.y))
                self.jump_count += 1
            else:
                screen.blit(jump_left_p[self.jump_count // 2], (self.static_x, self.y))
                self.jump_count += 1
        else:
            if self.idle_left:
                screen.blit(idle_left_p[self.idle_count // 6], (self.static_x, self.static_y))
                self.idle_count += 1
            else:
                screen.blit(idle_right_p[self.idle_count // 6], (self.static_x, self.static_y))
                self.idle_count += 1
        # TODO hitbox will need to be moving with x instead of static_x
        self.hitbox = (self.static_x + 17, self.y + 7, self.height, self.width)
        # Displaying the players hitbox with a red rectangle
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)


    def move_right(self):
        self.x += self.speed
        if(self.x >= PLAYER_STATIC_X):
            self.static_x = PLAYER_STATIC_X
        else:
            self.static_x = self.x

    def move_left(self):
        self.x -= self.speed
        if(self.x <= PLAYER_STATIC_X):
            self.static_x = self.x
