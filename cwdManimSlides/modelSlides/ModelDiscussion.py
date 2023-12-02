from manim import *

class ModelDiscussion(Scene):
    def construct(self):
        ttl = Tex(r'Model Discussion').scale(2)
        ttl.move_to(ORIGIN)
        underline = Underline(ttl, color=RED)
        self.add(ttl, underline)