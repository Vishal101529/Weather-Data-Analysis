import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Weather Data Analysis Project

# Create sample weather data
data = {
    "Day": np.arange(1, 8),
    "Temperature": [28, 30, 32, 29, 31, 27, 33],
    "Humidity": [65, 70, 60, 75, 68, 80, 55],
    "Rainfall": [2, 0, 5, 3, 1, 8, 0]
}

df = pd.DataFrame(data)

# Display weather data
print("Weather Data:")
print(df)

# Calculate statistics
print("\nAverage Temperature:", np.mean(df["Temperature"]))
print("Maximum Temperature:", np.max(df["Temperature"]))
print("Minimum Temperature:", np.min(df["Temperature"]))
print("Average Humidity:", np.mean(df["Humidity"]))
print("Total Rainfall:", np.sum(df["Rainfall"]))

# Plot temperature
plt.plot(df["Day"], df["Temperature"], marker="o")
plt.title("Weekly Temperature Analysis")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid()
plt.show()
