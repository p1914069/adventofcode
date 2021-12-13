
if __name__ == '__main__':
    f = open("input_1.txt", "r")
    data = f.read()

    liste = data.split('\n')
    liste_nbre = []

    compteur = 0
    saut = 0

    var = 0

    compteur_sommes = 0
    somme_a = 0
    somme_b = 0

    n_a = 0
    n_b = 0


    for i in liste:
        liste_nbre.append(int(i))

        if saut == 1:
            if int(i) > var:
                compteur = compteur +1

        else:
            saut = 1
        var = int(i)

    for j in range(0, len(liste_nbre)-3):
        n1 = liste_nbre[j]
        n2 = liste_nbre[j+1]
        n3 = liste_nbre[j+2]
        n4 = liste_nbre[j+3]

        for n_a in range(0, 2):
            somme_a = n1 + n2 + n3

        for n_b in range(1, 3):
            somme_b = n2 + n3 + n4

        if somme_a < somme_b:
            compteur_sommes = compteur_sommes +1

        print(f'Tour numéro: {j}')
        print(f'→ Somme A: {somme_a}')
        print(f'→ Somme B: {somme_b}\n')

    print(f'\nNombres augmentations: {compteur_sommes}')


