if __name__ == '__main__':
    f = open("input_3.txt", "r")
    data = f.read().split('\n')

    liste = []
    petite_liste = []

    liste_compteurs = []
    petite_liste_compteurs = []

    gamma = []
    gamma_int = 0

    epsilon = []
    epsilon_int = 0

    compteur_g = 0
    compteur_e = 0

    liste_oxygene = []
    liste_co2 = []


    for i in data:
        petite_liste = list(i)
        liste.append(petite_liste)

    nb0_col = 0
    nb1_col = 0

    for i in range(0, 12):
        nb0_col = 0
        nb1_col = 0

        for j in liste:

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
    print(f'\n → Epsilon: {epsilon}\n')

    # gamma = 3903
    # epsilon = 384

    print('Résultat 1ère partie = 749 376')

    # 2eme partie

    liste_oxygene = liste
    print(liste_oxygene)

    nb_lignes = len(liste_oxygene)

    print(liste_oxygene)


