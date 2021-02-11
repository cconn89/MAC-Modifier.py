#!/usr/bin/python
#inspired by zsecurity's Python Ethical Hacking course

#LIBRARIES
import subprocess
import optparse
import re

#HEADER
print("\n.\n.\n.\n\nCCONN MAC Address Modifier v.3\n\nThis tool can \
be used to modify the MAC address of any interface on your host. This\
 program was written in Python for Linux/Unix systems, and requires you\
 to use sudo or root priviledges to function correctly.\n")

print("\n[+] Your current network settings are as follows -\n")
subprocess.call(["ifconfig"])
print("\n")

#MAIN FUNCTIONS
def GetArgs():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Select i\
    nterface to change MAC address (example: eth0, wlan0, etc...)")
    parser.add_option("-m", "--new_mac", dest="new_mac", help="Input new MA\
    C address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info.")
    return options

def ChangeMac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def CheckModifiedMac(interface):
   ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
   modified_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
   if modified_mac:
       return modified_mac.group(0)
   else:
       print("[-] Could not read MAC address")

     options = GetArgs()

ChangeMac(options.interface, options.new_mac)

modified_mac = CheckModifiedMac(options.interface)

print("\n[+] Modified MAC = " + str(modified_mac))

#dev-notes: by using [brackets] to LIST the entire command argument 
#rather than using '+', you make the script more secure, by not 
#allowing the user to inject additional commands with ';'. This avoids
#shell=True, a known security hazard (lines 16, 35-38)

#dev-notes: you can use Windows by changing all instances of ifconfig 
#to ipconfig, and running the program as Administrator

#old//dev-notes: you can use Python 3 by switching 'raw_input' to 'input'
#'raw input' removes the trailing new line (instead options are given at
#the command line when the program is exectuted, rather than the program
#requesting user input at run time)
