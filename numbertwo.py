import numpy as np
import matplotlib.pyplot as plt

# Define the range of x values
x = np.arange(0, 10, 0.01)

# Define the CDF
def cdf(x):
    if x < 1:
        return 0
    elif 1 <= x < 2:
        return 0.15 
    elif 2 <= x < 4:
        return 0.15 + 0.2 
    elif 4 <= x < 7:
        return 0.35 + 0.25 
    else:
        return 1

# Calculate CDF values for the range of x
cdf_values = [cdf(val) for val in x]

# Define the PMF (discrete probability mass function)
pmf_values = [cdf_values[0]]
for i in range(1, len(x)):
    pmf_values.append(cdf_values[i] - cdf_values[i-1])

# Create CDF plot
plt.figure(1)
plt.plot(x, cdf_values, label="CDF")
plt.xlabel("x")
plt.ylabel("F(x)")
plt.title("Cumulative Distribution Function (CDF)")
plt.grid()

# Create PMF plot
plt.figure(2)
plt.bar(x, pmf_values, width=0.2, label="PMF")
plt.xlabel("x")
plt.ylabel("P(X=x)")
plt.title("Probability Mass Function (PMF)")
plt.grid()

# Calculate mean and standard deviation
# Define the probabilities and corresponding values
probabilities = [0.15, 0.20, 0.25, 0.4]
values = [1, 2, 4, 7]

# Calculate mean and standard deviation using NumPy
mean = np.dot(values, probabilities)
variance = np.dot((np.array(values) - mean)**2, probabilities)
std_deviation = np.sqrt(variance)

print("Mean (E[X]):", mean)
print("Standard Deviation (s[X]):", std_deviation)

plt.show()
