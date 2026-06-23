import numpy as np
import matplotlib.pyplot as plt


langs = ["python" , "Java" ,"C++"]
vote = [10,80,10]
explodes =[0.2,0.1,0.1]

plt.pie(vote,labels=langs,explode=explodes,autopct="%.2f%%",pctdistance=1.5)
plt.show()

