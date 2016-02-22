#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This is a game all about collecting resources to advance while avoiding enemies and thieves"""

#importing tools
import pygame

#importing other game modules
import tilemap
import display
import mech


class main:
    def __init__(self):
        self.game_window = display.DisplayWindow()
        self.game_tilemap = display.DisplayTileMap()


    def game_exit(self):
        pygame.quit()
        quit()


    def game_update(self):
        main_char = tilemap.TileMap.gameObjInstances[0]
        #Getting user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                self.game_exit()
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_UP:
                    #mech.Mechanic.move_rel(main_char, (0,-main_char.moveSpeed))
                    main_char.position[1] -= 1
                if event.key == pygame.K_DOWN:
                    #mech.Mechanic.move_rel(main_char, (0,main_char.moveSpeed))
                    main_char.position[1] += 1
                if event.key == pygame.K_RIGHT:
                    main_char.position[0] += 1
                    #mech.Mechanic.move_rel(main_char, (main_char.moveSpeed,0))
                if event.key == pygame.K_LEFT:
                    main_char.position[0] -= 1
                    #mech.Mechanic.move_rel(main_char, (-main_char.moveSpeed,0))

        display.DisplayTileMap.update(self.game_tilemap)


##Runing game
game = main()
while True:
    main.game_update(game)