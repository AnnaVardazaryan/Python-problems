import json
old = open("new.txt", "r")
new = open("new2.txt", "w")
with open("dict.json") as f:
    dic = json.load(f)

for line in old:
    word = line.split(" ")
    for i in word:
        for key, val in dic.items():
            if val == i:
                new.write(key + " ")
                break
        else:
            new.write(i)




