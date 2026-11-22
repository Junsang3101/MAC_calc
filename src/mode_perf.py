from .perf import get_perf

def mode_perf():
    print("\n== 크기별 성능 분석 ==\n")
    matrix5 = make_matrix(5, 5)
    matrix13 = make_matrix(13, 13)
    matrix25 = make_matrix(25, 25)
    print(f"== 5 x 5 ==\n10회 평균 연산 시간: {get_perf(matrix5, matrix5) * 1000}ms\n연산 횟수: {5**2}")
    print(f"== 13 x 13 ==\n10회 평균 연산 시간: {get_perf(matrix13, matrix13) * 1000}ms\n연산 횟수: {13**2}")
    print(f"== 25 x 25 ==\n10회 평균 연산 시간: {get_perf(matrix25, matrix25) * 1000}ms\n연산 횟수: {25**2}")
    
    while True:    
        print("\n1. 사용자 지정 크기 테스트")
        print("2. 돌아가기")
        try:
            choice = int(input("\n선택: "))
        except (EOFError, KeyboardInterrupt, ValueError):
            return

        if not isinstance(choice, int):
            print("-<다시 입력해주세요>-")
            continue

        if choice == 1:
            size = 0
            while True:
                try:
                    size = int(input("크기(n x n) n: "))
                except (EOFError, KeyboardInterrupt, ValueError):
                    return

                if not isinstance(size, int) or size <= 0:
                    print("-<다시 입력해주세요>-")
                    continue
                break

            c_matrix = make_matrix(size, size)
            print(f"\n== {size} x {size} ==\n10회 평균 성능: {get_perf(c_matrix, c_matrix) * 1000}ms\n연산 횟수 = {size**2}")

        if choice == 2:
            return
        else:
            continue

def make_matrix(rows, cols):
    matrix = [[0 for c in range(cols)] for r in range(rows)]
    return matrix