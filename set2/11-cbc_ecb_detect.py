import base64
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(plaintext):
	padding = 1
	while (len(plaintext) + padding) % 16 != 0:
		padding += 1
	plaintext += chr(padding) * padding
	return plaintext

def encrypt(plaintext, mode):
	prepend = random.randint(5,10)
	append = random.randint(5,10)
	print "Mode: %s, Prepend: %d bytes, Append: %d bytes" %(mode, prepend, append)

	plaintext = get_random_bytes(prepend) + plaintext + get_random_bytes(append)
	plaintext = pad(plaintext)
	key = get_random_bytes(16)
	cipher = AES.new(key, mode)
        ciphertext = cipher.encrypt(plaintext)
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
	# Interesting plaintext, will detect ECB if len(prepend) >= 9
	plaintext = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
	enc = None

	for i in range(10):
		if (random.randint(0,1) == 0):
			enc = encrypt(plaintext, AES.MODE_ECB)
		else:
			enc = encrypt(plaintext, AES.MODE_CBC)
		print detection_oracle(enc)

if __name__ == '__main__':
	main()
