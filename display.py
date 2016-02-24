#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This module handles displaying to the screen"""

#importing tools
import pygame

#importing other game modules


class DisplayWindow:
    displaySize = (800,600)

    def __init__(self):
        self.gameDisplay = pygame.display.set_mode(self.displaySize)
        pygame.display.set_caption("Colligo")

    def update(self):
        pygame.display.update()


class DisplayTilemap():
    def __init__(self, window, map):
        window.gameDisplay.fill(map.canvasColor)
        window.update()
        self.window = window

    def update(self, tilemap):
        self.window.gameDisplay.fill(tilemap.canvasColor)
        for block in tilemap.map:
            #print(tilemap.map)
            self.window.gameDisplay.blit(block.sprite,(tilemap.map[block][0]*16+(self.window.displaySize[0]/2),tilemap.map[block][1]*16+(self.window.displaySize[1]/2)))
        self.window.update()


"""
class Menu():
    displayAboveLevel = False


class StartMenu(Menu):
    pass


class InventoryMenu(Menu):
    pass


class PauseMenu(Menu):
    pass


class DeathMenu(Menu):
    pass
"""