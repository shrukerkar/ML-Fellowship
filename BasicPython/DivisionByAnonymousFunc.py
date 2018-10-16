
List=[30,45,60,75,150,10]

Division= lambda x:(x%15==0)

result=list(filter(Division,List))

print(result)