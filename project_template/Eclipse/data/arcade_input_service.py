import sys
from data.point import Point

import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []

        self._attack = False
    
    def set_key(self, key, modifiers):
        #Ignoring modifies ar this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = 0

        if arcade.key.LEFT in self._keys:
            x = -1
        elif arcade.key.RIGHT in self._keys:
            x = 1
        if arcade.key.UP in self._keys:
            y = 1
        elif arcade.key.DOWN in self._keys:
            y = -1

        if arcade.key.SPACE in self._keys:
                self._attack = True

        velocity = Point(x, y)
        return velocity
            
    def get_attack(self):
        #if arcade.key.SPACE in self._keys:
        #        self._attack = True
                #print("ATTACK")
        return self._attack

    def end_attack(self):
        self._attack = False
