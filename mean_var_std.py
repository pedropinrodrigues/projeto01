import numpy as np

def calculate(data):
    # Converte a lista em uma matriz 3x3
    matriz = np.array(data).reshape(3, 3)

    # Cálculos
    calculations = {
        'mean': [
            np.mean(matriz, axis=0).tolist(), # Média ao longo das colunas
            np.mean(matriz, axis=1).tolist(), # Média ao longo das linhas
            np.mean(matriz).tolist()          # Média achatada
        ],
        'variance': [
            np.var(matriz, axis=0).tolist(),  # Variância ao longo das colunas
            np.var(matriz, axis=1).tolist(),  # Variância ao longo das linhas
            np.var(matriz).tolist()           # Variância achatada
        ],
        'standard deviation': [
            np.std(matriz, axis=0).tolist(),  # Desvio padrão ao longo das colunas
            np.std(matriz, axis=1).tolist(),  # Desvio padrão ao longo das linhas
            np.std(matriz).tolist()           # Desvio padrão achatado
        ],
        'max': [
            np.max(matriz, axis=0).tolist(),  # Máximo ao longo das colunas
            np.max(matriz, axis=1).tolist(),  # Máximo ao longo das linhas
            np.max(matriz).tolist()           # Máximo achatado
        ],
        'min': [
            np.min(matriz, axis=0).tolist(),  # Mínimo ao longo das colunas
            np.min(matriz, axis=1).tolist(),  # Mínimo ao longo das linhas
            np.min(matriz).tolist()           # Mínimo achatado
        ],
        'sum': [
            np.sum(matriz, axis=0).tolist(),  # Soma ao longo das colunas
            np.sum(matriz, axis=1).tolist(),  # Soma ao longo das linhas
            np.sum(matriz).tolist()           # Soma achatada
        ],
    }

    return calculations

# Dados de exemplo
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(lista)
print(result)
