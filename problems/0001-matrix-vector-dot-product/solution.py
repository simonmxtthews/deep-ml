def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	numCols = len(a[0])
	size = len(b)
	if numCols != size: 
		return -1
	dot = []
	i = 0
	for x in range(size):
		sum = 0
		for y in range(numCols):
			sum += a[x][y] * b[y]
		dot.append(sum)
	return dot;