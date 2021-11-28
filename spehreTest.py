from manim import *

class ExampleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        sphere1 = Sphere(
            center=(3, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        sphere1.set_color(RED)
        self.add(sphere1)
        sphere2 = Sphere(center=(-1, -3, 0), radius=2, resolution=(18, 18))
        sphere2.set_color(GREEN)
        self.add(sphere2)
        sphere3 = Sphere(center=(-1, 2, 0), radius=2, resolution=(16, 16))
        sphere3.set_color(BLUE)
        self.add(sphere3)