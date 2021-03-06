import cltk

from cltk.corpus.utils.importer import CorpusImporter

from cltk.stem.latin.declension import CollatinusDecliner

corpus_importer = CorpusImporter('latin')

corpus_importer.import_corpus('latin_models_cltk')

ablative = "ablative"
nominative = "nominative"
genitive = "genitive"
accusative = "accusative"
dative = "dative"
vocative = "vocative"
singular = "singular"
plural = "plural"


def decline(noun, case, number):
    
    decliner = CollatinusDecliner()
    list = decliner.decline(noun, flatten=True)
    if case == nominative and number == singular:
       return list[0]
    if case == nominative and number == plural:
       return list[6]
    if case == vocative and number == singular:
       return list[1]
    if case == vocative and number == plural:
       return list[7]
    if case == accusative and number == singular:
       return list[2]
    if case == accusative and number == plural:
      return list[8]
    if case == genitive and number == singular:
      return list[3]
    if case == genitive and number == plural:
      return list[9]
    if case == dative and number == singular:
      return list[4]
    if case == dative and number == plural:
      return list[10]
    if case == ablative and number == singular:
      return list[5]
    if case == ablative and number == plural:
      return list[11]

"""# Latin Noun Decliner
1.  Type the nominative form of any noun into the quotes.
2.  Type the desired case (nominative, vocative, genitive, accusative, dative, ablative) in *lowercase*.
3.  Type the desired number (singular, plural) in *lowercase*.
4. Click the button in the top left corner.
"""

decline("vir", accusative, singular)

import random

import time


nouns = ["fama", "familia", "fortuna", "puella", "terra", "vita", "agricola", "carrus", "equus", "servus", "cibus", "copia", "cura", "forma", "numerus", "regina", "nauta", "percunia", "unda", "amicus", "dominus", "femina", "littera", "praeda", "pupa", "animus", "gladius", "iniuria", "memoria", "poena", "provincia", "pugna", "victoria", "ager", "casa", "filia", "hora", "puer", "vir", "disciplina", "discipulus", "lingua", "magister", "patria", "amicitia", "annus", "castra", "consilium", "frumentum", "gloria", "gratia", "materia", "praemium", "socius", "captivus", "cena", "medicus", "mensa", "colonus", "filius", "auxilium", "bellum", "concordia", "dea", "deus", "nuntius", "officium", "causa", "oppidum", "populus", "atrium", "sportula", "tablinum", "templum", "adulescentulus", "caper", "corium", "feriae", "flagellum", "liberi", "locus", "otium", "pretium", "studium", "terminus", "grammaticus", "liber", "schola", "verbum", "ludus", "poeta", "sententia", "finitimus", "ira", "proelium", "somnus", "dux", "homo", "lex", "miles", "pax", "salus"]

declensions = [accusative, genitive, dative, ablative, vocative]

number = [singular, plural]
#terra, vita, agricola, carrus, equus, servus, cibus, copia, cura, forma, numerus, regina, nauta, percunia, unda, amicus, dominus, femina, littera, praeda, pupa, animus, gladius, iniuria, memoria, poena, provincia, pugna, victoria, ager, casa, filia, hora, puer, vir, disciplina, discipulus, lingua, magister, patria, amicitia, annus, castra, consilium, frumentum, gloria, gratia, materia, praemium, socius, captivus, cena, medicus, mensa, colonus, filius, arma, auxilium, bellum, concordia, dea, deus, nuntius, officium, causa, oppidum, populus, atrium, sportula, tablinum, templum, adulescentulus, caper, corium, feriae, flagellum, liberi, locus, otium, pretium, studium, terminus, grammaticus, liber, schola, verbum, ludus, poeta, sententia, finitimus, ira, proelium, somnus, dux, homo, lex, miles, pax, salus]

def practice():
  x = random.randint(0, 101)
  y = random.randint(0, 4)
  z = random.randint(0, 1)
  print("What is " + nouns[x] + " in the " + declensions[y] + " " + number[z] + " form?")
  print(" ")
  print(" ")
  answer = input("First answer: ")
  if answer == "terminus":
    return
  if answer == decline(nouns[x], declensions[y], number[z]):
    print(' ')
    print(' ')
    print("""\
            Ita vero!         
              ___       
              \\||      
             ,'_,-\     
             ;'____\    
             || =\=|    
             ||  - |                               
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\      / , ;                            
     /  ,' | _ - ',/, ;
    (  (   |     /, ,,;
     \  \  |     ',,/,;
      \  \ |    /, / ,;
     (| ,^.|   / ,, ,/;
      `-'./ `-._,, ,/,;
           ´-._ `-._,,;
           |/,,`-._ `-.
           |, ,;, ,`-._\



                    """)
  else:
    print(' ')
    print(" ")
    print("Id est falsus...")
    print(" ")
    time.sleep(1) 
    print(" ")
    answer = input("Try again: ")
    if answer == decline(nouns[x], declensions[y], number[z]):
      print(" ")
      print(" ")
      print("""\
            Ita vero!         
              ___       
              \\||      
             ,'_,-\     
             ;'____\    
             || =\=|    
             ||  - |                               
         ,---'._--''-,,---------.--.----_,         
        / `-._- _--/,,|  ___,,--'--'._<            
       /-._,  `-.__;,,|'                           
      /   ;\      / , ;                            
     /  ,' | _ - ',/, ;
    (  (   |     /, ,,;
     \  \  |     ',,/,;
      \  \ |    /, / ,;
     (| ,^.|   / ,, ,/;
      `-'./ `-._,, ,/,;
           ´-._ `-._,,;
           |/,,`-._ `-.
           |, ,;, ,`-._\



                    """)

    else:
      x = decline(nouns[x], declensions[y], number[z])
      print(" ")
      print(" ")
      print("The answer was " + x)
      time.sleep(1)

  time.sleep(2) 
  print(" ")
  print("-----------------------------------------------------------------")
  print(" ")
  practice()

"""# Declension Game

---
"""

practice()
