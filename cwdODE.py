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

    S = x[0]    # Susceptible
    A = x[1]    # Asymptomatic (for a period)
    I = x[2]    # Infected
    E_c = x[3]  # Exposed Carcasses
    E_p = x[4]  # Exposed Plant

    N = S+A+I   # Total Population

    dS = r*(S+A)*(1 - (N)/K) - beta1*S*E_c - beta2*S*E_p - beta3*S*A - beta4*S*I
    dA = beta1*S*E_c + beta2*S*E_p + beta3*S*A + beta4*S*I - gamma*A
    dI = gamma*A - alpha*I
    dE_c = alpha*I - delta_c*E_c
    dE_p = eps_p*I - delta_p*E_p

    return [dS,dA,dI,dE_c,dE_p]