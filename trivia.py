import listw

alphabet={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}

for x in listw.ans:
    for y in x: 
        alphabet[y]+=1
sort_alphabet = sorted (alphabet.items(), key = lambda x:x[1], reverse=True)
for i in sort_alphabet:
    print (i[0],'=',i[1])
print (len(listw.ans))
alphalist = 'qwertyuiopasdfghjklzxcvbnm'
print (len(alphalist))
for alpha in alphalist:
    for words in listw.ans:
        count=0
        for letter in words:
            if (alpha==letter):
                count+=1
            if (count>=3):
                print (words)

