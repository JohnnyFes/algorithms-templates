fi = open("input.txt", "r")
fo = open("output.txt", "w")
fl = fi.readline()[:-1]
sl = fi.readline()
r = int(fl) + int(sl)
fo.write(str(r))
fi.close()
fo.close()
