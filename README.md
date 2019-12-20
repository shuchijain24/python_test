# python_test
Calling C function from python

Calling C function from Python Program through ctypes module
STEPS-

1. Creating a C file(.c extension) with some required functions. (Saved it as myfunction.c) 


#include <stdio.h>



int square(int i) 



{ 


return i * i; 



}



2.Creating a shared library file(.so extension).



$ cc -fPIC -shared -o my_functions.so my_functions.c



3. In the Python program, create a ctypes.CDLL instance from the shared file.



from ctypes import * so_file = "/<absolute path from the home directory my_functions.so"



my_functions = CDLL(so_file)



4.At the end, call the C function using the format {CDLL_instance}.{function_name}({function_parameters}).



print(type(my_functions)) 



print(my_functions.square(10))
