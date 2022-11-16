
def conway1(strin):
    # Cette fonction calcule une iteration de la suite de Conway   
    l = len(strin)
    i = 0
    strout=''
    while (i < l):
        compteur = 0
        # je compte les caractères identiques
        while (i+compteur < l and strin[i+compteur] == strin[i]):
            compteur += 1
        strout = strout + str(compteur) + strin[i] 
        # je fais avancer l'index i
        i = i+compteur
    return(strout)

def conway(x):
    ###
    # Cette fonction recherche la suite de Conway
    # l'argument d'entrée x est le nombre d'itérations à effectuer
    ###
    stringi='1'
    for i in range(x):
        print(stringi)
        stringi=conway1(stringi)

conway(10)
