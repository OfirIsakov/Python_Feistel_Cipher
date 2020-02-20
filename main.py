from feistel import FeistelCipher


KEYS = {}  # these are the keys to the round function respectively, left side key right side balance point


def main():
	pass
	# a = FeistelCipher(b'abcd', b'1', 0.5)
	# print(a.get_data())
	# a.calculate()
	# print(a.get_data())

	# b = FeistelCipher(a.get_data(), b'2', 0.5)
	# print(b.get_data())
	# b.calculate()
	# b.left, b.right = b.right, b.left
	# print(b.get_data())
	# b.calculate()
	# print(b.get_data())

	# c = FeistelCipher(b.get_data(), b'1', 0.5)
	# print(c.get_data())
	# c.calculate()
	# c.left, c.right = c.right, c.left
	# print(c.get_data())


if __name__ == '__main__':
	main()