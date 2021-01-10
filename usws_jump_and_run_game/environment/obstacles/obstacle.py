#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()


class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, screen):
        self.hitbox = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def move_right(self):
        self.x += self.speed
        self.hitbox = (self.x, self.y, self.width, self.height)

    def move_left(self):
        self.x -= self.speed
        self.hitbox = (self.x, self.y, self.width, self.height)
