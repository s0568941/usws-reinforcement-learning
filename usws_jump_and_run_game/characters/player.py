#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import math

pygame.init()

from usws_jump_and_run_game.utils.constants import *

# Array mit Bildern des Characters
walk_right_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/run/right1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/right2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/right3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/right4.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/right5.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/right6.png'), (int(1.6 * 50), int(1.6 * 37)))]

walk_left_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/run/left1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/left2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/left3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/left4.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/left5.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/run/left6.png'), (int(1.6 * 50), int(1.6 * 37)))]

jump_right_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpR1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpR2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpR3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpR4.png'), (int(1.6 * 50), int(1.6 * 37)))]

jump_left_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpL1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpL2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpL3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/jump/jumpL4.png'), (int(1.6 * 50), int(1.6 * 37)))]

idle_right_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/idle/idleR1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/idle/idleR2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/idle/idleR3.png'), (int(1.6 * 50), int(1.6 * 37)))]

idle_left_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/idle/idleL1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/idle/idleL2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/idle/idleL3.png'), (int(1.6 * 50), int(1.6 * 37)))]


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
        self.jump_velocity = JUMP_VELOCITY
        self.idle_left = False
        self.idle_right = False
        self.idle_count = 0
        self.jump_count = 0
        self.last_dir = ''
        self.hitbox = (self.x + PLAYER_HITBOX_PADDING_X, self.y + PLAYER_HITBOX_PADDING_Y, self.height, self.width)
        self.is_on_obstacle = False
        self.obstacles = []
        self.movement_blocked = False

    def draw(self, screen):
        # Mithilfe von walk_count wird ein Bild aus dem Array ausgesucht, was die Bewegung animiert
        if (self.walk_count + 1) >= 18:
            self.walk_count = 0

        if (self.idle_count + 1) >= 18:
            self.idle_count = 0

        if (self.jump_count + 1) >= 8:
            self.jump_count = 0

        if self.left:
            screen.blit(walk_left_p[self.walk_count // 3], (self.static_x, self.y))
            self.walk_count += 1
        elif self.right:
            screen.blit(walk_right_p[self.walk_count // 3], (self.static_x, self.y))
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
                screen.blit(idle_left_p[self.idle_count // 6], (self.static_x, self.y))
                self.idle_count += 1
            else:
                screen.blit(idle_right_p[self.idle_count // 6], (self.static_x, self.y))
                self.idle_count += 1
        # TODO hitbox will need to be moving with x instead of static_x
        self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
        # Displaying the players hitbox with a red rectangle
        pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def move_right(self):
        self.check_for_horizontal_obstacles(right=True)
        if not self.movement_blocked:
            self.x += self.speed
            if self.x >= PLAYER_STATIC_X:
                self.static_x = PLAYER_STATIC_X
            else:
                self.static_x = self.x

            self.check_for_vertical_obstacles()
            if not self.is_on_obstacle:
                self.fall_from_obstacle()

    def move_left(self):
        self.check_for_horizontal_obstacles(right=False)
        if not self.movement_blocked:
            self.x -= self.speed
            if self.x <= PLAYER_STATIC_X:
                self.static_x = self.x

            self.check_for_vertical_obstacles()
            if not self.is_on_obstacle:
                self.fall_from_obstacle()

    # checks if an obstacle is in front of the player and blocks its movement
    def check_for_horizontal_obstacles(self, right=True):
        moving_hitbox_x = self.static_x + PLAYER_HITBOX_PADDING_X
        next_x_coords_left_side = moving_hitbox_x - self.speed
        next_x_coords_right_side = moving_hitbox_x + self.hitbox[2] + self.speed
        char_feet_y = self.hitbox[1] + self.hitbox[3]
        for obstacle in self.obstacles:
            obstacle_x = obstacle.hitbox[0]
            obstacle_total_width = obstacle.hitbox[0] + obstacle.hitbox[2]
            obstacle_y = obstacle.hitbox[1]
            if right:
                if obstacle_x <= next_x_coords_right_side <= obstacle_total_width \
                        and char_feet_y > obstacle_y:
                    self.movement_blocked = True
                    return self.movement_blocked
            else:
                if obstacle_total_width >= next_x_coords_left_side >= obstacle_x \
                        and char_feet_y > obstacle_y:
                    self.movement_blocked = True
                    return self.movement_blocked

        self.movement_blocked = False
        return self.movement_blocked

    def check_for_vertical_obstacles(self):
        for obstacle in self.obstacles:
            # check if player is on obstacle
            moving_hitbox_x = self.static_x + PLAYER_HITBOX_PADDING_X
            moving_hitbox_y = self.y + PLAYER_HITBOX_PADDING_Y
            if math.ceil(moving_hitbox_y + self.hitbox[3]) == obstacle.hitbox[1]:
                obstacle_right_edge = obstacle.hitbox[0] + obstacle.hitbox[2]
                if obstacle.hitbox[0] < moving_hitbox_x < obstacle_right_edge \
                        or obstacle.hitbox[0] < (moving_hitbox_x + self.hitbox[2]) < obstacle_right_edge:
                    self.is_on_obstacle = True
                    return self.is_on_obstacle

        self.is_on_obstacle = False
        return False

    def fall_from_obstacle(self):
        if self.y < Y_STARTING_POSITION and not self.is_jump:
            is_landed = False
            while not is_landed:
                deb = (- self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
                if (self.hitbox[1] + self.hitbox[3]) - deb <= (Y_STARTING_POSITION + self.hitbox[3]):
                    self.y -= (- self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                    self.jump_velocity -= 1
                    self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
                else:
                    self.y = math.ceil(self.y)
                    diff = abs(int(Y_STARTING_POSITION - self.y))
                    vel_counter = 100
                    while diff != 0:
                        vel_counter -= vel_counter * 1 / 2
                        # TODO smoother falling velocity
                        self.y -= -(1 / 4) * (1 / 150)
                        self.jump_velocity -= 1
                        diff = abs(int(Y_STARTING_POSITION - self.y))
                        self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

                if math.ceil(self.y) == Y_STARTING_POSITION:
                    is_landed = True
                    self.is_on_obstacle = True
                    self.jump_velocity = JUMP_VELOCITY
                    self.is_jump = False

    def jump(self):
        if self.jump_velocity >= -JUMP_VELOCITY:
            char_feet_y = self.hitbox[1] + self.hitbox[3]
            char_left_edge_hitbox_x = self.hitbox[0]
            char_right_hitbox_x = self.hitbox[0] + self.hitbox[2]
            for obstacle in self.obstacles:
                obstacle_y = obstacle.hitbox[1]
                obstacle_left_edge_x = obstacle.hitbox[0]
                obstacle_right_edge_x = obstacle.hitbox[0] + obstacle.hitbox[2]
                # first part: obstacle y is underneath players feet
                # second part:
                if obstacle_y >= char_feet_y \
                        and char_left_edge_hitbox_x >= obstacle_left_edge_x \
                        and char_right_hitbox_x <= obstacle_right_edge_x \
                        and self.jump_velocity < 0 \
                        and not self.is_on_obstacle:
                    is_landed = False
                    while not is_landed:
                        self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
                        # for debug:
                        deb = (self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                        if (self.hitbox[1] + self.hitbox[3]) - deb <= obstacle.hitbox[1]:
                            self.y -= (self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                            self.jump_velocity -= 1
                            self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
                        else:
                            diff = abs(int((self.hitbox[1] + self.hitbox[3]) - obstacle.hitbox[1]))
                            vel_counter = 100
                            while diff != 0:
                                vel_counter -= vel_counter * 1 / 2
                                self.y -= -(1 / 20) * (1 / 150)
                                self.jump_velocity -= 1
                                diff = abs(int((self.hitbox[1] + self.hitbox[3]) - obstacle.hitbox[1]))
                                self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

                        if math.ceil(self.hitbox[1] + self.hitbox[3]) == obstacle.hitbox[1]:
                            is_landed = True
                            self.is_on_obstacle = True
                            self.jump_velocity = JUMP_VELOCITY
                            self.is_jump = False

                else:
                    self.y -= (self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                    self.jump_velocity -= 1
                    self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
        else:
            self.jump_velocity = JUMP_VELOCITY
            self.is_jump = False
