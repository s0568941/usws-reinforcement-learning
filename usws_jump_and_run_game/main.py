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
from usws_jump_and_run_game.environment.obstacles.spike import Spike
from usws_jump_and_run_game.characters.hyena import Hyena
from usws_jump_and_run_game.characters.scorpio import Scorpio
from usws_jump_and_run_game.characters.skull import Skull

#player
player = Player(X_STARTING_POSITION, Y_STARTING_POSITION, 20, 40)

#LEVEL

#Checkpoint 1 - Till third platform
scorpio1 = Scorpio(150, 620, 25, 40, 300, "Scorpio1")
platform = Platform(350, 600, 80, 50)
hyena1 = Hyena(500, 620, 25, 40, 800, "Hyena1")
platform2 = Platform(900, 580, 100, 70)
#spike = Spike(1230, 620, 50, 30)
#spike2 = Spike(1230, 620, 50, 30)
skull1 = Skull(1020, 440, 25, 25, 580, "Skull1")
platform3 = Platform(1080, 580, 100, 70)

#Checkpoint 2 - Till Heart collectable
platform4 = Platform(1500, 560, 120, 90)
scorpio2 = Scorpio(1500, 540, 25, 40, 1600, "Scorpio2")

#small islands
platform5 = Platform(1680, 560, 60, 30)
platform6 = Platform(1800, 560, 60, 30)

platform7 = Platform(1920, 560, 600, 30)
hyena2 = Hyena(1920, 525, 25, 40, 2120, "Hyena2")
platform8 = Platform(2050, 480, 340, 30)
platform9 = Platform(2115, 400, 210, 30)
platform10 = Platform(2147, 320, 146, 30)
platform11 = Platform(2180, 240, 80, 440)#letzter wert auf 440 #treelike
skull2 = Skull(2200, 100, 25, 25, 180, "Skull2")
hyena3 = Hyena(2260, 525, 25, 40, 2460, "Hyena3")

#Checkpoint 3 - Till Skull platform

#small islands
platform12 = Platform(2580, 560, 60, 30)
platform13 = Platform(2700, 560, 60, 30)

platform14 = Platform(2820, 560, 600, 100) #skull island
skull3 = Skull(2900, 420, 25, 25, 520, "Skull3")
skull4 = Skull(3100, 450, 25, 25, 520, "Skull4")
skull5 = Skull(3300, 420, 25, 25, 520, "Skull5")
# two spikes

# Checkpoint 4 - till last platform section
hyena4 = Hyena(3420, 620, 25, 40, 3820, "Hyena4")
#spike
hyena5 = Hyena(3900, 620, 25, 40, 4100, "Hyena5")
scorpio3 = Scorpio(3900, 620, 25, 40, 4100, "Scorpio3")

# Checkpoint 5 - till end
platform15 = Platform(4200, 560, 30, 100)
#spike
platform16 = Platform(4300, 600, 30, 60)
#spike
platform17 = Platform(4400, 560, 30, 100)
skull6 = Skull(4395, 460, 25, 25, 600, "Skull6")
#spike
platform18 = Platform(4500, 640, 30, 20)
#spike
platform19 = Platform(4600, 560, 30, 100)




obstacles = [platform, platform2, platform3, platform4, platform5,platform6,platform7,platform8,platform9,platform10,platform11,platform12,platform13,platform14,platform15, platform16, platform17, platform18,platform19]
player.obstacles = obstacles

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
main_program_run = True
startscreen_run = False
game_run = False
ki_run = False
game_over = False
input_done = False

#Start Screen setup
title = pygame_f.makeLabel(SCREENTITLE, 60, 300, 230, "black", "Arial", "clear")
start_game_text = pygame_f.makeLabel(START_GAME_TEXT, 35, 300, 300, "black", "Arial", "clear")
start_ki_text = pygame_f.makeLabel(START_KI_TEXT, 35, 300, 350, "black", "Arial", "clear")
end_game_text = pygame_f.makeLabel(END_GAME_TEXT, 35, 300, 400, "black", "Arial", "clear")
nassim_text = pygame_f.makeLabel(NASSIM_TEXT, 25, 1100, 600, "black", "Arial", "clear")
nico_text = pygame_f.makeLabel(NICO_TEXT, 25, 1100, 650, "black", "Arial", "clear")

#Game Over Screen Setup
go_title = pygame_f.makeLabel(GO_TITLE, 100, 430, 150, "black", "Arial", "clear")
kill_text = pygame_f.makeLabel(KILL_TEXT, 40, 500, 300, "black", "Arial", "clear")
return_text = pygame_f.makeLabel(RETURN_TEXT, 35, 400, 350, "black", "Arial", "clear")



def redraw_game_window():
    # Aktualisiere das Fenster (background & player)
    player.draw(pygame_f.screen)
    for obstacle in obstacles:
        obstacle.draw(pygame_f.screen)
    hyena1.draw(pygame_f.screen)
    scorpio1.draw(pygame_f.screen)
    skull1.draw(pygame_f.screen)
    scorpio2.draw(pygame_f.screen)
    hyena2.draw(pygame_f.screen)
    skull2.draw(pygame_f.screen)
    hyena3.draw(pygame_f.screen)
    skull3.draw(pygame_f.screen)
    skull4.draw(pygame_f.screen)
    skull5.draw(pygame_f.screen)
    hyena4.draw(pygame_f.screen)
    hyena5.draw(pygame_f.screen)
    scorpio3.draw(pygame_f.screen)
    skull6.draw(pygame_f.screen)
    pygame_f.updateDisplay()

def check_collision(player, enemy):
    global game_over
    if player.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and player.hitbox[1] + player.hitbox[3] > enemy.hitbox[1]:
        if player.hitbox[0] + player.hitbox[2] > enemy.hitbox[0] and player.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
            game_over = True
            game_over_screen()
    elif player.is_dead:
        game_over = True
        game_over_screen()
    else:
        game_over = False

def game_over_screen():
    global game_run
    clock.tick(27)

    pygame_f.showLabel(go_title)
    pygame_f.showLabel(kill_text)
    pygame_f.showLabel(return_text)
    pygame_f.updateDisplay()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                global main_program_run
                main_program_run = False
            if event.type == pygame.KEYDOWN:
                main_program_run = True
                game_run = False
                hide_game_over_screen()
                return




def hide_start_screen():
    pygame_f.hideLabel(title)
    pygame_f.hideLabel(start_game_text)
    pygame_f.hideLabel(start_ki_text)
    pygame_f.hideLabel(end_game_text)
    pygame_f.hideLabel(nassim_text)
    pygame_f.hideLabel(nico_text)
    pygame_f.updateDisplay()

def hide_game_over_screen():
    pygame_f.hideLabel(go_title)
    pygame_f.hideLabel(kill_text)
    pygame_f.hideLabel(return_text)

    #Todo: needs to hide/delete all sprites and platforms





def start_screen():
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global main_program_run
            main_program_run = False

    pygame_f.showLabel(title)
    pygame_f.showLabel(start_game_text)
    pygame_f.showLabel(start_ki_text)
    pygame_f.showLabel(end_game_text)
    pygame_f.showLabel(nassim_text)
    pygame_f.showLabel(nico_text)
    pygame_f.updateDisplay()

#Hauptstartscreen immer true bei run
while main_program_run:
    start_screen()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_p]:
        game_run = True
    elif keys[pygame.K_SPACE]:
        ki_run = True

    #1. Spiel starten manuell
    while game_run:
        # erhöht die FPS-Anzahl um das Spiel fluessiger zu gestalten
        hide_start_screen()
        clock.tick(27)
        #prüft jeden enemy ob eine collision vorliegt
        check_collision(player, hyena1)
        check_collision(player, scorpio1)
        check_collision(player, skull1)
        check_collision(player, scorpio2)
        check_collision(player, hyena2)
        check_collision(player, skull2)
        check_collision(player, hyena3)
        check_collision(player, skull3)
        check_collision(player, skull4)
        check_collision(player, skull5)
        check_collision(player, hyena4)
        check_collision(player, hyena5)
        check_collision(player, scorpio3)
        check_collision(player, skull6)


        # Schaue nach ob eines der events das Spiel beenden moechte (Fensterkreuz)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
                main_program_run = False
                # sys.exit() waere eine andere alternative
        if game_over == False:
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
                    #ToDo: Enemy parent class to minimize code
                    skull1.adapt_to_screen_right()
                    hyena1.adapt_to_screen_right()
                    scorpio1.adapt_to_screen_right()
                    scorpio2.adapt_to_screen_right()
                    hyena2.adapt_to_screen_right()
                    skull2.adapt_to_screen_right()
                    hyena3.adapt_to_screen_right()
                    skull3.adapt_to_screen_right()
                    skull4.adapt_to_screen_right()
                    skull5.adapt_to_screen_right()
                    hyena4.adapt_to_screen_right()
                    hyena5.adapt_to_screen_right()
                    scorpio3.adapt_to_screen_right()
                    skull6.adapt_to_screen_right()


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
                    # ToDo: Enemy parent class to minimize code
                    skull1.adapt_to_screen_left()
                    hyena1.adapt_to_screen_left()
                    scorpio1.adapt_to_screen_left()
                    scorpio2.adapt_to_screen_left()
                    hyena2.adapt_to_screen_left()
                    skull2.adapt_to_screen_left()
                    hyena3.adapt_to_screen_left()
                    skull3.adapt_to_screen_left()
                    skull4.adapt_to_screen_left()
                    skull5.adapt_to_screen_left()
                    hyena4.adapt_to_screen_left()
                    hyena5.adapt_to_screen_left()
                    scorpio3.adapt_to_screen_left()
                    skull6.adapt_to_screen_left()

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

        #END OF 1.



    # 2. Spiel starten KI
    # Wenn 2 ausgewählt vom Spieler dann KI Code sarteb
    #ToDo KI Code
    while ki_run == True:
        # Schaue nach ob eines der events das Spiel beenden moechte (Fensterkreuz)
        print("IM KI CODE")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ki_run = False
                main_program_run = False

        #END OF 2.

pygame.quit()
