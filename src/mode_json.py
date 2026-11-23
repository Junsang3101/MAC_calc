from pathlib import Path
import json
from .judge import normalize_label, judge, compar

def load_json(filepath: Path | str = None):

    try:
        with open(filepath, "r", encoding="utf-8") as src:
            data = json.load(src)
    except FileNotFoundError:
        print(f"{filepath}이 존재하지 않습니다. 해당 경로에 'data.json' 파일을 넣거나 올바른 주소를 인자로 입력해주세요.")

    return data

def run_case(pattern, filter):
    temp = judge(filter, pattern)
    same = compar(temp["Cross"], temp["X"])
    compute = len(pattern["input"]) ** 2
    print("\n== 개별 테스트 결과 ==\n")
    if same:
        print(f"Cross: {temp['Cross']}\nX: {temp['X']}")
        print(f"Cross 와 X의 일치도가 사실상 동일합니다.")
        print(f"계산 시간: {temp['perf']* 1000}ms")
        print(f"연산 횟수 {compute}")
    elif temp["Cross"] > temp["X"]:
        print(f"Cross: {temp['Cross']}\nX: {temp['X']}")
        print(f"검사 결과: Cross")
        print(f"계산 시간: {temp['perf']* 1000}ms")
        print(f"연산 횟수 {compute}")
    elif temp["Cross"] < temp["X"]:
        print(f"Cross: {temp['Cross']}\nX: {temp['X']}")
        print(f"검사 결과: X")
        print(f"계산 시간: {temp['perf']* 1000}ms")
        print(f"연산 횟수 {compute}")
    print("\n======================\n")

def mode_json(path: Path | str = None):
    if path is not None:
        filepath = Path(path)
    else:
        filepath = Path(__file__).parent.parent / "data.json"

    print("\n == json 분석 모드 ==\n")
    data = load_json(filepath)
    print("파일을 성공적으로 읽어왔습니다.")

    try:
        filter_5 = data["filters"]["size_5"]
        filter_13 = data["filters"]["size_13"]
        filter_25 = data["filters"]["size_25"]
    except (KeyError, ValueError):
        print(f"필터를 불러오는데 실패했습니다. {filepath}를 확인해주세요.")
    print("필터를 성공적으로 읽어왔습니다.")

    try:
        patterns = []
        for k in data["patterns"]:
            patterns.append(data["patterns"][k])
    except (KeyError, ValueError):
        print(f"패턴을 읽어오는데 실패했습니다. {filepath}를 확인해주세요.")
    print("패턴을 성공적으로 읽어왔습니다.")

    normalize_map = {
        'x': 'X',
        '+': 'Cross',
        'cross': 'Cross'
    }

    filter_5 = normalize_label(filter_5, normalize_map)
    filter_13 = normalize_label(filter_13, normalize_map)
    filter_25 = normalize_label(filter_25, normalize_map)
    print("필터를 성공적으로 정규화했습니다.")
    for idx in range(len(patterns)):
        patterns[idx] = normalize_label(patterns[idx], normalize_map)
    print("패턴을 성공적으로 정규화했습니다.")

    result = {
        "succ_c": 0,
        "fail_c": 0,
        "Fails": []
    }

    '''
    # Fails 요소
    {
        "index": null, #int
        "reason": null  #str
    }
    '''

    print()
    for idx in range(len(patterns)):
        # 필터 크기에 해당하는 패턴이 맞는가
        print(f"{len(patterns[idx]['input'])} x {len(patterns[idx]['input'][0])} 크기의 패턴 검사")

        p_size = len(patterns[idx]['input']) * len(patterns[idx]['input'][0])
        if p_size == 5**2:
            run_case(patterns[idx], filter_5)
        elif p_size == 13**2:
            run_case(patterns[idx], filter_13)
        elif p_size == 25**2:
            run_case(patterns[idx], filter_25)
        else:
            result["Fails"] += {
                "index": idx,
                "reason": "SizeMismatch"
            }
            print(f"{p_size}")
            print(f"{idx+1}번 패턴 작업 실패. (SizeMismatch)")
            result["fail_c"] += 1
            continue
        result["succ_c"] += 1

    print(f"== 종합 결과 ==")
    print(f"총 테스트 수: {result['succ_c'] + result['fail_c']}")
    print(f"성공: {result['succ_c']}")
    print(f"실패: {result['fail_c']}")
    print(f"실패 사유:")
    for reason in result["Fail"]:
        print("test", reason)