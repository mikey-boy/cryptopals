import base64

from Crypto.Cipher import AES

def decrypt_block(ciphertext,key):
	cipher = AES.new(key, AES.MODE_ECB)
	plaintext = cipher.decrypt(ciphertext)
	return plaintext

def encrypt_block(plaintext, key):
	cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(plaintext)
        return ciphertext

def xor_blocks(b1, b2):
	b3 = bytearray([0]*len(b1))
	for i in range(0, len(b1)):
		b3[i] = b1[i] ^ b2[i]
	return b3

# Decrypt AES ciphertext in CBC mode 
def cbc_decrypt(ciphertext, iv):
	plaintext = ""
	
	
# Encrypt AES ciphertext in CBC mode 
def cbc_encrypt(plaintext, iv, key):
	ciphertext = b''
	bin_pt = bytearray()
	bin_pt.extend(plaintext)

	for i in range(0, len(bin_pt), 16):
		block = bin_pt[i:i+16]
		block = xor_blocks(block, iv)
		ciphertext += encrypt_block(block, key) 
	

def main():
	key = b'YELLOW SUBMARINE'
	#with open('7-file.txt') as fh:
	#	ciphertext = base64.b64decode(fh.read())
	
	cbc_encypt('hello how ar you', bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), key)

if __name__ == '__main__':
	main()
