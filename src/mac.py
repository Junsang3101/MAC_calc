def mac(data: list[list[int]], filter: list[list[int]]):
    if not data:
        raise ValueError("x패턴 행렬이 비어있습니다.")
    elif not filter:
        raise ValueError("필터 행렬이 비어있습니다.")
    
    data_rows, data_cols = len(data), len(data[0])
    filter_rows, filter_cols = len(data), len(data[0])
 
    if data_rows != filter_rows and data_cols != filter_cols:
        raise ValueError("패턴과 필터의 크기가 불일치합니다.")

    matched = sum(
        1
        for r in range(data_rows)
        for c in range(data_cols)
        if data[r][c] * filter[r][c] != 0
    )

    total_cells = data_rows * data_cols
    return (matched / total_cells) * 100