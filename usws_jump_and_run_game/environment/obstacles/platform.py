#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

from usws_jump_and_run_game.environment.obstacles.obstacle import Obstacle


class Platform(Obstacle):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
