#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

class Skull(object):

    skull_left = [
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull1L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull2L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull3L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull4L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull5L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull6L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull7L.png'), (int(1.75 * 25), int(1.75 * 25))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/skull/skull8L.png'), (int(1.75 * 25), int(1.75 * 25)))]



    def __init__(self, x, y, width, height, end, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.y, self.end]
        self.walk_count = 0
        self.speed_x = 5
        self.speed_y = 2
        self.hitbox = (self.x, self.y, self.height, self.width)

    def draw(self, screen):
        self.move()
        if self.walk_count + 1 >= 24:
            self.walk_count = 0

        screen.blit(self.skull_left[self.walk_count//3], (self.x, self.y))
        self.walk_count += 1

        self.hitbox = (self.x + 9, self.y + 9, self.height, self.width)
        # Displaying the hyenas hitbox with a red rectangle
        #pygame.draw.rect(screen, (0, 255, 0), self.hitbox, 2)

    def adapt_to_screen_left(self):
        self.x -= self.speed_x

    def adapt_to_screen_right(self):
        self.x += self.speed_x

    def move(self):
        if self.speed_y > 0:
            if self.y + self.speed_y < self.path[1]:
                self.y += self.speed_y
            else:
                self.speed_y = self.speed_y * -1
                self.walk_count = 0

        else:
            if self.y - self.speed_y > self.path[0]:
                self.y += self.speed_y
            else:
                self.speed_y = self.speed_y * -1
                self.walk_count = 0