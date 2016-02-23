#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This module handles map data"""

#importing tools
import pygame

#importing other game modules
import gameObjs


class Tilemap:
    gameObjInstances = [gameObjs.Colligo()]
    map = {(0,0):gameObjInstances[0]}
    canvasColor = (255,255,255)
    activeMap = ''

    def update(self):
        ##new_map = self.map.keys()
        for block in self.map:
            new_map[tuple(new_map[block].position)] = new_map[block]
        #self.map = new_map

    def load_overworld(self):
        ##Clearing Out Current Level
        self.map.clear()
        self.gameObjInstances.clear()
        ##Defining New Level
        self.activeMap = 'overworld'
        self.gameObjInstances = [gameObjs.Colligo]
        self.map = {(0,0):self.gameObjInstances[0]}
        self.canvasColor = (111,227,0)

    def load_house(self):
        ##Clearing Out Current Level
        self.map.clear()
        self.gameObjInstances.clear()
        ##Defining New Level
        self.activeMap = 'house'
        self.gameObjInstances = [gameObjs.Colligo]
        self.map = {(0,0):self.gameObjInstances[0]}
        self.canvasColor = (139,89,19)