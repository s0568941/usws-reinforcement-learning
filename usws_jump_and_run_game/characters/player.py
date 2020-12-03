#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

    def draw(self, window):
        if self.walk_count + 1 >= 27:
            self.walk_count = 0
