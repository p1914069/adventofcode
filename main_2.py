if __name__ == '__main__':
    f = open("input_2.txt", "r")

    # Technique 1
    # data = [[l.split(" ")[0], int(l.split(" ")[1])] for l in f.read().split('\n')]

    # Technique 2
    data = f.read().split('\n')
    instruction = []
    # instruction: [tabline1, tabline2, tabline3,...]
    # tabline: ['forward', 2]
    # → instruction: [['forward', 2], ['down', 6],...]

    for l in data:
        line = l.split(" ")
        tabline = [line[0], int(line[1])]
        instruction.append(tabline)

    profondeur = 0
    avance = 0
    visee = 0

    # Partie 1
    # for i in instruction:
    #     if i[0] == "forward":
    #         avance = avance + i[1]
    #     if i[0] == "down":
    #         profondeur = profondeur + i[1]
    #     if i[0] == "up":
    #         profondeur = profondeur - i[1]
    #
    # resultat_1 = avance * profondeur

    # Partie 2
    for i in instruction:
        if i[0] == "down":
            visee = visee + i[1]
        if i[0] == "up":
            visee = visee - i[1]
        if i[0] == "forward":
            avance = avance + i[1]
            profondeur = profondeur + visee * i[1]

    resultat_2 = avance * profondeur

    print(instruction)

    print(f'\nRésultat de la multiplication: {resultat_2}')
