function soln = diseaseODE(t,y,r,k,beta,mu,a,m,eps,tau,b)
    S = y(1);
    I = y(2);
    E = y(3);
    P = y(4);

    dS = S * (r * (1 - (S+I)/k) - beta * E);
    dI = beta * S * E - mu * I - (a * I * P) / (m + I);
    dE = eps * I - tau * E;
    dP = P * (-d + b*I / (m + I));

    soln = [dS, dI, dE, dP];
end