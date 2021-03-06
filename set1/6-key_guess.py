# Decrypts a base64'd repeating-xor-encrypted text

import sys
import base64

if len(sys.argv) != 2:
	print "Usage: python %s [base64_txt]" %sys.argv[0]
	exit(1)

def xor(a,b):
	if a == b:
		return "0"
	return "1"

def b64_to_bin(data):
	return ''.join([format(ord(c), '08b') for c in base64.b64decode(data)])


# Hamming distance is the number of differing bits of two binary strings
def hamming_distance(bin1, bin2):
	diff = 0
	for i in range(min(len(bin1),len(bin2))):
		if bin1[i] != bin2[i]:
			diff += 1
	return diff

bin=b64_to_bin(sys.argv[1])
out=""
lst = []

for keysize in range (2, 20):
	hd1 = hamming_distance(bin[0:keysize*8], bin[keysize*8:keysize*16]) / keysize
	hd2 = hamming_distance(bin[keysize*16:keysize*24], bin[keysize*24:keysize*32]) / keysize
	lst+=[[keysize, hd1+hd2]]

print lst


