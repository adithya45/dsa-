import matplotlib.pyplot as plt
import numpy as np

# Generate values for n
n = np.linspace(1, 100, 100)  # You can adjust the range and number of points as needed

# Calculate f(n) = n * log(n)
f_n = n * np.log(n)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(n, f_n, label='f(n) = n * log(n)', color='b', linestyle='-', linewidth=2)
plt.xlabel('n')
plt.ylabel('f(n)')
plt.title('time complexity of quick sort')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
