from feistel import FeistelCipher, FeistelNetwork


KEYS = [b'key', b'key2', b'lol', b'ok', b'key2']  # these are the keys to the round function respectively


def main():
	network = FeistelNetwork(b'Hello Eve. Meet me under the bridge at 10PM.', KEYS)
	network.encrypt()
	print('encrypted->', network.data)
	network.decrypt()
	print('decrypted->', network.data)


if __name__ == '__main__':
	main()