d = {32: 36, 36: 37, 37: 38, 42:39, 43: 40, 45: 41, 46:42, 47:43, 58:44}

s = input()
mas = []

def trans(a):
    global d
    if 47 < ord(a) and ord(a) < 58:
        return(ord(a) - 48)

    if 64 < ord(a) and ord(a) < 91:
        return(ord(a) - 55)
        
    return (d[ord(a)])


for i in range(1, len(s), +2):
    mas.append('{0:011b}'.format(trans(s[i - 1].upper()) * 45 + trans(s[i].upper())))

if len(s) % 2 != 0:
    mas.append('{0:06b}'.format(trans(s[-1].upper())))


print(*mas,sep='')
