import json

data = {'a':1, 'b':2, 'c':3}
d1 = json.dumps(data, False, 4)
print d1
