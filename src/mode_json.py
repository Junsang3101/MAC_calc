from pathlib import Path
import json

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

    data = load_json(filepath)
    try:
        filer_5 = data["filters"]["size_5"]
        filer_13 = data["filters"]["size_13"]
        filer_25 = data["filters"]["size_25"]
    except (KeyError, ValueError):
        print(f"필터를 불러오기에 실패했습니다. {filepath}를 확인해주세요.")

    try:
        pattern_5 = data["patterns"]["size_5_1"]
        #pattern_5.append(data["patterns"]["size_5_2"])
        pattern_13 = data["patterns"]["size_13_1"]
        #pattern_13.append(data["patterns"]["size_13_2"])
        pattern_25 = data["patterns"]["size_5_1"]
        #pattern_25.append(data["patterns"]["size_25_2"])
    except (KeyError, ValueError):
        print(f"패턴을 불러오기에 실패했습니다. {filepath}를 확인해주세요.")
    print(pattern_5, pattern_13, pattern_25)
    