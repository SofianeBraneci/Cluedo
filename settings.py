# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:40:39 2020

@author: hp
"""
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PLAYERS_COLOR = [YELLOW, RED, (0,0,255), (0,255,255), (128,0,128), WHITE]

# game settings
WIDTH = 770   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 846  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = DARKGREY

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

DIR = os.path.dirname(__file__)

WALL = (166,122,91)

INSID = (250, 240, 220)