
from ctypes import *

so_file = "/<absolute path from the home directory>/my_functions.so"
my_functions = CDLL(so_file)

print (type(my_functions))

print (my_functions.square(10))
print (my_functions.square(5))

