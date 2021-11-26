from typing import Collection
from manim import *

class simEqn(Scene):
    def construct(self):
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

        proptext1 = Tex('Human-like civilizations rarely reach a posthuman stage', font_size = 35) # explanation to prop 1
        proptext2 = Tex('There will be no individuals or civilizations that have an interest in creating simulations', font_size = 35) # explanation to prop 2
        proptext3 = Tex('There are a large number of human-like civilizations that are living in a simulation', font_size = 35) # explanation to prop 3

        # horizontal groups
        propPhrase1 = VGroup(prop1, proptext1).arrange(RIGHT)
        propPhrase2 = VGroup(prop2, proptext2).arrange(RIGHT)
        propPhrase3 = VGroup(prop3, proptext3).arrange(RIGHT)

        # vertical groups
        allPropPhrases =VGroup(propPhrase1,propPhrase2, propPhrase3).arrange(DOWN)

        # Animate the main equations
        self.play(Write(eqntext[0]),Write(eqntext[1]),Write(eqntext[2])) # frist half of eqn
        self.wait()

        self.play(Write(eqntext[3]), Write(eqntext[4])) # second half of eqn
        self.wait(1)

        # self.play(FadeOut(eqntext)) # remove unsimplified eqn

        # self.play(Write(simpEqn)) # insert simplified eqn

        self.play(ReplacementTransform(eqntext,simpEqn))
        self.wait()

        self.play(simpEqn.animate.shift(2*UP)) # move simp eqn up for more room

        # Animate the explanations and propositions
        self.play(Write(allPropPhrases[0]))
        self.wait(4)

        self.play(Write(allPropPhrases[1].shift(DOWN)))
        self.wait(4)

        self.play(Write(allPropPhrases[2].shift(2*DOWN)))
        self.wait(4)

        #remove everything
        self.play(FadeOut(simpEqn), FadeOut(allPropPhrases))