# Decrypts a single character xor encrypted text

import sys
import base64

if len(sys.argv) != 2:
	print "Usage: python %s [hexstring]"
	print "! No leading 0x or \\x in hexstring"
	exit(1)

# Check if bin_val contains unprintable ASCII
def unprintable(bin_val):
	for i in range(0, len(bin_val), 8):
		int_val = int(bin_val[i:i+8],2)
		if (int_val < 32 or int_val > 126) and int_val != 10 and int_val != 9:
			return True
	return False

def xor(a,b):
	if a == b:
		return "0"
	return "1"

def repeat_xor(bin, c):
	output=""
	for i in range(len(bin)):
		output+=xor(bin[i], c[i%8])
	return output

# Convert hex to binary, fill to make sure leading zeros aren't removed
bin_val=bin(int(sys.argv[1].lstrip("0x"),16))[2:].zfill(len(sys.argv[1]) * 4)
ascii_txts=[]
keys=[]
for i in range(256):
	c = '{0:08b}'.format(i)
	out = repeat_xor(bin_val,c)

	if unprintable(out):
		continue

	ascii=""
	for j in range(0, len(out), 8):
		ascii += chr(int(out[j:j+8], 2))
	ascii_txts += [ascii]
	keys += [i]

# Do a frequency analysis on the ascii txts
for i in range(0, len(ascii_txts)):
	m = {}
	for char in ascii_txts[i]:
		if char in m:
			m[char] += 1
		else:
			m[char] = 1

	sum = 0
	common = ['e', 't', 'a', 'o', 'i', ' ']
	for j in common:
		if j in m:
			sum += m[j]

	if sum >= int(len(ascii_txts[i])*0.35):
		#print "key:" + str(keys[i]) + " txt:" + ascii_txts[i]
		print ascii_txts[i]
