import hashlib
from itertools import cycle


class FeistelNetwork:
	def __init__(self, data: bytes, keys: dict):
		self.data = data
		self.cipher = FeistelCipher(data, None)
		self.rounds = len(keys)
		self.keys = keys

	def encrypt(self):
		temp = self.cipher
		temp.key = self.keys[0]
		temp.calculate()

		for i in range(1, self.rounds):
			temp.key = self.keys[i]
			temp.calculate()

		temp.sawp_sides()
		self.data = temp.data

	def decrypt(self):
		temp = self.cipher
		temp.key = self.keys[self.rounds-1]
		temp.calculate()

		for i in range(self.rounds-2, -1, -1):
			temp.key = self.keys[i]
			temp.calculate()

		temp.sawp_sides()
		self.data = temp.data


class FeistelCipher:
	'''
	data: The data to encrypt/decrypt
	key: The key to use in the encryption/decryption
	balance_point: 
	'''
	def __init__(self, data: bytes, key: bytes, balance_point: float=0.5):
		self.key = key
		self.data = data
		self.left_size = round(balance_point * len(data))
		self.right_size = len(data) - self.left_size

	'''
	Function encrypts/decrypts the stored values by the Feistel Cipher laws
	'''
	def calculate(self):
		self.right_size, self.left_size = self.left_size, self.right_size
		right = self.data[self.left_size:]
		right_after_round = self.__round_function(right, self.key)

		left = self.data[:self.left_size]
		xored_left = self.__bytes_xor(left, right_after_round)

		# save outputs in inverted sides
		self.data = right + xored_left

	def __round_function(self, data: bytes, key: bytes):
		round_hash = hashlib.sha256()
		round_hash.update(data)
		round_hash.update(key)
		return round_hash.digest()

	def sawp_sides(self):
		left = self.data[:self.right_size]
		right = self.data[self.right_size:]
		self.data = right + left
		self.right_size, self.left_size = self.left_size, self.right_size

	'''
	Private function that XORs the given value with the given key
	'''
	def __bytes_xor(self, value: bytes,  key: bytes) -> bytes:
		return bytes(v^k for v, k in zip(value, cycle(key)))

