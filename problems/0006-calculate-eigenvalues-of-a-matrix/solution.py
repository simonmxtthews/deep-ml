import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]

	trA = a + d
	detA = a * d - b * c
	disc = pow(trA, 2) - 4 * detA

	if disc < 0:
		return []

	#λ^2 − trAλ + detA = 0
	lamA = (trA + math.sqrt(disc)) / 2
	lamB = (trA - math.sqrt(disc)) / 2

	eigenvalues = [lamA, lamB]

	eigenvalues.sort(reverse=True)

	return eigenvalues