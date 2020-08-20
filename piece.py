# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 18:42:57 2020

@author: hp
"""

from confi import *
from sprites import *

class Piece:
    
    def __init__(self):
        self.cases = []
        self.index = 0
    
    def add_case(self, case):
        self.cases.append(case)
        
    
    def __repr__(self):
        return str(self.cases)
    
    def get_next_spot(self):
        spot = self.cases[self.index]
        self.index = (self.index + 1) % len(self.cases)
        return spot
    


class Planche:
    def __init__(self, game):
        self.game = game
        self.pieces = dict()
        # print(self.pieces)
        self.board = []
        self.map_board = []
        with open('board.txt', 'rt') as f:
            
            for line in f:
                self.map_board.append(line[:-1])
        # print(self.map_board)
    
    def construct(self):
        
        for row, tiles in enumerate(self.map_board):
            temp = []
            for col, tile in enumerate(tiles):
                if tile in CHARS:
                    player = Player(self.game, col, row, PLAYERS_COLOR.pop())
                    self.game.players_sprite.add(player)
                    self.game.players.append(player)
                    temp.append(player)
                elif tile == ' ':
                    wall = Wall(self.game, col, row)
                    temp.append(wall)
                elif tile in ETRANCE.keys():
                    # print("entrance " + ETRANCE[tile])
                    entrance = Entrance(self.game, col, row, ETRANCE[tile])
                    temp.append(entrance)
                elif tile in ROOMS.keys():
                    # print(tile)
                    
                    roomtile = TileRoom(self.game, col, row)
                    temp.append(roomtile)
                    if tile in self.pieces.keys():
                        self.pieces[tile].add_case(roomtile)
                    else:
                        self.pieces[tile] = Piece()
                        self.pieces[tile].add_case(roomtile)
                elif tile == '0':
                    tile = Tile(self.game, col, row)
                    temp.append(tile)
            self.board.append(temp)
    
    def on_entrance(self, x, y):
        return isinstance(self.board[y][x], Entrance)
    
    def searche_empty_tile(self, room):
        # print(room)
        tiles = self.pieces[room]
        if room == '4':
            tiles.cases.sort(key=lambda case: (case.y, case.x), reverse=True)
        tile = tiles.get_next_spot()
        self.game.player.set_position(tile.x, tile.y)
        

                    
                
                

    
                            
                
                    
                    
            
    