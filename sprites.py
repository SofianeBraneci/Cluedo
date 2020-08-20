# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:40:33 2020

@author: hp
"""
import random
import pygame as pg
from settings import *
from fenetre import DialogueWindow, ExecutorThreadDialogue
import tkinter as tk
from tkinter import messagebox
from feuille import FeuilleEnquete
from confi import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, color):
        self.groups = game.players_sprite
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.moves = 0
        self.cartes = []
        self.y = y
        self.feuille = FeuilleEnquete(SUSPECTS,ARMES, LIEUX)
        self.was_in_room = False
    def throw_dice(self):
        self.moves = sum([random.choice([1,2,3,4,5,6]), random.choice([1,2,3,4,5,6])])
        print(self.moves)
    def add_carte(self, carte):
        self.cartes.append(carte)
    
    def move(self, dx=0, dy=0):
        if not self.collid_with_walls(dx, dy) and not self.collid_with_player(dx, dy) and self.moves > 0:
            self.x += dx
            self.moves -= 1
            self.y += dy
            # if self.game.is_in_room(self.y, self.x):
            #     DialogueWindow(self).create()
            if self.game.planche.on_entrance(self.x, self.y) and not self.was_in_room:
                print('Standing on entrance '+ ROOMS[self.game.planche.board[self.y][self.x].to])                
                self.moves = 0
                self.game.planche.searche_empty_tile(self.game.planche.board[self.y][self.x].to)
                self.was_in_room = True
                
                ExecutorThreadDialogue(self, self.game).start()
            if self.game.planche.on_entrance(self.x, self.y) and  self.was_in_room:
                self.was_in_room = False
        if self.x >= WIDTH:
            self.x = WIDTH
        if self.y <=0:
            self.y = 0
        if self.x < 0:
            self.x = 0
        if self.y >= HEIGHT:
            self.y = HEIGHT

        
    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    def get_carte(self, nom):
        for carte in cartes: 
            if carte.nom == nom:
                return carte
    
    def collid_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and self.y + dy == wall.y:
                return True
        return False
    def collid_with_player(self, dx=0, dy=0):
        for wall in self.game.players_sprite:
            if wall.x == self.x + dx and self.y + dy == wall.y:
                return True
        return False
    
    def set_position(self, x, y):
        self.x, self.y = x, y
        

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WALL)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Entrance(pg.sprite.Sprite):
    def __init__(self, game, x, y, to):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(DARKGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        # la piece ou on vas ce rendre
        self.to = to
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class TileRoom(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(INSID)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Tile(pg.sprite.Sprite):
    
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.image.load(os.path.join(DIR, 'floor.png')).convert()
        # self.image.fill(pg.color.Color(255,255,255,128))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
