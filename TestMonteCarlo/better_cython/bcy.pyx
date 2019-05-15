import random

def dice6_cy1(int N, int ndice, int nsix):
    cdef int M = 0            # no of successful events
    cdef int six, r
    cdef double p
    for i in range(N):        # repeat N experiments
        six = 0               # how many dice with six eyes?
        for j in range(ndice):
            r = random.randint(1, 6)  # roll die no. j
            if r == 6:
               six += 1
        if six >= nsix:       # successful event?
            M += 1
    p = float(M)/N
    return p
