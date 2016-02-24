#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This module handles map data"""

#importing tools
import pygame
import copy

#importing other game modules
import gameObjs


class Tilemap:
    gameObjInstances = [gameObjs.Colligo()]
    map = {gameObjInstances[0]:(0,0)}
    canvasColor = (255,255,255)
    activeMap = ''

    def update_pos(self):
        for gameObj in self.map:
            self.map[gameObj] = tuple(gameObj.position)




    def load_overworld(self):
        ##Clearing Out Current Level
        self.map.clear()
        self.gameObjInstances.clear()
        ##Defining New Level
        self.activeMap = 'overworld'
        self.gameObjInstances = [gameObjs.Colligo]
        self.map = {self.gameObjInstances[0]:(0,0)}
        self.canvasColor = (111,227,0)

    def load_house(self):
        ##Clearing Out Current Level
        self.map.clear()
        self.gameObjInstances.clear()
        ##Defining New Level
        self.activeMap = 'house'
        self.gameObjInstances = [gameObjs.Colligo]
        self.map = {self.gameObjInstances[0]:(0,0)}
        self.canvasColor = (139,89,19)