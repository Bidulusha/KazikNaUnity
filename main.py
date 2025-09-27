base = [1,6,4,2,7,5,3]
s = int(input())

for i in range(0, 70):
    s = i
    if (base[(s // 7) % 7] + s - (s // 7) * 7 - 1) % 7 == 0:
        print(7)
    else:
        print((base[(s // 7) % 7] + s - (s // 7) * 7 - 1) % 7)