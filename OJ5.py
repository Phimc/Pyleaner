M = int(input())
essay = input().strip(".-?!',").lower().split()
memo = []
searchtime = 0
le = 0
dot = [".","-","?","!","'","," ]
for word in essay:
    if word in dot:
        continue
    word = word.strip(".-?!',")
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