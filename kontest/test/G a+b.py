fi = open("input.txt", "r")
fo = open("output.txt", "w")
j = fi.readline()[:-1]
r = sum(int(i in j) for i in fi.readline())
fo.write(str(r))
fi.close()
fo.close()
