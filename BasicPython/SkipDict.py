
import os

#path='/home/shruti/Downloads'

#for file_name in os.listdir(path):
#    result_path=os.path.join(path,file_name)
#    if os.path.isdir(result_path):
#        continue

directory = "/home/shruti/PycharmProjects/PythonMachineLearning"
print(filter(os.path.isfile, os.listdir(directory)))

print(os.getcwd())