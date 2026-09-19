import numpy as np

def cross_product(a, b):
    c1 = a[1]*b[2] - a[2]*b[1]
    c2 = -1*(a[0]*b[2]- a[2]*b[0])
    c3 = a[0]*b[1]- a[1]*b[0]

    return [c1,c2,c3]