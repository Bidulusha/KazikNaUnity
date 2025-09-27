a = input()
b = input()

d = {}

for i in b:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


for i in range(len(a) - len(b) + 1):
    t = d.copy()
    for j in range(len(b)):
        if(a[i + j] in t and t[a[i + j]] - 1 > -1):
            t[a[i + j]] -= 1
        else:
            break
    else:
        print(i + 1)
        break
else:
    print(0)



