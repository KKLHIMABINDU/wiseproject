list = [ ]
for i in range(901,999):
	for j in range(901,999):
		x=i*j
		l=x
		rev = 0
		while (l!=0):
			rem = l % 10
			rev = rev * 10 + rem
			l = l // 10
		if (rev == x):
			list.append(rev)
print(max(list))


