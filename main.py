from projet.functions import tp, ts, afficher
import numpy as np


if __name__ == "__main__":
    mat = np.array(
        [
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0],
        ]
    )
    _ts = ts(mat)
    _tp = tp(_ts)
    afficher(_ts, "au plus vite")
    afficher(_tp, "sequentiel")
