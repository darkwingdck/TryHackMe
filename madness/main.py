s = 'y2RPJ4QaPF!B'
print(ord(s[0]))
print(chr(121))
s1 = ['', '', '', '', '', '', ]
for i in range(0, 127):
	for j in range(0, 13):
		s1[j] = chr(ord(s[j])+i)
	print(s1)
