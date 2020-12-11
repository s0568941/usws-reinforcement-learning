#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Das ist die main File, welche das Game startet

import pygame
# Initialisiert alle notwendigen module fuer pygame
pygame.init()
# import additional pygame functions
import usws_jump_and_run_game.pygame_functions as pygame_f

from usws_jump_and_run_game.characters.player import Player
player = Player(690, 620, 15, 28)

clock = pygame.time.Clock()

# Konstanten
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1380, 690
JUMP_VELOCITY = 8

# Laden des Bildes aus 'pictures'
pygame_f.screenSize(SCREEN_WIDTH, SCREEN_HEIGHT)
pygame_f.setAutoUpdate(False)
pygame_f.setBackgroundImage('environment/pictures/hills_bg_scaled.png')
#Titel und Groesse fuer das Fenster setzen
pygame_f.pygame.display.set_caption('USWS Jump and Run')

# Boolean: True = Spiel laeuft | False = Spiel Ende
run = True

# Auslagerung der Zeichenaktionen

def redrawGameWindows():
    # Aktualisiere das Fenster (background & player)
    player.draw(pygame_f.screen)
    pygame_f.updateDisplay()


while run:
    # erhöht die FPS-Anzahl um das Spiel fluessiger zu gestalten
    clock.tick(27)

    # Schaue nach ob eines der events das Spiel beenden moechte (Fensterkreuz)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            #sys.exit() waere eine andere alternative

    # Hole eine aktuelle Liste der Tasten, die gedrueckt wurden
    keys = pygame.key.get_pressed()


    # Bewege den Spieler auf Basis der gedrueckten Tasten mit der Geschwindigkeit des Spielers
    # Pruefe auch ob Spieler durch die Bewegung noch im Screen bleibt
    if keys[pygame.K_LEFT] and player.x > player.speed:
        pygame_f.scrollBackground(player.speed, 0)
        player.x -= player.speed
        if not player.is_jump:
            player.left = True
            player.right = False
            player.idle_left = True
            player.idle_right = False
            player.last_dir = 'l'

    elif keys[pygame.K_RIGHT]:
        #and player.x < (SCREEN_WIDTH - player.width - player.speed)
        pygame_f.scrollBackground(-player.speed, 0)
        player.x += player.speed
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
        if player.jump_velocity >= -JUMP_VELOCITY:
            player.y -= (player.jump_velocity * abs(player.jump_velocity)) * (1 / 2)
            player.jump_velocity -= 1
        else:
            player.jump_velocity = JUMP_VELOCITY
            player.is_jump = False

    redrawGameWindows()

pygame.quit()
