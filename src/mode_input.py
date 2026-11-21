from .mac import mac
from .perf import get_perf
from .judge import compar

def input_matrix(rows, colums, min_val, max_val):
    '''n * n 크기의 행렬 입력받기'''
    matrix: list[list[int]] = []
    for i in range(rows):
        while True:
            try:
                raw = input(f"{min_val} ~ {max_val} {colums}개 입력: ")
                raw = raw.split()
                if not (len(raw) == colums):
                    print("다시 입력해주세요.")
                    continue
                row = []
                for j, value in enumerate(raw):
                    num = int(value)
                    if not (min_val <= num <= max_val):
                        raise(ValueError)
                    row.append(num)

            except (KeyboardInterrupt, EOFError):
                return
            except ValueError:
                j -= 1
                print("다시 입력해주세요.")
                continue

            matrix.append(row)
            break

    return matrix

def mode_input():
    print("\n== 필터 A ==\n")
    filter_A = input_matrix(3, 3, 0, 1)
    if filter_A is None: return
    print("\n== 필터 B ==\n")
    filter_B = input_matrix(3, 3, 0, 1)
    if filter_A is None: return
    print("\n=== 타겟 ===\n")
    pattern = input_matrix(3, 3, 0, 1)
    if filter_A is None: return
    
    compar_A = mac(filter_A, pattern)
    compar_B = mac(filter_B, pattern)
    same = compar(compar_A, compar_B)

    if same:
        print(f"\nA: {compar_A}\nB: {compar_B}\n패턴과 필터 A, B와의 일치도가 사실상 동일합니다.\n")
        print(f"성능 분석(3x3): {get_perf(pattern, filter_A)*1000}ms")
    elif compar_A > compar_B:
        print(f"\nA: {compar_A}\nB: {compar_B}\nA패턴과 더 유사합니다.\n")
        print(f"성능 분석(3x3): {get_perf(pattern, filter_B)*1000}ms")
    elif compar_A < compar_B:
        print(f"\nA: {compar_A}\nB: {compar_B}\nB패턴과 더 유사합니다.")
        print(f"성능 분석(3x3): {get_perf(pattern, filter_A)*1000}ms")