from manim import *

class IntroduceModel(Scene):
    def construct(self):
        introText = Text('Our Model')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        susceptible = Tex(r'$S^{\prime} = $ susceptible')
        asymptomatic = Tex(r'$A^{\prime} = $ asymptomatic')
        infected = Tex(r'$I^{\prime} = $ infected')
        environmentC = Tex(r'$E_c^{\prime} = $ environment (carcasses)')
        environmentP = Tex(r'$E_p^{\prime} = $ environment (plants)')

        introGroup = VGroup(susceptible, asymptomatic, infected, environmentC, environmentP).arrange(DOWN, aligned_edge=LEFT)

        bracket1 = MathTex(r"\left\{ \begin{array}{c} \\ \\ \\ \end{array} \right.")
        bracket1.stretch_to_fit_height(introGroup.height)
        bracket1.next_to(introGroup, LEFT, buff=0.1)

        intro = VGroup(introGroup, bracket1)
        intro.move_to(ORIGIN)
        topText.next_to(intro, UP, buff=0.8)

        self.add( intro, topText )

class GenerateModel(Scene):
    def construct(self):
        introText = Text('Our Model')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        sEqn = Tex(r'$S^{\prime} = r(S+A)(1-\frac{S+A+I}{K}) - S(\beta_1 A + \beta_2 I + \beta_3 E_c + \beta_4 E_p )$')
        aEqn = Tex(r'$A^{\prime} = S(\beta_1 A + \beta_2 I + \beta_3 E_c + \beta_4 E_p ) - \gamma A$')
        iEqn = Tex(r'$I^{\prime} = \gamma A - \alpha I$')
        ecEqn = Tex(r'$E_c^{\prime} = \alpha I - \delta_c E_c$')
        epEqn = Tex(r'$E_p^{\prime} = \epsilon_p I - \delta_p E_p$')

        eqnGroup = VGroup( sEqn, aEqn, iEqn, ecEqn, epEqn ).arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\left\{ \begin{array}{c} \\ \\ \\ \end{array} \right.")
        bracket.stretch_to_fit_height(eqnGroup.height)
        bracket.next_to(eqnGroup, LEFT, buff=0.1)

        eqn = VGroup(bracket, eqnGroup)
        eqn.move_to(ORIGIN)
        topText.next_to(eqn, UP, buff=0.8)

        self.add( topText, eqn )