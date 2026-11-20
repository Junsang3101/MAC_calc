EPSILON = 1e-9

def run():
    main_menu()

def main_menu():
    # 메인 메뉴 출력
    print("1. 사용자 입력")
    print("2. json 분석")
    print("4. 종료")

    # 메뉴 선택
    choice = 0
    while True:
        try:
            choice = int(input("선택: "))
        except (ValueError, KeyboardInterrupt, EOFError):
            print("다시 입력해주세요.")
        if not isinstance(choice, int):
            print("다시 입력해주세요.")
            main_menu()
        break

    if choice == 1:
        custom_filter_menu()
    elif choice == 2:
        setted_menu()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        print("다시 입력해세요.")
        return main_menu()

    print("정상적으로 종료되었습니다.")

def custom_filter_menu():
    filter_A = []
    filter_B = []
    target = []
    print("== 필터 A ==")
    filter_A = input_matrix(3, 3, 0, 1)
    
    print("== 필터 B ==")
    filter_B = input_matrix(3, 3, 0, 1)
    print("=== 타겟 ===")
    target = input_matrix(3, 3, 0, 1)

    compar_A = matrix_rate(filter_A, target)
    compar_B = matrix_rate(filter_B, target)
    diff = abs(compar_A - compar_B)
    if diff < EPSILON:
        print(f"일치도가 사실상 동일합니다. (A: {compar_A} B: {compar_B}, 일치도 차이 절대값: {diff})")
    elif compar_A > compar_B:
        print(f"필터 A와 더 일치합니다. (A: {compar_A} B: {compar_B}), 일치도 차이 절대값: {diff})")
    elif compar_A < compar_B:
        print(f"필터 B와 더 일치합니다. (A: {compar_A} B: {compar_B}), 일치도 차이 절대값: {diff})")

def setted_menu():
    pass

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

            except (KeyboardInterrupt, EOFError, ValueError):
                print("다시 입력해주세요.")
                continue
            except ValueError:
                j -= 1
                continue

            matrix.append(row)
            break

    return matrix

class InvalidMatrixComparison(Exception):
    '''잘못된 행렬 비교'''
    def __init__(self):
        super().__init__(f"필터와 데이터의 크기가 서로 다릅니다.")

def matrix_rate(data: list[list[int]], filter: list[list[int]]):
    rows_compar = len(data) == len(filter)
    colums_compar = len(data[0]) == len(filter[0])
    if not rows_compar and colums_compar:
        raise InvalidMatrixComparison()

    match = 0
    mismatch = 0
    total_result = []
    rows = len(filter)
    colums = len(filter[0])
    for i in range(rows):
        row = []
        for j in range(colums):
            result = data[i][j] == filter[i][j]
            if result:
                result = 1   
            else:
                result = 0

            if result:
                match += 1
            elif not result:
                mismatch += 1
            
        total_result.append(row)

    return match  / (mismatch + match) * 100