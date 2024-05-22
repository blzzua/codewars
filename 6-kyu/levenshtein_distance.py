# https://www.codewars.com/kata/545cdb4f61778e52810003a2

def levenshtein(a,b):
    if a == '':
        return len(b)
    if b == '':
        return len(a)
    n = len(a)
    m = len(b)
    matrix = [[0] * (m+1) for _ in range(n+1)]
    for j, _ in enumerate(matrix[0]):
        matrix[0][j] = j
    for i, _ in enumerate(matrix):
        matrix[i][0] = i
        
    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = matrix[i-1][j] + 1
            deletion = matrix[i][j-1] + 1
            substitution = matrix[i-1][j-1] + int(a[i-1]!= b[j-1])
            matrix[i][j] = min(insertion, deletion, substitution)

    return matrix[-1][-1]

