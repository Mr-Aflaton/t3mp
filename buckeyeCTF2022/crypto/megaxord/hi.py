f = open("megaxord.txt", 'rb')
s = f.read()
f.close()
ff = open("hi.txt", "a")
print(type(s))


for i in range(0, 258):
	ff.write("".join([chr(int(j)^i) for j in s]))

