#!/usr/bin/env python

from math  import sin, cos
#from numpy import *

class Robot:
    """
        Class Robot is a model of N-leg robot.
        Each leg has M joints.
        Joints can moves in 2 dimensions.
    """
    
    def __init__(self, legs):
        """
            Init legs by angles' matrix
            and legs' length vector.
        """
        for matrix in legs:
            leg = Leg(matrix);
            self.legs.append(leg);
    
    def stability(self):
        """
            Check the robot.
            Is it's position stable?
        """
        pass
    
    def onGround(self):
        """
            Check the robot.
            Are all legs on the ground?
        """
        pass

class Leg:
    """
        Robot's leg.
    """
    
    def __init__(self, matrix):
        """
            matrix[i][0] - phalanx' length.
            matrix[i][j] - the angle of i joint,
                           in j - 1 dimension rotation.
        """
        j = Joint(1,0,0);
        self.vector = Vector(0,0,0);
        
        for m in matrix:
            j = Joint( m[0], m[1] + j.vertical, m[2] + j.horizontal );
            self.joints.append( j );
            self.vector.add( j.vector );
        

class Joint:
    """
        Joint of robot's leg.
    """
    
    def __init__(self, length, vertical, horizontal):
        self.length = length;
        self.vertical = vertical;
        self.horizontal = horizontal;
        self.vector = Vector( self.length * cos( self.horizontal ) , \
                              self.length * sin( self.vertical   ) , \
                              self.length * cos( self.vertical   ) );

class Vector:
    """
        XYZ
    """
    
    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;
    
    def add(self, vector):
        self.x += vector.x;
        self.y += vector.y;
        self.z += vector.z;

if __name__ == "__main__":
    pass
