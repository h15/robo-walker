#!/usr/bin/env python

from math import sin, cos, sqrt, acos, degrees

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
        [ A, B, C, D ] = self.getGroundConstants( self.legs[0], self.legs[1], self.legs[2] );
        height = Vector( A, B, C );
        
        angles = [];
        
        # if sum of 3 angles of 3 fixed points and heigh eq. 360 - it's good.
        for i in range( len(self.legs) ):
            for j in range( i + 1, len(self.legs) ):
                for k in range( j + 1, len(self.legs) ):
                    # calc angles with caching
                    if ( angles[i][j] == None ):
                        angles[i][j] = getAngle( height, self.legs[i], leg1[j] );
                    if ( angles[j][k] == None ):
                        angles[j][k] = getAngle( height, self.legs[j], leg1[k] );
                    if ( angles[i][k] == None ):
                        angles[j][k] = getAngle( height, self.legs[j], leg1[k] );
                    
                    if fabs ( angles[i][j] + angles[j][k] + angles[i][k] - 360 ) < 1:
                        return True;
        return False;
    
    def isAllLegsOnTheGround(self, ground):
        [ A, B, C, D ] = ground;
        
        for leg in self.legs:
            if fabs( A * leg.x + B * leg.y + C * leg.z - D ) > 1:
                return False;
        
        return True;
    
    def getGroundConstants(self, Leg1, Leg2, Leg3):
        """
            Get equation of the plane by 
            Ax + By + Cz = D
        """ 
        L1 = Leg1.vector;
        L2 = Leg2.vector;
        L3 = Leg3.vector;
        
        A = ( (L2.y - L1.y) * (L3.z - L1.z) - (L2.z - L1.z) * (L3.y - L1.y) );
        B = ( (L2.x - L1.x) * (L3.z - L1.z) - (L2.z - L1.z) * (L3.x - L1.x) );
        C = ( (L2.x - L1.x) * (L3.y - L1.y) - (L2.y - L1.y) * (L3.x - L1.x) );
        
        D = L1.x * A - L1.y * B + L1.z * C;
        
        return [ A, B, C, D ];
    
    def getAngle( height, leg1, leg2 ):
        a = b = height;
        a.sub(leg1.vector);
        b.sub(leg2.vector);
        
        angle = degrees(acos ( a.smul(b) / (a.len * b.len) ));
        angle %= 180;
        
        return angle;

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
    
    def sub(self, vector):
        self.x -= vector.x;
        self.y -= vector.y;
        self.z -= vector.z;
    
    def abs(self):
        """
            |self|
        """
        return sqrt( self.x * self.x + self.y * self.y + self.z * self.z );
    
    def smul(self, vector):
        """
            Scalar multiplication.
        """
        return ( self.x * vector.x + self.y * vector.y + self.z * vector.z );
        
if __name__ == "__main__":
    pass
