def reflectivite(relation, etendu):
    reflectif = True
    for i in range(etendu):
        a = [i, i]
        if a not in relation:
            print("il manque " + str(a))
            reflectif = False
            break

    return reflectif


def irreflectivite(relation):
    irreflectif = True
    for paire in relation:
        boucle = [paire[0], paire[0]]
        if boucle in relation:
            print("Il y a la boucle " + str(boucle))
            irreflectif = False
            break
    return irreflectif


def symetrique(relation):
    for paire in relation:
        temp = [paire[1], paire[0]]
        if temp not in relation:
            print("Il manque le retour pour " + str(paire))
            return False
    return True


def asymetrique(relation):
    if (irreflectivite(relation)) == False:
        return False
    else:
        for paire in relation:
            retour = [paire[1], paire[0]]
            if retour in relation:
                print("Il y a un retour pour cette paire: " + str(paire))
                return False
    return True


def antisymetrique(relation):
    for paire in relation:
        if paire[0] != paire[1]:
            retour = [paire[1], paire[0]]
            if retour in relation:
                print("Il y a un retour pour cette paire: " + str(paire))
                return False

    return True


def transitivite(relation):
    transitif = True
    if (len(relation) > 0):
        for paire in relation:
            a = paire[0]
            b = paire[1]
            for secondepaire in relation:
                if secondepaire[0] == b:
                    c = secondepaire[1]
                    temp = [a, c]
                    if (temp not in relation):
                        transitif = False
                        print("La paire " + str(paire) + "et la paire " + str(
                            [b, c]) + "sont présente, mais pas la paire " + str(
                            temp))
                        return transitif
    return transitif


def clotureTransitive(cloture):
    liste = []
    i = 0
    j = 0
    for paire in cloture:
        liste.append(paire)
    while(True):
        for paire in liste:
            a = paire[0]
            b = paire[1]
            for secondepaire in liste:
                if secondepaire[0] == b:
                    c = secondepaire[1]
                    transition = [a, c]
                    if transition not in liste:
                        liste.append(transition)
                        i += 1
        if i == j:
            break
        else:
            j = i
    return liste