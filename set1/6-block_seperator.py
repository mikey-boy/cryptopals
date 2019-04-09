# Given an (repeating xor) encrypted string, we seperate into n strings given the amount
# of keys used to encrypt.

import sys
import base64

if len(sys.argv) != 3:
	print "Usage: python %s [hex string] [number of keys]" % sys.argv[0]
	exit(1)

hexstr = sys.argv[1]
n_keys = int(sys.argv[2])
out = [""] * n_keys

if len(hexstr) % 2 != 0:
	print "Error: hex string is of odd length"
	exit(1)

for i in range(0, len(hexstr), 2):
	out[i/2%n_keys] += hexstr[i] + hexstr[i+1]

for j in range(len(out)):
	print str(j) + ": 0x" + out[j]
