import socket

import termcolor

import subprocess

import sys

import pyfiglet

from datetime import datetime





subprocess.call('clear', shell=True)



ascii_banner = pyfiglet.figlet_format("PORT SCANNER")

print(termcolor.colored(ascii_banner , 'magenta'))

print("-" * 50)

print("Scanning started at: " + str(datetime.now()))

print("-" * 50)



def scan(target, ports):

    print(termcolor.colored('\n' + "Starting Scan For " +str(target), 'cyan'))

    for port in range(1,ports):

        scan_port(target,port)



def scan_port(ipaddress, port):

    try:

        sock = socket.socket()

        sock.connect((ipaddress, port))

        print("[+] Port Opened " + str(port))

        sock.close()

    except:

    	pass



targets = input(termcolor.colored("[*] Enter Targets To Scan (split them by , ): ", 'cyan'))

ports = int(input(termcolor.colored("[*] Enter How Many Ports You Want To Scan: ", 'cyan')))





if ',' in targets:

    print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))

    for ip_addr in targets.split(','):

        scan(ip_addr.strip(' '),ports)



        

else:

    scan(targets,ports)

   

sys.exit(' X ERROR X ') 





