dico = {}
import sys
import os
import collections
import json
import yaml
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString
import locale
from dialog import Dialog
import os

### definition des  variable de fonctionnement

locale.setlocale(locale.LC_ALL, '')
d = Dialog(dialog="dialog")
d.set_background_title("System Etudiant")
fpath = ""
outpath = ""
anonyme = False
Format = ""
filepath = ""

### function 

def main(file): ### fonction pour ouvrir le fichier d'entree et cree le dico
    global dico
    try:
        with open(file, "r") as infile:
            data = infile.read().splitlines(True)
            for ligne in data[1:]:
                ligne = ligne.rstrip("\n")
                temp = ligne.split(";")
                tempdico = {}
                #for item in temp:
                    #print("%s "% item,end="")
                tempdico["NOM"] = temp[2]
                tempdico["PRENOM"] = temp[3]
                tempdico["GROUPE"] = temp[4]
                tempdico["NOTE"] = temp[-1]
                tempdico["NUMERO"] = temp[0]
                dico[temp[1]] = tempdico
        dico.pop(getList(dico)[0])
    except (FileNotFoundError, PermissionError, IOError):
        print("Problem with file:", file)

def getList(dict): ### fonction pour avoir une list de toutes les cle d'un dico
    return list(dict.keys())

def out(dic,outfiles): ### creation fichier anonyme
    try: 
        with open(outfiles, "w") as outfile:
            for eleve in getList(dic):
                outfile.write("%s;%s\n"%(eleve,dic[eleve]["NOTE"]))
    except (FileNotFoundError, PermissionError, IOError):
        print("Problem with file")

def find_duplicate(a): ### Trouver les duplicata
    return ([item for item, count in collections.Counter(a).items() if count > 1])

def remove_duplicate(dicot,duplist):  ### Enlever duplicata
    for item in duplist:
        del dico[item]

def anonym(dico): ### ceation d'un dico anonyme
    temp = {}
    for eleve in getList(dico):
        temp[eleve] = dico[eleve]["NOTE"]
    return temp

def outtojson(dico,path): ### creation ficher en format json
    with open(path,"w" ,encoding='utf8') as f:
        json.dump(dico,f,ensure_ascii=False)

def outtoyml(dico,path): ### creation ficher en format yml
    with open(path,"w") as f:
        yaml.dump(dico, f, allow_unicode=True)

def outtoxml(dico,path): ### creation ficher en format xml
    with open(path,"w") as f:
        temp = dicttoxml(dico,custom_root='etudiant', attr_type=False)
        dom = parseString(temp)
        xml = dom.toprettyxml()
        f.write(xml)

###### affichage

def mainmenu(): ###menu principale
    global fpath
    code, tag = d.menu("Coisir operation:",
                       choices=[("(1)", "Spécifier le nom du fichier à traiter"),
                                ("(2)", "Générer un fichier anonymiser"),
                                ("(3)", "Afficher le fichier anonymiser"),
                                ("(4)", "Afficher la note de l’étudiant en fonction de son numéro d’étudiant"),
                                ("(5)", "Afficher la note de l’étudiant en fonction de son nom"),
                                ("(6)", "Afficher la ou les notes de l’étudiants en fonction de son prénom"),
                                ("(7)", "Afficher les noms, prénoms, numéros dont la note est comprise dans un intervalledonné par l’utilisateur")],title="Input file: %s" % fpath,width=150)
    if code == d.OK: ### apres que le mennu selectionne return code et le tag selectionner 
      #  print(tag)
        main(fpath)
        if tag == "(1)": ### appel les differents menu
            fpath = getfile()
        elif tag == "(2)":
            path = getexitpath()
            out(dico,path)
        elif tag == "(3)":
            afficheanonyme()
        elif tag == "(4)":
            affichegui(option1())
        elif tag == "(5)":
            affichegui(option2())
        elif tag == "(6)":
            affichegui(option3())
        elif tag == "(7)":
            code, range = d.inputbox("Mettre un intervalle avec comme sytaxe n-n")
            if code == d.OK:
                tempstr = option4(range)
                if tempstr == None:
                    d.msgbox("Aucun eleve trouver")
                elif not tempstr == "":
                    affichegui(tempstr)
                
            else:
                mainmenu()
        mainmenu()

### fonction pour cree les different STR pour l'affichage 

def option1():
    tempstr = ""
    tempdico = {}
    for item in getList(dico):
        tempdico[item] = dico[item]["NOTE"]
    tempdico = dict(sorted(tempdico.items()))
    for item in getList(tempdico):
        tempstr = tempstr + ("%s : %s  \n"%(item,tempdico[item]))
    return(tempstr)

def option2():
    tempstr = ""
    tempdico = {}
    for item in getList(dico):
        tempdico[dico[item]["NOM"]] = dico[item]["NOTE"]
    tempdico = dict( sorted(tempdico.items(), key=lambda x: x[0].lower()) )
    for item in getList(tempdico):
        tempstr = tempstr + ("%s : %s  \n"%(item,tempdico[item]))
    return(tempstr)

def option3():
    tempstr = ""
    tempdico = {}
    for item in getList(dico):
        tempdico[dico[item]["PRENOM"]] = dico[item]["NOTE"]
    tempdico = dict( sorted(tempdico.items(), key=lambda x: x[0].lower()) )
    for item in getList(tempdico):
        tempstr = tempstr + ("%s : %s  \n"%(item,tempdico[item]))
    return(tempstr)

def option4(range):
    temprange = str(range).split("-")
    try:
        temprange[0] = int(temprange[0])
        temprange[1] = int(temprange[1])
    except ValueError:
        pass
    if len(temprange) != 2 :
        d.msgbox("Erreur d'intervalle")
        return ""
    elif temprange[1] < temprange[0]:
        d.msgbox("Interval dans le mauvais sens")
        return ""

    tempstr = ""
    tempdico = {}
    tempdico2 = {}
    for item in getList(dico):
        if temprange[0] <= int(dico[item]["NOTE"]) <= temprange[1]:
            tempdico[item] = [item,dico[item]["PRENOM"],dico[item]["NOM"],dico[item]["NOTE"]]
            tempdico2[item] = dico[item]["NOTE"]
    tempdico2 =  dict(sorted(tempdico2.items(), key=lambda item2: item2[1]))
    if not any(tempdico2):
        return None
    for item in getList(tempdico2):
        tempstr = tempstr + ("%s %s %s : %s  \n"%(tempdico[item][0],tempdico[item][1],tempdico[item][2],tempdico[item][3]))
    return(tempstr)

### Fonction pour afficher les STR cree precedament dans une boite    

def affichegui(string):
    d.scrollbox(string)

### Fonction pour afficher le ficher de sortie

def afficheanonyme():
    global outpath
    try:
        with open(outpath, "r") as infile:
            data = infile.read()
            d.scrollbox(data)   
    except (FileNotFoundError, PermissionError, IOError):
        print("Problem with file:", outpath)
                 
 ### fonction pour demander le ficher d'entree                               

def getfile():
    code, path = d.fselect(os.getcwd())  
    if code == d.OK:
        if os.path.isfile(path):
            return path
        else:
            d.msgbox("Erreur Fichier")
            print("erreur")
    else:
        mainmenu()

 ### fonction pour demander le ficher de sortie                              

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


### fonctionnement en ligne de commande avec option

if __name__ == '__main__':
    try:
        if len(sys.argv) <= 1: ###test le nombre d'arguments
            print("Mauvais nombre d’arguments")
            print("-help pour aide")
            exit(1)
        else:
            for i in range(1,len(sys.argv)):
                if sys.argv[i] == "-input":  ### met dans la variable global le fichier d'entree
                    fpath = sys.argv[i+1]
                elif sys.argv[i] == "-output":   #### met dans la variable global le fichier de sortie et teste si le fichier exste deja
                    if os.path.isfile(sys.argv[i+1]):
                        while True:
                            ans = input("Fichier existe deja ecraser ? (O/N) ")
                            if (str(ans).lower() == "o"):
                                outpath = sys.argv[i+1]
                                break
                            elif (str(ans).lower() == "n"):
                                exit(0)
                    else:
                        outpath = sys.argv[i+1]
                elif sys.argv[i] == "-help":  ### affiche aide et stop le programme
                    print("-input pour specifier le fichier a traiter")
                    print("-output pour specifier le fichier de sortie")
                    print("-format pour specifier le format fichier de sortie")
                    print("Format supporter : yml , json , xml")
                    print("-format pour specifier le format fichier de sortie")
                    print("-a pour anonimyser")
                    print("-menu pour demmarer le gui")
                    exit()
                elif sys.argv[i] == "-a": ## activer anonyme avec la variable global
                    anonyme = True
                elif (sys.argv[i] == "-menu") or (sys.argv[i] == "-m"): ## active menu
                    mainmenu()
                elif (sys.argv[i] == "-format") or (sys.argv[i] == "-f"):
                    if (sys.argv[i+1] == "yml") or (sys.argv[i+1] == "xml") or (sys.argv[i+1] == "json"):
                        Format = sys.argv[i+1]
                if os.path.isfile(fpath):
                    main(fpath)
                else:
                    print("Pas de fichier à traiter ou fichier non existant")
                    exit(1)
            if outpath != "": ### traitement des foramt 
                if not anonyme:
                    tempdico = dico
                else:
                    tempdico = anonym(dico)
                if Format == "" and anonyme == True:
                    out(dico,outpath)
                elif Format == "":
                    print("Fichier non modifier")
                elif Format == "yml":
                    outtoyml(tempdico,outpath)
                elif Format == "xml":
                    outtoxml(tempdico,outpath)
                elif Format == "json":
                    outtojson(tempdico,outpath)
    except KeyboardInterrupt :      #### Pour forcer l'arret avec un CTR + C
        print()
        print("Arreter par l'utilisateur")