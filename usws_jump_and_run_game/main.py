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
from usws_jump_and_run_game.characters.player import Player
from usws_jump_and_run_game.environment.obstacles.platform import Platform

player = Player(X_STARTING_POSITION, Y_STARTING_POSITION, 20, 40)
platform = Platform(900, 600, 100, 30)
obstacles = [platform]
player.obstacles = obstacles

clock = pygame.time.Clock()

# Setup screen and background
pygame_f.screenSize(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame_f.setAutoUpdate(False)
pygame_f.setBackgroundImage('environment/pictures/hills_bg_scaled2.png')
pygame_f.pygame.display.set_caption('USWS Jump and Run')

# Boolean: True = Spiel laeuft | False = Spiel Ende
run = True


# Auslagerung der Zeichenaktionen

def redraw_game_window():
    # Aktualisiere das Fenster (background & player)
    player.draw(pygame_f.screen)
    platform.draw(pygame_f.screen)
    pygame_f.updateDisplay()


while run:
    # erhöht die FPS-Anzahl um das Spiel fluessiger zu gestalten
    clock.tick(27)

    # Schaue nach ob eines der events das Spiel beenden moechte (Fensterkreuz)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            # sys.exit() waere eine andere alternative

    # Hole eine aktuelle Liste der Tasten, die gedrueckt wurden
    keys = pygame.key.get_pressed()

    # Bewege den Spieler auf Basis der gedrueckten Tasten mit der Geschwindigkeit des Spielers
    # Pruefe auch ob Spieler durch die Bewegung noch im Screen bleibt
    if keys[pygame.K_LEFT] and player.x > player.speed:
        # Scrolling background is deactivated once player arrives at the center and proceeds to the left
        if player.x > PLAYER_STATIC_X and not player.movement_blocked:
            pygame_f.scrollBackground(player.speed, 0)
            platform.move_right()
        else:
            pygame_f.scrollBackground(0, 0)
        player.move_left()

        if not player.is_jump:
            player.left = True
            player.right = False
            player.idle_left = True
            player.idle_right = False
            player.last_dir = 'l'

    elif keys[pygame.K_RIGHT]:
        # TODO: Add limit when level is finished
        #  and player.x < (SCREEN_WIDTH - player.width - player.speed)
        # Scrolling background is activated once player arrives at the center
        if player.x > PLAYER_STATIC_X and not player.movement_blocked:
            pygame_f.scrollBackground(-player.speed, 0)
            platform.move_left()
        else:
            pygame_f.scrollBackground(0, 0)
        player.move_right()

        if not player.is_jump:
            player.left = False
            player.right = True
            player.idle_left = False
            player.idle_right = True
            player.last_dir = 'r'

    else:
        pygame_f.scrollBackground(0, 0)
        player.left = False
        player.right = False

    # Wenn der Spieler nicht springt, dann bewegt er sich normal mit der Geschwindigkeit
    if not player.is_jump:
        if keys[pygame.K_SPACE]:
            pygame_f.scrollBackground(0, 0)
            player.is_jump = True
            player.left = False
            player.right = False
            player.walk_count = 0

    # Wenn der Spieler springt, dann erfolgt das mithilfe einer quadratischen Formel
    # https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
    else:
        player.jump()

    if player.is_fall and not player.is_on_obstacle and player.y != Y_STARTING_POSITION:
        player.fall_from_obstacle()

    redraw_game_window()

pygame.quit()
