import os.path, time


print("last modified: %s" % time.ctime(os.path.getmtime('/home/shruti/ua.csv')))

print("created: %s" % time.ctime(os.path.getctime('/home/shruti/ua.csv')))
