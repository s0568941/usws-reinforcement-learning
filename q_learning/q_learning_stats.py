#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Generates Graphical Statistics for Q Learning - Statistics are displayed after training is finished / the game is terminated by the user

import matplotlib.pyplot as plt
from matplotlib import style
import os
import pickle

style.use('ggplot')

EXPLORATION_RATE_DIR = 'data/exploration_rates.pickle'
REWARDS_DIR = 'data/rewards.pickle'
DISTANCE_DIR = 'data/distances.pickle'


def unpickle(path):
    data = None
    if os.path.isfile(path):
        with open(path, 'rb') as handle:
            data = pickle.load(handle)
    return data

def generate_stats():
    exploration_rate = unpickle(EXPLORATION_RATE_DIR)
    rewards = unpickle(REWARDS_DIR)
    distances = unpickle(DISTANCE_DIR)

    if rewards is not None:
        plt.plot(range(len(rewards)), rewards, 'g-')
        plt.title('Rewards per Episode')
        plt.ylabel('Rewards')
        plt.xlabel('Episode')
        plt.show()

    if distances is not None:
        plt.plot(range(len(distances)), distances, 'b-')
        plt.title('Distance per Episode')
        plt.ylabel('Distance')
        plt.xlabel('Episode')
        plt.show()

    if exploration_rate is not None and rewards is not None:
        plt.plot(exploration_rate, rewards, 'o-')
        plt.title('Rewards per Exploration Rate')
        plt.ylabel('Rewards')
        plt.xlabel('Exploration Rate')
        plt.show()

    if exploration_rate is not None and distances is not None:
        plt.plot(exploration_rate, distances, 'y-')
        plt.title('Distance per Exploration Rate')
        plt.ylabel('Distance')
        plt.xlabel('Exploration Rate')
        plt.show()
