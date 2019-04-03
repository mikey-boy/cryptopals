# Converts a hex string (provided as only arg) and converts it to base64

# Remember! Always operate on raw bytes, never on encoded strings.
# Only use hex and base64 for pretty-printing.

import sys
import binascii

if len(sys.argv) != 2:
	print "Please provide hexstring as only argument"
	exit(1)

b64_out = ""
b64_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
hex     = sys.argv[1]


while len(hex) % 3 != 0:
	hex.append("0")

for i in range (0, len(hex), 6):
	chunk = hex[i:i+6]

	# Convert hex to bin (with leading zeros)
	scale = 16 ## equals to hexadecimal
	num_of_bits = 24
	bin_out = bin(int(chunk, 16))[2:].zfill(num_of_bits)

	# Convert bin to base64
	b64_out += b64_set[int(bin_out[:6], 2)]
	b64_out += b64_set[int(bin_out[6:12], 2)]
	b64_out += b64_set[int(bin_out[12:18], 2)]
	b64_out += b64_set[int(bin_out[18:24], 2)]

print str(b64_out)
