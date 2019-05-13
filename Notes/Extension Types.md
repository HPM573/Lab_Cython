# Extension types (AKA. cdef classes)
Cython supports second kind of class -> extension types -> cdef classes 
- somewhat restricted compared to Python classes
- more memory efficient and faster than generic python classes 
- use C struct to store fields and methods instead of Python dict 
- store arbitrary C types in fields without requiring Python wrapper 
- access fields and methods directly at C level without passing through Python dictionary lookup 

Normal Python classes can inherit from cdef classes BUT not the other way around 
- it also can inherit from any number of python classes and extension types 
Need to know complete inheritance hierarchy to lay out C structs and restrict it to single inheritance
