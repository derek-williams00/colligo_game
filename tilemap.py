#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This is a game all about collecting resources to advance while avoiding enemies and thieves"""

#importing tools
import pygame

#importing other game modules
import gameObjs


class TileMap:
    gameObjInstances = [gameObjs.Colligo]


class Overworld(TileMap):
    map = {(0,0):TileMap.gameObjInstances[0]}
    canvasColor = (111,227,0)

class House(TileMap):
    map = {(0,0):TileMap.gameObjInstances[0]}
    canvasColor = (139,89,19)