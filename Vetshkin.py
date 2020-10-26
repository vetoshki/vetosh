import random

file=open('name.txt','w')
n="Komar"
file.write(n)
file.close()

file=open('name.txt','a')
spisok=[int(random.random()*1000) for i in range(1000)]
for i in spisok:
    file.write(str(i))
    file.write(str(""))
file.close()
 
znach=open('znach.txt','w')

pv=[]
for i in spisok:
    if i==58:
        pv.append(i)
        pv.append("")
for j in pv:
    znach.write(str(j))
znach.close()

znach=open('znach.txt','r')
reat=znach.read()
print(reat)
znach.close()

import random

slovar={}
file=open('zadan.txt','w')
spisok=[int(random.random()*1000) for i in range (1000)]
spisok.sort()
for i in spisok:
    if i+4<=len(spisok):
        if (spisok[i+3]>=58)&(spisok[i+4]<=500):
            slovar[spisok[i+3]]=spisok[i+4]
print (slovar)
file.close 