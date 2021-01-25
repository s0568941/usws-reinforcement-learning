#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Constants

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1380, 690
FRAME_RATE = 27

# Player Constants
JUMP_VELOCITY = 10
RUN_SPEED = 5
X_STARTING_POSITION = 10
Y_STARTING_POSITION = 595
PLAYER_STATIC_X = (SCREEN_WIDTH // 2)
PLAYER_HITBOX_PADDING_X = 30
PLAYER_HITBOX_PADDING_Y = 15
END_OF_SCREEN = 4850


# Start Screen Constants
SCREENTITLE = "USWS JUMP AND RUN PROJECT"
NASSIM_TEXT = "Nassim Uhrmann, s0568941 "
NICO_TEXT = "Nico Schultze, s0569571"
START_GAME_STYLE_1 = "Press 1 to play style 1 (free movement)."
START_GAME_STYLE_2 = "Press 2 to play style 2 (continuous running movement)."
START_KI_STYLE_1 = "Press A to let the AI play version 1."
START_KI_STYLE_2 = "Press B to let the AI play version 2."
END_GAME_TEXT = "Press ESC to exit the game."

# Game Over Screen Constants
GO_TITLE = "GAME OVER"
GO_WIN_TITLE = "WINNER"
KILL_TEXT = "- You died a tragic death -"
WIN_TEXT = "- You collected a rare US Liberty Gold coin -"
RETURN_TEXT = "Press the SPACEBAR button to return to the startscreen."

# Directories for Statistics
Q_TABLE_DIR = '../q_learning/q_table.pickle'
Q_TABLE_V2_DIR = '../q_learning/q_table_v2.pickle'
REWARDS_DIR = '../q_learning/data/rewards.pickle'
DISTANCE_DIR = '../q_learning/data/distances.pickle'
EXPLORATION_RATE_DIR = '../q_learning/data/exploration_rates.pickle'

