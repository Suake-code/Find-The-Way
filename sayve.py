import numpy as np
import json
def save(lastlevel):
	if lastlevel == int:
		lastlevel = 0
	lastlevel = str(lastlevel)
	try:
		sauvegarde = open("sauvegarde.txt")
		print("Fichier trouvé")
	except FileNotFoundError:
		print("Création d'une nouvelle sauvegarde")
		sauvegarde = open("sauvegarde.txt", "x")
	sauvegarde.close()
	sauvegarde = open("sauvegarde.txt", "r")
	txtsave =(sauvegarde.read())
	print ("Contenu du fichier de sauvegarde :",txtsave)
	sauvegarde.close()
	if txtsave == "":
		print("Fichier vide")
		sauvegarde = open("sauvegarde.txt", "a")
		sauvegarde.write(lastlevel)
		sauvegarde.close()
		sauvegarde = open("sauvegarde.txt", "r")
		print("Fichier de sauvegarde mis à jours", "\nContenu du fichier de sauvegarde :",sauvegarde.read())
		sauvegarde.close()
		lastlevel = int(lastlevel)
	elif int(txtsave) < int(lastlevel):
		sauvegarde = open("sauvegarde.txt", "w")
		sauvegarde.write(lastlevel)
		sauvegarde.close()
		sauvegarde = open("sauvegarde.txt", "r")
		print("Nouveau niveau débloqué", "\nContenu du fichier de sauvegarde :",sauvegarde.read())
		sauvegarde.close()
		lastlevel = int(lastlevel)
	else :
		print("Pas de niveau débloqué")
		lastlevel = int(txtsave)
	return(lastlevel)





def savve(pnl, salle):
    try:
        sauvegardecustom = open("sauvegardecustom.txt")
        print("Fichier trouvé")
    except FileNotFoundError:
        print("Création d'une nouvelle sauvegarde")
        sauvegardecustom = open("sauvegardecustom.txt", "x")
    sauvegardecustom.close()
    if pnl == 1:
        sauvegardecustom = open("sauvegardecustom.txt", "w")
        json.dump(salle.tolist(), sauvegardecustom)
        sauvegardecustom.close()
    if pnl == 0:
        sauvegardecustom = open("sauvegardecustom.txt", "r")
        sallestr = sauvegardecustom.read()
        print ("Contenu du fichier de sauvegardecustom :",sallestr)
        sauvegardecustom.close()
        salle = np.asarray(json.loads(sallestr))
    return(salle)