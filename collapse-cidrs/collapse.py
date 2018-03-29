import fileinput
from ipaddr import *

nets = []

for line in fileinput.input():
    nets.append(IPNetwork(line.strip()))

for net in collapse_address_list(nets):
    print(str(net))
