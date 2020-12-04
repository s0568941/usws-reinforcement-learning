#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Das ist die main File, welche das Game startet

import pygame
# Initialisiert alle notwendigen module fuer pygame
pygame.init()

from usws_jump_and_run_game.characters.player import Player
player = Player(10, 480, 20, 40)

# Konstanten
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
JUMP_VELOCITY = 8

#Titel und Groesse fuer das Fenster setzen
pygame.display.set_caption("USWS Jump and Run")
screen = pygame.display.set_mode(SIZE)

# Boolean: True = Spiel laeuft | False = Spiel Ende
run = True

while run:
    pygame.time.delay(100)

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
        player.x -= player.speed

    if keys[pygame.K_RIGHT] and player.x < (SCREEN_WIDTH - player.width - player.speed):
        player.x += player.speed

    # Wenn der Spieler nicht springt, dann bewegt er sich normal mit der Geschwindigkeit
    if not player.is_jump:
        if keys[pygame.K_UP] and player.y > player.speed:
            player.y -= player.speed

        if keys[pygame.K_DOWN] and player.y < (SCREEN_HEIGHT - player.height - player.speed):
            player.y += player.speed
            
        if keys[pygame.K_SPACE]:
            player.is_jump = True
    # Wenn der Spieler springt, dann erfolgt das mithilfe einer quadratischen Formel
    # https://www.geeksforgeeks.org/python-making-an-object-jump-in-pygame/
    else:
        if player.jump_velocity >= -JUMP_VELOCITY:
            player.y -= (player.jump_velocity * abs(player.jump_velocity)) * (1 / 2)
            player.jump_velocity -= 1
        else:
            player.jump_velocity = JUMP_VELOCITY
            player.is_jump = False



    # Vorerst Schwarzer Hintergrund (RGB)
    screen.fill((0, 0, 0))
    # Spieler wird vorerst durch ein Rechteck dargestellt
    pygame.draw.rect(screen, (255, 0, 0), (player.x, player.y, player.width, player.height))
    # Aktualisiere das Fenster
    pygame.display.update() 
    
pygame.quit()