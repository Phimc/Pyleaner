M = int(input())
essay = input().split()
memo = []
searchtime = 0
le = 0
dot = [".","-","?","!","'","," ]
for word in essay:
    word = word.strip(".-?!',").lower()
    if word != '':
        if word in memo:
            le += 1
            continue
        elif len(memo) <= M-1:
            memo.append(word)
            searchtime += 1
            le += 1
        else:
            memo.pop(0)
            memo.append(word)
            searchtime += 1
            le += 1
print(le)
print(searchtime)