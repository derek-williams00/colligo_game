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
        self.char_moving = [False,False,False,False] #Up Down Left Right




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
                if event.key == pygame.K_UP:
                    self.char_moving[0] = True
                    print('kevent up')
                if event.key == pygame.K_DOWN:
                    self.char_moving[1] = True
                    print('kevent down')
                if event.key == pygame.K_RIGHT:
                    self.char_moving[2] = True
                    print('kevent right')
                if event.key == pygame.K_LEFT:
                    self.char_moving[3] = True
                    print('kevent left')


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.char_moving[0] = False
                    print('kevent up')
                    print(self.main_char.position)
                if event.key == pygame.K_DOWN:
                    self.char_moving[1] = False
                    print('kevent down')
                    print(self.main_char.position)
                if event.key == pygame.K_RIGHT:
                    self.char_moving[2] = False
                    print('kevent right')
                    print(self.main_char.position)
                if event.key == pygame.K_LEFT:
                    self.char_moving[3] = False
                    print('kevent left')
                    print(self.main_char.position)


        if self.char_moving[0]:
            #mech.Mechanic.move_rel(main_char, (0,-main_char.moveSpeed))
            self.main_char.position[1] -= self.main_char.moveSpeed/32
        if self.char_moving[1]:
            #mech.Mechanic.move_rel(main_char, (0,main_char.moveSpeed))
            self.main_char.position[1] += self.main_char.moveSpeed/32
        if self.char_moving[2]:
            self.main_char.position[0] += self.main_char.moveSpeed/32
            #mech.Mechanic.move_rel(main_char, (main_char.moveSpeed,0))
        if self.char_moving[3]:
            self.main_char.position[0] -= self.main_char.moveSpeed/32

            #mech.Mechanic.move_rel(main_char, (-main_char.moveSpeed,0))

        #for the time being
        self.game_map.update_pos()
        self.display_map.update(self.game_map)



##Runing game
game = Main()
clock = pygame.time.Clock()
while True:
    Main.game_update(game)
    clock.tick(32)