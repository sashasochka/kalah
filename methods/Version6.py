#!/usr/bin/env python2
import sys
if __name__ == "__main__":
    from method import Method
else:
    from methods.method import Method

precomputed = lambda state: {
    # <ideal game>
   ((5, 5, 5, 5, 5, 5), (5, 5, 5, 5, 5, 5)): 1 # p1 start
 , ((5, 0, 6, 6, 6, 6), (5, 5, 5, 5, 5, 5)): 2 # p1 continue
 , ((6, 6, 5, 5, 5, 5), (5, 0, 0, 7, 7, 7)): 0 # defense for p2 after move of p1
 , ((0, 7, 6, 6, 6, 6), (5, 0, 0, 7, 7, 7)): 3 # continue previous for p2
    # </ideal game>

 # <alt defense>
 , ((6, 6, 6, 5, 5, 5), (5, 0, 6, 0, 7, 7)): 0 # defense for p2 after move of p1
 , ((0, 7, 7, 6, 6, 6), (5, 0, 6, 0, 7, 7)): 5 # continue previous for p2
  # <attack>
 , ((6, 1, 7, 1, 8, 7), (0, 7, 7, 6, 6, 0)): 0 # p1
 , ((0, 2, 8, 2, 9, 9), (0, 7, 7, 6, 6, 0)): 3 # cont p1
  # </attack>
 , ((0, 7, 0, 7, 7, 1), (1, 1, 10, 3, 9, 9)): 2 # p2
 # </alt defense>
 , ((0, 6, 6, 6, 6, 6), (5, 5, 5, 5, 5, 5)): 1 # p2 ?? separate
# gener
,((5,5,5,5,5,5),(5,5,5,5,5,5)):1
,((5,0,6,6,6,6),(5,5,5,5,5,5)):2
,((6,6,5,5,5,5),(5,0,0,7,7,7)):0
,((0,7,6,6,6,6),(5,0,0,7,7,7)):5
,((6,1,1,8,8,7),(0,7,6,6,6,0)):0
,((0,2,2,9,9,8),(0,7,6,6,6,0)):4
,((1,8,7,7,7,0),(0,2,2,9,0,9)):1
,((1,3,3,9,0,9),(1,0,8,8,8,1)):3
,((2,1,9,9,9,2),(1,3,3,0,1,10)):0
,((1,3,3,0,1,10),(0,2,10,9,9,2)):5
,((1,3,11,10,10,3),(2,4,4,0,1,0)):2
,((3,5,5,1,2,1),(2,3,0,11,11,4)):5
,((3,5,5,1,2,0),(2,3,0,11,11,4)):4
,((3,5,5,1,0,1),(2,3,0,11,11,4)):5
,((3,5,5,1,0,0),(2,3,0,11,11,4)):1
,((3,0,6,2,1,1),(2,3,0,11,11,4)):5
,((3,0,6,2,1,0),(2,3,0,11,11,4)):3
,((0,3,0,11,11,4),(3,0,6,0,2,0)):5
,((4,1,7,0,2,0),(0,3,0,11,11,0)):4
,((4,1,7,0,0,1),(0,3,0,11,11,0)):5
,((4,1,7,0,0,0),(0,3,0,11,11,0)):0
,((0,0,0,11,11,0),(0,2,8,1,0,0)):3
,((1,3,9,2,0,1),(1,0,0,0,12,1)):5
,((1,3,9,2,0,0),(1,0,0,0,12,1)):3
,((0,0,0,0,12,1),(1,3,9,0,1,0)):5
,((0,0,0,0,12,0),(1,3,9,0,1,0)):4
,((2,4,0,1,2,1),(1,1,1,0,0,1)):4
,((2,4,0,1,0,2),(1,1,1,0,0,1)):3
,((1,0,1,0,0,1),(2,4,0,0,0,2)):2
,((2,4,0,0,0,2),(1,0,0,0,0,1)):0
,((1,0,0,0,0,1),(0,5,0,0,0,2)):5
,((1,0,0,0,0,0),(0,5,0,0,0,2)):0
}.get(state, None)

class Version6Method(Method):
    _name = "Version6"
    _short_name = "Version6"

    def __init__(self, player_num, ai_level=4):
        super(Version6Method, self).__init__(player_num, ai_level)
        self._ai_level = ai_level + 2

    def _other_player(self):
        return (self._player + 1) % 2

    def _terminal_test(self, state, player, depth=0):
#        print(player, state.to_string(), depth, self._ai_level)
        return depth >= self._ai_level or state.is_finished(player)

    def _utility(self, state):
        utility = [0,0]
        for player in (self._player,self._other_player()):
            u = utility[player] = state.player_kalah(player)
            for index, stones in enumerate(state.player_holes(player)):
                u += min(stones, 6 - index)
                if stones + index >= 7:
                    u -= min(stones + index - 6 , 6)
                if stones + index >= 13:
                    u += 14 - stones - index


        return utility[self._player] - utility[self._other_player()]

    def _max_value(self, state, depth=1):
        if self._terminal_test(state, self._player, depth):
            return self._utility(state)
        value = -float('inf')
        neighbors = state.get_all_neighbors(self._player)
        for new_state in neighbors:
            value = max(value, self._min_value(new_state['state'], depth + 1))
            print('St', new_state['state'].to_string())
        return value

    def _min_value(self, state, depth=1):
        if self._terminal_test(state, self._other_player(), depth):
#            print("   "*depth, state.to_string(), self._utility(state))
            return self._utility(state)
        value = float('inf')
        neighbors = state.get_all_neighbors(self._other_player())
        for new_state in neighbors:
            value = min(value, self._max_value(new_state['state'], depth + 1))
            print('St', new_state['state'].to_string())
        return value

    def make_move(self, state):
        print("Input state:", state.to_string())

        # States
        my_state = tuple(state.player_holes(self._player))
        opp_state = tuple(state.player_holes(self._other_player()))
        state_tup = (my_state, opp_state)
        # States with kalahs
        my_state_with_kalah = (my_state, state.player_kalah(self._player))
        opp_state_with_kalah = (opp_state, state.player_kalah(self._other_player()))
        state_tup_with_kalah = (my_state_with_kalah, opp_state_with_kalah)

        # Try precomputed value
        precomp = precomputed(state_tup)
        if precomp is not None:
            print('Using precomputed move')
            return precomp

        #with open('exp_data.txt', 'a') as logfile:
        #    logfile.write(state_tup)
        #    logfile.write('\n')

        # Minimax algorithm
        neighbors = state.get_all_neighbors(self._player)
        best_value, best_state = -float('inf'), None
        for new_state in neighbors:
            value = self._min_value(new_state['state'])
            if best_value < value :
                best_value, best_state = value, new_state
        print(best_value, best_state['state'].to_string())
        return best_state['hole'][0]


if __name__ == "__main__":
    from state import KalahState
    state = KalahState(0)
    state._kalahs = [0, 0]
    all_holes = map(int, sys.argv[1:])
    assert(len(all_holes) == 12)
    state._holes = [all_holes[:6], all_holes[6:]]
    method = Version6Method(1, 3)
    print(method.make_move(state))

