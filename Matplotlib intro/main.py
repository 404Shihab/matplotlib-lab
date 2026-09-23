import matplotlib.pyplot as plt
import numpy as np

# pyplot provides a user-friendly interface for plotting

# print(matplotlib.__version__)

# Using NumPy arrays for numerical data and efficient operations
x = np.array([2022, 2023, 2024, 2025])
y = np.array([12, 23, 19, 22])

plt.plot(x, y)  # Plot y values against x values and connect the points with lines

# plt.plot(y)  # If x values are not provided, NumPy indices (0, 1, 2, ...) are used as x values

plt.show()  # Display the plot