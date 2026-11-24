import time
from .mac import mac
from .perf import get_perf

EPSILON = 1e-9

def compar(A: float | int, B: float | int, epsilon: float = EPSILON):
    return abs(float(A) - float(B)) < epsilon

def normalize_label(raw: dict):
    result = {}
    for key, value in raw.items():
        base_key = str(key).strip().lower()
        final_key = base_key[:1].upper() + base_key[1:]
        if base_key == "+":
            base_key = "Cross"

        base_value = value
        final_value = base_value
        if isinstance(base_value, str):
            if base_value == "+":
                base_value = "Cross"
            else:    
                final_value = base_value[:1].upper() + base_value[1:]
        result[final_key]=final_value

    return result

def judge(filter, pattern: list[list[int]]) -> dict:
    a = mac(pattern["Input"], filter["Cross"])
    b = mac(pattern["Input"], filter["X"])

    perf = get_perf(filter["X"], pattern["Input"], 1) + get_perf(filter["Cross"], pattern["Input"], 1) / 2
    result = {
        "Cross": a,
        "X": b,
        "perf": perf,
        "size": len(pattern["Input"])
    }

    #print(result)
    return result

    if compar(a, b):
        return None
    elif a > b:
        return "Cross"
    elif a < b:
        return "X"