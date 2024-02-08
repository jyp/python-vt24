# Assumption: the word occurs in only one list
# Assumption: the word does not occur anywhere, then the function findSynonyms will return None.

synonyms = [["parcel", "package"],
            ["​remedy​", "cure"],
            ["harmony", "concord", "concordance"]]

def findSynonyms(word):
    for synonym_set in synonyms:
        if word in synonym_set:
            result = []
            for s in synonym_set:
                if s != word:
                    result.append(s)
            return result

##########
## Test code

print(findSynonyms("parcel"))
print(findSynonyms("package"))
print(findSynonyms("concord"))
print(findSynonyms("hello?"))
