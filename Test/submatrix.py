# importando a biblioteca numpy
import numpy as np

# recebe a ordem da matrix quadrada n x n do usuário
n = int(input("Qual é a ordem da matrix desejada?"))

# cria uma matrix aleatória de números inteiros de 0 a 10
matrix = np.random.randint(10, size=(5, 5))

# mostra a matrix completa
print(matrix)

# seleciona a submatrix

x1 = int(input("A partir de qual linha será a submatrix?"))
x2 = int(input("Até qual linha será a submatrix?"))

y1 = int(input("A partir de qual coluna será a submatrix?"))
y2 = int(input("Até qual coluna será a submatrix?"))

submatrix = matrix[(x1-1):x2, (y1-1):y2]

# imprime para o usuário a submatrix

print(submatrix)