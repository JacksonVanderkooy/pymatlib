## Credit: https://www.halvorsen.blog/documents/programming/python/resources/powerpoints/Transfer%20Functions%20with%20Python.pdf

import control
import numpy as np
import matplotlib.pyplot as plt

num = np.array([2])
den = np.array([3 , 1])

H = control.tf(num , den)

print ('H(s) =', H)

t, y = control.step_response(H)

plt.plot(t,y)
plt.title("Step Response")
plt.grid()