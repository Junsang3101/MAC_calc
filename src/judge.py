import time
from .mac import mac
from .perf import get_perf

EPSILON = 1e-9

def compar(A: float | int, B: float | int, epsilon: float = EPSILON):
    return abs(float(A) - float(B)) < epsilon

def normalize_label(raw: dict, map: dict):
    result = {}
    for key, value in raw.items():
        base_key = str(key).strip().lower()
        final_key = base_key
        final_value = value
        for target, replacement in map.items():
            if base_key == target:
                final_key = replacement

            if isinstance(value, str) and value == target:
                final_value = replacement

        result[final_key] = final_value

    return result

def judge(filter, pattern: list[list[int]]) -> dict:
    a = mac(pattern["input"], filter["Cross"])
    b = mac(pattern["input"], filter["X"])

    perf = get_perf(filter["X"], pattern["input"], 1) + get_perf(filter["Cross"], pattern["input"], 1) / 2
    result = {
        "Cross": a,
        "X": b,
        "perf": perf
    }

    #print(result)
    return result

    if compar(a, b):
        return None
    elif a > b:
        return "Cross"
    elif a < b:
        return "X"