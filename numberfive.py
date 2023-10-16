import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the Gaussian distributions
mean_X, stdev_X = 0, 1
mean_Y, stdev_Y = -4, 3

# Create a range of values for x and y
x = np.linspace(mean_X - 5 * stdev_X, mean_X + 5 * stdev_X, 100)
y = np.linspace(mean_Y - 5 * stdev_Y, mean_Y + 5 * stdev_Y, 100)

# Calculate the PDFs for X and Y using the Gaussian probability density function
pdf_X = (1 / (stdev_X * np.sqrt(2 * np.pi))) * np.exp(-(x - mean_X)**2 / (2 * stdev_X**2))
pdf_Y = (1 / (stdev_Y * np.sqrt(2 * np.pi))) * np.exp(-(y - mean_Y)**2 / (2 * stdev_Y**2))

# Plot the PDFs on the same axes
plt.plot(x, pdf_X, label='PDF of X (0,1)')
plt.plot(y, pdf_Y, label='PDF of Y (-4,3)')
plt.xlabel('x or y')
plt.ylabel('f(x) or f(y)')
plt.title('PDFs of Gaussian Random Variables X and Y')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
