import matplotlib.pyplot as plt
from cwdODE import cwdODE
from scipy.integrate import solve_ivp

# Values to nail down
IV = [50,5,0,0,0]
tspan = [0, 100]
r=2
K=55

alpha=4
gamma=1/2
delta_c=3
delta_p=3
eps_p=4

# Values that aren't nailed down
beta1=0.005
beta2=0.005
beta3=0.01
beta4=0.01

R0 = IV[0]*( beta1/gamma + beta2/alpha + beta3/delta_c + ( beta4 * eps_p )/( alpha * delta_p ) )
soln = solve_ivp( cwdODE, tspan, IV, args=( r, K, alpha, beta1, beta2, beta3, beta4, gamma, delta_c, delta_p, eps_p ), method='RK45' )

plt.plot( soln.t, soln.y[0], color='blue' )
plt.plot( soln.t, soln.y[1], color='orange' )
plt.plot( soln.t, soln.y[2], color='red' )
plt.plot( soln.t, soln.y[3], color='black' )
plt.plot( soln.t, soln.y[4], color='green' )

plt.title(f'CWD Simulation Where R0 = {R0:.4f}\nbeta3 = {beta3} & beta4 = {beta4}')
plt.ylabel('Population')
plt.xlabel('time')
plt.legend(['Susceptible','Asymptomatic','Infected','Exposed Carcasses','Exposed Plants'])

plt.show()