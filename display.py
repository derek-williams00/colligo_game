#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This is a game all about collecting resources to advance while avoiding enemies and thieves"""

#importing tools
import pygame

#importing other game modules
import tilemap


class DisplayWindow:
    displaySize = (800,600)
    gameDisplay = pygame.display.set_mode(displaySize)
    active_tilemap = tilemap.Overworld
    pygame.display.set_caption("Colligo")
    pygame.display.update()


class Display:
    displayTypes = {}


class DisplayTileMap(Display):
    def __init__(self, map=DisplayWindow.active_tilemap):
        DisplayWindow.gameDisplay.fill((255,0,0))
        pygame.display.update()

    def update(self, tell=False):
        for block in DisplayWindow.active_tilemap.map:
            DisplayWindow.gameDisplay.blit(DisplayWindow.active_tilemap.map[block].sprite,(block[0]*16+(DisplayWindow.displaySize[0]/2),block[1]*16+(DisplayWindow.displaySize[1]/2)))
            pygame.display.update()
            if tell:
                print(DisplayWindow.active_tilemap.map[block].sprite,(block[0]*16+(DisplayWindow.displaySize[0]/2),block[1]*16+(DisplayWindow.displaySize[1]/2)))



class Menu(Display):
    displayAboveLevel = False


class StartMenu(Menu):
    pass


class InventoryMenu(Menu):
    pass


class PauseMenu(Menu):
    pass


class DeathMenu(Menu):
    pass