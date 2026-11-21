EPSILON = 1e-9

def compar(A: float | int, B: float | int, epsilon: float = EPSILON):
    return abs(float(A) - float(B)) < epsilon

def normalize(raw: dict, map: dict):
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

def judge_Cross_X(a: list[list[int]], b: list[list[int]]):
    if not len(a) == len(b) and len(a[0]) == len(b[0]):
        raise 