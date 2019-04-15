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
def cbc_decrypt(ciphertext, iv, key):
	plaintext = bytearray()
		
	for i in range(0, len(ciphertext), 16):
		block = ciphertext[i:i+16]
		dec_block = bytearray()
		dec_block.extend(decrypt_block(block, key))
		plaintext.extend(xor_blocks(dec_block, iv))
		iv = ciphertext[i:i+16]
	return plaintext
	
	
# Encrypt AES ciphertext in CBC mode 
def cbc_encrypt(plaintext, iv, key):
	ciphertext = bytearray()
	bin_pt = bytearray()
	bin_pt.extend(plaintext)

	for i in range(0, len(bin_pt), 16):
		block = bin_pt[i:i+16]
		block = xor_blocks(block, iv)
		ciphertext.extend(encrypt_block(block, key))
		iv = ciphertext[i:i+16]
	return ciphertext 
		

def main():
	key = b'YELLOW SUBMARINE'
	txt = 'Hmm aint that interesting no pad'	
	
	print "Plaintext: %s" % txt
	enc = cbc_encrypt(txt, bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), key)
	print "Encrypted: %s" % enc
	dec = cbc_decrypt(enc, bytearray([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), key)
	print "Decrypted: %s" % dec 

if __name__ == '__main__':
	main()
