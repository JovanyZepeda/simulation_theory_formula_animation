from typing import Collection
from manim import *
from manim.utils import scale
import numpy as np
from numpy import dot


class testDots(ThreeDScene):
    def construct(self):
        
        # Dot! - The real civilization DOT
        dot1 = Dot(color=RED).scale(2)

        # MANY DOTS! - The simulated Civilizations DOTS
        max_range = 1 # max -n and +n range for x y and z 
        xyz_coord = dict() # dict for (var_index: [x,y,z] )

        var_index = 0 # index variable for the nested for loop

        for x in range(-max_range, max_range+1):
            for y in range(-max_range, max_range+1):
                for z in range(-max_range, max_range+1):
                    xyz_coord[f"{var_index}"] = Dot(np.array([x,y,z]))
                    var_index = var_index+1
        
        #3D axis
        axes = ThreeDAxes()
######################################---------------------------------------############################################################
       
        # camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(2)

        #add real dot
        self.add(dot1)

        # Add simDots
        for SimDots in xyz_coord.values():
            self.add(SimDots)
            self.wait(0.2)