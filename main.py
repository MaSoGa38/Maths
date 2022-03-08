# coding: UTF-8
"""
Script: Maths/main
Création: mathiassoler, le 08/03/2022
"""


# Imports

# Fonctions
def cal_deter(matrice: list):
    ordre = len(matrice)
    if ordre == 1:
        return matrice[0]
    elif ordre == 2:
        return matrice[0][0]*matrice[1][1] - matrice[0][1]*matrice[1][0]
    else:
        return

# Programme principal
def main():
    pass


if __name__ == '__main__':
    main()
# Fin
