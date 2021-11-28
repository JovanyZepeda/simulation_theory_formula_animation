from typing import Collection
from manim import *
from manim.utils import scale
import numpy as np
from numpy import dot


class SimSphereTest(ThreeDScene,MovingCameraScene):
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
                    xyz_coord[f"{var_index}"] = Dot3D(np.array([x,y,z]), radius= 0.1, resolution= (8,8), color= BLUE)
                    var_index = var_index+1
        
        #3D axis
        axes = ThreeDAxes()
######################################---------------------------------------############################################################
       
        # camera orientation
        self.camera.frame.save_state()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        self.add(axes)
        self.camera.frame.animate.scale(0.5)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.wait(2)

       
        # Add simDots
        for SimSphere in xyz_coord.values():
            self.add(SimSphere)
            self.wait(0.2)