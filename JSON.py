# JSOn => Javascript object notation
# convert JSON TO PYTHON

import json

# student = '{"firstname": "navraj","lastname":"gautam","location":"lalitpur"}'
# print(student)

# convert = json.loads(student)  #converting json into dict and printing as string
# print(type(convert))

# print(convert["firstname"])

#converting a py dict into str

staff = {"firstname":"navraj","lastname":"gautam","location":"lalitpur"}
convert = json.dumps(staff)
print(type(convert))


