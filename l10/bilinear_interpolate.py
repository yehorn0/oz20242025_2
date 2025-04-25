import numpy as np


def bilinear_interpolate(matrix: np.ndarray, x: float, y: float) -> float:
    x0 = int(np.floor(x))
    x1 = min(x0 + 1, matrix.shape[1])

    y0 = int(np.floor(y))
    y1 = min(y0 + 1, matrix.shape[0])

    dx = x - x0
    dy = x - x0

    Q00 = matrix[x0, y0]
    Q01 = matrix[x0, y1]
    Q10 = matrix[x1, y0]
    Q11 = matrix[x1, y1]

    top = (1. - dx) * Q00 + dx * Q01
    bottom = (1. - dx) * Q10 + dx * Q11
    value = (1. - dy) * top + dy * bottom

    return value


if __name__ == '__main__':
    matrix = np.array([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90],
    ])

    interpolated_value = bilinear_interpolate(matrix, x=1.2, y=1.5)

    print(f"Interpolated value: {interpolated_value}")
