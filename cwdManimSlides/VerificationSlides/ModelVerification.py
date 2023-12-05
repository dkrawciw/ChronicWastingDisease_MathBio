from manim import *
from numpy import genfromtxt, array
import matplotlib.pyplot as plt

class VerificationIntro(Scene):
    def construct(self):
        ttl = Tex(r'Verification and Results').scale(2)
        ttl.move_to(ORIGIN)
        underline = Underline(ttl, color=BLUE)
        self.add(ttl, underline)

class Denominators(Scene):
    def construct(self):
        R0 = Tex(r'$R_0 =$ ', r'$S(\frac{\beta_1}{\gamma} + \frac{\beta_2}{\alpha} + \frac{\beta_3}{\delta_c} + \frac{\beta_4 \epsilon_p}{\alpha \delta_p})$').scale(2)
        denBrace = Brace(R0[1], direction=DOWN, color=RED)
        denText = denBrace.get_text(r'$\gamma$, $\alpha$, $\delta_c$, $\delta_p$ $\not= 0$\\Otherwise CWD Will Diverge')
        self.add( R0, denBrace, denText)