## Packages
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import control

## Functions
from matplotlib.pyplot import figure, close, xlim, ylim, title, xlabel, ylabel, plot

## Variables
s = control.TransferFunction.s

## Custom Functions
def step(tf):
    t, y = control.step_response(tf)
    plt.plot(t,y)
    plt.grid()
    return t,y

def impulse(tf):
    t, y = control.impulse_response(tf)
    plt.plot(t,y)
    plt.grid()
    return t,y

## Settings
plt.ion()