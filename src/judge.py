EPSILON = 1e-9

def compar(A: float | int, B: float | int, epsilon: float = EPSILON):
    return abs(float(A) - float(B)) < epsilon

def normalize(raw):
    pass