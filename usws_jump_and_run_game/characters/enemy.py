#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

class Enemy:
    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walk_count = 0
        self.hitbox = (self.x, self.y, self.height, self.width)
        self.is_overcome = False

    def draw(self):
        pass

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
