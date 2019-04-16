import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad

key = get_random_bytes(16)

def encrypt_oracle(plaintext,key):
	cipher = AES.new(key, AES.MODE_ECB)
	ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
	return ciphertext

def detection_oracle(ciphertext):
	block_set = set()
	for i in range(0, len(ciphertext), 16):
		if (ciphertext[i:i+16] in block_set):
			return "ECB mode detected"
		else:
			block_set.add(ciphertext[i:i+16])
	return "CBC mode detected"

def main():
	with open('12-file.txt') as fh:
		unknown_text = base64.b64decode(fh.read())

	# Discover the block size
	enc = bytearray()
	enc.extend(encrypt_oracle(unknown_text, key))

	block = "A"
	while(True):
		enc2 = bytearray()
		enc2.extend(encrypt_oracle(block + unknown_text, key))
		if enc[0:2] == enc2[len(block):len(block)+2]:
			break
		else:
			block += "A"

	block_size = len(block)
	print "Block size is %d bytes" % block_size

	# Discover encryption mode
	enc = encrypt_oracle(block * 3 + unknown_text, key)
	print detection_oracle(enc)

	# Discover unknown text
	print "len %d" % len(encrypt_oracle(unknown_text, key))
	plaintext = ''
	for i in range(0, len(encrypt_oracle(unknown_text, key)), block_size):
		# Discover block
		for j in reversed(range(block_size)):
			target = "A" * (j)
			target_enc = encrypt_oracle(target + unknown_text, key)
			# Discover byte
			for k in range(0,256):
				probe = "A" * (j) + plaintext  + chr(k)
				probe_enc = encrypt_oracle(probe + unknown_text, key)
				if target_enc[i:i+block_size] == probe_enc[i:i+block_size]:
					plaintext += probe[-1]
					break
	print plaintext


if __name__ == '__main__':
	main()
