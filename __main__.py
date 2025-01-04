from packet import ETH_Frame, ARP_Body, SEND_PACKET
from addresses import MAC, IPv4

CONFIG = {

	"INT": "wlan0",						# Network interface
	"OP": 1,							# OP Code (1 [req]; 2 [res])

	# I should use a library to reliably
	# detect the client MAC / IP
	"SHA": MAC(MAC.OWN_MAC()), 			# Its not perfect...
	"SPA": IPv4("192.168.0.60"), 		# OWN_IP doesn't work...

	"THA": MAC("ff:ff:ff:ff:ff:ff"),	# Broadcast THA
	"TPA": IPv4("192.168.0.160"),		# Target IP

}

# Create Packet Parts
# (ethernet frame + arp body)

eth_frame = ETH_Frame(CONFIG["THA"], CONFIG["SHA"], 0x0806)
arp_packet = ARP_Body(CONFIG["OP"],  CONFIG["SHA"], CONFIG["SPA"], CONFIG["THA"], CONFIG["TPA"])

# Unify Packet

packet = eth_frame.frm + arp_packet.pkt

# Debugging

conf_str = "\n │  ".join([f"{k}: {str(v)}" for k, v in CONFIG.items()])
pack_str = f"\n │  ethernet frame: {eth_frame.frm}\n │  packet body:    {arp_packet.pkt}\n │  full packet:    {packet}"

print(f"\n\033[0;34mConfiguration:\n │  {conf_str}\033[0m\n")
print(f"\033[0;32mPrepared ARP packet (pkt 1):\033[0;2m{pack_str}\033[0m\n")

# Send the packet

SEND_PACKET(CONFIG["INT"], packet)

print("\033[0;32mPacket Sent\033[0m\n")
