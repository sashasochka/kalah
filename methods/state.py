#!/usr/bin/env python
"""Contains state class for the Kalah

@author: Oleksii Molchanovskyi
@organization: Kyiv Polytechnic Institute
@country: Ukraine

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from copy import deepcopy

MoveNotEnds = 0
MoveEnds = 1
MoveEndsInPlayersKalah = 2
MoveEndsInPlayersEmptyHole = 3
WrongMove = 4

class KalahStateList(object):
    _list = []
    def __init__(self):
        self._list = []
    def add_state(self, state, active_player, active_hole=-1, active_kalah=False):
        self._list.append({'state':state.copy(), 'player':active_player, 'hole':active_hole, 'kalah':active_kalah})
    def get_list(self):
        return self._list

class KalahState(object):
    _holes_num = 6
    _holes = [[], []]
    _kalahs = [0, 0]
    last_moves = None
    last_move_result = MoveEnds
    
    def __init__(self, stones_per_hole, holes_num=6):
        self._holes_num = holes_num
        self._holes = [[], []]
        self._kalahs = [0, 0]
        for hole in range(self._holes_num):
            self._holes[0].append(stones_per_hole)
            self._holes[1].append(stones_per_hole)
            
    def holes_num(self):
        return self._holes_num
    
    def player_holes(self, player):
        return self._holes[player]
        
    def player_kalah(self, player):
        return self._kalahs[player]
        
    def player_points(self, player):
        return self._kalahs[player]
            
    def move(self, player, hole_num):
        self.last_moves = None
        last_moves = KalahStateList()
        
        def opposite_hole(hole_num):
            return self._holes_num - hole_num - 1
        
        def make_turn(player, hole_num=-1, skip_kalah=False):
            # place stones to player's holes
            for hole in range(hole_num+1, self._holes_num):
                self._holes[player][hole] += 1
                last_moves.add_state(self, player, hole)
                self.amount_of_stones -= 1
                if not self.amount_of_stones:
                    if not skip_kalah and self._holes[player][hole]==1:
                        return MoveEndsInPlayersEmptyHole, hole
                    return MoveEnds, hole
            
            # place stones to player's kalah
            if not skip_kalah:
                self._kalahs[player] += 1
                last_moves.add_state(self, player, active_kalah=True)
                self.amount_of_stones -= 1
                if not self.amount_of_stones:
                    return MoveEndsInPlayersKalah, -1

            return MoveNotEnds, float('inf')
            
        if hole_num<0 or hole_num>=self._holes_num or player<0 or player>1:
            return WrongMove
        self.amount_of_stones = self._holes[player][hole_num]
        if not self.amount_of_stones:
            return WrongMove
        
        other_player = (player+1) % 2
        self._holes[player][hole_num] = 0
        last_moves.add_state(self, player, hole_num)
        while self.amount_of_stones:
            turn_result, last_hole = make_turn(player, hole_num)
            if turn_result==MoveEndsInPlayersKalah:
                self.last_moves = last_moves
                if self.is_finished(player):
                    self.last_move_result = MoveEnds
                else:
                    self.last_move_result = MoveEndsInPlayersKalah
                return self.last_move_result
            elif turn_result==MoveEndsInPlayersEmptyHole:
                if self._holes[other_player][opposite_hole(last_hole)]>0:
                    self._holes[player][last_hole] = 0
                    self._kalahs[player] += 1
                    last_moves.add_state(self, player, last_hole, active_kalah=True)
                    kalah_add = self._holes[other_player][opposite_hole(last_hole)]
                    self._holes[other_player][opposite_hole(last_hole)] = 0
                    last_moves.add_state(self, other_player, opposite_hole(last_hole))
                    self._kalahs[player] += kalah_add
                    last_moves.add_state(self, player, active_kalah=True)
                self.last_moves = last_moves
                self.last_move_result = MoveEnds
                return self.last_move_result
            elif turn_result==MoveEnds:
                self.last_moves = last_moves
                self.last_move_result = MoveEnds
                return self.last_move_result
            
            turn_result, last_hole = make_turn(other_player, skip_kalah=True)
            hole_num = -1
            
        self.last_moves = last_moves
        self.last_move_result = MoveEnds
        return self.last_move_result
        
    def get_last_moves(self):
        return self.last_moves
    
    def is_finished(self, player):
        for hole in self._holes[player]:
            if hole:
                return False
        return True
        
    def end_game(self):
        for player in [0,1]:
            for hole in range(self._holes_num):
                self._kalahs[player] += self._holes[player][hole]
                self._holes[player][hole] = 0
        return self._kalahs
        
    def to_string(self):
        return "(" + str(self._holes[0]) + ", " + str(self._kalahs[0]) + ") (" + str(self._holes[1]) + ", " + str(self._kalahs[1]) + ")"
        
    def __print__(self):
        print self.to_string()
        
    def copy(self):
        last_moves, self.last_moves = self.last_moves, None
        state = deepcopy(self)
        self.last_moves = last_moves
        return state
        
    def is_temporary(self):
        return self._temporary
        
    def get_neighbors(self, player):
        neighbors = []
        for hole in range(self._holes_num):
            if self._holes[player][hole]:
                new_state = self.copy()
                result = new_state.move(player, hole)
                if result==MoveEndsInPlayersKalah:
                    new_player = player
                else:
                    new_player = (player+1) % 2
                neighbors.append({'state':new_state, 'result':result, 'hole':[hole], 'player':new_player})
        return neighbors
        
    def get_all_neighbors(self, player):
        neighbors = self.get_neighbors(player)
        while True:
            for i in range(len(neighbors)):
                if neighbors[i]['result']==MoveEndsInPlayersKalah:
                    new_state = neighbors.pop(i)
                    new_neighbors = new_state['state'].get_neighbors(player)
                    for new_new_state in new_neighbors:
                        new_new_state['hole'] = new_state['hole'] + new_new_state['hole']
                    neighbors = neighbors + new_neighbors
            else:
                break
#        map(lambda x: x['state'].__print__(), neighbors) 
        return neighbors
        
if __name__ == "__main__":
    state = KalahState(0)
    state._kalahs = [6,4]
    state._holes = [[0, 4, 8, 7, 2, 4], [0, 0, 0, 0, 0, 1]]
    n = state.get_neighbors(1)
    for x in n:
        print x['hole'], x['state'].to_string(), x['player']