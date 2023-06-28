fi = open("input.txt", "r")
fo = open("output.txt", "w")
n, l1, l2 = fi.read().splitlines()
m1 = l1.split(' ')
m2 = l2.split(' ')
r: str = ''
for i in range(0, int(n)):
    r += m1[i] + ' ' + m2[i] + (' ' if i != n else '')
fo.write(str(r))
fi.close()
fo.close()
