import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

linear_data = pd.read_csv('linear_data.csv')

coefficients = np.polyfit(linear_data['X'], linear_data['Y'], 2)
fitted_line = np.polyval(coefficients, linear_data['X'])

plt.scatter(linear_data['X'], linear_data['Y'], label='Data Points', color='blue')
plt.plot(linear_data['X'], fitted_line, color='red', label=f"Fitted Line: y={coefficients[0]:.2f}x + {coefficients[1]:.2f}")
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Fitted Line')
plt.legend()
plt.show()
