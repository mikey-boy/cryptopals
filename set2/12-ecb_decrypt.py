import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

def encrypt_oracle(plaintext,key):
	cipher = AES.new(key, AES.MODE_ECB)
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
	with open('12-file.txt') as fh:
		unknown_text = base64.b64decode(fh.read())

	# Discover the padding needed
	padding = ""
	while(True):
		try:
			encrypt_oracle(padding + unknown_text, key)
			break
		except ValueError:
			padding += "A"
	print "Padding of length %d needed" % len(padding)


	# Discover the block size
	block = "A"
	while(True):
		try:
			encrypt_oracle(padding + block + unknown_text, key)
			break
		except ValueError:
			block += "A"
	print "Block size is %d bytes" % len(block)

	# Discover encryption mode
	enc = encrypt_oracle(padding + block*3 + unknown_text, key)
	print detection_oracle(enc)


if __name__ == '__main__':
	main()
