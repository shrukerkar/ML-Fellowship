
# Write a Python program to create a stacked bar plot with error bars.
#Note: Use bottom to stack the women?s bars on top of the men?s bars.
#Sample Data:
#Means (men) = (22, 30, 35, 35, 26)
#Means (women) = (25, 32, 30, 35, 29)
#Men Standard deviation = (4, 3, 4, 1, 5)
#Women Standard deviation = (3, 5, 2, 3, 3)

import matplotlib.pyplot as plt
import numpy as np


N=5
men=(22, 30, 35, 35, 26)
women=(25, 32, 30, 35, 29)

men_std_dev=(4, 3, 4, 1, 5)
women_std_dev=(3, 5, 2, 3, 3)

index=np.arange(N)
width=0.35

p1 = plt.bar(index, men, width, yerr=men_std_dev, color='red')
p2 = plt.bar(index, women_std_dev,width,bottom=men, yerr=women_std_dev,color='green')

plt.ylabel('Scores')
plt.xlabel('Groups')
plt.title('Scores by group\n' + 'and gender')
plt.xticks(index,('Gr1', 'Gr2', 'Gr3', 'Gr4', 'Gr5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()