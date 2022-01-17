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

    liste_a_tester = []

    for i in range(1, 12):
        liste_compteurs.append(petite_liste_compteurs)

    for i in data:
        petite_liste = list(i)
        liste.append(petite_liste)

    nb0_col = 0
    nb1_col = 0

# OXYGENE
    liste_oxygene = liste

    for i in range(0, 12):
        nb0_col = 0
        nb1_col = 0

        for j in liste_oxygene:

            if int(j[i]) == 0:
                nb0_col = nb0_col + 1
            else:
                nb1_col = nb1_col + 1

        if nb0_col > nb1_col:
            for j in liste_oxygene:
                if int(j[i]) == 0:
                    liste_a_tester.append(j)

        else:
            for j in liste_oxygene:
                if int(j[i]) == 1:
                    liste_a_tester.append(j)

        print(f'\nNombre de 0 colonne {i}: {nb0_col}')
        print(f'Nombre de 1 colonne {i}: {nb1_col}')

        liste_oxygene = list(liste_a_tester)
        liste_a_tester.clear()
        print(len(liste_oxygene))

    print(f' → OXYGENE: {liste_oxygene}')
    print('Résultat = 3871')

# C02
    liste_CO2 = liste

    for i in range(0, 9):
        nb0_col = 0
        nb1_col = 0

        for j in liste_CO2:

            if int(j[i]) == 0:
                nb0_col = nb0_col + 1
            else:
                nb1_col = nb1_col + 1

        if nb1_col < nb0_col:
            for j in liste_CO2:
                if int(j[i]) == 1:
                    liste_a_tester.append(j)

        else:
            for j in liste_CO2:
                if int(j[i]) == 0:
                    liste_a_tester.append(j)

        print(f'\nNombre de 0 colonne {i}: {nb0_col}')
        print(f'Nombre de 1 colonne {i}: {nb1_col}')

        liste_CO2 = list(liste_a_tester)
        liste_a_tester.clear()
        print(len(liste_CO2))

    print(f' → CO2: {liste_CO2}')
    print('Résultat = 613')

    # print(f'\n → Gamma: {gamma}')
    # print(f'\n → Epsilon: {epsilon}\n')
    #
    # # gamma = 3903
    # # epsilon = 384
    #
    # print('Résultat 1ère partie = 749 376')

