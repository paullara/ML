import numpy as np 
import matplotlib.pyplot as plt

def distance_robber(t):
    return 2.5 * t 

def distance_sheriff(t):
    return 3 * (t - 5)

coefficients = [-0.5, 15]
t_catch = np.roots(coefficients)[0]

d_catch = distance_robber(t_catch)

t = np.linspace(0, 40, 4000)

d_r = distance_robber(t)
d_s = distance_sheriff(t)


#create a plot 
fig, ax = plt.subplots()
plt.title('A Bank Robber Caught')
plt.xlabel('Time (in min)')
plt.ylabel('Distance (in km)')
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])
ax.plot(t, d_r, c='green', label='Robber')
ax.plot(t, d_s, c='brown', label='Sheriff')
plt.axvline(x=t_catch, color='purple', linestyle='--')
plt.axhline(y=d_catch, color='purple', linestyle='--')

plt.legend()

plt.show()
