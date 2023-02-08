## Credit: https://www.halvorsen.blog/documents/programming/python/resources/powerpoints/Transfer%20Functions%20with%20Python.pdf

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Define Transfer Function
num = np.array([2])
den = np.array([3 , 1])

H = signal.TransferFunction(num , den)

print ('H(s) =', H)

# Step Response
t, y = signal.step(H)

# Plotting
plt.plot(t, y)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("y")
plt.grid()
plt.show()