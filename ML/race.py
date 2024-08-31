import numpy as np 
import matplotlib.pyplot as plt 

def runner_a_distance(t):
    return 4 * t

def runner_b_distance(t):
    return 5 * (t - 10)

# Solve for the time when Runner B catches Runner A
# The equation is 4t = 5(t - 10)
# Simplifying: 4t = 5t - 50 -> -t = -50 -> t = 50
coefficients = [-1, 50]
t_catch = np.roots(coefficients)[0]

# Calculate the distance at the catch time
d_catch = runner_a_distance(t_catch)

# Define the time array for plotting
# Chosen 6000 points for a smooth plot over 60 minutes
t = np.linspace(0, 60, 6000)

# Calculate the distances for plotting
d_a = runner_a_distance(t)
d_b = runner_b_distance(t)

# Create the plot
fig, ax = plt.subplots()
plt.title('Runner B Catches Runner A')
plt.xlabel('Time (in min)')
plt.ylabel('Distance (in km)')

# Set x-axis limits based on the range of t
ax.set_xlim([0, 60])

# Set y-axis limits with some buffer above the max distance
ax.set_ylim([0, 250])

# Plot the distances
ax.plot(t, d_a, c='blue', label='Runner A')
ax.plot(t, d_b, c='red', label='Runner B')

# Plot the lines at the catch point
plt.axvline(x=t_catch, color='purple', linestyle='--', label='Catch time')
plt.axhline(y=d_catch, color='purple', linestyle='--', label='Catch distance')

# Add the legend
plt.legend()

# Show the plot
plt.show()

# Print the calculated catch time and distance
print(f'Runner B catches Runner A at t = {t_catch} minutes, distance = {d_catch} km')
