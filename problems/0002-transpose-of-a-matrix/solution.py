def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    numRows = len(a)    # 2
    numCols = len(a[0]) # 3

    out = []

    for x in range(numCols):
        out.append([])
        for y in range(numRows):
            out[x].append(a[y][x])

    return out
    