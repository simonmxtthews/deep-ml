def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here
	#matrix[0] = [x * 10 for x in matrix[0]]
	return [[x * scalar for x in row] for row in matrix]