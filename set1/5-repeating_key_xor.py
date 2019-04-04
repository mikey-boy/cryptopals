# Encrypts ASCII text using repeating key XOR

import sys
import binascii

if len(sys.argv) != 3:
	print "Please provide ASCII text and key"
	exit(1)

def xor(a,b):
	if a == b:
		return "0"
	return "1"

# We will convert each ascii character to an 8-bit block
def ascii_to_bin(ascii):
	out=""
	while ascii:
		out+=bin(int(binascii.hexlify(ascii[0]),16))[2:].zfill(8)
		ascii=ascii[1:]
	return out

bin1=ascii_to_bin(sys.argv[1])
bin2=ascii_to_bin(sys.argv[2])
out=""
for i in range (len(bin1)):
	out += xor(bin1[i],bin2[i%len(bin2)])

print hex(int(out, 2)).rstrip("L")

