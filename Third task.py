#1804
'''
f = open('1804.txt')
mas = f.read()
splt = []
word = ''

for i in mas:
    if i == ' ':
        splt.append(word)
        word = ''
    else:
        word += i
if word:
    splt.append(word)

n = int(input())
otv = []

for i in splt:
    if len(i) >= n:
        otv.append(i)

print(*otv)
'''

#0976
'''
f = open('0976.txt')
s = f.read()
k = 0
kmax = 0
for i in range(len(s)):
    if (k % 5 == 0 and s[i] == 'B') or (k % 5 == 1 and s[i] == 'E')\
       or (k % 5 == 2 and s[i] == 'B') or (k % 5 == 3 and s[i] == 'R')\
       or (k % 5 == 4 and s[i] == 'A'):
        k += 1
        kmax = max(kmax, k)
    else:
        k = 0
f.close()
print(kmax)
'''

#1201
'''
a = 4
m = [5, 4, 7, 2]
if sum(m) % 2 == 0 and max(m) <= sum(m) - max(m):
    print('YES')
else:
    print('NO')
'''

#0203
'''
def f(x):
    if x == 0:
        return 1
    if x < 0:
        return 0
    return f(x - 1) + f(x - 2) + f(x - 3)
print(f(5))
'''

#0814
'''
a = []
k = 0

for i in range(10 ** 6, (10 ** 6) * 20):
    s = ''
    while i > 0:
        if i % 11 <= 9:
            s = str(i % 11) + s
        if i % 11 == 10:
            s = 'A' + s
        i //= 11
    if s.count('A') == 0 and s.count('6') == 0:
        continue
    else:
        if ('A3A' in s) or ('636' in s) or ('A36' in s) or ('63A' in s)\
           or ('A4A' in s) or ('646' in s) or ('A46' in s) or ('64A' in s)\
           or ('A5A' in s) or ('656' in s) or ('A56' in s) or ('65A' in s)\
           or ('A7A' in s) or ('676' in s) or ('A76' in s) or ('67A' in s):
            k += 1
print(k)
'''
