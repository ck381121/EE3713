import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mean_temperature = 12
variance = 196

# Create a range of temperature values
t_values = np.linspace(mean_temperature - 3 * np.sqrt(variance), mean_temperature + 3 * np.sqrt(variance), 1000)

# Calculate the PDF using the Gaussian (normal) distribution
pdf_values = norm.pdf(t_values, loc=mean_temperature, scale=np.sqrt(variance))

# Plot the PDF
plt.figure(figsize=(8, 6))
plt.plot(t_values, pdf_values, label='PDF', color='blue')
plt.title('Probability Density Function (PDF) of T')
plt.xlabel('Temperature (°F)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.legend()
plt.show()
