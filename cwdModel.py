import matplotlib.pyplot as plt
from cwdODE import cwdODE
from scipy.integrate import solve_ivp

# Values to nail down
IV = [50,5,0,0,0]
tspan = [0, 100]
r=2
K=100

alpha=4
gamma=1/2
delta_c=3
delta_p=1
eps_p=4

# Values that aren't nailed down
beta1=0.005
beta2=0.004
beta3=0.0014
beta4=0.0003


# R0 = beta4/alpha - (eps_p*beta2)/(alpha*delta_p) + beta1/delta_c + beta3/gamma
soln = solve_ivp( cwdODE, tspan, IV, args=( r,K,alpha,beta1,beta2,beta3,beta4,gamma,delta_c,delta_p,eps_p ), method='RK45' )

plt.plot( soln.t, soln.y[0], color='blue' )
plt.plot( soln.t, soln.y[1], color='orange' )
plt.plot( soln.t, soln.y[2], color='red' )
plt.plot( soln.t, soln.y[3], color='black' )
plt.plot( soln.t, soln.y[4], color='green' )

plt.title(f'CWD Simulation Where Five Asymptomatic CWD Deer Interact with a Susceptible Population')
plt.ylabel('Population')
plt.xlabel('time')
plt.legend(['Susceptible','Asymptomatic','Infected','Exposed Carcasses','Exposed Plants'])

plt.show()