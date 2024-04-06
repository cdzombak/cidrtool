#!/usr/bin/env python3
import argparse
import ipaddress
import sys
from typing import List

__CIDRTOOL_VERSION__ = "<dev>"


def collapse4():
    nets: List[ipaddress.IPv4Network] = []
    for line in sys.stdin:
        nets.append(ipaddress.IPv4Network(line.strip()))
    for net in ipaddress.collapse_addresses(nets):
        print(str(net))


def collapse6():
    nets: List[ipaddress.IPv6Network] = []
    for line in sys.stdin:
        nets.append(ipaddress.IPv6Network(line.strip()))
    for net in ipaddress.collapse_addresses(nets):
        print(str(net))


def expand():
    for line in sys.stdin:
        block = ipaddress.ip_network(line.strip())
        for host in block.hosts():
            print(str(host))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c4", "--collapse4", action="store_true",
                        help="Collapse IPv4 CIDR blocks from stdin")
    parser.add_argument("-c6", "--collapse6", action="store_true",
                        help="Collapse IPv6 CIDR blocks from stdin")
    parser.add_argument("-e", "--expand", action="store_true",
                        help="Expand CIDR blocks from stdin into all usable (non-broadcast) hosts")
    parser.add_argument("-v", "--version", action="version",
                        version="cidrtool " + __CIDRTOOL_VERSION__,
                        help="Print version and exit")
    args = parser.parse_args()

    n = 0
    if args.collapse4:
        n += 1
    if args.collapse6:
        n += 1
    if args.expand:
        n += 1
    if n != 1:
        parser.error("Exactly one of -c4, -c6, -e must be specified.")

    if args.collapse4:
        collapse4()
    elif args.collapse6:
        collapse6()
    elif args.expand:
        expand()
