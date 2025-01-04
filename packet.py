from addresses import MAC, IPv4

import socket, struct

class ETH_Frame:

	def __init__(eth, tha: MAC, sha: MAC, ether_type: int):

		eth.tha, eth.sha = tha, sha
		eth.ether_type = ether_type

		eth.bin_tha = eth.tha.pack()
		eth.bin_sha = eth.sha.pack()

		eth.frm_fmt = "!6s6sH"

		eth.frm = struct.pack(
			eth.frm_fmt,
			eth.bin_tha,
			eth.bin_sha,
			eth.ether_type)

class ARP_Body:

	# Sources:
	# RFC 826 (https://datatracker.ietf.org/doc/html/rfc826)
	# Wikipedia (https://en.wikipedia.org/wiki/Address_Resolution_Protocol)

	def __init__(ar, op: int, sha: MAC, spa: IPv4, tha: MAC, tpa: IPv4):

		ar.hrd = 1
		ar.pro = 0x0800
		ar.hln = 6
		ar.pln = 4

		ar.op = op

		ar.sha = sha
		ar.spa = spa
		ar.tha = tha
		ar.tpa = tpa

		ar.bin_sha = ar.sha.pack()
		ar.bin_spa = ar.spa.pack()
		ar.bin_tha = ar.tha.pack()
		ar.bin_tpa = ar.tpa.pack()

		ar.pkt_fmt = "!HHBBH6s4s6s4s"

		ar.pkt = struct.pack(
			ar.pkt_fmt,
			ar.hrd, ar.pro, ar.hln, ar.pln,
			ar.op,
			ar.bin_sha, ar.bin_spa,
			ar.bin_tha, ar.bin_tpa)

def SEND_PACKET(interface: str, packet: bytes):
	raw_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW)
	raw_socket.bind((interface, 0))
	raw_socket.send(packet)
