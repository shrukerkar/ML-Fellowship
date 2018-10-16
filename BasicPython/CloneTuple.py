
from copy import deepcopy
t=(1,[],"Hello",True)
print(t)
tuple=deepcopy(t)
print(tuple)
tuple[1].append(60)
print(tuple)
