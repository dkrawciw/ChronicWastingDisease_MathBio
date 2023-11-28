import matplotlib.pyplot as plt
from cwdODE import cwdODE
from scipy.integrate import solve_ivp

IV = [50,0,4,0,0]
tspan = [0, 300]
r=2/(12)
K=100
alpha=1/6
beta1=0.001
beta2=0.001
beta3=0.0005
beta4=0.0001
gamma=1/24
delta_c=0.2
delta_p=0.2
eps_p=0.1

soln = solve_ivp( cwdODE, tspan, IV, args=( r,K,alpha,beta1,beta2,beta3,beta4,gamma,eps_p ), method='RK45' )

plt.plot( soln.t, soln.y[0], color='blue' )
plt.plot( soln.t, soln.y[1], color='orange' )
plt.plot( soln.t, soln.y[2], color='red' )
plt.plot( soln.t, soln.y[3], color='black' )
plt.plot( soln.t, soln.y[4], color='green' )

plt.title('')
plt.ylabel('Population')
plt.xlabel('time')
plt.legend(['Susceptible','Asymptomatic','Infected','Exposed Carcasses','Exposed Plants'])

plt.show()