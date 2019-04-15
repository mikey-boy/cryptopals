import sys


def main():
	if len(sys.argv) != 3:
		print "Usage: %s [plaintext] [block_len]" % sys.argv[0]
		exit(1)

	plaintext = sys.argv[1]
	block_len = int(sys.argv[2])
	padding = 1

	while (len(plaintext) + padding) % block_len != 0:
		padding += 1

	plaintext += ('\\x%02x' % padding) * padding
	print plaintext

if __name__ == '__main__':
	main()
