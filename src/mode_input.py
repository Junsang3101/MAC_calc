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
    print("== 필터 A ==")
    filter_A = input_matrix(3, 3, 0, 1)
    if filter_A is None: return
    print("== 필터 B ==")
    filter_B = input_matrix(3, 3, 0, 1)
    if filter_A is None: return
    print("=== 패턴 ===")
    pattern = input_matrix(3, 3, 0, 1)
    if filter_A is None: return
    
    compar_A = mac(filter_A, pattern)
    compar_B = mac(filter_B, pattern)
    same = compar(compar_A, compar_B)

    print("== 결과 ==")
    if same:
        print(f"A mac점수: {compar_A}\nB mac 점수: {compar_B}\n결과: 판정불가(UNDECIDED)")
        print(f"성능 분석(3x3): {get_perf(pattern, filter_A)*1000}ms")
    elif compar_A > compar_B:
        print(f"\nA mac점수: {compar_A}\nB mac 점수: {compar_B}\n결과: A")
        print(f"성능 분석(3x3): {get_perf(pattern, filter_B)*1000}ms")
    elif compar_A < compar_B:
        print(f"\nA mac점수: {compar_A}\nB mac 점수: {compar_B}\n결과: B")
        print(f"성능 분석: {get_perf(pattern, filter_A)*1000}ms")
        print(f"연산 횟수: {3**2}")