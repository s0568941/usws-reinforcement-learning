# usws-reinforcement-learning

## Start the Game
To start the game, the following modules need to be installed: 
<br /><br />
`pygame` 
- `pip install pygame`
<br />
or, if multiple different versions of python are installed:
<br />
- `pip3 install pygame`
<br />

`pickle` - is used to save data to train the agent 
- `pip install pickle`
<br />
or, if multiple different versions of python are installed:
<br />
- `pip3 install pickle`
<br />


After the modules have been installed;
run `usws_jump_and_run_game/main.py`, which should open the game menu.
<br />
From here you can choose to play the game on your own, or to train an agent to play the game.

## Increasing the Frame Rate for Training
To accelerate the training process, increase the constant `FRAME_RATE` in 
`usws_jump_and_run_game/utils/constants.py` 
#####Do not forget to set it back to around 27 - 30 FPS if you want to let a human play the game


## Saving Data From Training
Data is saved as a `*.pickle`, which is why the `pickle` module needs to be installed. <br />

The Q-Table is automatically saved in `usws-reinforcement-learning/q_learning/q_table.pickle`.
Each time you start to train the agent, this file will be used as a Q-Table (if it exists; 
otherwise it will initialise a new one). If you want to start with an empty Q-Table, you need to
delete the existing `q_table.pickle` - or rename it. <br />
 
Statistics data is saved as a `*.pickle` in `usws-reinforcement-learning/q_learning/data`.<br />
If you want to collect data from multiple trainings, make sure to rename the files as they otherwise
will be overwritten (`q_learning/q_learning_stats.py` contains the constants at the top of the file
which indicate where the data will be saved).

Please note, that when you switch between the two training versions, you should move your saved `.pickle`
data or rename the files, because otherwise they get overwritten or, in case of the Q Table, you will
get invalid results.

## Create Graphs From Saved Data
If you have saved data from training as a `*.pickle` (data is being saved and displayed automatically
after training finishes or after you click on the close button of the game window), you can 
view it by adjusting the path for the data at the top of the `q_learning/q_learning_stats.py` script and
then run the same file `q_learning/q_learning_stats.py` and its method `generate_stats()`.  

## Deactivate Exploration
After the agent has been trained properly and you have saved the `q_taböe.pickle`,
you can let the agent take actions only based on what he learned. <br />
This means that he will not take any random actions.<br />
To do this, set the `train_agent` flag at the very beginning of the
`usws_jump_and_run_game/main.py` file to `False`.
#####Do not forget to set it back to `True` once you want the agent to properly train again.

## Download Presentation Slides
The size of the slides of our presentation is too large which is why we uplaoded them here:
https://www.transfernow.net/wk70uH012021

## Sources
These are the sources we have used to develop the game 
and to implement the Q-Learning algorithm:

Q-Learning Algorithm:
<br />
- https://pythonprogramming.net/q-learning-reinforcement-learning-python-tutorial/
- https://www.tensorflow.org/agents/tutorials/0_intro_rl
- https://towardsdatascience.com/a-beginners-guide-to-q-learning-c3e2a30a653c
- https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56https://towardsdatascience.com/simple-reinforcement-learning-q-learning-fcddc4b6fe56

Game Design and Animations:
- Player: https://rvros.itch.io/animated-pixel-hero
- Coin: https://kvsr.itch.io/animated-coin-pixel
- Skull: https://untiedgames.itch.io/floating-skull-enemy
- Hyena and Scorpion: https://free-game-assets.itch.io/free-enemy-sprite-sheets-pixel-art
- Platform: https://www.deviantart.com/chickenman-16/art/Minecraft-Dirt-Wallpaper-306039162
- Background: https://edermunizz.itch.io/free-pixel-art-hill

Game Development:
- `pygame_functions.py` provides the functionality for
scrolling backgrounds. The source code can be found here:
https://github.com/StevePaget/Pygame_Functions
- Jump Formula: https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
