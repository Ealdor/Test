file = open('Spanish.dic', 'r+')
file2 = open('spanish.dic', 'w')

for line in file:
	word = line.strip().split('/')[0]
	file2.write(word+'\n')