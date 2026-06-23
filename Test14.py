import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style

x= np.arange(100)
fig, axs = plt.subplots(2,2)

axs[0,0].plot(x,np.sin(x))
axs[0,0].set_title("Sine wave")

axs[0,1].plot(x,np.sin(x))
axs[0,0].set_title("Sine wave")


plt.show()

