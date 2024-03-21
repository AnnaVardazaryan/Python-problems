import json


def convertToTitle(columnNumber):
    if columnNumber <= 26:
        return chr(columnNumber + 64)
    if columnNumber % 26 != 0 and columnNumber < 703:
        return chr(columnNumber // 26 + 64) + chr(columnNumber % 26 + 64)
    if columnNumber % 26 == 0 and columnNumber < 703:
        return chr(columnNumber // 26 + 63) + 'Z'
    else:
        return convertToTitle(columnNumber // 26) + chr(columnNumber % 26 + 64)


old = open("text.txt", "r")
new = open("new.txt", "w")
d = {}
num = 0
for line in old:
    word = line.split(" ")
    for i in word:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

for x in list(d):
    if d[x] == 1:
        del(d[x])

num = 1
for key in d:
    d[key] = convertToTitle(num)
    num += 1

old.seek(0)

for line in old:
    word = line.split(" ")
    for i in word:
        if i in d:
            new.write(d[i] + ' ')
        else:
            new.write(i + ' ')
json = json.dumps(d)
f = open("dict.json", "w")
f.write(json)
f.close()
