# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 03:43:11 2013

@author: Admin
"""

if __name__ == "__main__":
    from method import Method
else:
    from methods.method import Method
    
precomputed = lambda state: {
        ((5, 5, 5, 5, 5, 5), (5, 5, 5, 5, 5, 5)): 1
}.get(state, None)

class OleksandrMethod(Method):
    _name = "Oleksandr"
    _short_name = "Oleksandr"
    
    def __init__(self, player_num, ai_level=1):
        super(OleksandrMethod, self).__init__(player_num, ai_level)
        self._ai_level = min((ai_level+1)/2, 3)
    
    def _other_player(self):
        return (self._player + 1) % 2
    
    def _terminal_test(self, state, player, depth=0):
#        print player, state.to_string(), depth, self._ai_level
        if depth>=self._ai_level or state.is_finished(player):
            return True
        return False
    
    def _utility(self, state):
        utility = [0,0]
        for player in (self._player,self._other_player()):
            utility[player] = state.player_kalah(player) + sum(state.player_holes(player))
        return utility[self._player] - utility[self._other_player()]
    
    def _max_value(self, state, depth=1):
        if self._terminal_test(state, self._player):
            return self._utility(state)
        value = -float('inf')
        neighbors = state.get_all_neighbors(self._player)
        for new_state in neighbors:
            value = max(value, self._min_value(new_state['state'], depth))
        return value
            
    def _min_value(self, state, depth=1):
        if self._terminal_test(state, self._other_player(), depth):
#            print "   "*depth, state.to_string(), self._utility(state)
            return self._utility(state)
        value = float('inf')
        neighbors = state.get_all_neighbors(self._other_player())
        for new_state in neighbors:
            value = min(value, self._max_value(new_state['state'], depth+1))
        return value
    
    def make_move(self, state):
        print "Input state:", state.to_string()
        neighbors = state.get_all_neighbors(self._player)
        best_value, best_state = -float('inf'), None

        my_state = state.player_holes(self._player)
        opp_state = state.player_holes(self._other_player())
        state_tup = (tuple(my_state), tuple(opp_state))

# first 2 moves if 1st player
        precomp = precomputed(state_tup)
        if precomp is not None:
            print 'Using precomputed move'
            return precomp

        for new_state in neighbors:
            value = self._min_value(new_state['state'])
            if best_value < value :
                best_value, best_state = value, new_state
        if best_state:
            print best_value, best_state['state'].to_string()
            return best_state['hole'][0]
        return -1
        
if __name__ == "__main__":
    from state import KalahState
    state = KalahState(0)
    state._kalahs = [6,4]
    state._holes = [[0, 4, 8, 7, 2, 4], [0, 0, 0, 0, 0, 1]]
    method = OleksandrMethod(1, 1)
    print method.make_move(state)
