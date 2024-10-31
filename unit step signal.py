import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(-10, 10, 1000)  # From -10 to 10 with 1000 points

# Define the unit step function
u = np.where(t >= 0, 1, 0)

# Define a sine wave
sine_wave = np.sin(t)

# Multiply the two signals
product_signal = u * sine_wave

# Plot the individual signals and the product signal
plt.figure(figsize=(10, 6))

# Plot unit step
plt.subplot(3, 1, 1)
plt.plot(t, u, label="Unit Step Signal")
plt.title("Unit Step Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot sine wave
plt.subplot(3, 1, 2)
plt.plot(t, sine_wave, label="Sine Wave", color="orange")
plt.title("Sine Wave")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

# Plot product signal
plt.subplot(3, 1, 3)
plt.plot(t, product_signal, label="Product Signal (Unit Step * Sine Wave)", color="purple")
plt.title("Product Signal")
plt.xlabel("Time (t)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
