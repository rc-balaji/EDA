import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generating synthetic temperature data over time
np.random.seed(0)  # for reproducibility
dates = pd.date_range(start='2024-01-01', periods=100, freq='D')
temperatures = np.random.normal(loc=20, scale=5, size=100)  # Normal distribution, mean=20, std=5

# Creating a DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Temperature': temperatures
})

# Scatter Plot
plt.figure(figsize=(12, 8))  # Set the figure size
plt.subplot(2, 2, 1)  # First subplot in a 2x2 layout
plt.scatter(df['Date'], df['Temperature'], color='blue')
plt.title('Scatter Plot of Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
# plt.grid(True)

# Bar Plot
plt.subplot(2, 2, 2)  # Second subplot in a 2x2 layout
plt.bar(df['Date'].dt.strftime('%Y-%m-%d'), df['Temperature'], color='red')
plt.title('Bar Plot of Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
# plt.xticks(rotation=90)  # Rotate x-axis labels for better visibility

# Histogram
plt.subplot(2, 2, 3)  # Third subplot in a 2x2 layout
plt.hist(df['Temperature'], bins=10, color='green')
plt.title('Histogram of Temperatures')
plt.xlabel('Temperature (°C)')
plt.ylabel('Frequency')

# Box Plot
plt.subplot(2, 2, 4)  # Fourth subplot in a 2x2 layout
plt.boxplot(df['Temperature'])
plt.title('Box Plot of Temperatures')
plt.xticks([1], ['Temperature'])  # Custom x-axis label
plt.ylabel('Temperature (°C)')

plt.tight_layout()  # Adjusts plot parameters to give a pleasing layout
plt.show()
