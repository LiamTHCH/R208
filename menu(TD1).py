import errno
import locale
from dialog import Dialog
import os
locale.setlocale(locale.LC_ALL, '')
d = Dialog(dialog="dialog")
d.set_background_title("System Etudiant")
import affich
outpath = ""
def mainmenu():

        code, tag = d.menu("Coisir op:",
                       choices=[("(1)", "Spécifier le nom du fichier à traiter"),
                                ("(2)", "Générer un fichier anonymiser"),
                                ("(3)", "Afficher le fichier anonymiser"),
                                ("(4)", "Afficher la note de l’étudiant en fonction de son numéro d’étudiant"),
                                ("(5)", "Afficher la note de l’étudiant en fonction de son nom"),
                                ("(6)", "Afficher la ou les notes de l’étudiants en fonction de son prénom"),
                                ("(7)", "Afficher les noms, prénoms, numéros dont la note est comprise dans un intervalledonné par l’utilisateur")],title="Input file: %s" % affich.fpath,width=150)
        if code == d.OK:
            print(tag)
            if tag == "(1)":
                getfile()
            elif tag == "(2)":
                path = getexitpath()
                affich.main(affich.fpath)
                affich.out(affich.dico,path)
                mainmenu()
            elif tag == "(3)":
                afficheanonyme()
                
                                
                                
def afficheanonyme():
    global outpath
    try:
        with open(outpath, "r") as infile:
            data = infile.read()
            code, path = d.scrollbox(data)   
        mainmenu()
    except (FileNotFoundError, PermissionError, IOError):
        print("Problem with file:", outpath)
                 
                                

def getfile():
    code, path = d.fselect(os.getcwd())  
    if code == d.OK:
        if os.path.isfile(path):
            affich.fpath = path
            print("ok")
            mainmenu()
        else:
            d.msgbox("Erreur Fichier")
            print("erreur")
    else:
        mainmenu()

def getexitpath():
    global outpath
    code, path = d.dselect(os.getcwd())  
    outpath = path
    if code == d.OK:
        if os.path.isfile(path):
            d.msgbox("Fichier existe déjà")
            print("erreur")
            mainmenu()
        else:
            return path
    else:
        mainmenu()


if __name__ == '__main__':
    mainmenu()