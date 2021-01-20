#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Das ist die main File, welche das Game startet
import pygame

# Initialisiert alle notwendigen module fuer pygame
pygame.init()
# import additional pygame functions
import usws_jump_and_run_game.utils.pygame_functions as pygame_f
# import constants
from usws_jump_and_run_game.utils.constants import *
# Parameters from q learning
from q_learning.q_learning import *
import random
import numpy as np
import math
import os.path
# To save the Q Table
import pickle
from usws_jump_and_run_game.characters.player import Player
from usws_jump_and_run_game.environment.obstacles.platform import Platform
from usws_jump_and_run_game.environment.obstacles.spike import Spike
from usws_jump_and_run_game.characters.hyena import Hyena
from usws_jump_and_run_game.characters.scorpio import Scorpio
from usws_jump_and_run_game.characters.skull import Skull
from usws_jump_and_run_game.environment.obstacles.coin import Coin


class Game:
    def __init__(self):
        # Player initialisation
        self.player = Player(X_STARTING_POSITION, Y_STARTING_POSITION, 20, 40)
        self.clock = pygame.time.Clock()

        # LEVEL

        # Checkpoint 1 - Start of first Area
        self.scorpio1 = Scorpio(150, 620, 25, 40, 300)
        self.platform = Platform(350, 600, 80, 50)
        self.hyena1 = Hyena(500, 620, 25, 40, 800)
        self.platform2 = Platform(900, 580, 100, 70)
        self.spike = Spike(1000, 620, 80, 30)
        self.skull1 = Skull(1020, 440, 25, 25, 580)
        self.platform3 = Platform(1080, 580, 100, 70)

        # Checkpoint 2 - Start of Main Tree
        self.platform4 = Platform(1500, 560, 120, 90)
        self.scorpio2 = Scorpio(1500, 540, 25, 40, 1590)

        # small islands
        self.spike2 = Spike(1620, 620, 60, 30)
        self.platform5 = Platform(1680, 560, 60, 30)
        self.spike3 = Spike(1740, 620, 60, 30)
        self.platform6 = Platform(1800, 560, 60, 30)
        self.spike4 = Spike(1860, 620, 60, 30)
        # Main tree
        self.platform7 = Platform(1920, 560, 600, 30)
        self.hyena2 = Hyena(1920, 525, 25, 40, 2120)
        self.platform8 = Platform(2050, 480, 340, 30)
        self.spike5 = Spike(2125, 450, 50, 30)
        self.spike6 = Spike(2265, 450, 50, 30)
        self.platform9 = Platform(2115, 400, 210, 30)
        self.platform10 = Platform(2147, 320, 146, 80)
        self.platform11 = Platform(2180, 240, 80, 440)
        self.skull2 = Skull(2200, 100, 25, 25, 180)
        self.hyena3 = Hyena(2260, 525, 25, 40, 2460)
        # small islands
        self.spike7 = Spike(2520, 620, 60, 30)
        self.platform12 = Platform(2580, 560, 60, 30)
        self.spike8 = Spike(2640, 620, 60, 30)
        self.platform13 = Platform(2700, 560, 60, 30)
        self.spike9 = Spike(2755, 620, 60, 30)

        # Checkpoint 4 - Start of Skull section
        self.platform14 = Platform(2820, 560, 600, 100)
        self.skull3 = Skull(2850, 420, 25, 25, 520)
        self.spike10 = Spike(2950, 530, 50, 30)
        self.skull4 = Skull(3100, 450, 25, 25, 520)
        self.spike11 = Spike(3250, 530, 50, 30)
        self.skull5 = Skull(3350, 420, 25, 25, 520)

        # Checkpoint 4 - Start of animal section
        self.hyena4 = Hyena(3420, 620, 25, 40, 3780)
        self.spike12 = Spike(3820, 640, 60, 30)
        self.scorpio3 = Scorpio(3900, 620, 25, 40, 4100)

        # Checkpoint 5 - Start of last section
        self.platform15 = Platform(4200, 560, 30, 100)
        self.spike13 = Spike(4230, 640, 70, 30)
        self.platform16 = Platform(4300, 600, 30, 60)
        self.spike14 = Spike(4330, 640, 70, 30)
        self.platform17 = Platform(4400, 560, 30, 100)
        self.spike15 = Spike(4430, 640, 70, 30)
        self.platform18 = Platform(4500, 620, 30, 40)
        self.spike16 = Spike(4530, 640, 70, 30)
        self.platform19 = Platform(4600, 560, 30, 100)
        self.skull6 = Skull(4595, 400, 25, 25, 520)
        self.coin = Coin(4800, 590, 25, 25)

        # Arranging obstacles in Array
        self.obstacles = [self.platform, self.platform2, self.platform3, self.platform4, self.platform5, self.platform6,
                          self.platform7, self.platform8, self.platform9,
                          self.platform10, self.platform11, self.platform12, self.platform13, self.platform14,
                          self.platform15, self.platform16, self.platform17,
                          self.platform18, self.platform19, self.spike, self.spike2, self.spike3, self.spike4,
                          self.spike5, self.spike6, self.spike7, self.spike8, self.spike9, self.spike10,
                          self.spike11, self.spike12, self.spike13, self.spike14, self.spike15, self.spike16, self.coin]
        self.player.obstacles = self.obstacles

        # Arranging enemies in Array
        self.enemies = [self.scorpio1, self.scorpio2, self.scorpio3, self.hyena1, self.hyena2, self.hyena3, self.hyena4,
                        self.skull1, self.skull2, self.skull3, self.skull4,
                        self.skull5, self.skull6]

        # for debugging:
        self.counter = 0

        self.setup_screen()
        # Boolean: True = Spiel laeuft | False = Spiel Ende
        self.main_program_run = True
        self.startscreen_run = False
        self.version_1_run = False
        self.version_2_run = False
        self.ki_version_1_run = False
        self.ki_version_2_run = False
        self.game_over = False
        self.input_done = False

        # Start Screen setup
        self.title = pygame_f.makeLabel(SCREENTITLE, 60, 300, 230, "black", "Arial", "clear")
        self.start_style_1_text = pygame_f.makeLabel(START_GAME_STYLE_1, 35, 300, 300, "black", "Arial", "clear")
        self.start_style_2_text = pygame_f.makeLabel(START_GAME_STYLE_2, 35, 300, 350, "black", "Arial", "clear")
        self.start_ki_style_1_text = pygame_f.makeLabel(START_KI_STYLE_1, 35, 300, 400, "black", "Arial", "clear")
        self.start_ki_style_2_text = pygame_f.makeLabel(START_KI_STYLE_2, 35, 300, 450, "black", "Arial", "clear")
        self.end_game_text = pygame_f.makeLabel(END_GAME_TEXT, 35, 300, 500, "black", "Arial", "clear")
        self.nassim_text = pygame_f.makeLabel(NASSIM_TEXT, 25, 1100, 50, "black", "Arial", "clear")
        self.nico_text = pygame_f.makeLabel(NICO_TEXT, 25, 1100, 100, "black", "Arial", "clear")

        # Game Over Screen Setup
        self.go_title = pygame_f.makeLabel(GO_TITLE, 100, 430, 150, "black", "Arial", "clear")
        self.kill_text = pygame_f.makeLabel(KILL_TEXT, 40, 500, 300, "black", "Arial", "clear")
        self.return_text = pygame_f.makeLabel(RETURN_TEXT, 35, 350, 350, "black", "Arial", "clear")

        ### Q Learning ###
        self.exploration_rate = EXPLORATION_RATE
        # Track number of episodes for q learning
        self.current_episode = 0
        # Delta player - coin is the state
        self.state = None
        self.action = None
        # action space
        self.action_space = [MOVE_RIGHT, MOVE_LEFT, JUMP]
        self.action_space_v2 = [STAY, JUMP_V2]
        # Track number of steps per episode / game for q learning
        self.steps_per_episode = 0
        self.max_episodes_reached = self.ki_version_1_run and self.current_episode == NUMBER_EPISODES
        self.max_episodes_reached_v2 = self.ki_version_2_run and self.current_episode == NUMBER_EPISODES
        # Track rewards
        self.episode_rewards = []
        # Q Learning done?
        self.q_l_done = False
        self.rewards_current_episode = 0
        self.q_table = {}

    def reset(self):
        # Player initilisation
        self.player = Player(X_STARTING_POSITION, Y_STARTING_POSITION, 20, 40)
        self.clock = pygame.time.Clock()

        # LEVEL

        # Checkpoint 1 - Start of first Area
        self.scorpio1 = Scorpio(150, 620, 25, 40, 300)
        self.platform = Platform(350, 600, 80, 50)
        self.hyena1 = Hyena(500, 620, 25, 40, 800)
        self.platform2 = Platform(900, 580, 100, 70)
        self.spike = Spike(1000, 620, 80, 30)
        self.skull1 = Skull(1020, 440, 25, 25, 580)
        self.platform3 = Platform(1080, 580, 100, 70)

        # Checkpoint 2 - Start of Main Tree
        self.platform4 = Platform(1500, 560, 120, 90)
        self.scorpio2 = Scorpio(1500, 540, 25, 40, 1590)

        # small islands
        self.spike2 = Spike(1620, 620, 60, 30)
        self.platform5 = Platform(1680, 560, 60, 30)
        self.spike3 = Spike(1740, 620, 60, 30)
        self.platform6 = Platform(1800, 560, 60, 30)
        self.spike4 = Spike(1860, 620, 60, 30)
        # Main tree
        self.platform7 = Platform(1920, 560, 600, 30)
        self.hyena2 = Hyena(1920, 525, 25, 40, 2120)
        self.platform8 = Platform(2050, 480, 340, 30)
        self.spike5 = Spike(2125, 450, 50, 30)
        self.spike6 = Spike(2265, 450, 50, 30)
        self.platform9 = Platform(2115, 400, 210, 30)
        self.platform10 = Platform(2147, 320, 146, 80)
        self.platform11 = Platform(2180, 240, 80, 440)
        self.skull2 = Skull(2200, 100, 25, 25, 180)
        self.hyena3 = Hyena(2260, 525, 25, 40, 2460)
        # small islands
        self.spike7 = Spike(2520, 620, 60, 30)
        self.platform12 = Platform(2580, 560, 60, 30)
        self.spike8 = Spike(2640, 620, 60, 30)
        self.platform13 = Platform(2700, 560, 60, 30)
        self.spike9 = Spike(2755, 620, 60, 30)

        # Checkpoint 4 - Start of Skull section
        self.platform14 = Platform(2820, 560, 600, 100)
        self.skull3 = Skull(2850, 420, 25, 25, 520)
        self.spike10 = Spike(2950, 530, 50, 30)
        self.skull4 = Skull(3100, 450, 25, 25, 520)
        self.spike11 = Spike(3250, 530, 50, 30)
        self.skull5 = Skull(3350, 420, 25, 25, 520)

        # Checkpoint 4 - Start of animal section
        self.hyena4 = Hyena(3420, 620, 25, 40, 3780)
        self.spike12 = Spike(3820, 640, 60, 30)
        self.scorpio3 = Scorpio(3900, 620, 25, 40, 4100)

        # Checkpoint 5 - Start of last section
        self.platform15 = Platform(4200, 560, 30, 100)
        self.spike13 = Spike(4230, 640, 70, 30)
        self.platform16 = Platform(4300, 600, 30, 60)
        self.spike14 = Spike(4330, 640, 70, 30)
        self.platform17 = Platform(4400, 560, 30, 100)
        self.spike15 = Spike(4430, 640, 70, 30)
        self.platform18 = Platform(4500, 620, 30, 40)
        self.spike16 = Spike(4530, 640, 70, 30)
        self.platform19 = Platform(4600, 560, 30, 100)
        self.skull6 = Skull(4595, 400, 25, 25, 520)
        self.coin = Coin(4800, 590, 25, 25)

        # Arranging obstacles in Array
        self.obstacles = [self.platform, self.platform2, self.platform3, self.platform4, self.platform5, self.platform6,
                          self.platform7, self.platform8, self.platform9,
                          self.platform10, self.platform11, self.platform12, self.platform13, self.platform14,
                          self.platform15, self.platform16, self.platform17,
                          self.platform18, self.platform19, self.spike, self.spike2, self.spike3, self.spike4,
                          self.spike5, self.spike6, self.spike7, self.spike8, self.spike9, self.spike10,
                          self.spike11, self.spike12, self.spike13, self.spike14, self.spike15, self.spike16, self.coin]
        self.player.obstacles = self.obstacles

        # Arranging enemies in Array
        self.enemies = [self.scorpio1, self.scorpio2, self.scorpio3, self.hyena1, self.hyena2, self.hyena3, self.hyena4,
                        self.skull1, self.skull2, self.skull3, self.skull4,
                        self.skull5, self.skull6]

        # for debugging:
        self.counter = 0

        self.setup_screen()
        # Boolean: True = Spiel laeuft | False = Spiel Ende
        self.main_program_run = True
        self.startscreen_run = False
        self.version_1_run = False
        self.version_2_run = False
        self.game_over = False
        self.input_done = False

        # Start Screen setup
        self.title = pygame_f.makeLabel(SCREENTITLE, 60, 300, 230, "black", "Arial", "clear")
        self.start_style_1_text = pygame_f.makeLabel(START_GAME_STYLE_1, 35, 300, 300, "black", "Arial", "clear")
        self.start_style_2_text = pygame_f.makeLabel(START_GAME_STYLE_2, 35, 300, 350, "black", "Arial", "clear")
        self.start_ki_style_1_text = pygame_f.makeLabel(START_KI_STYLE_1, 35, 300, 400, "black", "Arial", "clear")
        self.start_ki_style_2_text = pygame_f.makeLabel(START_KI_STYLE_2, 35, 300, 450, "black", "Arial", "clear")
        self.end_game_text = pygame_f.makeLabel(END_GAME_TEXT, 35, 300, 500, "black", "Arial", "clear")
        self.nassim_text = pygame_f.makeLabel(NASSIM_TEXT, 25, 1100, 600, "black", "Arial", "clear")
        self.nico_text = pygame_f.makeLabel(NICO_TEXT, 25, 1100, 650, "black", "Arial", "clear")

        # Game Over Screen Setup
        self.go_title = pygame_f.makeLabel(GO_TITLE, 100, 430, 150, "black", "Arial", "clear")
        self.kill_text = pygame_f.makeLabel(KILL_TEXT, 40, 500, 300, "black", "Arial", "clear")
        self.return_text = pygame_f.makeLabel(RETURN_TEXT, 35, 350, 350, "black", "Arial", "clear")

        ### Q Learning ###
        self.steps_per_episode = 0
        self.rewards_current_episode = 0

        self.setup_screen()
        pygame_f.updateDisplay()

    #second level (if needed)
    def version_2(self):
        pass

    #second level reset (if needed)
    def version_2_reset(self):
        pass

    def dump(self, obj):
        for attr in dir(obj):
            print("obj.%s = %r" % (attr, getattr(obj, attr)))

    def setup_screen(self):
        # Setup screen and background
        pygame_f.screenSize(SCREEN_WIDTH, SCREEN_HEIGHT)
        pygame_f.setAutoUpdate(False)
        pygame_f.setBackgroundImage('environment/pictures/hills_bg_scaled2.png')
        pygame_f.pygame.display.set_caption('USWS Jump and Run')

    def redraw_game_window(self):
        # Aktualisiere das Fenster (background & player)
        self.player.draw(pygame_f.screen)
        for obstacle in self.obstacles:
            obstacle.draw(pygame_f.screen)
        for enemy in self.enemies:
            enemy.draw(pygame_f.screen)
        pygame_f.updateDisplay()

    def check_collision(self, player, enemy):
        global game_over
        # Q Learning
        if self.ki_version_1_run:
            if self.steps_per_episode > MAX_STEPS_PER_EPISODE or self.player.is_dead:
                self.game_over = True
                self.game_over_screen()
                self.episode_rewards.append(self.rewards_current_episode)
            if self.current_episode == NUMBER_EPISODES:
                self.main_program_run = False
                self.save_q_table()

        if self.ki_version_2_run:
            if self.steps_per_episode > MAX_STEPS_PER_EPISODE or self.player.is_dead:
                self.game_over = True
                self.game_over_screen()
                self.episode_rewards.append(self.rewards_current_episode)
            if self.current_episode == NUMBER_EPISODES:
                self.main_program_run = False
                self.save_q_table()

        if player.is_dead:
            if self.ki_version_1_run:
                self.q_learning(self.state, self.action)
            elif self.ki_version_2_run:
                self.q_learning_v2(self.state, self.action, self.action_space_v2)
            self.game_over = True
            self.game_over_screen()
        if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[
            1]:
            if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + \
                    enemy.hitbox[2]:
                if self.ki_version_1_run:
                    self.player.is_dead = True
                    self.q_learning(self.state, self.action)
                    self.game_over = True
                    self.game_over_screen()
                    return
                if self.ki_version_2_run:
                    self.player.is_dead = True
                    self.q_learning_v2(self.state, self.action, self.action_space_v2)
                    self.game_over = True
                    self.game_over_screen()
                    return
                game_over = True
                self.game_over_screen()
        else:
            game_over = False

    def get_distance_progress(self):
        global reward
        reward = 0
        if self.player.x > self.player.previous_x_q_learning:
            self.player.previous_x_q_learning = self.player.x
            reward += 50
        return reward

    def check_overcoming_obstacles(self):
        global reward
        reward = 0
        for obst in self.obstacles:
            if type(obst) is not Coin and self.player.static_x + PLAYER_HITBOX_PADDING_X > obst.x + obst.width + self.player.speed:
                if not obst.is_overcome and not self.player.is_dead:
                    obst.is_overcome = True
                    self.player.num_passed_obstacles += 1
                    if type(obst) is Platform:
                        reward += OVERCOME_PLATFORM_REWARD
                    else:
                        reward += OVERCOME_ENEMY_REWARD

        for enemy in self.enemies:
            if type(enemy) is not Coin and self.player.static_x + PLAYER_HITBOX_PADDING_X > enemy.x + enemy.width + self.player.speed:
                if not enemy.is_overcome and not self.player.is_dead:
                    enemy.is_overcome = True
                    self.player.num_passed_obstacles += 1
                    reward += OVERCOME_ENEMY_REWARD
                    return reward

        return reward

    def game_over_screen(self):
        global version_1_run
        global version_2_run
        self.clock.tick(27)

        pygame_f.showLabel(self.go_title)
        pygame_f.showLabel(self.kill_text)
        pygame_f.showLabel(self.return_text)
        pygame_f.updateDisplay()

        while True:
            # Did agent finish?
            self.max_episodes_reached = self.ki_version_1_run and self.current_episode == NUMBER_EPISODES
            if not self.max_episodes_reached and self.current_episode > 0:
                self.main_program_run = True
                self.version_1_run = False
                self.hide_game_over_screen()
                self.episode_rewards.append(self.rewards_current_episode)
                self.reset()
                return

            self.max_episodes_reached = self.ki_version_2_run and self.current_episode == NUMBER_EPISODES
            if not self.max_episodes_reached and self.current_episode > 0:
                self.main_program_run = True
                self.version_2_run = False
                self.hide_game_over_screen()
                self.episode_rewards.append(self.rewards_current_episode)
                self.reset()
                return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.main_program_run = False
                if event.type == pygame.KEYDOWN:
                    self.main_program_run = True
                    self.version_1_run = False
                    self.version_2_run = False
                    self.hide_game_over_screen()
                    self.reset()
                    return

    def hide_start_screen(self):
        pygame_f.hideLabel(self.title)
        pygame_f.hideLabel(self.start_style_1_text)
        pygame_f.hideLabel(self.start_style_2_text)
        pygame_f.hideLabel(self.start_ki_style_1_text)
        pygame_f.hideLabel(self.start_ki_style_2_text)
        pygame_f.hideLabel(self.end_game_text)
        pygame_f.hideLabel(self.nassim_text)
        pygame_f.hideLabel(self.nico_text)
        pygame_f.updateDisplay()

    def hide_game_over_screen(self):
        pygame_f.hideLabel(self.go_title)
        pygame_f.hideLabel(self.kill_text)
        pygame_f.hideLabel(self.return_text)

    def start_screen(self):
        self.clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.main_program_run = False
                self.save_q_table()

        pygame_f.showLabel(self.title)
        pygame_f.showLabel(self.start_style_1_text)
        pygame_f.showLabel(self.start_style_2_text)
        pygame_f.showLabel(self.start_ki_style_1_text)
        pygame_f.showLabel(self.start_ki_style_2_text)
        pygame_f.showLabel(self.end_game_text)
        pygame_f.showLabel(self.nassim_text)
        pygame_f.showLabel(self.nico_text)
        pygame_f.updateDisplay()

    def q_learning(self, state, action):
        self.steps_per_episode += 1

        new_state, reward, done, info = self.step(action)

        # Update q table
        if state not in self.q_table:
            self.q_table[state] = [0 for i in range(len(self.action_space))]
        if new_state not in self.q_table:
            self.q_table[new_state] = [0 for i in range(len(self.action_space))]

        self.q_table[state][action] = self.q_table[state][action] * (1 - LEARNING_RATE) + \
                                      LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(
            self.q_table[new_state]))

        self.state = new_state
        self.rewards_current_episode += reward

        if self.steps_per_episode % 20 == 0:
            print('------------------------------------')
            print('Step ', self.steps_per_episode)
            print('Episode', self.current_episode)
            print('self.exploration_rate', self.exploration_rate)
            print('Reward', reward)
            print('Rewards for episode', self.rewards_current_episode)
            print('Max Reward: ', max(self.episode_rewards) if len(self.episode_rewards) > 0 else 0)
            print('------------------------------------')

    def q_learning_v2(self, state, action, smaller_action_space):
        self.steps_per_episode += 1

        new_state, reward, done, info = self.step_v2(action)

        # Update q table
        if state not in self.q_table:
            self.q_table[state] = [0 for i in range(len(smaller_action_space))]
        if new_state not in self.q_table:
            self.q_table[new_state] = [0 for i in range(len(smaller_action_space))]

        self.q_table[state][action] = self.q_table[state][action] * (1 - LEARNING_RATE) + \
                                      LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(
            self.q_table[new_state]))

        self.state = new_state
        self.rewards_current_episode += reward

        if self.steps_per_episode % 20 == 0:
            print('------------------------------------')
            print('Step ', self.steps_per_episode)
            print('Episode', self.current_episode)
            print('self.exploration_rate', self.exploration_rate)
            print('Reward', reward)
            print('Rewards for episode', self.rewards_current_episode)
            print('Max Reward: ', max(self.episode_rewards) if len(self.episode_rewards) > 0 else 0)
            print('------------------------------------')

    def get_state(self):
        self.state = ((math.ceil(self.player.static_x - self.coin.x), math.ceil(self.player.y - self.coin.y)),)
        for obst in self.obstacles:
            if type(obst) is not Coin:
                self.state = self.state + (
                    (math.ceil(self.player.static_x - obst.x), math.ceil(self.player.y - obst.y)),)
        for enemy in self.enemies:
            self.state = self.state + ((math.ceil(self.player.static_x - enemy.x), math.ceil(self.player.y - enemy.y)),)
        return self.state

    def step(self, action):
        global reward, new_state, done, info
        reward = 0
        new_state = self.get_state()
        # Rewarding player for progressing further in the level
        reward += self.get_distance_progress()
        reward += self.check_overcoming_obstacles()
        if action == MOVE_RIGHT:
            reward += - MOVE_RIGHT_REWARD
        if action == MOVE_LEFT:
            reward += - MOVE_LEFT_REWARD
        if action == JUMP:
            reward += - JUMP_REWARD
        if self.player.is_dead:
            if self.player.num_passed_obstacles == 0:
                reward += - NO_OBSTACLES_PASSED_REWARD
            else:
                # the more obstacles are passed, the smaller the punishment
                reward += - (15 - self.player.num_passed_obstacles) * 4000
            reward += - DIE_REWARD
        if self.player.has_coin:
            reward += COIN_REWARD
        done = self.game_over
        info = self.player.has_coin
        return new_state, reward, done, info

    # for the constant running player version
    def step_v2(self, action):
        global reward, new_state, done, info
        reward = 0
        new_state = self.get_state()
        # Rewarding player for progressing further in the level
        reward += self.get_distance_progress()
        reward += self.check_overcoming_obstacles()
        if action == STAY:
            reward += - STAY_REWARD
        if action == JUMP_V2:
            reward += - JUMP_REWARD
        if self.player.is_dead:
            if self.player.num_passed_obstacles == 0:
                reward += - NO_OBSTACLES_PASSED_REWARD
            else:
                # the more obstacles are passed, the smaller the punishment
                reward += - (15 - self.player.num_passed_obstacles) * 4000
            reward += - DIE_REWARD
        if self.player.has_coin:
            reward += COIN_REWARD
        done = self.game_over
        info = self.player.has_coin
        return new_state, reward, done, info

    def decay_exploration_rate(self):
        # Exploration rate decay
        self.exploration_rate = MIN_EXPLORATION_RATE + (MAX_EXPLORATION_RATE - MIN_EXPLORATION_RATE) * \
                                np.exp(-EXPLORATION_DECAY_RATE * self.current_episode)

    def save_q_table(self):
        if self.q_table:
            with open('../q_learning/q_table.pickle', 'wb') as handle:
                pickle.dump(self.q_table, handle)

    def load_q_table(self):
        if not self.q_table:
            if os.path.isfile('../q_learning/q_table.pickle'):
                with open('../q_learning/q_table.pickle', 'rb') as handle:
                    self.q_table = pickle.load(handle)

    def play_game(self):
        # Hauptstartscreen immer true bei run
        while self.main_program_run:
            self.start_screen()
            keys = pygame.key.get_pressed()

            self.max_episodes_reached = self.ki_version_1_run and self.current_episode == NUMBER_EPISODES
            if not self.max_episodes_reached and self.ki_version_1_run:
                self.version_1_run = True
                self.ki_version_1_run = True
                self.current_episode += 1
                self.get_state()
                # Decay rate when training has already been running
                self.decay_exploration_rate()
            elif self.max_episodes_reached:
                self.main_program_run = False
                self.save_q_table()

            self.max_episodes_reached = self.ki_version_2_run and self.current_episode == NUMBER_EPISODES
            if not self.max_episodes_reached and self.ki_version_2_run:
                self.version_2_run = True
                self.ki_version_2_run = True
                self.current_episode += 1
                self.get_state()
                # Decay rate when training has already been running
                self.decay_exploration_rate()
            elif self.max_episodes_reached:
                self.main_program_run = False
                self.save_q_table()

            if keys[pygame.K_1]:
                self.version_1_run = True
            elif keys[pygame.K_a]:
                self.version_1_run = True
                self.ki_version_1_run = True
                self.current_episode += 1
                self.get_state()
                self.load_q_table()
            elif keys[pygame.K_2]:
                self.version_2_run = True
            elif keys[pygame.K_b]:
                self.version_2_run = True
                self.ki_version_2_run = True
                self.current_episode += 1
                self.get_state()
                self.load_q_table()

            # 1.version starten manuell
            while self.version_1_run:
                # erhöht die FPS-Anzahl um das Spiel fluessiger zu gestalten
                self.hide_start_screen()
                self.clock.tick(27)

                # prüft jeden enemy ob eine collision vorliegt
                for enemy in self.enemies:
                    self.check_collision(self.player, enemy)

                # Schaue nach ob eines der events das Spiel beenden moechte (Fensterkreuz)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.version_1_run = False
                        self.main_program_run = False
                        self.save_q_table()
                        # sys.exit() waere eine andere alternative
                if not self.game_over:
                    # Hole eine aktuelle Liste der Tasten, die gedrueckt wurden
                    keys = pygame.key.get_pressed() if not self.ki_version_1_run else None

                    ### Q Learning ###
                    state = self.state
                    # Exploration - Exploitation trade-off - set between 0 and 1 -> determines whether exploring or exploiting
                    exploration_rate_threshold = random.uniform(0, 1)
                    if exploration_rate_threshold > self.exploration_rate:
                        # exploit: choose action with highest q value for current state
                        if state not in self.q_table:
                            self.q_table[state] = [0 for i in range(len(self.action_space))]
                        action = np.argmax(self.q_table[state])
                    else:
                        # explore: choose an action randomly
                        action = random.choice(self.action_space)
                    self.action = action

                    # Bewege den Spieler auf Basis der gedrueckten Tasten mit der Geschwindigkeit des Spielers
                    # Pruefe auch ob Spieler durch die Bewegung noch im Screen bleibt
                    command_left = keys[pygame.K_LEFT] == 1 if not self.ki_version_1_run else action == MOVE_LEFT
                    command_right = keys[pygame.K_RIGHT] == 1 if not self.ki_version_1_run else action == MOVE_RIGHT
                    command_jump = keys[pygame.K_SPACE] == 1 if not self.ki_version_1_run else action == JUMP
                    if command_left and self.player.x > self.player.speed:
                        # Scrolling background is deactivated once player arrives at the center and proceeds to the left
                        if self.player.x > PLAYER_STATIC_X and not self.player.movement_blocked:
                            pygame_f.scrollBackground(self.player.speed, 0)
                            for obstacle in self.obstacles:
                                obstacle.move_right()
                            for enemy in self.enemies:
                                enemy.adapt_to_screen_right()
                        else:
                            pygame_f.scrollBackground(0, 0)
                        self.player.move_left()
                        self.player.is_obstacle_underneath_player()
                        self.player.is_player_underneath_obstacle()

                        if not self.player.is_jump:
                            self.player.left = True
                            self.player.right = False
                            self.player.idle_left = True
                            self.player.idle_right = False
                            self.player.last_dir = 'l'

                    elif command_right:
                        # Scrolling background is activated once player arrives at the center
                        if self.player.x > PLAYER_STATIC_X and not self.player.movement_blocked:
                            pygame_f.scrollBackground(-self.player.speed, 0)
                            for obstacle in self.obstacles:
                                obstacle.move_left()
                            for enemy in self.enemies:
                                enemy.adapt_to_screen_left()
                        else:
                            pygame_f.scrollBackground(0, 0)
                        self.player.move_right()
                        self.player.is_obstacle_underneath_player()
                        self.player.is_player_underneath_obstacle()

                        if not self.player.is_jump:
                            self.player.left = False
                            self.player.right = True
                            self.player.idle_left = False
                            self.player.idle_right = True
                            self.player.last_dir = 'r'
                    else:
                        pygame_f.scrollBackground(0, 0)
                        self.player.left = False
                        self.player.right = False

                    # Wenn der Spieler nicht springt, dann bewegt er sich normal mit der Geschwindigkeit
                    if not self.player.is_jump:
                        if command_jump:
                            pygame_f.scrollBackground(0, 0)
                            self.player.is_jump = True
                            self.player.left = False
                            self.player.right = False
                            self.player.walk_count = 0

                    # Wenn der Spieler springt, dann erfolgt das mithilfe einer quadratischen Formel
                    # https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
                    else:
                        self.player.jump()

                    if self.player.is_fall and not self.player.is_on_obstacle and self.player.y < Y_STARTING_POSITION and not self.player.is_colliding and not self.player.obstacle_underneath_player:
                        self.player.fall_from_obstacle()
                    if self.player.is_landing and self.player.is_player_underneath_obstacle():
                        self.player.fall_from_obstacle()
                    self.player.is_obstacle_underneath_player()
                    if self.player.obstacle_underneath_player and not self.player.is_on_obstacle and self.player.is_landing and not self.player.is_on_previous_obstacle:
                        self.player.land_on_obstacle()
                    if self.player.is_colliding and not self.player.is_landing:
                        self.player.collide_with_obstacle()
                    if self.player.is_landing and not self.player.is_jump:
                        self.player.land_on_obstacle()
                        if self.player.y > Y_STARTING_POSITION:
                            self.player.is_landing = False
                    if self.player.is_falling_to_ground:
                        if self.player.y > Y_STARTING_POSITION:
                            self.player.is_falling_to_ground = False

                    if not self.player.is_jump and not self.player.is_landing and not self.player.is_colliding:
                        self.player.check_for_vertical_obstacles()
                        self.player.is_player_on_obstacle()
                        if self.player.y != Y_STARTING_POSITION and not self.player.is_on_obstacle and not self.player.is_falling_to_ground:
                            self.player.y = Y_STARTING_POSITION
                            self.player.hitbox = (
                                self.player.static_x + 30, self.player.y + 15, self.player.height, self.player.width)

                    self.player.is_obstacle_underneath_player()
                    self.player.check_for_vertical_obstacles()

                    # for debugging:
                    if self.counter % 1000 == 0:
                        self.dump(self.player)
                    self.counter += 1

                    self.redraw_game_window()


                    player_starts_jump = self.player.is_jump and self.player.jump_velocity == JUMP_VELOCITY and action == JUMP
                    if not player_starts_jump:
                        self.steps_per_episode += 1

                        new_state, reward, done, info = self.step(action)

                        # Update q table
                        if state not in self.q_table:
                            self.q_table[state] = [0 for i in range(len(self.action_space))]
                        if new_state not in self.q_table:
                            self.q_table[new_state] = [0 for i in range(len(self.action_space))]

                        self.q_table[state][action] = self.q_table[state][action] * (1 - LEARNING_RATE) + \
                                                           LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(
                            self.q_table[new_state]))

                        self.state = new_state
                        self.rewards_current_episode += reward

                        if self.steps_per_episode % 20 == 0:
                            print('------------------------------------')
                            print('Step ', self.steps_per_episode)
                            print('Episode', self.current_episode)
                            print('self.exploration_rate', self.exploration_rate)
                            print('Reward', reward)
                            print('Rewards for episode', self.rewards_current_episode)
                            print('Max Reward: ', max(self.episode_rewards) if len(self.episode_rewards) > 0 else 0)
                            print('Last Reward: ', self.episode_rewards[len(self.episode_rewards) - 1] if len(self.episode_rewards) > 0 else 'None')
                            print('------------------------------------')




            # 2. version starten manuell - player is constantly running
            while self.version_2_run:
                # erhöht die FPS-Anzahl um das Spiel fluessiger zu gestalten
                self.hide_start_screen()
                self.clock.tick(27)

                # prüft jeden enemy ob eine collision vorliegt
                for enemy in self.enemies:
                    self.check_collision(self.player, enemy)

                # Schaue nach ob eines der events das Spiel beenden moechte (Fensterkreuz)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.version_2_run = False
                        self.main_program_run = False
                        self.save_q_table()
                        # sys.exit() waere eine andere alternative
                if not self.game_over:
                    # Hole eine aktuelle Liste der Tasten, die gedrueckt wurden
                    keys = pygame.key.get_pressed() if not self.ki_version_2_run else None

                    ### Q Learning ###
                    state = self.state
                    smaller_action_space = [STAY, JUMP_V2]
                    # Exploration - Exploitation trade-off - set between 0 and 1 -> determines whether exploring or exploiting
                    exploration_rate_threshold = random.uniform(0, 1)
                    if exploration_rate_threshold > self.exploration_rate:
                        # exploit: choose action with highest q value for current state
                        if state not in self.q_table:
                            self.q_table[state] = [0 for i in range(len(smaller_action_space))]
                        action = np.argmax(self.q_table[state])
                    else:
                        # explore: choose an action randomly
                        action = random.choice(smaller_action_space)
                    self.action = action

                    # Bewege den Spieler auf Basis der gedrueckten Tasten mit der Geschwindigkeit des Spielers
                    # Pruefe auch ob Spieler durch die Bewegung noch im Screen bleibt
                    command_jump = keys[pygame.K_SPACE] == 1 if not self.ki_version_2_run else action == JUMP_V2

                        # Scrolling background is activated once player arrives at the center
                    if self.player.x > PLAYER_STATIC_X and not self.player.movement_blocked:
                        pygame_f.scrollBackground(-self.player.speed, 0)
                        for obstacle in self.obstacles:
                            obstacle.move_left()
                        for enemy in self.enemies:
                            enemy.adapt_to_screen_left()
                    else:
                        pygame_f.scrollBackground(0, 0)
                    self.player.move_right()
                    self.player.is_obstacle_underneath_player()
                    self.player.is_player_underneath_obstacle()

                    if not self.player.is_jump:
                        self.player.right = True
                        self.player.idle_right = True
                        self.player.last_dir = 'r'


                    # Wenn der Spieler nicht springt, dann bewegt er sich normal mit der Geschwindigkeit
                    if not self.player.is_jump:
                        if command_jump:
                            pygame_f.scrollBackground(0, 0)
                            self.player.is_jump = True
                            self.player.right = False
                            self.player.walk_count = 0

                    # Wenn der Spieler springt, dann erfolgt das mithilfe einer quadratischen Formel
                    # https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
                    else:
                        self.player.jump()

                    if self.player.is_fall and not self.player.is_on_obstacle and self.player.y < Y_STARTING_POSITION and not self.player.is_colliding and not self.player.obstacle_underneath_player:
                        self.player.fall_from_obstacle()
                    if self.player.is_landing and self.player.is_player_underneath_obstacle():
                        self.player.fall_from_obstacle()
                    self.player.is_obstacle_underneath_player()
                    if self.player.obstacle_underneath_player and not self.player.is_on_obstacle and self.player.is_landing and not self.player.is_on_previous_obstacle:
                        self.player.land_on_obstacle()
                    if self.player.is_colliding and not self.player.is_landing:
                        self.player.collide_with_obstacle()
                    if self.player.is_landing and not self.player.is_jump:
                        self.player.land_on_obstacle()
                        if self.player.y > Y_STARTING_POSITION:
                            self.player.is_landing = False
                    if self.player.is_falling_to_ground:
                        if self.player.y > Y_STARTING_POSITION:
                            self.player.is_falling_to_ground = False

                    if not self.player.is_jump and not self.player.is_landing and not self.player.is_colliding:
                        self.player.check_for_vertical_obstacles()
                        self.player.is_player_on_obstacle()
                        if self.player.y != Y_STARTING_POSITION and not self.player.is_on_obstacle and not self.player.is_falling_to_ground:
                            self.player.y = Y_STARTING_POSITION
                            self.player.hitbox = (
                                self.player.static_x + 30, self.player.y + 15, self.player.height, self.player.width)

                    self.player.is_obstacle_underneath_player()
                    self.player.check_for_vertical_obstacles()

                    self.redraw_game_window()

                    player_starts_jump = self.player.is_jump and self.player.jump_velocity == JUMP_VELOCITY and action == JUMP
                    if not player_starts_jump:
                        self.steps_per_episode += 1

                        new_state, reward, done, info = self.step_v2(action)

                        # Update q table
                        if state not in self.q_table:
                            self.q_table[state] = [0 for i in range(len(smaller_action_space))]
                        if new_state not in self.q_table:
                            self.q_table[new_state] = [0 for i in range(len(smaller_action_space))]

                        self.q_table[state][action] = self.q_table[state][action] * (1 - LEARNING_RATE) + \
                                                           LEARNING_RATE * (reward + DISCOUNT_RATE * np.max(
                            self.q_table[new_state]))

                        self.state = new_state
                        self.rewards_current_episode += reward

                        if self.steps_per_episode % 20 == 0:
                            print('------------------------------------')
                            print('Step ', self.steps_per_episode)
                            print('Episode', self.current_episode)
                            print('self.exploration_rate', self.exploration_rate)
                            print('Reward', reward)
                            print('Rewards for episode', self.rewards_current_episode)
                            print('Max Reward: ', max(self.episode_rewards) if len(self.episode_rewards) > 0 else 0)
                            print('Last Reward: ', self.episode_rewards[len(self.episode_rewards) - 1] if len(self.episode_rewards) > 0 else 'None')
                            print('------------------------------------')

        pygame.quit()


game = Game()
game.play_game()
