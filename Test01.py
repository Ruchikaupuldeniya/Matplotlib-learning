import numpy as np
import matplotlib.pyplot as plt

X_data = np.random.random(50)* 100
Y_data = np.random.random(50)*100

print(X_data)

plt.scatter(X_data,Y_data,c="#00f",s=50,marker="*",alpha = 0.3)
plt.show()



