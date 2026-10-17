"""
Subnet Calculator
-----------------
Type any IPv4 address with its CIDR prefix (for example 192.168.1.10/24)
and this script works out the subnet it belongs to:

    network address, broadcast address, subnet mask, wildcard mask,
    the first and last usable host addresses, and how many hosts fit.

Built with Python's built-in `ipaddress` module -- no installs needed.
Part of Idris's project menu (#1). Co-built with Haven, Oct 17, 2026.
"""

import ipaddress


def show_subnet(interface):
    """Print everything worth knowing about one subnet."""
    network = interface.network          # the subnet itself, e.g. 192.168.1.0/24
    net_addr = network.network_address   # first address in the subnet
    broadcast = network.broadcast_address  # last address in the subnet
    total = network.num_addresses        # every address, usable or not

    # Usable hosts: normally we lose the network and broadcast addresses,
    # but /31 links use both addresses (RFC 3021) and a /32 is a single host.
    if network.prefixlen <= 30:
        usable = total - 2
        first_host = net_addr + 1
        last_host = broadcast - 1
    elif network.prefixlen == 31:
        usable = 2
        first_host = net_addr
        last_host = broadcast
    else:  # /32
        usable = 1
        first_host = last_host = net_addr

    # The network address in binary, one octet per group -- subnetting
    # is really just bit math, so we show the bits.
    binary = ".".join(f"{int(octet):08b}" for octet in str(net_addr).split("."))

    print()
    print(f"  IP address        : {interface.ip}")
    print(f"  Network address   : {net_addr}")
    print(f"  Broadcast address : {broadcast}")
    print(f"  Subnet mask       : {network.netmask}")
    print(f"  Wildcard mask     : {network.hostmask}")
    print(f"  Prefix length     : /{network.prefixlen}")
    print(f"  Total addresses   : {total}")
    print(f"  Usable hosts      : {usable}")
    print(f"  First usable host : {first_host}")
    print(f"  Last usable host  : {last_host}")
    print(f"  Network in binary : {binary}")
    print()


def main():
    print("=== Subnet Calculator ===")
    print("IPv4 only for v1. Type 'q' to quit.\n")

    while True:
        user_input = input("Enter an IP with CIDR (e.g. 192.168.1.10/24): ").strip()

        if user_input.lower() == "q":
            print("Bye!")
            break

        try:
            # strict=False means 192.168.1.10/24 is accepted and the
            # network it belongs to is worked out for us.
            interface = ipaddress.ip_interface(user_input)
        except ValueError:
            print("That doesn't look like a valid IP/CIDR.")
            print("Try something like 192.168.1.10/24\n")
            continue

        if interface.version != 4:
            print("That's IPv6 -- v1 speaks IPv4 only. (v2 material!)\n")
            continue

        show_subnet(interface)


if __name__ == "__main__":
    main()
