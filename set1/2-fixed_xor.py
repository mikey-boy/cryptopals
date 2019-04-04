# Computes the xor of two provided hex strings

import sys
import binascii

if len(sys.argv) != 3:
	print "Please provide both hexstrings"
	exit(1)

bin1 = bin(int(sys.argv[1],16))[2:].zfill(len(sys.argv[1]) * 4)
bin2 = bin(int(sys.argv[2],16))[2:].zfill(len(sys.argv[2]) * 4)
out = ""

for i in range (0, len(bin1)):

	if (bin1[i] == bin2[i]):
		out += "0"
	else:
		out += "1"

print hex(int(out, 2)).rstrip("L")
