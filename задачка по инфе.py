sh=input('Введите зашифрованное слово: ')
shifr=sorted(list(sh))
soot={}
for i in range(len(shifr)):
    if i==0:
        soot.update({shifr[i]:shifr.count(shifr[i])})
    elif shifr[i]!=shifr[i-1]:
        soot.update({shifr[i]:shifr.count(shifr[i])})
sootlett={}
for i in range(int(input('Введите количество букв в слове: '))):
    s=input('Буква-частота: ').split('-')
    sootlett.update({s[0]:int(s[1])})
for key in sootlett.keys():
    for k1 in soot.keys():
        if sootlett[key]==soot[k1]:
            sh=sh.replace(k1,key)
            soot[k1]=''
print(sh)


