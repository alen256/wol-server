import socket
import struct
import sys
import re


def wake_on_lan(mac, broadcast):
    """ Switches on remote computers using WOL. """

    # Check mac address format
    found = re.fullmatch(
        '^([A-F0-9]{2}(([:][A-F0-9]{2}){5}|([-][A-F0-9]{2}){5})|([\s][A-F0-9]{2}){5})|([a-f0-9]{2}(([:][a-f0-9]{2}){5}|([-][a-f0-9]{2}){5}|([\s][a-f0-9]{2}){5}))$',
        mac)
    # We must found 1 match , or the MAC is invalid
    if found:
        # If the match is found, remove mac separator [:-\s]
        mac = mac.replace(mac[2], '')
    else:
        raise ValueError('Incorrect MAC address format')

    # Pad the synchronization stream.
    data = ''.join(['FFFFFFFFFFFF', mac * 20])
    send_data = b''

    # Split up the hex values and pack.
    for i in range(0, len(data), 2):
        send_data = b''.join([send_data,
                              struct.pack('B', int(data[i: i + 2], 16))])

    # Broadcast it to the LAN.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.sendto(send_data, (broadcast, 7))
    print("wol {mac}".format(mac=mac))
    return True


def usage():
    print('Usage: wol.py [hostname]')


if __name__ == '__main__':
    try:
        wake_on_lan(sys.argv[1], "192.168.3.255")
    except:
        usage()




