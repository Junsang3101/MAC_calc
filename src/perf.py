import time
from .mac import mac
def make_matrix(size: int):
    return [[1 for cols in range(size)] for rows in range(size)]

def get_perf(size: int):
    matrix = make_matrix(size)
    total_compute = 0
    for i in range(10):
        start = time.perf_counter()
        mac(matrix, matrix)
        end = time.perf_counter()
        total_compute += end - start
    return total_compute / size