from relation import reflectivite, irreflectivite, symetrique, asymetrique, antisymetrique, transitivite


def devoir(relation, etendu):

    relation.sort(key=lambda tup: tup[0])
    print(relation)

    print("Reflexif " + str(reflectivite(relation, etendu)) + "\n")
    print("Irreflexif " + str(irreflectivite(relation)) + "\n")
    print("Symétrique " + str(symetrique(relation)) + "\n")
    print("Asymétrique " + str(asymetrique(relation)) + "\n")
    print("Antisymétrique " + str(antisymetrique(relation)) + "\n")
    print("Transitivité " + str(transitivite(relation)) + "\n")


if __name__ == '__main__':


    relation = []
    domaine = 50
    ensemble = [x for x in range(domaine)]
    for x in ensemble:
        for y in ensemble:
            if (x % 5 == y % 5):
                relation.append([x, y])
    devoir(relation, domaine)