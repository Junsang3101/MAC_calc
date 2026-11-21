import time
from .mac import mac
def make_matrix(size: int):
    return [[1 for cols in range(size)] for rows in range(size)]

def get_perf(pattern, filter, iterate = 10):
    total_compute = 0
    for i in range(iterate):
        start = time.perf_counter()
        mac(pattern, filter)
        end = time.perf_counter()
        total_compute += end - start
    return total_compute / iterate