from manim import *

class IntroTitle(Scene):
    def construct(self):
        ttl = Tex(r'Chronic Wasting Disease').scale(2.3)
        groupMembers = Tex(r'Michael DiChellis, Joey Dutton, Daniel Krawciw\\Seth Lewicki, Logan Pike, Ryan Pike', color=BLUE).scale(0.7)

        ttlPage = VGroup(ttl, groupMembers).arrange(DOWN, buff=0.5)
        ttlPage.move_to(ORIGIN)

        self.add(ttlPage)