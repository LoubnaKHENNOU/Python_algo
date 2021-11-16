from collections import Counter
from collections import OrderedDict
from math import acos
import math
import numpy as np
from numpy.linalg import norm



#from string import ascii_lowercase

textanglais = "English has developed over the course of more than 1,400 years. The earliest forms of English, a group of West Germanic (Ingvaeonic) dialects brought to Great Britain by Anglo-Saxon settlers in the 5th century, are collectively called Old English. Middle English began in the late 11th century with the Norman conquest of England."
textfrançais = "En France, la linguistique appliquée est ancrée dans les études de vocabulaire." 
nouveautext = "Les projets font l'objet d'une soutenance publique. Le jury comprend les responsables V. Segonne et M. Candito, éventuellement d'autres membres de l'équipe pédagogique, et l'ensemble des encadrants des projets. Lors de la soutenance, chaque membre du groupe devra prendre la parole. Prévoir une présentation PDF / PowerPoint ou autre. Une démonstration du programme sur vidéo-projecteur sera incluse dans la soutenance."

"""les 1-grammes"""

print("--------------------")
print("MODÈLE 1-GRAMME")


#Découper le nouveau texte en phrase
"""def text_to_phrase(nouveautext):
    nouveautext = nouveautext.split(".")
    return nouveautext"""

#print(text_to_phrase(nouveautext))
#print("Nombre de phrase est: ",len(text_to_phrase(nouveautext)))
#print()
    


#Créer un dictionnaire : les occurences d'un ensemble de caractère
def Dico(texte):
    dico = dict(Counter(sorted(texte)))
    return dico


print("Occurences des grammes du texte Anglais :" , Dico(textanglais))
#print()
#print("Occurences des grammes du texte français :" , Dico(textfrançais))
#print()






######################################1er_essai###############################################
"""
#Comparer un Dico(texte) avec Dico(textanglais)
#Ajuster les deux dictionnaires (textanglais et nouveautext, textfrançais et nouveautext)

AncienDico = {'a': 40, 'b': 60 }
NouveauDico = {'b': 50, 'z': 10, 'A': 10}

#Comparer entre les dictionnaires




def compare_entre_dico(AncienDico, NouveauDico):
    dict1 = {}
    for cle in AncienDico.keys():
        if cle not in NouveauDico.keys():
            #NouveauDico.update({cle, 0})
            NouveauDico[cle] = 0
    for cle in NouveauDico.keys():
        if cle not in AncienDico.keys():
            #AncienDico.update({cle, 0})
            AncienDico[cle] = 0
            #dict1 = OrderedDict(sorted(dict.items()))

    return dict(sorted(AncienDico.items())), dict(sorted(NouveauDico.items()))

#print(compare_entre_dico(Dico(textfrançais), Dico(nouveautext)))
#print()
#print(compare_entre_dico(Dico(textanglais), Dico(nouveautext)))
#print()

a,b = compare_entre_dico(Dico(textfrançais), Dico(nouveautext))
c,d = compare_entre_dico(Dico(textanglais), Dico(nouveautext))



#Convertir un dictionnaire en vecteur
def dict_à_vecteur(dictionnaire):
    vecteur = list(dictionnaire.values())
    return vecteur

#print(dict_à_vecteur(a))
#print()
#print(dict_à_vecteur(b))
#print()

#print(dict_à_vecteur(Dico(textfrançais)))

def calcul_cos_theta(vecteur1, vecteur2):
    #return np.dot(vecteur1, vecteur2)/( norm(vecteur1)* norm(vecteur2) )
    numer = 0
    denom1 = 0
    denom2 = 0
    for i in range (len(vecteur1)):
        numer += vecteur1[i] * vecteur2[i]
    for j in range (len(vecteur2)):
        denom1 += math.pow(vecteur1[j], 2)
        denom2 += math.pow(vecteur2[j], 2)
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    cos_theta = numer/denom
    #Calculer arccos pour faire sortir théta
    #theta = math.acos(cos_theta)
    return cos_theta



#print(calcul_cos_theta(dict_à_vecteur(a), dict_à_vecteur(b)))
#print(calcul_cos_theta(dict_à_vecteur(c), dict_à_vecteur(d)))
#print()"""
######################################1er_essai###############################################

#Mesure de similarité entre le dictionnaire de référence et le nouveau dictionnaire
def calcul_cos_theta3(AncienDico, NouveauDico):

    numer = 0
    denom1 = 0
    denom2 = 0

    common_key = AncienDico.keys() & NouveauDico.keys()
    #print(common_key)
    
    for cle in  common_key:
        numer += AncienDico[cle] * NouveauDico[cle]
    #print("numer", numer)
    
    for cle in AncienDico.keys():
        denom1 += math.pow(AncienDico[cle], 2)
    #print("denom1",denom1)   
        
    for cle in NouveauDico.keys():
        denom2 += math.pow(NouveauDico[cle], 2)
    #print("denom2",denom2)
    
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    #print("denom",denom)
    #print("--------------------")
    
    cos_theta = numer/denom
    
    
    #Calculer arccos pour faire sortir théta
    #theta = math.acos(cos_theta)
    return cos_theta

#print("--------------------")
print("Modèle 1-gramme: calcul du cos entre textanglais et nouveautext ", calcul_cos_theta3(Dico(textanglais),Dico(nouveautext)))
#print()
print("Modèle 1-gramme: calcul du cos entre textfrançais et nouveautext ",calcul_cos_theta3(Dico(textfrançais),Dico(nouveautext)))



#Mesurer la performance du modèle : score accuracy
#On découpe le nouveau texte en phrase
def text_tokenize(texte):
    nouveautexte = texte.replace(". ", ".")
    l = nouveautexte.split('.')
    listephrase =[]
    for e in l:
        if len(e)!= 0:
            listephrase.append(e)
    return listephrase   

#print("--------------------")
#print("Tokenisation de texte: " ,text_tokenize(nouveautext))



#Créer un dictionnaire à partir des 1-grammes de chaque phrase
def Dico_phrase(listdephrase):
    list_dico = []
    for elt in listdephrase:
        list_dico.append(Dico(elt))
    return list_dico

#print("--------------------")
#print("Liste des dictionnaires pour chaque phrase du texte : ", Dico_phrase(text_tokenize(nouveautext)))      


#Mesurer la similarité des dico crées avec les dico de réfécrence
def calcul_cos(anciendico,listdedico):

    numer = 0
    denom1 = 0
    denom2 = 0

    list_cos = []
    
    for i in range (len(listdedico)):
        
        common_key = anciendico.keys() & listdedico[i].keys()
        
        for cle in  common_key:
            numer += anciendico[cle] * listdedico[i][cle]
        
        for cle in anciendico.keys():
            denom1 += math.pow(anciendico[cle], 2)

        for cle in listdedico[i]:
            denom2 += math.pow(listdedico[i][cle], 2)

        denom = math.sqrt(denom1) * math.sqrt(denom2)
        cos_theta = numer/denom
        list_cos.append(cos_theta)
    
        
    
    
    #Calculer arccos pour faire sortir théta
    #theta = math.acos(cos_theta)
    return list_cos      
        
listdedico = Dico_phrase(text_tokenize(nouveautext))

#print("--------------------")
#print("liste des cos entre anglais et nouveau texte : ",calcul_cos(Dico(textanglais), listdedico))
#print()
#print("liste des cos entre français et nouveau texte : ",calcul_cos(Dico(textfrançais), listdedico))



#Comparer les cos du français/nouveautext et anglais/nouveautext pour chaque phrase du nouveau texte
listcos_anglais_nouveautext = calcul_cos(Dico(textanglais), listdedico)
listcos_francais_nouveautext = calcul_cos(Dico(textfrançais), listdedico)


def compare_cos(listcos_anglais_nouveautext, listcos_francais_nouveautext):
    nb_phrase_anglais = 0
    nb_phrase_français = 0
    nb_total_phrase_corpus = len(listcos_francais_nouveautext)
    #(ou nb_total_phrase_corpus = len(listcos_francais_nouveautext))

    for i in range(len(listcos_anglais_nouveautext)):
        if listcos_anglais_nouveautext[i] > listcos_francais_nouveautext[i]:
            nb_phrase_anglais += 1
        elif listcos_francais_nouveautext[i] > listcos_anglais_nouveautext[i]:
            nb_phrase_français += 1
        else:
             continue

    print("nb_phrase_anglais:", nb_phrase_anglais)
    print("nb_phrase_français:", nb_phrase_français)
    print("nb_total_phrase_corpus", len(listcos_anglais_nouveautext))
            
    #Score d'accuracy
    score_accuracy = 0
    if nb_phrase_anglais > nb_phrase_français:
        score_accuracy =  nb_phrase_anglais/nb_total_phrase_corpus * 100
        print("Le score d'accuracy : ", score_accuracy,"%. La langue du texte est l'anglais")
        print()
        
    elif nb_phrase_anglais < nb_phrase_français:
        score_accuracy =  nb_phrase_français/nb_total_phrase_corpus * 100
        print( "Le score d'accuracy : ", score_accuracy,"%. La langue du texte est le français")
        print()
        
    else:
        score_accuracy =  nb_phrase_français/nb_total_phrase_corpus * 100
        print( "Le score d'accuracy : ", score_accuracy,"%. Langue non detectée")

    


#Langue non detecetée car meme nombre de phrases detectées en français qu'en anglais
    
print()
compare_cos(listcos_anglais_nouveautext,listcos_francais_nouveautext)


        
        
    





    
"""LES bigrammes"""
print("--------------------")
print("MODÈLE BIGRAMME")

#séparer les mots en bigrammes
def texte_a_bigramme(text):
    n = len(text)
    reste_text = text[n-n%2:n]
    new_bigramme = []
    for i in range (0,n-n%2):
        new_bigramme.append(text[i:i+2])
    new_bigramme.append(reste_text)
    return new_bigramme


#print()
#print(texte_a_bigramme(textanglais))
#print()
#print(texte_a_bigramme(textfrançais))
#print()

#Créer un dictionnaire : les occurences des bigrammes dans le texte
def Dico(liste):
    dico = dict(Counter(sorted(liste)))
    return dico

#print("Occurences des bigrammes du texte Anglais :" , Dico(texte_a_bigramme(textanglais)))
#print()
#print("Occurences des bigrammes du texte Français :", Dico(texte_a_bigramme(textfrançais)))
#print()






######################################1er_essai###############################################
"""#Comparer entre les dictionnaires

def compare_entre_dico(AncienDico, NouveauDico):
    dict1 = {}
    for cle in AncienDico.keys():
        if cle not in NouveauDico.keys():
            #NouveauDico.update({cle, 0})
            NouveauDico[cle] = 0
    for cle in NouveauDico.keys():
        if cle not in AncienDico.keys():
            #AncienDico.update({cle, 0})
            AncienDico[cle] = 0
            #dict1 = OrderedDict(sorted(dict.items()))

    return dict(sorted(AncienDico.items())), dict(sorted(NouveauDico.items()))

#print(compare_entre_dico(Dico(texte_à_bigramme(textanglais)), Dico(texte_à_bigramme(nouveautext))))
#print()
#print(compare_entre_dico(Dico(texte_à_bigramme(textfrançais)), Dico(texte_à_bigramme(nouveautext))))
#print()

a,b = compare_entre_dico(Dico(texte_a_bigramme(textfrançais)), Dico(texte_a_bigramme(nouveautext)))
c,d = compare_entre_dico(Dico(texte_a_bigramme(textanglais)), Dico(texte_a_bigramme(nouveautext)))

#Convertir un dictionnaire en vecteur
def dict_à_vecteur(dictionnaire):
    vecteur = list(dictionnaire.values())
    return vecteur

#print(dict_à_vecteur(a))
#print()
#print(dict_à_vecteur(b))
#print()

#Calculer la similarité entre les dictionnaires
def calcul_cos_theta(vecteur1, vecteur2):
    return np.dot(vecteur1, vecteur2)/( norm(vecteur1)* norm(vecteur2) )

    
    numer = 0
    denom1 = 0
    denom2 = 0
    for i in range (len(vecteur1)):
        numer += vecteur1[i] * vecteur2[i]
    for j in range (len(vecteur2)):
        denom1 += math.pow(vecteur1[j], 2)
        denom2 += math.pow(vecteur2[j], 2)
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    cos_theta = numer/denom
    #Calculer arccos pour faire sortir théta
    theta = math.acos(cos_theta)
    return theta



#print(calcul_cos_theta(dict_à_vecteur(a), dict_à_vecteur(b)))
#print(calcul_cos_theta(dict_à_vecteur(c), dict_à_vecteur(d)))
#print()"""
######################################1er_essai###############################################



def calcul_cos_theta3(AncienDico, NouveauDico):

    numer = 0
    denom1 = 0
    denom2 = 0

    common_key = AncienDico.keys() & NouveauDico.keys()
    #print(common_key)
    
    for cle in  common_key:
        numer += AncienDico[cle] * NouveauDico[cle]
    #print("numer", numer)
    
    for cle in AncienDico.keys():
        denom1 += math.pow(AncienDico[cle], 2)
    #print("denom1",denom1)   
        
    for cle in NouveauDico.keys():
        denom2 += math.pow(NouveauDico[cle], 2)
    #print("denom2",denom2)
    
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    #print("denom",denom)
    #print("--------------------")
    
    cos_theta = numer/denom
    
    #Calculer arccos pour faire sortir théta
    #theta = math.acos(cos_theta)
    return cos_theta


print("Modèle bigramme: calcul du cos entre textanglais et nouveautext ",calcul_cos_theta3(Dico(texte_a_bigramme(textanglais)),Dico(texte_a_bigramme(nouveautext))))
print()
print("Modèle bigramme: calcul du cos entre textfrançais et nouveautext ",calcul_cos_theta3(Dico(texte_a_bigramme(textfrançais)),Dico(texte_a_bigramme(nouveautext))))


#Mesurer la performance du modèle : score accuracy
#Mesurer la similarité des dico des phrases crés avec les dico de référence
listdedico2 = Dico_phrase(texte_a_bigramme(nouveautext))

#print("--------------------")
#print("liste des cos entre anglais et nouveau texte : ",calcul_cos(Dico(texte_a_bigramme(textanglais)), listdedico2))
#print()
#print("liste des cos entre français et nouveau texte : ",calcul_cos(Dico(texte_a_bigramme(textfrançais)), listdedico2))


#Comparer les cos du français/nouveautext et anglais/nouveautext pour chaque phrase du nouveau texte

listcos_anglais_nouveautext2 = calcul_cos(Dico(texte_a_bigramme(textanglais)), listdedico2)
listcos_francais_nouveautext2 = calcul_cos(Dico(texte_a_bigramme(textfrançais)), listdedico2)

print()
compare_cos(listcos_anglais_nouveautext2,listcos_francais_nouveautext2)





"""LES Trigrammes"""
print("--------------------")
print("MODÈLE TRIGRAMME")
#séparer les mots en trigrammes

def texte_a_trigramme(text):
    n = len(text)
    reste_text = text[n-n%3:n]
    new_trigramme = []
    for i in range (0,n-n%3):
        new_trigramme.append(text[i:i+3])
    new_trigramme.append(reste_text)
    return new_trigramme


#print(texte_a_trigramme(textanglais))
#print()
#print(texte_a_trigramme(textfrançais))

#Créer un dictionnaire : les occurences des trigrammes dans le texte
def Dico(liste):
    dico = dict(Counter(sorted(liste)))
    return dico

#print("Occurences des trigrammes du texte Anglais :" , Dico(texte_a_trigramme(textanglais)))
#print()
#print("Occurences des trigrammes du texte Français :", Dico(texte_a_trigramme(textfrançais)))
#print()




######################################1er_essai###############################################
"""#Comparer entre les dictionnaires
def compare_entre_dico(AncienDico, NouveauDico):
    dict1 = {}
    for cle in AncienDico.keys():
        if cle not in NouveauDico.keys():
            #NouveauDico.update({cle, 0})
            NouveauDico[cle] = 0
    for cle in NouveauDico.keys():
        if cle not in AncienDico.keys():
            #AncienDico.update({cle, 0})
            AncienDico[cle] = 0
            #dict1 = OrderedDict(sorted(dict.items()))

    return dict(sorted(AncienDico.items())), dict(sorted(NouveauDico.items()))

#print(compare_entre_dico(Dico(texte_à_trigramme(textanglais)), Dico(texte_à_trigramme(nouveautext))))
#print()
#print(compare_entre_dico(Dico(texte_à_trigramme(textfrançais)), Dico(texte_à_trigramme(nouveautext))))
#print()

a,b = compare_entre_dico(Dico(texte_à_trigramme(textfrançais)), Dico(texte_à_trigramme(nouveautext)))
c,d = compare_entre_dico(Dico(texte_à_trigramme(textanglais)), Dico(texte_à_trigramme(nouveautext)))

#Convertir un dictionnaire en vecteur
def dict_à_vecteur(dictionnaire):
    vecteur = list(dictionnaire.values())
    return vecteur

#print(dict_à_vecteur(a))
#print()
#print(dict_à_vecteur(b))
#print()

#Calculer la similarité entre les dictionnaires
def calcul_cos_theta(vecteur1, vecteur2):
    #return np.dot(vecteur1, vecteur2)/( norm(vecteur1)* norm(vecteur2) )

    numer = 0
    denom1 = 0
    denom2 = 0
    
    for i in range (len(vecteur1)):
        numer += vecteur1[i] * vecteur2[i]
    print("numer", numer)
    
    for j in range (len(vecteur2)):
        denom1 += math.pow(vecteur1[j], 2)
        #print(vecteur1[j])
        denom2 += math.pow(vecteur2[j], 2)

    print("denom1",denom1)
    print("denom2",denom2)
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    print("denom",denom)
    cos_theta = numer/denom
    print("--------------------")
    
    #Calculer arccos pour faire sortir théta
    #theta = math.acos(cos_theta)
    return cos_theta


#print(calcul_cos_theta(dict_à_vecteur(a), dict_à_vecteur(b)))
#print(calcul_cos_theta(dict_à_vecteur(c), dict_à_vecteur(d)))
print()"""
######################################1er_essai###############################################
#Remarques


# construire un corpus de test : au moins mille phrase chacun de la meme longueur
#on évalue la performance en terme
#la relation entre la performance de modèle et la longueur de texte à détecter : construire des corpus de longueur différent
#et chaque corpus avec 10mille exemple
#le nombre
#le pourcentage d'exemple correctement detecté
#on calcule un vecteur de chaque phrase  en bigramme

#liste de référence(
#liste de prédiction(nouveautexte)

#moyenne de l'accuracy
#le modèle le plus performant

#longueur de texte et performance 
#trançonner le corpus
#sortir des graphes ou des tableaux


       
def calcul_cos_theta3(AncienDico, NouveauDico):
    numer = 0
    denom1 = 0
    denom2 = 0
    
    common_key = AncienDico.keys() & NouveauDico.keys()
    #print(common_key)
    
    for cle in  common_key:
        numer += AncienDico[cle] * NouveauDico[cle]
    #print("numer", numer)
    
    for cle in AncienDico.keys():
        denom1 += math.pow(AncienDico[cle], 2)
    #print("denom1",denom1)   
        
    for cle in NouveauDico.keys():
        denom2 += math.pow(NouveauDico[cle], 2)
    #print("denom2" ,denom2)
    
    denom = math.sqrt(denom1) * math.sqrt(denom2)
    #print("""denom""",denom)
    #print("--------------------")

    cos_theta = numer/denom
    
    #Calculer arccos pour faire sortir théta
    return cos_theta


print("Modèle trigramme: calcul du cos entre textanglais et nouveautext ",calcul_cos_theta3(Dico(texte_a_trigramme(textanglais)),Dico(texte_a_trigramme(nouveautext))))
print()
print("Modèle trigramme: calcul du cos entre textfrançais et nouveautext ",calcul_cos_theta3(Dico(texte_a_trigramme(textfrançais)),Dico(texte_a_trigramme(nouveautext))))

#Mesurer la performance du modèle : score accuracy

#Mesurer la similarité des dico des phrases crés avec les dico de référence
listdedico3 = Dico_phrase(texte_a_trigramme(nouveautext))

#print("--------------------")
#print("liste des cos entre anglais et nouveau texte : ",calcul_cos(Dico(texte_a_trigramme(textanglais)), listdedico3))
#print()
#print("liste des cos entre français et nouveau texte : ",calcul_cos(Dico(texte_a_trigramme(textfrançais)), listdedico3))


#Comparer les cos du français/nouveautext et anglais/nouveautext pour chaque phrase du nouveau texte

listcos_anglais_nouveautext3 = calcul_cos(Dico(texte_a_trigramme(textanglais)), listdedico3)
listcos_francais_nouveautext3 = calcul_cos(Dico(texte_a_trigramme(textfrançais)), listdedico3)

print()
compare_cos(listcos_anglais_nouveautext3,listcos_francais_nouveautext3)
   
