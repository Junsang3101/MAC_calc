from src.mode_input import mode_input
from src.mode_json import mode_json
from src.mode_perf import mode_perf

def main():
    # 메뉴 선택
    while True:
        # 메인 메뉴 출력
        print("\n== 메뉴 ==\n")
        print("1. 사용자 입력")
        print("2. json 분석")
        print("3. 크기별 성능 분석")
        print("4. 종료")

        choice = 0
        while True:
            try:
                choice = int(input("선택: "))
            except ValueError:
                print("다시 입력해주세요.")
            except (KeyboardInterrupt, EOFError):
                return
            if not isinstance(choice, int):
                print("-<다시 입력해주세요>-")
                main()
            break

        if choice == 1:
            mode_input()
        elif choice == 2:
            mode_json()
        elif choice == 3:
            mode_perf()
        elif choice == 4:
            print("정상 종료되었습니다.")
            return
        else:
            print("-<다시 입력해세요>-")
            continue
 
if __name__ == "__main__":
    main()
