from manim import *

class R0CalculatonIntro(Scene):
    def construct(self):
        ttl = Tex(r'$R_0$ Calculation').scale(2)
        ttl.move_to(ORIGIN)
        underline = Underline(ttl, color=GREEN)
        self.add(ttl, underline)

class InfectedClasses(Scene):
    def construct(self):
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

        box = SurroundingRectangle(VGroup(aEqn, iEqn, ecEqn, epEqn), color=RED)
        infClass = Text(f'Infected\nClasses', color=RED)
        infClass.next_to(box, RIGHT, buff=0.5)

        self.add( eqn, box, infClass )

class FMatrix(Scene):
    def construct(self):
        F = MathTex(r'F = \begin{bmatrix} \beta_1 S & \beta_2 S & \beta_3 S & \beta_4 S \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}').scale(2)
        self.add( F )

class VMatrix(Scene):
    def construct(self):
        V = MathTex(r'V = \begin{bmatrix} 0 & 0 & \gamma & 0 \\ 0 & 0 & -\gamma & \alpha \\ \delta_c & 0 & 0 & -\alpha \\ 0 & \delta_p & 0 & -\epsilon_p \end{bmatrix}').scale(2.3)
        self.add( V )

class InverseVMatrix(Scene):
    def construct(self):
        invV = MathTex(r'V^{-1} = \begin{bmatrix} \frac{1}{\delta_c} & \frac{1}{\delta_c} & \frac{1}{\delta_c} & 0 \\ \\ -\frac{\epsilon_p}{\alpha \delta_p} & -\frac{\epsilon_p}{\alpha \delta_p} & 0 & \frac{1}{\delta_p} \\ \\ \frac{1}{\gamma} & 0 & 0 & 0 \\ \\ \frac{1}{\alpha} & \frac{1}{\alpha} & 0 & 0 \end{bmatrix}').scale(1.5)
        self.add( invV )

class MatrixProduct(Scene):
    def construct(self):
        matProd = MathTex(r'FV^{-1} = \begin{bmatrix} S ( \frac{\beta_2}{\alpha} + \frac{\epsilon_p \beta_4}{\alpha \delta_p} + \frac{\beta_3}{\delta_c} + \frac{\beta_1}{\gamma} ) & S (\frac{\beta_2}{\alpha} + \frac{\epsilon_p \beta_4}{\alpha \delta_p} + \frac{\beta_3}{\delta_c}) & S \frac{\beta_3}{\delta_c} & S \frac{\beta_4}{\delta_p} \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{bmatrix}').scale(0.9)
        eigOne = Tex(r'$\lambda_1 = S ( \frac{\beta_2}{\alpha} + \frac{\epsilon_p \beta_4}{\alpha \delta_p} + \frac{\beta_3}{\delta_c} + \frac{\beta_1}{\gamma} )$')
        eig234 = Tex(r'$\lambda_2 = \lambda_3 = \lambda_4 = 0$')

        eigGroup = VGroup(eigOne, eig234).arrange(DOWN, center=True)
        eigGroup.next_to(matProd, DOWN, buff=0.4)

        totalText = VGroup( matProd, eigGroup )
        totalText.move_to(ORIGIN)

        box = SurroundingRectangle(eigOne, color=GREEN)
        R0Text = Tex(r'$R_0$ Value', color=GREEN)
        R0Text.next_to(box, RIGHT, buff=0.4)

        self.add( totalText, box, R0Text )

class R0Value(Scene):
    def construct(self):
        # R0Eqn1 = Tex(r'$S \frac{\beta_1 \alpha \delta_c \delta_p + \beta_2 \delta_c \delta_p \gamma + \beta_3 \alpha \delta_p \gamma + \beta_4 \delta_c \gamma \epsilon_p}{\alpha \delta_c \delta_p \gamma}$').scale(1.6)
        # altern = Tex(r'OR', color=BLUE)
        R0 = Tex(r'$R_0 =$ ', r'$S ($',r'$\frac{\beta_1}{\gamma} $', r' + ', r'$\frac{\beta_2}{\alpha}$', r' + ', r'$\frac{\beta_3}{\delta_c}$', r' + ', r'$\frac{\beta_4 \epsilon_p}{\alpha \delta_p}$', r'$)$').scale(2)
        # displayEqns = VGroup(R0Eqn1, altern, R0Eqn2).arrange(DOWN, center=True, buff=0.5)
        self.add( R0 )

class R0ValueAsymp(Scene):
    def construct(self):
        R0 = Tex(r'$R_0 =$ ', r'$S ($',r'$\frac{\beta_1}{\gamma} $', r' + ' + r'$\frac{\beta_2}{\alpha}$', r' + ', r'$\frac{\beta_3}{\delta_c}$', r' + ', r'$\frac{\beta_4 \epsilon_p}{\alpha \delta_p}$', r'$)$').scale(2)

        downBrace = Brace(R0[2], direction=DOWN, color=RED)
        upBrace = Brace(R0[2], direction=UP, color=BLUE)
        labelDown = downBrace.get_text(r'Rate of becoming\\fully symptomatic')
        labelUp = upBrace.get_text(r'Asymptomatic\\Transmission\\Rate')

        self.add( R0, downBrace, upBrace, labelDown, labelUp )

class R0ValueInfec(Scene):
    def construct(self):
        R0 = Tex(r'$R_0 =$ ', r'$S ($', r'$\frac{\beta_1}{\gamma} $', r' + ', r'$\frac{\beta_2}{\alpha}$', r' + ', r'$\frac{\beta_3}{\delta_c}$', r' + ', r'$\frac{\beta_4 \epsilon_p}{\alpha \delta_p}$', r'$)$').scale(2)

        downBrace = Brace(R0[4], direction=DOWN, color=RED)
        upBrace = Brace(R0[4], direction=UP, color=BLUE)
        labelDown = downBrace.get_text(r'Infected\\Death Rate')
        labelUp = upBrace.get_text(r'Infected\\Transmission\\Rate')

        self.add( R0, downBrace, upBrace, labelDown, labelUp )

class R0ValueCarcass(Scene):
    def construct(self):
        R0 = Tex(r'$R_0 =$ ', r'$S ($',r'$\frac{\beta_1}{\gamma} $', r' + ', r'$\frac{\beta_2}{\alpha}$', r' + ', r'$\frac{\beta_3}{\delta_c}$', r' + ', r'$\frac{\beta_4 \epsilon_p}{\alpha \delta_p}$', r'$)$').scale(2)

        downBrace = Brace(R0[6], direction=DOWN, color=RED)
        upBrace = Brace(R0[6], direction=UP, color=BLUE)
        labelDown = downBrace.get_text(r'Carcass\\Decay Rate')
        labelUp = upBrace.get_text(r'Carcass\\Transmission\\Rate')

        self.add( R0, downBrace, upBrace, labelDown, labelUp )

class R0ValuePlants(Scene):
    def construct(self):
        R0 = Tex(r'$R_0 =$ ', r'$S ($',r'$\frac{\beta_1}{\gamma} $', r' + ', r'$\frac{\beta_2}{\alpha}$', r' + ', r'$\frac{\beta_3}{\delta_c}$', r' + ', r'$\frac{\beta_4 \epsilon_p}{\alpha \delta_p}$', r'$)$').scale(2)

        downBrace = Brace(R0[8], direction=DOWN, color=RED)
        upBrace = Brace(R0[8], direction=UP, color=BLUE)
        labelDown = downBrace.get_text(r'CWD decay\\+\\Death Rate')
        labelUp = upBrace.get_text(r'Transmission\\Rates\\',r'from', r' and ', r'to',r'\\Plants')

        u1 = Underline(labelUp[1],color=YELLOW)
        u2 = Underline(labelUp[3],color=YELLOW)

        underlines = VGroup(u1, u2)

        self.add( R0, downBrace, upBrace, labelDown, labelUp, underlines )