import listw

# printing occurance of each letter in the list of answers
alphabet = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0,
    "e": 0,
    "f": 0,
    "g": 0,
    "h": 0,
    "i": 0,
    "j": 0,
    "k": 0,
    "l": 0,
    "m": 0,
    "n": 0,
    "o": 0,
    "p": 0,
    "q": 0,
    "r": 0,
    "s": 0,
    "t": 0,
    "u": 0,
    "v": 0,
    "w": 0,
    "x": 0,
    "y": 0,
    "z": 0,
}

for x in listw.answers:
    for y in x:
        alphabet[y] += 1
sort_alphabet = sorted(alphabet.items(), key=lambda x: x[1], reverse=True)
for i in sort_alphabet:
    print(i[0], "=", i[1])
print(len(listw.answers))

# words with more than 3 of the same letter
alphalist = "qwertyuiopasdfghjklzxcvbnm"
print(len(alphalist))
for alpha in alphalist:
    for words in listw.answers:
        count = 0
        for letter in words:
            if alpha == letter:
                count += 1
            if count >= 3:
                print(words)
print(len(listw.guesses))

# words with the least entropy
("qajaq", 1.8901929060587057)
("jujus", 2.0394702600664427)
("immix", 2.0553250345034906)
("xylyl", 2.1896376350793587)
("yukky", 2.2053433495356694)
("pzazz", 2.213681643477487)
("jaffa", 2.2319731403499548)
("fuffy", 2.242142022507353)
("kudzu", 2.2664892650213484)
("gyppy", 2.281434184484281)

# words with the most entropy
("soare", 5.885202744292758)
("roate", 5.884856313732008)
("raise", 5.878302956493171)
("reast", 5.867738020843565)
("raile", 5.865153829041265)
("slate", 5.855819244109515)
("salet", 5.83602278209248)
("crate", 5.835215982633282)
("irate", 5.832798880940905)
("trace", 5.830429108079757)

# Average number of guesses: 3.4647033347769596
