# Preparation du projet 3

def partie_1():
    # Créer un fichier texte (carte.txt) contenant la variable text

    text = "WWWW-----W\nW-------WW\nWWW-M--WWW\nWWWWWW--WW\n"
    file = open("carte.txt","r+")
    print("Tên của file là: ", file.name)
    file.write(text)
    file.write("hahahahah\n")
    file.close()



def partie_2():
    # Afficher en console le fichier texte créé à la partie 1

    file = open("carte.txt")
    print(file.read())

    file.close()



def partie_3(lettre):
    # Vérifier si la lettre entrée en paramètre est présente
    # dans le fichier créé à l'exercice 1 (retourner True si
    # la lettre est présente et False sinon)

    n = 0
    file = open("carte.txt")

    for line in file:
        for char in line:
            if lettre == char:
                n += 1
    if n > 0:
         print(True)
    else:
         print(False)

    file.close()




def partie_4(lettre):
    # Trouver la position de la lettre passée en paramètre dans
    # le fichier créé à l'exercice 1. Si lettre == "M", la fonction
    # doit renvoyer le tuple (4, 2) car le lettre "M" est dans la colonne
    # 4 (numérotation à partir de 0) et la ligne 2 dans la variable text de
    # l'exercice 1.

    n = -1

    file = open("carte.txt")

    for line in file:
        n=n+1
        for char in line:
            if lettre == char:
                m = line.find(lettre)
                print("tuple = (",m,",",n,")")

    file.close()



def partie_5():
    # Créer un dictionnaire contenant toutes les lettres présentes
    # dans le fichier texte de l'exercice avec leur nombre d'apparition
    # dans le fichier : {"W": 22, "M": 1}

    dic = {}
    n = 0

    file = open("carte.txt")

    str = file.read()

    key1 = str[0]
    value1 = str.count(key1)
    dic[key1] = value1
    #print(dic)

    for char in str:
        if char != key1:
            key2 = char
            value2 = str.count(key2)
            dic[key2] = value2
    print(dic)

    file.close()


def partie_6():
    # Demander si le joueur veut continuer le jeu (avec input). Si la
    # réponse est "oui" ou "o", on repose la même question. Si la réponse
    # est "non" ou "n", la boucle s'arrête. Si une autre réponse est donnée,
    # afficher "Réponse non correcte" puis reposer la question.




    while True:
        print("est ce que tu veux continuer le jeu? ")
        s = input()
        if s == "oui" or s == "o":
            continue

        elif s == "non" or s == "n":
            print("la boucle s'arrête")
            break

        else:
            print("Réponse non correcte")



if __name__ == "__main__":
    partie_1()
    partie_2()
    print(partie_3("M"))
    print(partie_4("M"))
    partie_5()
    partie_6()