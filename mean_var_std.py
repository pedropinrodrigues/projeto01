import numpy as np

def calculate(list):

    matriz = np.array(list).reshape(3, 3)

    # mean = []
    # mean.append(np.mean(matriz, axis=0, dtype=np.int8))
    # mean.append(np.mean(matriz, axis=0, dtype=np.int8))
    # print(mean)

    calculations = {
        'Mean': {
            'axis1': np.mean(matriz, axis=0, dtype=np.int8).tolist(),
            'axis2': np.mean(matriz, axis=0, dtype=np.int8).tolist(),
            'flattened': int(np.mean(list, dtype=np.int8))
        },
        'Variance': {
        },
    }
    print(calculations)

    return calculations

list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
calculate(list)