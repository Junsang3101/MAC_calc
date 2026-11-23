# MAC_calc
## 0. 미션 개요
본 프로젝트는 '코디세이 입학 연수 미션 1-3: AI가 계산하는 방법 흉내내기'로
파이썬으로 MAC연산을 만드는 것입니다.
- **목표**: MAC 연산이 무엇인지 이해하고 MAC 연산의 핵심 원리를 직접 코드로 구현해보며 크기에 따른 시간 복잡도와의 관계를 스스로 탐구한다.

## 1. 개발 환경
|개발 환경|버전|
|-|-|
|python|3.12.10|
``` powershell
PS C:\Users\User\Documents\3101junsang\mac_calc> python --version
Python 3.12.10
```

## 2. 기능 목록
- 1. 3 * 3 필터A, 필터B를 만든 후 MAC 연산
- 2. data.json 의 필터와 패턴을 읽어와 정규화해 MAC 연산 후 'X' 인지 'Cross'인지 검사
- 3. 행렬의 크기에 따른 연산 시간과 연산 횟수 구하기

## 3. 파일 구조
디스코드의 '미션3_MiniNPUSimulator.pdf' 를 보고 작업하며 모듈을 나눴으나  
결합도가 매우 높게 구현되었습니다.

``` text
mac_calc
│  .gitignore
│  data.json
│  main.py
│  README.md
│  __init__.py
│  
└─src
    │  judge.py
    │  mac.py
    │  mode_input.py
    │  mode_json.py
    │  mode_perf.py
    │  perf.py
    │  __init__.py
```

## 4. 프로그램 구조
main 모듈을 통해 메인 메뉴를 구현하고 위 서술된 기능 1, 2, 3 메뉴를 포함한 모듈들을  
`src/` 아래에 구성하였습니다.  
  
`mode*`: 하위 기능 메뉴들  
`mac`: mac 연산 
`judge`: `epsilon` 기반 A, B 비교 및 정규화, `data.json`에 맞는 함수가 들어있습니다.  
`perf`: 패턴, 필터, 테스트 횟수를 입력받아 평균 연산시간을 구하는 함수

## 5. 실행 방법
프로젝트 최상위 폴더에서 `python main.py`입력

## 6. 기능 요구사항 수행 목록

- [x] 데이터 구조: class로 구현하지 않고 list[list[int]] 로 연산하도록 했습니다.
``` python
# 리스트 예시
matrix = [[0 for c in cols] for r in rows]
# matrix[r][c] 로 해당 요소에 접근 가능
```
- [x] [모드 1 입력 처리(3x3)](./src/mode_input.py)
- [x] [모드 2 JSON 로드 및 스키마 검증](./src/mode_json.py): *결합도 높게 하드 코딩되었음
- [x] [정규화 구현](./src/judge.py): `normalize`함수로 구현 *X, Cross 이외 정규화 불가
- [x] [MAC 연산 구현](./src/mac.py)
- [x] [점수 비교 정책](./src/judge.py): `compar` -> 두 `float` 값을 `epsilon` 이하의 오차를 `True`로 처리함

## 7. 리포트

**실행 흐름**:
- 모드 1: 정수 (0, 1) 3개를 한 줄로 행렬 3개 입력 받기 -> 행렬 1,3 과 2,3 mac연산 후 결과 출력
- 모드 2: `data.json`파일을 읽어옴 -> 필터와 패턴을 읽어옴 -> 패턴과 필터를 정규화  
-> 패턴의 크기에 대응하는 필터가 있다면 mac 연산/출력 -> 최종 결과 출력