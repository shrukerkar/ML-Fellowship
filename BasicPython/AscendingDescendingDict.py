
import operator


d={'Shruti':1,'Kerker':2,'Prabodh':3}

sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Ascending order : ',sorted_d)
sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)
print('Descending order : ',sorted_d)


