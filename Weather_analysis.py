import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load weather dataset
df = pd.read_csv('/content/weather.csv')

# Display dataset
print("Weather Data:")
print(df)

# Statistical Analysis using NumPy
print("\nWeather Statistics:")
print(df.describe())

print("\nAverage Temperature:", np.mean(df["Temperature"]))
print("Maximum Temperature:", np.max(df["Temperature"]))
print("Minimum Temperature:", np.min(df["Temperature"]))
print("Average Humidity:", np.mean(df["Humidity"]))
print("Total Rainfall:", np.sum(df["Rainfall"]))

# Temperature Analysis
plt.figure(figsize=(8, 5))
plt.plot(df['Day'], df['Temperature'], marker='o')
plt.title("Daily Temperature Analysis")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.savefig('/content/temperature.png')
plt.show()

# Humidity Analysis
plt.figure(figsize=(8, 5))
plt.plot(df['Day'], df['Humidity'], marker='o')
plt.title("Daily Humidity Analysis")
plt.xlabel("Day")
plt.ylabel("Humidity (%)")
plt.grid()
plt.savefig('/content/humidity.png')
plt.show()

# Rainfall Analysis
plt.figure(figsize=(8, 5))
plt.bar(df['Day'], df['Rainfall'])
plt.title("Daily Rainfall Analysis")
plt.xlabel("Day")
plt.ylabel("Rainfall")
plt.savefig('/content/rainfall.png')
plt.show()
