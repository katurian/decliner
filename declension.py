import cltk

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

decline("amica", genitive, plural)
