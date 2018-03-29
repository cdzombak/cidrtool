import ipaddress
import json

blocks = json.load(open('netblocks.json'))['netblocks']

for block_str in blocks:
	block = ipaddress.ip_network(block_str)
	for host in block.hosts():
		print(str(host))
