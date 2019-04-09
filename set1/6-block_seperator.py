# Given an (repeating xor) encrypted string, we seperate into n strings given the amount
# of keys used to encrypt.

import sys
import base64

if len(sys.argv) != 3:
	print "Usage python %s [base64 string] [number of keys]" % sys.argv[0]
	exit(1)

def b64_to_bin(data):
        return ''.join([format(ord(c), '08b') for c in base64.b64decode(data)])


bin1 = b64_to_bin(sys.argv[1])
n_keys = int(sys.argv[2])
out = [""] * n_keys
pos = 0

print bin1

for i in range(0, len(bin1), 8):
	out[pos%n_keys] += bin1[i:i+8]
	pos+=1

print out

for i in range(len(out)):
	print str(i) + ": " + hex(int(out[i], 2))
