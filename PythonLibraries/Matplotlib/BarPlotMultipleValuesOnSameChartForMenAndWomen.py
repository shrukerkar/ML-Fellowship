
# Write a Python program to create bar plot of scores by group and gender. Use multiple X values on the same chart for men and women.
# Sample Data:
# Means (men) = (22, 30, 35, 35, 26)
# Means (women) = (25, 32, 30, 35, 29)

import matplotlib.pyplot as plt
import numpy as np

num_groups=5
men=(22, 30, 35, 35, 26)
women=(25, 32, 30, 35, 29)

fig,ax=plt.subplots()
index=np.arange(num_groups)
bar_width=0.35

rect1=plt.bar(index,men,alpha=0.8,color='r',label='men')

rect2=plt.bar(index,women,alpha=0.8,color='b',label='women')

plt.xlabel('Men&Women')
plt.ylabel('scores')
plt.title('score by Men&Women')
plt.xticks(index+bar_width,('G1','G2','G3','G4','G5'))
plt.show()