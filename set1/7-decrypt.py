import base64

from Crypto.Cipher import AES


def decrypt_ecb_cipher(ciphertext,key):
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext = cipher.decrypt(ciphertext)
	return plaintext

def main():
	key = b'YELLOW SUBMARINE'
	with open('7-file.txt') as fh:
		ciphertext = base64.b64decode(fh.read())
	msg = decrypt_ecb_cipher(ciphertext, key)
	print(msg)

if __name__ == '__main__':
	main()
