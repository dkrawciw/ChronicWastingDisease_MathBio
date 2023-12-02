def cwdODE(t,x, r=0, K=0, alpha=0, beta1=0, beta2=0, beta3=0, beta4=0, gamma=0, delta_c=0, delta_p=0, eps_p=0):
    # r is the maximum rate of growth of the population
    # K is the maximum capacity of the population
    # alpha is the death rate of CWD on infected populations
    # beta1 is the rate of susceptible becoming asymptomatic after interracting with exposed carcasses
    # beta2 is the rate of susceptible becoming asymptomatic after interracting with exposed plants
    # beta3 is the rate of susceptible becoming asymptomatic after interracting with asymptomatic deer
    # beta4 is the rate of susceptible becoming asymptomatic after interracting with fully infected deer
    # gamma is the rate of asymptomatic deer becoming fully infected
    # delta_c is the rate of decay of the disease present in carcasses
    # delta_p is the rate of decay of the disease present in plants
    # eps_p is the rate that infected deer expose plants to CWD

    # S -> Susceptible
    # A -> Asymptomatic (for a period)
    # I -> Infected
    # E_c -> Exposed Carcasses
    # E_p -> Exposed Plant

    S, A, I, E_c, E_p = x
    
    N = S+A+I   # Total Population

    dS = r*(S+A)*(1 - N/K) - S * (beta1*A + beta2*I + beta3*E_c + beta4*E_p)
    dA = S*(beta1*A + beta2*I + beta3*E_c + beta4*E_p) - gamma*A
    dI = gamma*A - alpha*I
    dE_c = alpha*I - delta_c*E_c
    dE_p = eps_p*I - delta_p*E_p

    return [dS,dA,dI,dE_c,dE_p]