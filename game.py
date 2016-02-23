#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This is a game all about collecting resources to advance while avoiding enemies and thieves"""

#importing tools
import pygame

#importing other game modules
import tilemap
import display


class Main:
    def __init__(self):
        #Game control classes
        self.game_map = tilemap.Tilemap()
        tilemap.Tilemap.load_overworld(self.game_map)
        self.display_window = display.DisplayWindow()
        self.display_map = display.DisplayTilemap(self.display_window,self.game_map)
        ##Loading Colligo for user manipulation
        self.main_char = self.game_map.gameObjInstances[0]




    def game_exit(self):
        pygame.quit()
        quit()


    def game_update(self):
        #Getting user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(event)
                self.game_exit()
            if event.type == pygame.KEYDOWN:
                #print(event)
                if event.key == pygame.K_UP:
                    #mech.Mechanic.move_rel(main_char, (0,-main_char.moveSpeed))
                    self.main_char.position[1] -= 1
                    print('kevent up')
                    print(self.main_char.position[1])
                if event.key == pygame.K_DOWN:
                    #mech.Mechanic.move_rel(main_char, (0,main_char.moveSpeed))
                    self.main_char.position[1] += 1
                    print('kevent down')
                if event.key == pygame.K_RIGHT:
                    self.main_char.position[0] += 1
                    print('kevent right')
                    #mech.Mechanic.move_rel(main_char, (main_char.moveSpeed,0))
                if event.key == pygame.K_LEFT:
                    self.main_char.position[0] -= 1
                    print('kevent left')
                    #mech.Mechanic.move_rel(main_char, (-main_char.moveSpeed,0))

        #for the time being
        self.game_map.update()
        self.display_map.update(self.game_map)



##Runing game
game = Main()
while True:
    Main.game_update(game)