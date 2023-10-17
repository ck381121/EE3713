import numpy as np

# Define the corrected PMF values for X
pmf_values_x = [0.15, 0.20, 0.25, 0.40]
values_x = [2, 5, 17, 50 ]

# Calculate mean and standard deviation of X using NumPy
mean_x = np.dot(values_x, pmf_values_x)
variance_x = np.dot((np.array(values_x) - mean_x)**2, pmf_values_x)
std_deviation_x = np.sqrt(variance_x)



# Calculate mean and standard deviation of Y = H(X) using the properties of the transformation

variance_y = (2 * mean_x * std_deviation_x) + (std_deviation_x ** 2)  # Variance of Y = X^2 + 1


print("Mean of Y (E[Y]):", mean_x)
print("Standard Deviation of Y (stdev[Y]):", variance_x)

