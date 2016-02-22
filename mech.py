#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This is a game all about collecting resources to advance while avoiding enemies and thieves"""

#importing tools
import pygame

#importing other game modules
import tilemap
import display


class Mechanic:
    def move_abs(self, obj, pos=(0,0)):
        obj.position = pos

    def move_rel(self, obj, change=(0,0)):
        obj.position = (obj, (change[0]+obj.position[0],change[1]+obj.position[1]))

    def collision(self,obj1,obj2):
        pass
