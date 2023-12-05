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

class AnalyzeModelSusceptible(Scene):
    def construct(self):
        introText = Text('Susceptible')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        sEqn = Tex(r'$S^{\prime} =$ ', r'$r$', r'$(S+A)(1-$', r'$\frac{S+A+I}{K}$', r'$)$', r' $-$ ', r'$S(\beta_1 A + \beta_2 I + \beta_3 E_c + \beta_4 E_p )$')

        eqnGroup = VGroup( sEqn ).arrange(DOWN, aligned_edge=LEFT)
        eqnGroup.move_to(ORIGIN)
        topText.move_to(ORIGIN+3*UP)

        rBrace = Brace(sEqn[1], direction=UP, color=GREEN)
        rLabel = rBrace.get_text(r'$r \rightarrow$ Maximum\\Growth Rate')
        explainR = VGroup(rBrace, rLabel)

        kBrace = Brace(sEqn[3], direction=DOWN, color=GREEN)
        kLabel = kBrace.get_text(r'$K \rightarrow$ Maximum\\Carrying Capacity')
        explainK = VGroup(kBrace, kLabel)

        betaBrace = Brace(sEqn[6], direction=UP, color=GREEN)
        betaLabel = betaBrace.get_text(r'$\beta \rightarrow$ Transmission Rates')
        explainBeta = VGroup(betaBrace, betaLabel)

        self.add( topText, eqnGroup, explainR, explainK, explainBeta )

class AnalyzeModelAsymptomatic(Scene):
    def construct(self):
        introText = Text('Asymptomatic')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        aEqn = Tex(r'$A^{\prime} =$ ', r'$S(\beta_1 A + \beta_2 I + \beta_3 E_c + \beta_4 E_p )$', r' $-$ ', r'$\gamma A$').scale(1.4)

        eqnGroup = VGroup( aEqn ).arrange(DOWN, aligned_edge=LEFT)
        eqnGroup.move_to(ORIGIN)
        topText.move_to(ORIGIN+3*UP)

        betaBrace = Brace(aEqn[1], direction=UP, color=BLUE)
        betaLabel = betaBrace.get_text(r'$\beta \rightarrow$ Transmission Rates')
        explainBeta = VGroup(betaBrace, betaLabel)

        gammaBrace = Brace(aEqn[3], direction=DOWN, color=BLUE)
        gammaLabel = gammaBrace.get_text(r'$\gamma \rightarrow$ Rate of\\becoming fully\\symptomatic')
        gammaLabel.shift(LEFT)
        explainGamma = VGroup(gammaBrace, gammaLabel)

        self.add( topText, eqnGroup, explainBeta, explainGamma )

class AnalyzeModelInfected(Scene):
    def construct(self):
        introText = Text('Infected (Fully Symptomatic)')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        iEqn = Tex(r'$I^{\prime} =$ ', r'$\gamma A$', r' $-$ ', r'$\alpha I$').scale(2)

        eqnGroup = VGroup(iEqn).arrange(DOWN, aligned_edge=LEFT)
        eqnGroup.move_to(ORIGIN)
        topText.move_to(ORIGIN+3*UP)

        gammaBrace = Brace(iEqn[1], direction=UP, color=RED)
        gammaLabel = gammaBrace.get_text(r'$\gamma \rightarrow$ Rate of becoming\\fully symptomatic')
        explainGamma = VGroup(gammaBrace, gammaLabel)

        alphaBrace = Brace(iEqn[3], direction=DOWN, color=RED)
        alphaLabel = alphaBrace.get_text(r'$\alpha \rightarrow$ Death Rate')
        explainAlpha = VGroup(alphaBrace, alphaLabel)

        self.add( topText, eqnGroup, explainGamma, explainAlpha )

class AnalyzeModelCarcasses(Scene):
    def construct(self):
        introText = Text('Environment (Carcasses)')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        ecEqn = Tex(r'$E_c^{\prime} =$ ', r'$\alpha I$', r' $-$ ', r'$\delta_c E_c$').scale(2)

        eqnGroup = VGroup(ecEqn).arrange(DOWN, aligned_edge=LEFT)
        eqnGroup.move_to(ORIGIN)
        topText.move_to(ORIGIN+3*UP)

        alphaBrace = Brace(ecEqn[1], direction=UP, color=YELLOW)
        alphaLabel = alphaBrace.get_text(r'$\alpha \rightarrow$ Death Rate')
        explainAlpha = VGroup(alphaBrace, alphaLabel)

        deltaCBrace = Brace(ecEqn[3], direction=DOWN, color=YELLOW)
        deltaCLabel = deltaCBrace.get_text(r'$\delta_c \rightarrow$ Decay Rate\\of carcasses')
        explainDeltaC = VGroup(deltaCBrace, deltaCLabel)

        self.add( topText, eqnGroup, explainAlpha, explainDeltaC )

class AnalyzeModelPlants(Scene):
    def construct(self):
        introText = Text('Environment (Plants)')
        underline = Underline(introText)
        topText = VGroup(introText, underline)

        epEqn = Tex(r'$E_p^{\prime} =$ ', r'$\epsilon_p I$', r' $-$ ', r'$\delta_p E_p$').scale(2)

        eqnGroup = VGroup(epEqn).arrange(DOWN, aligned_edge=LEFT)
        eqnGroup.move_to(ORIGIN)
        topText.move_to(ORIGIN+3*UP)

        epsilonBrace = Brace(epEqn[1], direction=UP, color=ORANGE)
        epsilonLabel = epsilonBrace.get_text(r'$\epsilon_p \rightarrow$ Rate of Plants\\Carrying CWD')
        explainEpsilon = VGroup(epsilonBrace, epsilonLabel)

        deltaPBrace = Brace(epEqn[3], direction=DOWN, color=ORANGE)
        deltaPLabel = deltaPBrace.get_text(r'$\delta_c \rightarrow$ Decay Rate of\\CWD in Plants')
        explainDeltaC = VGroup(deltaPBrace, deltaPLabel)

        self.add( topText, eqnGroup, explainEpsilon, explainDeltaC )