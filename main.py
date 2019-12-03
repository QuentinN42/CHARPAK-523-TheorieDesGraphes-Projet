from projet.functions import tp, ts, afficher
from projet.tortue import graph, t
import numpy as np


if __name__ == "__main__":
    mat = np.array(
        [
            [1, 0, 0, 1, 0, 0],
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
    graph(mat, weight=False)
    t.up()
    t.setpos(1000, 1000)
    input()
