import socket

def get_address_for_host(host):
    try:
        address = socket.gethostbyname_ex(host)
    except socket.gaierror:
        address = []
    return address

# Modify this to take a list of hosts
lookup = get_address_for_host('www.idd.com')

print(repr(lookup))