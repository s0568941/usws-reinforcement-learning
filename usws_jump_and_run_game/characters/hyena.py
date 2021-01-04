#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

class Hyena(object):

    hyena_left = [
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena1.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena2.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena3.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena4.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena5.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena6.png'), (int(1.2 * 44), int(1.2 * 27)))]


    hyena_right = [
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena1R.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena2R.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena3R.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena4R.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena5R.png'), (int(1.2 * 44), int(1.2 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/hyena/Hyena6R.png'), (int(1.2 * 44), int(1.2 * 27)))]

    def __init__(self, x, y, width, height, end, name):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.speed = 6
        self.hitbox = (self.x + 5, self.y + 5, self.height, self.width)

    def draw(self, screen):
        self.move()
        if self.walk_count + 1 >= 18:
            self.walk_count = 0
        if self.speed > 0:
            screen.blit(self.hyena_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            screen.blit(self.hyena_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1

        self.hitbox = (self.x + 5, self.y + 5, self.height, self.width)
        # Displaying the hyenas hitbox with a red rectangle
        #pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

        # screen moves to the right
    def adapt_to_screen_left(self):
        self.x += -5
        self.path[1] += -5
        self.path[0] += -5

    # screen moves to the left
    def adapt_to_screen_right(self):
        self.x += 5
        self.path[1] += 5
        self.path[0] += 5

    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0

        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0