import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf

# Generate a time series with trend and seasonality
np.random.seed(42)
time = pd.date_range(start='2020-01-01', periods=1000, freq='D')
trend = np.linspace(0, 10, 1000)
seasonal = 10 * np.sin(np.linspace(0, 20 * np.pi, 1000))
noise = np.random.normal(loc=0, scale=2, size=1000)
data = trend + seasonal + noise
ts = pd.Series(data=data, index=time)

# Decompose the time series into its components
result = seasonal_decompose(ts, model='additive')

# Plot the observed, trend, seasonal, and residual components
result.plot()
plt.gcf().set_size_inches(10, 8)
plt.tight_layout()
plt.show()

# Histogram of the time series
plt.figure(figsize=(10, 4))
sns.histplot(ts, bins=30, kde=True, color='blue')
plt.title('Histogram of Time Series Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Box plot of the time series
plt.figure(figsize=(6, 4))
sns.boxplot(y=ts, color='cyan')
plt.title('Box Plot of Time Series Data')
plt.show()

# Autocorrelation plot
plt.figure(figsize=(10, 4))
plot_acf(ts, lags=50)
plt.title('Autocorrelation Plot')
plt.show()

# Moving average
moving_avg = ts.rolling(window=12).mean()
plt.figure(figsize=(10, 4))
plt.plot(ts, label='Original')
plt.plot(moving_avg, color='red', label='Moving Average')
plt.title('Time Series with Moving Average')
plt.legend()
plt.show()
