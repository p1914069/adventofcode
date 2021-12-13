if __name__ == '__main__':
    f = open("input_3.txt", "r")
    data = f.read().split('\n')

    liste = []
    petite_liste = []

    liste_compteurs = []
    petite_liste_compteurs = []

    gamma = []
    epsilon = []

    for i in range(1, 12):
        liste_compteurs.append(petite_liste_compteurs)

    for i in data:
        petite_liste = list(i)
        liste.append(petite_liste)

    nb0_col = 0
    nb1_col = 0

    # for j in liste:
    #     # Colonne 1
    #     if int(j[0]) == 0:
    #         nb0_col1 = nb0_col1 + 1
    #     else:
    #         nb1_col1 = nb1_col1 + 1
    #     # Colonne 2
    #     if int(j[1]) == 0:
    #         nb0_col1 = nb0_col1 + 1
    #     else:
    #         nb1_col1 = nb1_col1 + 1
    #     # Colonne 3
    #     if int(j[2]) == 0:
    #         nb0_col1 = nb0_col1 + 1
    #     else:
    #         nb1_col1 = nb1_col1 + 1
    #     # Colonne 4
    #     if int(j[3]) == 0:
    #         nb0_col1 = nb0_col1 + 1
    #     else:
    #         nb1_col1 = nb1_col1 + 1
    #     # Colonne 5
    #     if int(j[4]) == 0:
    #         nb0_col1 = nb0_col1 + 1
    #     else:
    #         nb1_col1 = nb1_col1 + 1
    #     # Colonne 6
    #     if int(j[5]) == 0:
    #         nb0_col1 = nb0_col1 + 1
    #     else:
    #         nb1_col1 = nb1_col1 + 1

    for i in range(0, 12):
        nb0_col = 0
        nb1_col = 0

        for j in liste:
            # Colonne 1
            if int(j[i]) == 0:
                nb0_col = nb0_col + 1
            else:
                nb1_col = nb1_col + 1

        if nb0_col > nb1_col:
            gamma.append(0)
            epsilon.append(1)
        else:
            gamma.append(1)
            epsilon.append(0)

        print(f'\nNombre de 0 colonne {i}: {nb0_col}')
        print(f'Nombre de 1 colonne {i}: {nb1_col}')

    print(f'\n → Gamma: {gamma}')
    print(f'\n → Epsilon: {epsilon}')

    # convertisseur gamma → nombre
    for i in gamma:
        pass