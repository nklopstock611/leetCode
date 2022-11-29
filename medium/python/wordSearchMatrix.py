board = [
            ["A","B","C"],
            ["S","F","C"],
            ["A","D","E"]
        ]
word = "ABCCED"
g = {}

# intento fallido de construir el grafo...
for i in range(len(board)):
    for j in range(len(board[i])):
        l = []
        # esquinas de arriba
        if (j - 1) < 0 and (i - 1) < 0:
            l.append(board[i + 1][j])
            l.append(board[i][j + 1])
        elif (j + 1) >= len(board) and (i - 1) < 0:
            l.append(board[i][j - 1])
            l.append(board[i + 1][j])
        # bordes de arriba
        elif (i - 1) < 0:
            l.append(board[i][j - 1])
            l.append(board[i + 1][j])
            l.append(board[i][j + 1])
        # esquinas de abajo
        elif (j + 1) > len(board[i]) and (i + 1) >= len(board):
            l.append(board[i + 1][j])
            l.append(board[i][j + 1])
        elif (j + 1) >= len(board[i]) and (i + 1) >= len(board):
            l.append(board[i][j - 1])
            l.append(board[i - 1][j])
        # bordes de abajo
        elif (i + 1) >= len(board):
            l.append(board[i][j - 1])
            l.append(board[i - 1][j])
            l.append(board[i][j + 1])
        # bordes de izquierda
        elif (j - 1) < 0:
            l.append(board[i + 1][j])
            l.append(board[i - 1][j])
            l.append(board[i][j + 1])
        # bordes de derecha
        elif (j + 1) >= len(board[i]):
            l.append(board[i + 1][j])
            l.append(board[i - 1][j])
            l.append(board[i][j - 1])
        # centro
        else:
            l.append(board[i][j - 1])
            l.append(board[i + 1][j])
            l.append(board[i - 1][j])
            l.append(board[i][j + 1])

        g[board[i][j]] = l

print(g)

# algoritmo recursivo que recibe dos parametros:
# recibe el nodo actual y el nodo al que tiene conección.


