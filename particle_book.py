# particle.py
from __future__ import print_function
from scipy import constants as constants

#def possible_flavors():
 #   return["up","down","top","bottom","strange","charm"]

class Particle(object):
    """A particle is a constituent unit of the universe.
    128

    Attributes
    ----------

    c : charge in units of [e]
    m : mass in units of [kg]
    r : position in units of [meters]
    """
    roar = "I am a particle!"

    def __init__(self, charge, mass, position):
        """Initializes the particle with supplied values for
        charge c, mass m, and position r.
        """
        self.c = charge
        self.m = mass
        self.r = position

    def hear_me(self):
        myroar = self.roar + (
            "\n My charge is:      " + str(self.c) +
            "\n My mass is:        " + str(self.m) +
            "\n My x position is:  " + str(self.r['x']) + 
            "\n My y position is:  " + str(self.r['y']) + 
            "\n My z position is:  " + str(self.r['z'])
        )
        print(myroar)
    
    def delta_x_min(self, delta_p_x):
        hbar = constants.hbar
        delx_min = hbar / (2.0 * delta_p_x)
        return delx_min
    #@staticmethod
    #def possible_flavors():
     #   return ["up", "down", "top", "bottom", "strange", "charm"]
    
    