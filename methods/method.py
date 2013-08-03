#!/usr/bin/env python
"""Contains abstract basic class for searching methods for playing Kalah.

Contains class Method that declares general functions for the real methods. 
Also it implements some functions that a similar for all searching methods.

All methods should be inherited from the Method class.

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

class Method(object):
    
    _name = "Unknown"
    _short_name = "Unknown"
    _run_time_limit = 60
    _player = 1
    _disabled = False
    _ai_level = 1
    
    def __init__(self, player_num, ai_level=1):
        self._player = player_num
        self._ai_level = ai_level
    
    def name(self):
        return self._name
        
    def short_name(self):
        return self._short_name
    
    def is_disabled(self):
        return self._disabled
        
    def set_run_time_limit(self, run_time_limit):
        self._run_time_limit = run_time_limit
        
    def set_player(self, player_num):
        self._player = player_num
        
    def make_move(self, state):
        """
        Returns hole number
        """
        return -1