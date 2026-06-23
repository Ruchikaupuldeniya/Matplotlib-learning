import numpy as np
import matplotlib.pyplot as plt

stock_A = [100,102,99,101,101,100,102]
stock_B = [90,95,102,104,105,101,109]
stock_C = [110,115,100,105,100,98,95]

plt.plot(stock_A,label="Company1")
plt.plot(stock_B,label ="Company2")
plt.plot(stock_C,label ="Company3")

plt.legend(loc="lower center")


plt.show()

