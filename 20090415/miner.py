def start_matrix(col, row):
    matrix = []
    for c in range(col):
        matrix.append([])
        for _ in range(row):
            matrix[c].append(0) 

    return matrix
    
def coloca_bomba(matriz, lin, col):
    matriz[lin][col]=-1
    return matriz 
    
def define_valor(matriz, lin, col):
    
    return matriz 