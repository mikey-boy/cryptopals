file = open('8-file.txt', 'r')
ciphertext=file.readline().rstrip('\n')

while(ciphertext):
	block_set = set()

	for i in range(0, len(ciphertext), 32):
		if (ciphertext[i:i+32] in block_set):
			print "Ciphertext match in %s" % ciphertext
		else:
			block_set.add(ciphertext[i:i+32])

	ciphertext=file.readline().rstrip('\n')
