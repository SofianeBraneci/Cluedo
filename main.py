# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:40:23 2020

@author: hp
"""

import pygame as pg
import sys
from carte import Carte

from actions import Secret
from random import choice
from fenetre import *
import tkinter as tk
from tkinter import messagebox
import threading
from settings import *
from sprites import *
from piece import Planche

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        # self.img = pg.image.load(os.path.join(DIR, 'cluedo-board-game.jpg'))
        pg.key.set_repeat(500, 100)
        # self.load_data()
        self.players = []
        self.cartes = []
        self.current_player_info = None
        self.index = 0



    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.players_sprite = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        # self.grid = []
        self.planche = Planche(self)
        self.planche.construct()
        d = {'suspect':[], 'arme':[], 'lieu':[]}
        for suspect in SUSPECTS:
            d['suspect'].append(Carte(suspect, 'suspect'))
        for arme in ARMES:
            d['arme'].append(Carte(arme, 'arme'))
        for lieu in LIEUX:
            d['lieu'].append(Carte(lieu, 'lieu'))
        
        self.solution = Secret('', '', '')
        for key in d.keys():
            if key == 'suspect':
                self.solution.suspect = d[key].pop(random.randint(0, len(d[key])-1)).nom
            if key == 'arme':
                self.solution.arme = d[key].pop(random.randint(0, len(d[key])-1)).nom
            else:
                self.solution.lieu = d[key].pop(random.randint(0, len(d[key])-1)).nom
        self.cartes = d['suspect'] + d['arme'] + d['lieu']
        random.shuffle(self.cartes)
        index = 0
        while len(self.cartes ) > 0:
            self.players[index].add_carte(self.cartes.pop())
            index = (index + 1) % (len(self.players))
        print(self.solution)
        
        # chaque joueur coche ces cases
        for player in self.players:
            player.feuille.update(player.cartes)
        
        self.player = self.players[self.index]
        self.player.throw_dice()
        ExecutorThreadInfo(self.player).start()
    
    def next_player(self):
        self.index = (self.index +1 ) %len(self.players)
        self.player = self.players[self.index]
    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.players_sprite.update()
        self.walls.update()
    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        
        self.walls.draw(self.screen)
        self.players_sprite.draw(self.screen)
        
#        self.screen.blit(self.text, self.text_rect)
        pg.display.flip()
        

    def events(self):
        # catch all events here
        
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)
            
                if event.key == pg.K_c:
                    # quand on change de player on charge la nvl vue 
                    self.index = (self.index +1 ) %len(self.players)
                    self.player = self.players[self.index]
                    self.player.throw_dice()
                    ExecutorThreadInfo(self.player).start()
                

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()