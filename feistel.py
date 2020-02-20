import hashlib
from itertools import cycle


class FeistelCipher:
	'''
	data: The data to encrypt//decrypt
	key: The key to use in the encryption/decryption
	balance_point: 
	'''
	def __init__ (self, data: bytes, key: bytes, balance_point: float=0.5):
		self.key = key
		self.left = data[:int(balance_point * len(data))]
		self.right = data[int(balance_point * len(data)):]

	'''
	Function encrypts/decrypts the stored values by the Feistel Cipher laws
	'''
	def calculate(self):
		# hash right
		right_hash = hashlib.sha256()
		right_hash.update(self.right)
		right_hash.update(self.key)
		hashed_right = right_hash.digest()

		# xor the values
		xored_value = self.__xor(self.left, hashed_right)

		# save outputs in inverted sides
		self.left = self.right
		self.right = xored_value

	def get_data(self):
		return self.left + self.right

	'''
	Private function that XORs the given value with the given key
	'''
	def __xor(self, value_to_xor: bytes,  key_to_xor_with: bytes) -> bytes:
		return bytes(value^key for value, key in zip(value_to_xor, cycle(key_to_xor_with)))

