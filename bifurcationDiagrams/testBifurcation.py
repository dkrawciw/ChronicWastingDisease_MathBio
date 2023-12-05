import matplotlib.pyplot as plt
from cwdODE import cwdODE
from scipy.integrate import solve_ivp
from numpy import linspace, array

# Values to nail down
IV = [50,5,0,0,0]
tspan = [0, 100]
r=2
K=55

alpha=4
gamma=1/2
delta_c=1
delta_p=1
eps_p=4

# Values that aren't nailed down
beta1=0.005
beta2=0.004
beta3=0
beta4=0

betaVals = linspace(0,0.1,100)
roots = []
for bifurcationVal in betaVals:
    soln = solve_ivp( cwdODE, tspan, IV, args=(r,K,alpha,beta1,beta2,beta3,bifurcationVal,gamma,delta_c,delta_p,eps_p), method='RK23' )
    edgeRoots = array(soln.y)
    roots.append( soln.y[:,-1] )

roots = array( roots )

plt.figure(dpi=1200)
plt.title('Stability of the Susceptible Population as\nthe Transmission Rate of CWD Plants Changes')
plt.xlabel('Transmission Rate of CWD Plants')
plt.ylabel('Long-Term Stability of Populations')
plt.plot( betaVals, roots[:,0], color='blue')
plt.savefig('Beta4Bifurcation.png')