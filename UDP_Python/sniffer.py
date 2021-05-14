import socket 
import struct
import binascii
import os
import pye
import time

def main():
	while True:
		if os.name == "nt":
			s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
			s.bind(("YOUR_INTERFACE_IP",0))
			s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)
			s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
		else:
			s=socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

		# Capture packets from network
		#time.sleep(1)
		pkt=s.recvfrom(65565)
		# extract packets with the help of pye.unpack class 
		unpack=pye.unpack()
		print("\n\n===&gt;&gt; [+] ------------ Ethernet Header----- [+]")
		for i in unpack.eth_header(pkt[0][0:14]).items():
			a,b=i
			print("{} : {} | ".format(a,b),end="")
		print("\n===&gt;&gt; [+] ------------ IP Header ------------[+]")
		for i in unpack.ip_header(pkt[0][14:34]).items():
			a,b=i
			print("{} : {} | ".format(a,b),end="")
		print("\n===&gt;&gt; [+] ------------ Tcp Header ----------- [+]")
		for  i in unpack.tcp_header(pkt[0][34:54]).items():
			a,b=i
			print("{} : {} | ".format(a,b),end="")
		


if __name__ == '__main__':
	main()
