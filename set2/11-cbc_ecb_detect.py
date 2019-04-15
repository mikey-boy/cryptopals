import base64
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(plaintext):
	padding = 1
	while (len(plaintext) + padding) % AES.block_size != 0:
		padding += 1
	plaintext += ('\\x%02x' % padding) * padding
	return plaintext

def encrypt(plaintext, mode):
	prepend = random.randint(5,10)
	append = random.randint(5,10)
	print "Mode: %s, Prepend: %d bytes, Append: %d bytes" %(mode, prepend, append)

	plaintext = get_random_bytes(prepend) + plaintext + get_random_bytes(append)
	key = get_random_bytes(16)
	cipher = AES.new(key, mode)
        ciphertext = cipher.encrypt(plaintext)
	return ciphertext

def detection_oracle(ciphertext):


def main():
	plaintext = 'Hmm aint that interesting there might be a pad'
	enc = None

	for i in range(10):
		if (random.randint(0,1) == 0):
			enc = encrypt(plaintext, AES.MODE_ECB)
		else: 
			enc = encrypt(plaintext, AES.MODE_CBC)
		detection_oracle(enc)		

if __name__ == '__main__':
	main()
