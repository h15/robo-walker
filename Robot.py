#!/usr/bin/env python

class Robot:
    """
        Class Robot is a model of four-leg robot.
        Each leg has 2 joints. 1st joint can move in two dimensions.
        2nd joint moves in one only.
    """
    
    
    
    def __init__(self, legCount):
        

class Leg:
    """
        Class Robot has 4 legs. This is class for it's leg.
        Class Leg has 2 joints. 1st joint can move in two dimensions.
        2nd joint moves in one only.
    """
    
    def __init__(self, a1, a2, b1):
        """
            a1 and a2 are the angles of 1st joint rotation.
            b1 is the angle of 2nd joint rotation.
        """
        self.a1 = a1;
        self.a2 = a2;
        self.b1 = b1;

if __name__ == "__main__":
    pass
