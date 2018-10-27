
#Write a Python program to create a horizontal bar chart with differently ordered colors.
#Note: Use bottom to stack the women?s bars on top of the men?s bars.
#Sample Data Set:
#languages = [['Language','Science','Math'],
#['Science','Math','Language'],
#['Math','Language','Science']]
#numbers = [{'Language':75, 'Science':88, 'Math':96},
#{'Language':71, 'Science':95, 'Math':92},
#{'Language':75, 'Science':90, 'Math':89}]

import matplotlib.pyplot as plt
import numpy as np

numbers = [{'Language':75, 'Science':88, 'Math':96},
{'Language':71, 'Science':95, 'Math':92},
{'Language':75, 'Science':90, 'Math':89}]

languages = [['Language','Science','Math'],
['Science','Math','Language'],
['Math','Language','Science']]

color=['r','g','b']
names=sorted(numbers[0].keys())


values = np.array([[data[name] for name in order] for data,order in zip(numbers,languages)
lefts =np.insert(np.cumsum(values, axis=1),0,0, axis=1)[:, :-1]
orders = np.array(languages)
bottoms = np.arange(len(languages))

for name, color in zip(names, color):
	idx = np.where(orders == name)
	value = values[idx]
	left = lefts[idx]
	plt.bar(left=left, height=0.8, width=value, bottom=bottoms,color=color, orientation="horizontal", label=name)
plt.yticks(bottoms+0.4, ["Student-%d" % (t+1) for t in bottoms])
plt.legend(loc="best", bbox_to_anchor=(1.0, 1.00))
plt.subplots_adjust(right=0.75)

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

plt.show()

