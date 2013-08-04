#!/usr/bin/env python
"""One of the minmax method implementation for playing Kalah.

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

#
# For the purposes of the testing. Please check the code at the bottom of 
# the file to details
#
if __name__ == "__main__":
    from method import Method
else:
    from methods.method import Method
    
class MinMaxMethod(Method):
    """Class with MinMax method for playing Kalah
    
    Main idea:
        Build a searching tree where each node is a game's state. When expanding
        the active player's node then use _min_value function to find a best
        move for an opponent player. In other case _max_value to find a best
        move for the active player. 
        We finish tree expanding when its height is equal to self._ai_level.
        For each leaf node we calculate a heuristic function value with 
        _utility function.
        
        In the code below we call this player - Max, an opponent - Min.
    
    Attributes:
        Please refer to method.py for details    
    """
    _name = "Min-max"
    _short_name = "Min-max"
    
    def __init__(self, player_num, ai_level=1):
        """Inits MinMaxMethod object
        
        Args:
            Please refer Method class description for details
        """
        super(MinMaxMethod, self).__init__(player_num, ai_level)
        self._ai_level = max(1, min(ai_level, 5))
    
    def _other_player(self):
        """Returns an opponent player's number (0 or 1)"""
        return (self._player + 1) % 2
    
    def _terminal_test(self, state, player, depth=0):
        """Checks if the state for player is a terminal one (a leaf)
        
        Args:
            state: state to check
            player: active player's number for the specified state
            depth: node's depth in the searching tree
        Returns:
            True/False: if not is finished or not
        """
#        print player, state.to_string(), depth, self._ai_level
        if depth>=self._ai_level or state.is_finished(player):
            return True
        return False
    
    def _utility(self, state):
        """Calculates a heuristic function value for a state
        
        The result is a sum of player's kalah contents and all of his/her
        holes or pits.
        
        Args:
            state: 
                
        Returns:
            Heuristic value for the specified state
        """
        utility = [0,0]
        for player in [self._player,self._other_player()]:
            utility[player] = state.player_kalah(player) + sum(state.player_holes(player))
        return utility[self._player] - utility[self._other_player()]
    
    def _max_value(self, state, depth=1):
        """Part of MinMax algorithm for the Max player
        
        Args:
            state: specific state
            depth: depth of the state in a searching tree
            
        Returns:
            Heuristic function value for this state. If this state is a 
            terminal then return result of self._utility function. In other 
            case recursively  runs the algorithm for the state's children
            and calculates the result as maximum value of all kids.
        """
        if self._terminal_test(state, self._player):
            return self._utility(state)
        value = -float('inf')
        neighbors = state.get_all_neighbors(self._player)
        for new_state in neighbors:
            value = max(value, self._min_value(new_state['state'], depth))
        return value
            
    def _min_value(self, state, depth=1):
        """Part of MinMax algorithm for the Min player
        
        Args:
            state: specific state
            depth: depth of the state in a searching tree
            
        Returns:
            Heuristic function value for this state. If this state is a 
            terminal then return result of self._utility function. In other 
            case recursively runs the algorithm for the state's children
            and calculates the result as minimum value of all kids.
        """
        if self._terminal_test(state, self._other_player(), depth):
#            print "   "*depth, state.to_string(), self._utility(state)
            return self._utility(state)
        value = float('inf')
        neighbors = state.get_all_neighbors(self._other_player())
        for new_state in neighbors:
            value = min(value, self._max_value(new_state['state'], depth+1))
        return value
    
    def make_move(self, state):
        """Makes a decision of the player's next move
        
        The MinMax algorithm is the basis of this function.
        
        Args:
            state: current board state
        
        Returns:
            Player's hole number which defines a player's next move
        """
        print "Input state:", state.to_string()
        neighbors = state.get_all_neighbors(self._player)
        best_value, best_state = -float('inf'), None
        for new_state in neighbors:
            value = self._min_value(new_state['state'])
            if best_value < value :
                best_value, best_state = value, new_state
        if best_state:
            print best_value, best_state['state'].to_string()
            return best_state['hole'][0]
        return -1
        
#
# You can test method with changing the board state below and simply executing 
# this module 
#
if __name__ == "__main__":
    from state import KalahState
    state = KalahState(0)
    state._kalahs = [6,4]
    state._holes = [[0, 4, 8, 7, 2, 4], [0, 0, 0, 0, 0, 1]]
    method = MinMaxMethod(1, 1)
    print method.make_move(state)