from manim import *

class GenerateModel(Scene):
    def construct(self):
        sEqn = Tex(r'$S^{\prime} = r(S+A)(1-\frac{S+A+I}{K}) - S(\beta_1 E_c + \beta_2 E_p + \beta_3 A + \beta_4 I )$')
        aEqn = Tex(r'$A^{\prime} = S(\beta_1 E_c + \beta_2 E_p + \beta_3 A + \beta_4 I ) - \gamma A$')
        iEqn = Tex(r'$I^{\prime} = \gamma A - \alpha I$')
        ecEqn = Tex(r'$E_c^{\prime} = \alpha I - \delta_c E_c$')
        epEqn = Tex(r'$E_p^{\prime} = \epsilon_p I - \delta_p E_p$')

        eqnGroup = VGroup( sEqn, aEqn, iEqn, ecEqn, epEqn ).arrange(DOWN, aligned_edge=LEFT)

        bracket = MathTex(r"\left\{ \begin{array}{c} \\ \\ \\ \end{array} \right.")
        bracket.stretch_to_fit_height(eqnGroup.height)
        bracket.next_to(eqnGroup, LEFT, buff=0.1)

        eqn = VGroup(bracket, eqnGroup)
        eqn.move_to(ORIGIN)

        self.add( eqn )