#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This module handles all the different tile blocks and entities in the game"""

#importing tools
import pygame

#importing other game modules


class GameObj:
    position = [0,0]
    tileSize = (1,1)


class Character(GameObj):
    sprite = pygame.image.load('character.png')
    moveSpeed = 1
    health = 100
    strength = 25
    hostile = False


class InanimateObj(GameObj):
    pass


class Colligo(Character):
    pass
    #position = [-16,4]


class Tree(InanimateObj):
    pass