import numpy as np

import numpy as np

def calculate(lista):
    # 1) Validar longitud
    if len(lista) < 9:
        raise ValueError("La lista debe contener nueve números")

    # 2) Convertir a array numpy 3x3
    arr = np.array(lista).reshape(3, 3)

    # 3) Calcular estadísticas
    mean_axis0 = arr.mean(axis=0).tolist()
    mean_axis1 = arr.mean(axis=1).tolist()
    mean_flat = arr.mean().item()

    var_axis0 = arr.var(axis=0).tolist()
    var_axis1 = arr.var(axis=1).tolist()
    var_flat = arr.var().item()

    std_axis0 = arr.std(axis=0).tolist()
    std_axis1 = arr.std(axis=1).tolist()
    std_flat = arr.std().item()

    max_axis0 = arr.max(axis=0).tolist()
    max_axis1 = arr.max(axis=1).tolist()
    max_flat = arr.max().item()

    min_axis0 = arr.min(axis=0).tolist()
    min_axis1 = arr.min(axis=1).tolist()
    min_flat = arr.min().item()

    sum_axis0 = arr.sum(axis=0).tolist()
    sum_axis1 = arr.sum(axis=1).tolist()
    sum_flat = arr.sum().item()

    calculations = {
        'mean': [mean_axis0, mean_axis1, mean_flat],
        'variance': [var_axis0, var_axis1, var_flat],
        'standard deviation': [std_axis0, std_axis1, std_flat],
        'max': [max_axis0, max_axis1, max_flat],
        'min': [min_axis0, min_axis1, min_flat],
        'sum': [sum_axis0, sum_axis1, sum_flat]
    }

    return calculations
