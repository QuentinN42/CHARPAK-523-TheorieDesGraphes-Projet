import numpy as np


class CycleError(Exception):
    """
    Raised when a cylce is found in the graph
    """
    pass


def tp(_ts: list):
    """
    renvoit la liste des taches avec un seul executant
    :param _ts: liste des taches parallele
    :return: temps dans un planning sequentiel
    """
    return [tache for jour in _ts for tache in jour]


def ts(mat: np.ndarray) -> list:
    """
    retourne le temp sequentiel
    :param mat: la matrice de taches
    :return: temp sequentiel
    """
    _ts: list = []
    n = len(mat)
    _taked = np.zeros(n, dtype=bool)
    while sum(_taked) != n:
        _add = [
            i
            for i, e in enumerate(list(mat.transpose()))
            if not _taked[i] and not sum(np.where(_taked, 0, e) != 0)
        ]
        if not _add:
            raise CycleError("A cycle is found in this graph")
        _taked[_add] = True
        _ts.append(_add)
    return _ts


def afficher(t: list, name: str = None):
    """
    affiche le temps
    """
    if name:
        print(f"Planning {name} :")
    else:
        print(f"Planning :")
    for i, e in enumerate(t):
        if type(e) == list:
            print(f"{i}: {','.join(map(str,e))}")
        else:
            print(f"{i}: {e}")
