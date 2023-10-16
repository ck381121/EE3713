import numpy as np
import matplotlib.pyplot as plt
import math

# Function to plot and label a PDF
def plot_and_label_pdf(z, f_z, title):
    plt.plot(z, f_z, label='PDF')
    plt.xlabel('z')
    plt.ylabel('f(z)')
    plt.title(title)
    plt.legend()
    plt.show()

# Scenario a: Z is an exponential random variable
# Rate parameter
lambda_1 = 1/3
z1 = np.linspace(0, 20, 100)
f_z1 = lambda_1 * np.exp(-lambda_1 * z1)
plot_and_label_pdf(z1, f_z1, 'PDF of Exponential RV Z')

# Scenario b: Z is a uniform random variable
# Limits of the uniform distribution
a = 0
b = 6
z2 = np.linspace(a, b, 100)
f_z2 = 1 / (b - a)
plot_and_label_pdf(z2, f_z2 * np.ones_like(z2), 'PDF of Uniform RV Z')

# Scenario c: Z is an Erlang random variable
# Shape parameter and rate parameter
k = 4
lambda_3 = 1
z3 = np.linspace(0, 10, 100)
f_z3 = (z3**(k-1) * np.exp(-lambda_3 * z3)) / math.factorial(k-1)
f_z3 = f_z3 / sum(f_z3)  # Normalize the PDF
plot_and_label_pdf(z3, f_z3, 'PDF of Erlang RV Z')
