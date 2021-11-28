from typing import Collection
from manim import *
from manim.utils import scale
import numpy as np
from numpy import dot


class simEqn(ThreeDScene):
    def construct(self):

######################################-----------------INITIALIZATION BEGINS!----------------------############################################################
        # MATH EQNS WITH LATEX
        eqntext = MathTex(
            "f_{sim}", # f sim
            "=", # equal sign
            "\\frac{f_p N H} {(f_p N H) + 1}", # un simplified equation
            "\\Rightarrow", # arrow pointing to the right
            "\\frac{f_p f_I N_I} {(f_p f_I N_I) + 1}" # 
        )

        simpEqn = MathTex(
            "f_{sim}", # f sim
            "=", # equal sign
            "\\frac{f_p f_I N_I} {(f_p f_I N_I) + 1}" #
        )

        props = MathTex(
            "f_p \\approx 0", # Prop 1 
            "f_I \\approx 0", # prop 2
            "f_{sim} \\approx 1" # porposition 3
        )

        # all porpositions in all variable
        prop1 = props[0].set_color(BLUE).align_on_border(LEFT)
        prop2 = props[1].set_color(BLUE).align_on_border(LEFT)
        prop3 = props[2].set_color(BLUE).align_on_border(LEFT)

        # Text to explain the propositions
        proptext1 = Tex('Human-like civilizations rarely reach a posthuman stage', font_size = 35) # explanation to prop 1
        proptext2 = Tex('There will be no individuals or civilizations that have an interest in creating simulations', font_size = 35) # explanation to prop 2
        proptext3 = Tex('There are a large number of human-like civilizations that are living in a simulation', font_size = 35) # explanation to prop 3

        # horizontal groups
        propPhrase1 = VGroup(prop1, proptext1).arrange(RIGHT)
        propPhrase2 = VGroup(prop2, proptext2).arrange(RIGHT)
        propPhrase3 = VGroup(prop3, proptext3).arrange(RIGHT)

        # vertical groups
        allPropPhrases =VGroup(propPhrase1,propPhrase2, propPhrase3).arrange(DOWN)

        # Dot! - The real civilization DOT
        dot1 = Dot3D(ORIGIN, color=RED).scale(2)

        # MANY DOTS! - The simulated Civilizations DOTS
        max_range = 2 # max -n and +n range for x y and z 
        xyz_coord = VDict() # dict for (var_index: [x,y,z] )

        var_index = 0 # index variable for the nested for loop

        # Create the coords
        for x in range(-max_range, max_range+1):
            for y in range(-max_range, max_range+1):
                for z in range(-max_range, max_range+1):
                    xyz_coord[f"{var_index}"] = Dot3D(np.array([x,y,z]), radius= 0.1, resolution= (8,8), color= BLUE)
                    var_index = var_index+1
        
        # Create a group of 3D Dots
        DotGroup = VGroup()

        for dot_coords in xyz_coord.get_all_submobjects():
            DotGroup.add(*[dot_coords])

######################################-----------------ANIMATION BEGINS!----------------------############################################################
        # Animate the main equations
        self.play(Write(eqntext[0]),Write(eqntext[1]),Write(eqntext[2])) # frist half of eqn
        self.wait(1)

        self.play(Write(eqntext[3]), Write(eqntext[4])) # second half of eqn
        self.wait(1)

        self.play(ReplacementTransform(eqntext,simpEqn)) # Replace eqn with simplified version
        self.wait(5)

        self.play(simpEqn.animate.shift(2*UP)) # move simplified eqn up for more room

        # Animate the explanations and propositions
        self.play(Write(allPropPhrases[0]))
        self.wait(5)

        self.play(Write(allPropPhrases[1].shift(DOWN)))
        self.wait(5)

        self.play(Write(allPropPhrases[2].shift(2*DOWN)))
        self.wait(5)

        # Remove everything and replace it with a dot
        self.play(ReplacementTransform(allPropPhrases,dot1), ReplacementTransform(simpEqn,dot1))
        self.wait(1)

        # camera orientation to 3D
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES, zoom= 2.5)
        self.begin_3dillusion_camera_rotation(rate=0.2)

        # see the REAL Dot!
        self.wait(2)

        # BRING ALL THE FAKE DOTS!
        self.play(Transform(dot1,DotGroup))
        self.wait(8)

        #Remove everything
        self.play(FadeOut(dot1))