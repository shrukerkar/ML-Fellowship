
#Write a Python program to display the grid and draw line charts of the closing value of Alphabet Inc. between October 3, 2016 to October 7, 2016. Customized the grid lines with linestyle -, width .5. and color blue.
#Date,Close
#03-10-16,772.559998
#04-10-16,776.429993
#05-10-16,776.469971
#06-10-16,776.859985
#07-10-16,775.080017


import matplotlib.pyplot  as plt
import pandas as pd

df=pd.read_csv("/home/shruti/fdata.csv")
#print(df)
#df.hist()

plt.bar(df['Open'],df['High'])
plt.xlabel("Open")
plt.ylabel("High")
plt.title("coloumn chart")
plt.show()

