# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 01:09:34 2013

@author: Admin
"""

from methods.method import Method
from numpy.random import randint
from time import sleep

class RandomMethod(Method):
    _name = "Random"
    _short_name = "Random"
    
    def make_move(self, state):
        sleep(0.2)
        holes_num = state.holes_num()
        my_holes = state.player_holes(self._player)
        candidates = []
        for hole in range(holes_num):
            if my_holes[hole]>0:
                candidates.append(hole)
        if candidates:
            hole = candidates[randint(len(candidates))]
            return hole
        return -1