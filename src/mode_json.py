from pathlib import Path
import json
from .judge import normalize

def load_json(filepath: Path | str = None):

    try:
        with open(filepath, "r", encoding="utf-8") as src:
            data = json.load(src)
    except FileNotFoundError:
        print(f"{filepath}이 존재하지 않습니다. 해당 경로에 'data.json' 파일을 넣거나 올바른 주소를 인자로 입력해주세요.")

    return data

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

    filter_5 = normalize(filter_5, normalize_map)
    filter_13 = normalize(filter_13, normalize_map)
    filter_25 = normalize(filter_25, normalize_map)
    print("필터를 성공적으로 정규화했습니다.")

    for idx in range(len(patterns)):
        patterns[idx] = normalize(patterns[idx], normalize_map)
    print("패턴을 성공적으로 정규화했습니다.")
