import uuid, socket

class MAC:

	# NOTE: `OWN_MAC` irreliable at times
	@staticmethod
	def OWN_MAC() -> str:
		HEX = hex(uuid.getnode())[2:]
		ADR = ":".join([HEX[i:i+2] for i in range(0, len(HEX), 2)])
		return ADR

	@staticmethod
	def unpack(packed_mac: bytes) -> str:
		return ":".join(format(byte, "02x") for byte in packed_mac)

	def __init__(self, address: str):

		# Validate Address
		assert len(address.replace(":", "")) == 12, f"Assertion Error: Invalid MAC Address ({address})"
		for octet in address.split(":"):
			try: assert min([int(byte, 16) < (2 ** 8) for byte in address.split(":")]), "Assertion Error: Invalid MAC Address ({address})"
			except: raise ValueError(f"Assertion Error: Invalid MAC Address ({address})")

		# Setup Class
		self.addr = address

	def pack(self) -> bytes:
		return bytes.fromhex(self.addr.replace(":", ""))

class IPv4:

	# NOTE: `OWN_IP` irreliable at times
	@staticmethod
	def OWN_IP() -> str:
		return socket.gethostbyname(socket.gethostname())

	@staticmethod
	def unpack(packed_ip: bytes) -> str:
		return socket.inet_ntoa(packed_ip)

	def __init__(self, address):

		# Validate Given Address
		assert len(address.split(".")) == 4, f"Invalid IPv4 address ({address})"
		try: assert min([int(byte) < (2 ** 8) for byte in address.split(".")]), "Invalid IPv4 address ({address})"
		except: raise ValueError("Invalid IPv4 address ({address})")

		# Setup Class
		self.addr = address

	def pack(self) -> bytes:
		return socket.inet_aton(self.addr)
