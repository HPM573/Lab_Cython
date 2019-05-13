# Using C Libraries
- call external C libraries from Python code 
- use and wrap external C library in Cython code 
- appropriate error handling and considerations about designing suitable API for Python and Cython code
- Queue implementation in C
 
 ## Defining external declarations 
 - in .pxd is almost identical to header file 
 - can often just copy them over
 - However, you don't need to provide all the declarations! -> just the ones you use in your code or in other declarations
 - good practice: one .pxd file for each library that you use and sometimes for each header file if API is large
 
 ## Writing a Wrapper Class 
 - ```__cinit__``` -> always called immediately on construction before CPython even considers calling ```__init__```
 - avoid not initializing C pointers and having hard crashes
 - receives no parameters that were passed to constructor
 
 ## Memory Management
 - Python throws ```MemoryError``` with pointer errors that can arise from insufficient memory from creating new exception  
 - ```PyErr_NoMemory()``` -> C-API function that automatically substitutes this wheneber you write ```raise MemoryError``` or ```raise MemoryError()```
 - when Queue is no longer uses -> ```__dealloc__()```
 ```
 def __dealloc__(self):
    if self._c_queue is not NULL:
        cqueue.queue_free(self._c_queue)
```
## Compiling and linking 
- use setup.py
- Two ways to make sure Cython finds the necessary libraries 
1. tell disutils where to find c-source to compile implementation automatically 
2. build and install algorithm as system library and dynamically link it -> useful if other applications also use algorithm

### Static Linking 
- include compiler directives in .pyx file to build c-code automatically 
- ```sources```: compiler directive that gives path of C file that will be compiled and linked (statically) into resulting extension module 
- ```include_dirs```: relevant header files are found here 
- command to build project: ```python setup.py build_ext -i```

### Dynamic Linking
- create new object 
- useful if the library we are going to wrap is already installed on the system 

### Mapping Functionality 
- provide and observe interfaces

### Handling Errors
- raise errors to account for special cases 
