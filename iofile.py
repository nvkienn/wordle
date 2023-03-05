import itertools
a = ['G','Y','B']
b = [p for p in itertools.product(a,repeat = 5)]
d = {}
for i in b:
    d[list(i)]=0

with open ('outcomes_all.py','w') as f1:
    f1.write(str(d))

