from feistel import FeistelCipher


KEYS = {b'key': 0.5, b'key2': 0.5}  # these are the keys to the round function respectively, left side key right side balance point


def main():
	# this is how the network will work, just with more than 1 round
	b = FeistelCipher(b'abcd', b'key')
	print('data->', b.data)
	b.calculate()
	b.sawp_sides()
	print('encrypted->', b.data)
	b.calculate()
	b.sawp_sides()
	print('decrypted->', b.data)

	print()

	b = FeistelCipher(b'abcde', b'key')
	print('data->', b.data)
	b.calculate()
	b.sawp_sides()
	print('encrypted->', b.data)
	b.calculate()
	b.sawp_sides()
	print('decrypted->', b.data)


if __name__ == '__main__':
	main()