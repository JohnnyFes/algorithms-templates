def devide(value) -> str:
    return str(value / k)


fi = open("input.txt", "r")
fo = open("output.txt", "w")
n, q, k = fi.read().splitlines()
n = int(n)
k = int(k)
q = list(map(int, q.split(' ')))
s = [sum(q[:k]), ]
for i in range(0, n - k):
    s += [s[i] - q[i] + q[i + k]]
r = list(map(devide, s))
r = ' '.join(r)
fo.write(r)
fi.close()
fo.close()
