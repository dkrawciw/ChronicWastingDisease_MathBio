from manim import *
from numpy import genfromtxt, array
import matplotlib.pyplot as plt

class VerificationIntro(Scene):
    def construct(self):
        ttl = Tex(r'Verification and Results').scale(2)
        ttl.move_to(ORIGIN)
        underline = Underline(ttl, color=BLUE)
        self.add(ttl, underline)

class ShowBifurcationGraph(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-0.001, 0.1,0.0091], 
            y_range=[-0.001, 0.1,0.0091], 
            z_range=[0, 55,1],
            x_length=7,
            y_length=7,
            z_length=7
        )
        roots = genfromtxt('bifurcationData.csv', delimiter=',')

        dots = []

        for i in range( len(roots[:,0]) ):
            dots.append( Dot3D(point=roots[i,:], radius=0.1, color=BLUE) )

        for dot in dots:
            self.add(dot)
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=45*DEGREES, zoom=0.01)
        self.add(axes)
        self.begin_ambient_camera_rotation(rate=2)
        self.wait(2)