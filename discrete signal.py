import numpy as np
import matplotlib.pyplot as plt

# Define the discrete time points (e.g., integers from 0 to 10)
n = np.arange(0, 10, 1)

# Define a discrete signal (e.g., a simple sequence or sine wave at discrete intervals)
frequency = 1  # Frequency in Hz
amplitude = 1  # Amplitude
signal = amplitude * np.sin(2 * np.pi * frequency * n / len(n))

# Plot the discrete signal
plt.stem(n, signal)
plt.title("Discrete Signal - Sine Wave Samples")
plt.xlabel("n (Sample Number)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
