#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

class Scorpio(object):

    scorpio_left = [
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio1L.png'), (int(1 * 44), int(1 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio2L.png'), (int(1 * 44), int(1 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio3L.png'), (int(1 * 44), int(1 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio4L.png'), (int(1 * 44), int(1 * 27)))]

    scorpio_right = [
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio1R.png'), (int(1 * 44), int(1 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio2R.png'), (int(1 * 44), int(1 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio3R.png'), (int(1 * 44), int(1 * 27))),
        pygame.transform.scale(pygame.image.load('characters/pictures/enemies/scorpio/Scorpio4R.png'), (int(1 * 44), int(1 * 27)))]


    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.speed = 3
        self.hitbox = (self.x + 1, self.y + 3, self.height, self.width)

    def draw(self, screen):
        self.move()
        if self.walk_count + 1 >= 12:
            self.walk_count = 0
        if self.speed > 0:
            screen.blit(self.scorpio_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            screen.blit(self.scorpio_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1

        self.hitbox = (self.x + 1, self.y + 3, self.height, self.width)
        # Displaying the hyenas hitbox with a red rectangle
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

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