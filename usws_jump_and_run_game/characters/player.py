#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import math

from usws_jump_and_run_game.environment.obstacles.platform import Platform
from usws_jump_and_run_game.environment.obstacles.spike import Spike

pygame.init()

from usws_jump_and_run_game.utils.constants import *

# Array mit Bildern des Characters
walk_right_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/right1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/right2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/right3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/right4.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/right5.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/right6.png'), (int(1.6 * 50), int(1.6 * 37)))]

walk_left_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/left1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/left2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/left3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/left4.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/left5.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/run/left6.png'), (int(1.6 * 50), int(1.6 * 37)))]

jump_right_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpR1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpR2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpR3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpR4.png'), (int(1.6 * 50), int(1.6 * 37)))]

jump_left_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpL1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpL2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpL3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/jump/jumpL4.png'), (int(1.6 * 50), int(1.6 * 37)))]

idle_right_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/idle/idleR1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/idle/idleR2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/idle/idleR3.png'), (int(1.6 * 50), int(1.6 * 37)))]

idle_left_p = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/idle/idleL1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/idle/idleL2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/idle/idleL3.png'), (int(1.6 * 50), int(1.6 * 37)))]

dead_img = [
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R1.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R2.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R3.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R4.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R5.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R6.png'), (int(1.6 * 50), int(1.6 * 37))),
    pygame.transform.scale(pygame.image.load('characters/pictures/player/die/die_R7.png'), (int(1.6 * 50), int(1.6 * 37)))]




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
        self.dead_count = 0
        self.last_dir = ''
        self.hitbox = (self.x + PLAYER_HITBOX_PADDING_X, self.y + PLAYER_HITBOX_PADDING_Y, self.height, self.width)
        self.is_on_obstacle = False
        self.is_on_previous_obstacle = False
        self.obstacles = []
        self.movement_blocked = False
        self.fall_vel = 0
        self.is_fall = False
        self.is_falling_to_ground = False
        self.obstacle_underneath_player = False
        self.is_landing = False
        self.index_below_obstacle = None
        self.player_underneath_obstacle = False
        self.is_colliding = False
        self.index_above_obstacle = None
        self.is_dead = False

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

            self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
            self.check_for_vertical_obstacles()
            self.is_obstacle_underneath_player()
            if not self.is_on_obstacle and not self.is_colliding:
                self.fall_from_obstacle()

    def move_left(self):
        self.check_for_horizontal_obstacles(right=False)
        if not self.movement_blocked:
            self.x -= self.speed
            if self.x <= PLAYER_STATIC_X:
                self.static_x = self.x

            self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
            self.check_for_vertical_obstacles()
            self.is_obstacle_underneath_player()
            if not self.is_on_obstacle and not self.is_colliding:
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
            obstacle_bottom = obstacle_y + obstacle.hitbox[3]
            obstacle_on_same_level = char_feet_y >= obstacle_y and char_feet_y >= obstacle_bottom > self.hitbox[1]
            if right:
                if obstacle_x <= next_x_coords_right_side <= obstacle_total_width \
                        and obstacle_on_same_level:
                    if type(obstacle) is Spike:
                        self.is_dead = True
                        return self.movement_blocked
                    else:
                        self.movement_blocked = True
                        return self.movement_blocked
            else:
                if obstacle_total_width >= next_x_coords_left_side >= obstacle_x \
                        and obstacle_on_same_level:
                    if type(obstacle) is Spike:
                        self.is_dead = True
                        return self.movement_blocked
                    else:
                        self.movement_blocked = True
                        return self.movement_blocked

        self.movement_blocked = False
        return self.movement_blocked

    # check if player is on obstacle
    def check_for_vertical_obstacles(self, is_on_obstacle=None):
        global moving_hitbox_x, moving_hitbox_y
        for idx, obstacle in enumerate(self.obstacles):
            moving_hitbox_x = self.static_x + PLAYER_HITBOX_PADDING_X
            moving_hitbox_y = self.y + PLAYER_HITBOX_PADDING_Y
            # if players feet align with surface of obstacle:
            is_on_obst = is_on_obstacle if is_on_obstacle is not None else self.is_on_obstacle
            is_on_obst = True if type(obstacle) is Spike else is_on_obst
            if math.ceil(moving_hitbox_y + self.hitbox[3]) == obstacle.y or is_on_obst:
                obstacle_right_edge = obstacle.x + obstacle.hitbox[2]
                player_is_between_platform_edges = obstacle.x <= moving_hitbox_x < obstacle_right_edge \
                                                   or obstacle.x <= (moving_hitbox_x +
                                                                     self.hitbox[2]) <= obstacle_right_edge
                if player_is_between_platform_edges:
                    if type(obstacle) is Spike:
                        char_feet_y = math.ceil(self.y + PLAYER_HITBOX_PADDING_Y + self.hitbox[3])
                        obstacle_bottom = obstacle.y + obstacle.hitbox[3]
                        obstacle_on_same_level = char_feet_y >= obstacle.y and obstacle_bottom > self.y + PLAYER_HITBOX_PADDING_Y
                        if obstacle_on_same_level:
                            self.is_dead = True
                            self.movement_blocked = True
                            self.is_on_obstacle = False
                            return self.is_on_obstacle
                        else:
                            self.is_on_obstacle = False
                            self.is_fall = False
                    else:
                        self.is_on_obstacle = True
                        self.is_fall = False
                    return self.is_on_obstacle
                elif idx != len(self.obstacles) - 1:
                    continue

        self.is_on_obstacle = False
        self.is_fall = True
        return False

    def is_player_on_obstacle(self):
        self.check_for_vertical_obstacles(False)

    # player falls from obstacle as soon as he leaves the edge of the surface
    def fall_from_obstacle(self):
        if self.y < Y_STARTING_POSITION and not self.is_jump:
            self.is_fall = True
            self.is_obstacle_underneath_player()
            if self.obstacle_underneath_player and self.index_below_obstacle is not None:
                obstacle = self.obstacles[self.index_below_obstacle]
                char_feet_y = self.hitbox[1] + self.hitbox[3]
                obstacle_y = obstacle.y

                distance_to_obstacle = abs(int(obstacle_y - char_feet_y))
                self.fall_vel = math.sqrt(distance_to_obstacle)
                self.y -= -(self.fall_vel * abs(self.fall_vel)) * (1 / 2)
                self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

                player_is_on_obstacle = math.ceil(self.hitbox[1] + self.hitbox[3]) == obstacle_y
                if player_is_on_obstacle:
                    self.obstacle_underneath_player = False
                    self.is_on_obstacle = True
                    self.jump_velocity = JUMP_VELOCITY
                    self.is_jump = False
                    self.is_landing = False
                    self.is_fall = False

            else:
                self.is_falling_to_ground = True
                distance_to_ground = abs(int(Y_STARTING_POSITION - self.y))
                self.fall_vel = math.sqrt(distance_to_ground)
                self.y -= -(self.fall_vel * abs(self.fall_vel)) * (1 / 4)
                self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

                if math.ceil(self.y) == Y_STARTING_POSITION:
                    self.y = math.ceil(self.y)
                    self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
                    self.is_on_obstacle = False
                    self.is_landing = False
                    self.jump_velocity = JUMP_VELOCITY
                    self.is_jump = False
                    self.is_fall = False
                    self.is_falling_to_ground = False
                    self.check_for_vertical_obstacles(False)
                elif math.ceil(self.y) > Y_STARTING_POSITION:
                    self.is_falling_to_ground = False

            self.is_player_on_obstacle()



    def is_obstacle_underneath_player(self):
        global obstacle_underneath_player
        for idx, obstacle in enumerate(self.obstacles):
            char_feet_y = self.hitbox[1] + self.hitbox[3]
            char_left_edge_hitbox_x = self.static_x + PLAYER_HITBOX_PADDING_X + 15
            char_right_hitbox_x = char_left_edge_hitbox_x + self.hitbox[2] - 30
            obstacle_y = obstacle.y
            obstacle_left_edge_x = obstacle.x
            obstacle_right_edge_x = obstacle_left_edge_x + obstacle.hitbox[2]

            obstacle_underneath_player = obstacle_y >= char_feet_y \
                                         and char_left_edge_hitbox_x >= obstacle_left_edge_x \
                                         and char_right_hitbox_x <= obstacle_right_edge_x

            is_landing_or_landed = self.jump_velocity < 0 or not self.is_jump
            if obstacle_underneath_player and is_landing_or_landed and type(obstacle) is Platform:
                self.obstacle_underneath_player = obstacle_underneath_player
                if self.index_below_obstacle is not None:
                    if self.index_below_obstacle == idx and self.is_on_obstacle:
                        self.is_on_previous_obstacle = True
                    else:
                        self.index_below_obstacle = idx
                        self.is_on_previous_obstacle = False
                else:
                    self.index_below_obstacle = idx

                return obstacle_underneath_player
            elif idx != len(self.obstacles) - 1:
                continue  # check the other obstacles
            elif idx == len(self.obstacles) - 1 and self.y != Y_STARTING_POSITION:
                # if no obstacle underneath player and player is not on the ground: player falls
                self.is_fall = True
                self.obstacle_underneath_player = False
                self.index_below_obstacle = None
            elif idx == len(self.obstacles) - 1:
                self.obstacle_underneath_player = False
                self.index_below_obstacle = None

        return obstacle_underneath_player

    def is_player_underneath_obstacle(self):
        global player_underneath_obstacle
        for idx, obstacle in enumerate(self.obstacles):
            char_left_edge_hitbox_x = self.static_x + PLAYER_HITBOX_PADDING_X + 15
            char_right_hitbox_x = char_left_edge_hitbox_x + self.hitbox[2] - 30
            char_head = self.hitbox[1]
            obstacle_y = obstacle.y
            obstacle_left_edge_x = obstacle.x
            obstacle_right_edge_x = obstacle_left_edge_x + obstacle.hitbox[2]
            obstacle_bottom = obstacle_y + obstacle.hitbox[3]

            player_underneath_obstacle = char_left_edge_hitbox_x >= obstacle_left_edge_x \
                                         and char_right_hitbox_x <= obstacle_right_edge_x \
                                         and self.jump_velocity > 0 \
                                         and obstacle_bottom <= char_head

            underneath_obstacle = char_left_edge_hitbox_x >= obstacle_left_edge_x \
                                  and char_right_hitbox_x <= obstacle_right_edge_x \
                                  and obstacle_bottom <= char_head

            if not underneath_obstacle and idx == len(self.obstacles) - 1:
                self.is_colliding = False

            if player_underneath_obstacle:
                self.player_underneath_obstacle = player_underneath_obstacle
                self.index_above_obstacle = idx
                return player_underneath_obstacle
            elif idx != len(self.obstacles) - 1:
                continue  # check the other obstacles
            elif idx == len(self.obstacles) - 1:
                self.player_underneath_obstacle = False
                self.index_above_obstacle = None

        return player_underneath_obstacle

    def collide_with_obstacle(self):
        if self.index_above_obstacle is not None:
            self.is_jump = False
            self.is_colliding = True
            obstacle = self.obstacles[self.index_above_obstacle]
            char_head = self.hitbox[1]
            obstacle_y = obstacle.y
            obstacle_bottom = obstacle_y + obstacle.hitbox[3]

            jump_distance = (self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
            char_head_nxt_loc = char_head - jump_distance
            if char_head_nxt_loc < (obstacle_bottom + 8):
                # jump to the obstacle
                distance_to_obstacle = abs(int(char_head - (obstacle_bottom + 8)))
                if math.ceil(distance_to_obstacle) > 0:
                    self.fall_vel = math.sqrt(distance_to_obstacle)
                    exceleration = (self.fall_vel * abs(self.fall_vel)) * (1 / 2)
                    char_head_nxt_loc = (self.y + PLAYER_HITBOX_PADDING_Y - exceleration)
                    next_distance = char_head_nxt_loc - (obstacle_bottom + 8)
                    if next_distance < distance_to_obstacle \
                            and (self.hitbox[1] - exceleration) >= (obstacle_bottom + 8):
                        self.y -= (self.fall_vel * abs(self.fall_vel)) * (1 / 2)
                    else:
                        self.y -= -(self.fall_vel * abs(self.fall_vel)) * (1 / 2)
                    self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

                distance_to_obstacle = abs(int(self.hitbox[1] - (obstacle_bottom + 8)))
                if math.ceil(distance_to_obstacle) == 0:
                    # deactivate the jump
                    self.jump_velocity = -1
                    self.is_obstacle_underneath_player()
                    self.is_colliding = False
                    self.is_jump = False

                    if self.obstacle_underneath_player:
                        self.land_on_obstacle()
                    else:
                        self.fall_from_obstacle()
            else:
                self.y -= (self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                self.jump_velocity -= 1
                self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

    def land_on_obstacle(self):
        if self.index_below_obstacle is not None:
            self.is_landing = True
            self.is_jump = False
            obstacle = self.obstacles[self.index_below_obstacle]
            if type(obstacle) is Spike:
                self.is_landing = False
                self.obstacle_underneath_player = False
                return
            char_feet_y = self.hitbox[1] + self.hitbox[3]
            obstacle_y = obstacle.y

            distance_to_obstacle = abs(int(obstacle_y - char_feet_y))
            self.fall_vel = math.sqrt(distance_to_obstacle)
            exceleration = (self.fall_vel * abs(self.fall_vel)) * (1 / 2)
            char_feet_nxt_loc = (self.y + PLAYER_HITBOX_PADDING_Y + self.hitbox[3] - exceleration)
            next_distance = obstacle_y - char_feet_nxt_loc
            if next_distance < distance_to_obstacle \
                    and (self.hitbox[1] + self.hitbox[3] - exceleration) <= (obstacle_y):
                self.y -= (self.fall_vel * abs(self.fall_vel)) * (1 / 2)
            else:
                self.y -= -(self.fall_vel * abs(self.fall_vel)) * (1 / 2)
            self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)

            player_is_on_obstacle = math.ceil(self.hitbox[1] + self.hitbox[3]) == obstacle_y
            if player_is_on_obstacle:
                self.obstacle_underneath_player = False
                self.is_landing = False
                self.is_on_obstacle = True
                self.jump_velocity = JUMP_VELOCITY
                self.is_jump = False

    def jump(self):
        if self.jump_velocity >= -JUMP_VELOCITY:
            self.is_player_underneath_obstacle()
            if self.player_underneath_obstacle:
                self.collide_with_obstacle()

            self.is_obstacle_underneath_player()
            if self.obstacle_underneath_player and not self.is_on_previous_obstacle:
                self.land_on_obstacle()

            elif not self.obstacle_underneath_player and not self.player_underneath_obstacle or self.is_on_previous_obstacle:
                self.y -= (self.jump_velocity * abs(self.jump_velocity)) * (1 / 2)
                self.jump_velocity -= 1
                self.hitbox = (self.static_x + 30, self.y + 15, self.height, self.width)
        else:
            self.jump_velocity = JUMP_VELOCITY
            self.is_jump = False

    def reset_player(self):
        self.x = X_STARTING_POSITION
        self.y = Y_STARTING_POSITION
