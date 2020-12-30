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
from usws_jump_and_run_game.characters.hyena import Hyena
from usws_jump_and_run_game.characters.scorpio import Scorpio
from usws_jump_and_run_game.characters.skull import Skull

player = Player(X_STARTING_POSITION, Y_STARTING_POSITION, 20, 40)
platform = Platform(900, 550, 100, 30)
platform2 = Platform(1350, 600, 100, 30)
platform3 = Platform(1050, 600, 100, 20)
obstacles = [platform, platform2, platform3]
player.obstacles = obstacles
hyena1 = Hyena(550, 620, 25, 40, 800)
scorpio1 = Scorpio(200, 620, 25, 40, 500)
skull1 = Skull(1100, 520, 25, 25, 620)

clock = pygame.time.Clock()

# for debugging:
counter = 0
def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %r" % (attr, getattr(obj, attr)))

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
    for obstacle in obstacles:
        obstacle.draw(pygame_f.screen)
    hyena1.draw(pygame_f.screen)
    scorpio1.draw(pygame_f.screen)
    skull1.draw(pygame_f.screen)
    pygame_f.updateDisplay()

# TODO: Sofortiges sterben des character (derzeitig muss man noch eine Taste nach der Kollision drücken, damit diese registriert wird)
def check_collision():
    if player.hitbox[1] < hyena1.hitbox[1] + hyena1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > hyena1.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > hyena1.hitbox[0] and player.hitbox[0] < hyena1.hitbox[0] + hyena1.hitbox[2]:
            player.died()

    if player.hitbox[1] < skull1.hitbox[1] + skull1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > skull1.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > skull1.hitbox[0] and player.hitbox[0] < skull1.hitbox[0] + skull1.hitbox[2]:
                player.died()

    if player.hitbox[1] < scorpio1.hitbox[1] + scorpio1.hitbox[3] and player.hitbox[1] + player.hitbox[3] > scorpio1.hitbox[1]:
            if player.hitbox[0] + player.hitbox[2] > scorpio1.hitbox[0] and player.hitbox[0] < scorpio1.hitbox[0] + scorpio1.hitbox[2]:
                player.died()



while run:
    # erhöht die FPS-Anzahl um das Spiel fluessiger zu gestalten
    clock.tick(27)
    check_collision()
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
            for obstacle in obstacles:
                obstacle.move_right()
            skull1.adapt_to_screen_right()
            hyena1.adapt_to_screen_right()
            scorpio1.adapt_to_screen_right()
        else:
            pygame_f.scrollBackground(0, 0)
        player.move_left()
        player.is_obstacle_underneath_player()
        player.is_player_underneath_obstacle()

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
            for obstacle in obstacles:
                obstacle.move_left()
            skull1.adapt_to_screen_left()
            hyena1.adapt_to_screen_left()
            scorpio1.adapt_to_screen_left()
        else:
            pygame_f.scrollBackground(0, 0)
        player.move_right()
        player.is_obstacle_underneath_player()
        player.is_player_underneath_obstacle()

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

    if player.is_fall and not player.is_on_obstacle and player.y < Y_STARTING_POSITION and not player.is_colliding and not player.obstacle_underneath_player:
        player.fall_from_obstacle()
    if player.is_landing and player.is_player_underneath_obstacle():
        player.fall_from_obstacle()
    if player.obstacle_underneath_player and not player.is_on_obstacle and player.is_landing:
        player.land_on_obstacle()
    if player.is_colliding and not player.is_landing:
        player.collide_with_obstacle()
    if player.is_landing and not player.is_jump:
        player.land_on_obstacle()
        if player.y > Y_STARTING_POSITION:
            player.is_landing = False
    if player.is_falling_to_ground:
        if player.y > Y_STARTING_POSITION:
            player.is_falling_to_ground = False

    if not player.is_jump and not player.is_landing and not player.is_colliding:
        player.check_for_vertical_obstacles()
        player.is_player_on_obstacle()
        if player.y != Y_STARTING_POSITION and not player.is_on_obstacle and not player.is_falling_to_ground:
            player.y = Y_STARTING_POSITION
            player.hitbox = (player.static_x + 30, player.y + 15, player.height, player.width)

    # for debugging:
    if counter % 1000 == 0:
        dump(player)
    counter += 1
    redraw_game_window()

pygame.quit()
