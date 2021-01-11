#!/usr/bin/env python3
# -*- coding: utf-8 -*-

NUMBER_EPISODES = 25000
MAX_STEPS_PER_EPISODE = 500 #(kann man machen?!)
MOVE_REWARD = 1
JUMP_REWARD = 10
DIE_REWARD = 300
COIN_REWARD = 50

# ALPHA:
LEARNING_RATE = 0.1
# GAMMA:
DISCOUNT_RATE = 0.99

# EPSILON:
EXPLORATION_RATE = 1
MAX_EXPLORATION_RATE = 1
MIN_EXPLORATION_RATE = 0.01
EXPLORATION_DECAY_RATE = 0.01


# setup the q table
# action_space_size = env.action_space.n
# state_space_size = env.observation_space.n

# q_table = np.zeros((state_space_size, action_space_size))

# Q-Learning algorithm

# epsiode_rewards = [ ]
# for episode in range(NUMBER_EPISODES):
# start new game
# state = env.reset()

# done = False
# rewards_current_episode = 0

for step in range(MAX_STEPS_PER_EPISODE):
    # Exploration - Exploitation trade-off - set between 0 and 1 -> determines whether exploring or exploiting
    exploration_rate_threshold = random.uniform(0, 1)
    if exploration_rate_threshold > exploration_rate:
        # exploit: choose action with highest q value for current state
        action = np.argmax(q_table[state, :]
        else:
        # explore: sample an action randomly
        action = env.action_space.sample()

        new_state, reward, done, info = env.step(action)

        # Update q table
        q_table[state, action] = q_table[state, action] * (1 - LEARNING_RATE) + LEARNING_RATE * (
                    reward + DISCOUNT_RATE * np.max(q_table[new_state, : ])

        state = new_state
        rewards_current_episode += reward

        if done:
            break

exploration_rate = MIN_EXPLORATION_RATE + (MAX_EXPLORATION_RATE - MIN_EXPLORATION_RATE) * np.exp(
    - EXPLRATION_DECAY_RATE * episode)

episode_rewards.append(rewards_current_episode)