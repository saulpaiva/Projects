# importando a biblioteca numpy
import numpy as np


# cria uma matrix mat aleatória de números inteiros de 0 a 10
mat = np.random.randint(10, size=(16))


def nova_matrix(matrix, lins, cols):
    nova_matrix = matrix.reshape(lins, cols)
    return nova_matrix

# usando a função
print(nova_matrix(mat, 4, 4))