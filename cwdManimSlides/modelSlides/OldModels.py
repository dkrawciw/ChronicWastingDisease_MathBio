from manim import *

class FirstModelDescribe(Scene):
    def construct(self):
        oldModel = Text('First Liturature Model')
        titleUnderline = Underline(oldModel)
        oldModelTitle = VGroup(oldModel, titleUnderline)

        dS = Tex(r'$S^{\prime} =$ Susceptible')
        dI = Tex(r'$I^{\prime} =$ Infected')
        dE = Tex(r'$E^{\prime} =$ Environmental')
        dP = Tex(r'$P^{\prime} =$ Predator')

        eqns = VGroup(dS, dI, dE, dP).arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\left\{ \begin{array}{c} \\ \\ \\ \end{array} \right.")
        bracket.stretch_to_fit_height(eqns.height)
        bracket.next_to(eqns, LEFT, buff=0.1)

        oldModel1 = VGroup(eqns, bracket)
        oldModel1.move_to(ORIGIN)
        oldModelTitle.next_to(oldModel1, direction=UP,buff=0.7)

        self.add( oldModel1, oldModelTitle )

class GenerateOldModel(Scene):
    def construct(self):
        oldModel = Text('First Liturature Model')
        titleUnderline = Underline(oldModel)
        oldModelTitle = VGroup(oldModel, titleUnderline)

        dS = Tex(r'$S^{\prime} = S( r(1 - \frac{S+I}{k}) - \beta E )$')
        dI = Tex(r'$I^{\prime} = \beta S E - \mu I - \frac{a I P}{m + I}$')
        dE = Tex(r'$E^{\prime} = \epsilon I - \tau E$')
        dP = Tex(r'$P^{\prime} = \frac{b I}{m + I} - d$')

        eqns = VGroup(dS, dI, dE, dP).arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\left\{ \begin{array}{c} \\ \\ \\ \end{array} \right.")
        bracket.stretch_to_fit_height(eqns.height)
        bracket.next_to(eqns, LEFT, buff=0.1)

        oldModel1 = VGroup(eqns, bracket)
        oldModel1.move_to(ORIGIN)
        oldModelTitle.next_to(oldModel1, direction=UP,buff=0.7)

        self.add( oldModel1,oldModelTitle )

class CritiqueOldModel1(Scene):
    def construct(self):
        oldModel = Text('First Liturature Model')
        titleUnderline = Underline(oldModel)
        oldModelTitle = VGroup(oldModel, titleUnderline)

        dS = Tex(r'$S^{\prime} = S( r(1 - \frac{S+I}{k}) - \beta E )$')
        dA = Tex(r'$A^{\prime} =$ Asymptomatic', color=BLUE)
        dI = Tex(r'$I^{\prime} = \beta S E - \mu I - \frac{a I P}{m + I}$')
        dE = Tex(r'$E^{\prime} = \epsilon I - \tau E$')
        dP = Tex(r'$P^{\prime} = \frac{b I}{m + I} - d$')

        eqns = VGroup(dS, dA, dI, dE, dP).arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\left\{ \begin{array}{c} \\ \\ \\ \end{array} \right.")
        bracket.stretch_to_fit_height(eqns.height)
        bracket.next_to(eqns, LEFT, buff=0.1)

        oldModel1 = VGroup(eqns, bracket)
        oldModel1.move_to(ORIGIN + 3*LEFT)
        oldModelTitle.move_to(ORIGIN + 3*UP)

        box1 = SurroundingRectangle(dS, color=GREEN)
        box2 = SurroundingRectangle(VGroup(dI,dE), color=GREEN)
        box3 = SurroundingRectangle(dP, color=RED)

        goodParts = Text('Helpful Components', color=GREEN, font_size=30)
        missingPart = Text('Missing Component', color=BLUE, font_size=30)
        badParts = Text('Unhelpful Component', color=RED, font_size=30)
        critique = VGroup(goodParts, missingPart, badParts).arrange(DOWN, aligned_edge=LEFT)
        critique.move_to(ORIGIN + 3*RIGHT)

        self.add( oldModel1,oldModelTitle,box1,box2,box3,critique )