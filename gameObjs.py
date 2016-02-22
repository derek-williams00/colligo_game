#!/usr/bin/env python
__author__ = 'derek-williams00'
"""This is a game all about collecting resources to advance while avoiding enemies and thieves"""

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


class Tree(InanimateObj):
    pass