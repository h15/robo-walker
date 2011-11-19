#!/usr/bin/env python

class Robot:
    """
        Class Robot is a model of N-leg robot.
        Each leg has M joints.
        Joints can moves in K dimensions.
    """
    
    def __init__(self, legs):
        """
            Init legs by angles' matrix.
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
            matrix[i][j] is the angle of i joint,
                         in j dimension rotation.
        """
        self.matrix = matrix;
    
    def getVector(self):
        """
            Get equivalent vector
            from robot's body to the ground.
        """
        pass

if __name__ == "__main__":
    pass
