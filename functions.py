import numpy as np


def tp(ts: list):
    """
    renvoit la liste des taches avec un seul executant
    :param ts: liste des taches parallele
    :return: temps dans un planning sequentiel
    """
    return [tache for jour in ts for tache in jour]


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
        _add = [i for i, e in enumerate(list(mat.transpose())) if not _taked[i] and not sum(np.where(_taked, 0, e) != 0)]
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
