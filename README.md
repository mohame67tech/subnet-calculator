# Subnet Calculator

Type any IPv4 address with its CIDR prefix and get the full subnet picture:
network address, broadcast address, subnet mask, wildcard mask, first and
last usable hosts, host counts, and the network address in binary.

## Run it

```
python subnet_calculator.py
```

No installs needed — it uses Python's built-in `ipaddress` module.
Type `q` to quit.

## Example

```
Enter an IP with CIDR (e.g. 192.168.1.10/24): 192.168.1.10/24

  IP address        : 192.168.1.10
  Network address   : 192.168.1.0
  Broadcast address : 192.168.1.255
  Subnet mask       : 255.255.255.0
  Wildcard mask     : 0.0.0.255
  Prefix length     : /24
  Total addresses   : 256
  Usable hosts      : 254
  First usable host : 192.168.1.1
  Last usable host  : 192.168.1.254
```

## The idea worth remembering

- `ipaddress.ip_interface()` accepts a host address like `192.168.1.10/24`
  and works out the network it belongs to.
- Usable hosts = total addresses − 2 (network + broadcast are reserved),
  except `/31` links, which use both addresses, and `/32`, a single host.
- Subnetting is bit math: the binary line shows exactly where the network
  bits end and the host bits begin.

*Project menu #1 — built Oct 17, 2026.*
