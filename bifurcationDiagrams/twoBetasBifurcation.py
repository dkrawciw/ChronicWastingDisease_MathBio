import matplotlib.pyplot as plt
from cwdODE import cwdODE
from scipy.integrate import solve_ivp
from numpy import linspace, array, savetxt

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
beta2=0.004
# beta3=0.0014
# beta4=0.003

NumOfBetas = 100
beta3Vals = linspace(0,0.1,NumOfBetas)
beta4Vals = linspace(0,0.1,NumOfBetas)
roots = []

for beta3 in beta3Vals:
    for beta4 in beta4Vals:
        soln = solve_ivp( cwdODE, tspan, IV, args=(r,K,alpha,beta1,beta2,beta3,beta4,gamma,delta_c,delta_p,eps_p), method='RK23' )
        roots.append( [beta3, beta4, soln.y[0][-1]] )

roots = array( roots )

savetxt('bifurcationDiagrams/bifurcationData2.csv', roots, delimiter=',')

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(roots[:,0],roots[:,1],roots[:,2])
# ax.set_xlabel('beta3')
# ax.set_ylabel('beta4')
# ax.set_zlabel('Long-Term Susceptible Population')
# ax.set_title('Stability of the Susceptible Population as Parameters beta3 and beta4 are Changed')
# plt.show()
