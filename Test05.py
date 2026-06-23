import numpy as np
import matplotlib.pyplot as plt


langs = ["python" , "Java" ,"C++"]
vote = [10,80,10]

plt.pie(vote,labels=langs)
plt.legend(labels=langs)
plt.show()

