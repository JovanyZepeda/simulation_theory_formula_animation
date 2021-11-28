from typing import Collection
from manim import *
from manim.utils import scale
import numpy as np
from numpy import dot


class SimSphereTest(ThreeDScene, MovingCamera):
    def construct(self):
        
        # Dot! - The real civilization DOT
        dot1 = Dot3D(ORIGIN, color=RED).scale(2)

        # MANY DOTS! - The simulated Civilizations DOTS
        max_range = 2 # max -n and +n range for x y and z 
        # xyz_coord = dict() # dict for (var_index: [x,y,z] )
        xyz_coord = VDict() # dict for (var_index: [x,y,z] )

        var_index = 0 # index variable for the nested for loop

        for x in range(-max_range, max_range+1):
            for y in range(-max_range, max_range+1):
                for z in range(-max_range, max_range+1):
                    xyz_coord[f"{var_index}"] = Dot3D(np.array([x,y,z]), radius= 0.1, resolution= (8,8), color= BLUE)
                    var_index = var_index+1
        
######################################---------------------------------------############################################################
       # add real dot
        self.add(dot1)
        self.wait(3)


        # camera orientation
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom= 5)
        self.begin_3dillusion_camera_rotation(rate=0.2)

        self.wait(10)

        # # Add simDots
        # SphereGroup = VGroup()

        # for SimSphere in xyz_coord.get_all_submobjects():
        #     SphereGroup.add(*[SimSphere])

        # self.play(ReplacementTransform(dot1,SphereGroup))
        # self.wait(3)