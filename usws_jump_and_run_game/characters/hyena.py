#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame

pygame.init()

from usws_jump_and_run_game.characters.enemy import Enemy

class Hyena(Enemy):

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

    def __init__(self, x, y, width, height, end):
        super().__init__(x, y, width, height, end)
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
        # pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)