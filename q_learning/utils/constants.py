#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Constants and Parameters for Q Learning

# Control Player
# Version 1 - Player controls direction and jumps
MOVE_RIGHT = 0
MOVE_LEFT = 1
JUMP = 2
# Version 2 - continuously running
STAY = 0
JUMP_V2 = 1

# Q-Learning parameters which influence training length and results
# By changing the parameters, the agent's performance may improve or worsen
NUMBER_EPISODES = 25000
MAX_STEPS_PER_EPISODE = 15000
MOVE_RIGHT_REWARD = - 5
MOVE_LEFT_REWARD = 100
JUMP_REWARD = 500
DIE_REWARD = 50000
COIN_REWARD = 5000
OVERCOME_ENEMY_REWARD = 2000
OVERCOME_PLATFORM_REWARD = 1500
NO_OBSTACLES_PASSED_REWARD = 800000
# Version 2
STAY_REWARD = - 5


# ALPHA:
# the higher alpha, the quicker new q values are adopted
LEARNING_RATE = 0.5
# GAMMA:
DISCOUNT_RATE = 0.99

# EPSILON:
# the higher epsilon, the more likely it is that the agent takes random actions
EXPLORATION_RATE = 1
MAX_EXPLORATION_RATE = 1
MIN_EXPLORATION_RATE = 0.01
EXPLORATION_DECAY_RATE = 0.001
