if __name__ == '__main__':
    f = open("input_4.txt", "r")

    # ==== Liste des nombre à vérifier ====
    nb_a_verif = f.readline()
    liste_nb_a_verif = nb_a_verif.split(',')

    # Passer ces nombres en int
    for c in range(len(liste_nb_a_verif)):
        liste_nb_a_verif[c] = int(liste_nb_a_verif[c])

    print(liste_nb_a_verif)

    # ==== Liste des tableaux ====
    tableaux = f.read().split('\n\n')
    print(tableaux)

    c = 0
    while c in range(len(tableaux)):
        if tableaux[c] == '':
            tableaux.pop(c)
        else:
            c += 1
    print(f'\n{tableaux}')

    for c in range(len(tableaux)):
        tableaux[c] = tableaux[c].split('\n')
    print(f'\n{tableaux}')

    for i in range(len(tableaux)):
        j = 0
        while j in range(len(tableaux[i])):
            if tableaux[i][j] == '':
                tableaux[i].pop(j)
            else:
                j += 1
    print(f'\n{tableaux}')

    for i in range(len(tableaux)):
        for j in range(len(tableaux[i])):
            tableaux[i][j] = tableaux[i][j].split(' ')

    print('\n → Tableaux séparés par ligne')
    print(f'{tableaux}')

for i in range(len(tableaux)):
    for j in range(len(tableaux[i])):
        k = 0
        while k in range(len(tableaux[i][j])):
            if tableaux[i][j][k] == '':
                tableaux[i][j].pop(k)
            else:
                k += 1

for i in range(len(tableaux)):
    for j in range(len(tableaux[i])):
        k = 0
        while k in range(len(tableaux[i][j])):
            try:
                tableaux[i][j][k] = int(tableaux[i][j][k])
                k += 1
            except:
                tableaux[i][j].pop(k)

WIN = False
tableau_gagnant = 0
num_marque = 0

n = 0

while not WIN:

    for i in range(len(tableaux)):
        for j in range(len(tableaux[i])):
            for k in range(len(tableaux[i][j])):
                if tableaux[i][j][k] == liste_nb_a_verif[n]:
                    tableaux[i][j][k] = -1

    for i in range(len(tableaux)):
        for j in range(5):
            if (tableaux[i][j][0] == -1 and
                    tableaux[i][j][1] == -1 and
                    tableaux[i][j][2] == -1 and
                    tableaux[i][j][3] == -1 and
                    tableaux[i][j][4] == -1):
                WIN = True
                tableau_gagnant = i
                num_marque = liste_nb_a_verif[n]

    for i in range(len(tableaux)):
        for j in range(5):
            if (tableaux[i][0][j] == -1 and
                    tableaux[i][1][j] == -1 and
                    tableaux[i][2][j] == -1 and
                    tableaux[i][3][j] == -1 and
                    tableaux[i][4][j] == -1):
                WIN = True
                tableau_gagnant = i
                num_marque = liste_nb_a_verif[n]

    n += 1


def getScore(board):
    score = 0

    for j in range(5):
        for k in range(5):
            if tableaux[board][j][k] > 0:
                score += tableaux[board][j][k]

    score *= num_marque

    return score


score_gagnant = getScore(tableau_gagnant)

print(" → Le tableau gagnant: ", tableau_gagnant)

print(" → Le score du tableau gagnant: ", score_gagnant)
