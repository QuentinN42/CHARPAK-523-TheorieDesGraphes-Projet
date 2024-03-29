"""
Nour Boulahcen, Quentin Lieumont
Programe qui trouve le planning sequentiel et le planning au plus vite d'un graph de taches.
Il est montré dans le main quatres exemples de graphs.
La fonction peut etre testé plus en profondeur via un import :
>>> from main import test
>>> import numpy as np
>>> matrice = np.ones((2,2))
>>> test(matrice)
=============================
    Test sur la matrice :
  0 1
0 1 1
1 1 1
Le graph est cyclique
"""
from functions import tp, ts, afficher, CycleError
import numpy as np


def test(mat: np.ndarray, _graph: bool = True):
    """
    applique l'algorithme principal sur la matrice mat
    :param mat: matrice à tester
    :param _graph: trace un graphique turlte.py
    """
    assert mat.shape[0] == mat.shape[1]
    print("="*29)
    print("    Test sur la matrice :")
    print("  " + " ".join(map(str, range(len(mat)))))
    for i, l in enumerate(mat):
        print(str(i) + " " + " ".join(map(str, l.astype(int))))
    try:
        _ts = ts(mat)
        _tp = tp(_ts)
        afficher(_ts, "au plus vite")
        afficher(_tp, "sequentiel")
        print("\n"*5)
        if _graph:
            from tortue import graph, t
            graph(mat, weight=False)
            t.up()
            t.setpos(1000, 1000)
    except CycleError:
        print("Le graph est cyclique")
        print("\n"*5)
        return


if __name__ == "__main__":
    matrices = [
        np.array(
            [
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1],
                [1, 0, 0, 0, 0, 0],
            ]
        ),
        np.array(
            [
                [0, 0, 1],
                [1, 0, 1],
                [0, 0, 0],
            ]
        ),
        np.array(
            [
                [0, 0, 1],
                [1, 0, 1],
                [1, 0, 0],
            ]
        ),
        np.ones((5, 5)),
        np.zeros((5, 5))
    ]
    for matrice in matrices:
        test(matrice, _graph=False)
    input()
