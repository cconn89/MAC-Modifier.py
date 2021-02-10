#!/usr/bin/python
#inspired by zsecurity's Python Ethical Hacking course

#LIBRARIES
import subprocess
import optparser

#dev-notes: sub process allows us to execute system commands from our script,
#such as ifconfig. optparser allows us to use command line arguments when
#excecuting our script.

#HEADER
print("\n.\n.\n.\n\nCCONN MAC Address Modifier v.3\n\nThis tool can \
be used to modify the MAC address of any interface on your host. This\
 program was written in Python for Linux/Unix systems, and requires you\
 to use sudo or root priviledges to function correctly.\n")
print("\nYour current network settings are as follows -")
subprocess.call(["ifconfig"])

#VARIABLES

#MAIN
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

#dev-notes: by using [brackets] to LIST the entire command argument rather
#than using '+', you make the script more secure, by not allowing the user
#to inject additional commands with ';'. This avoids shell=True, a known
#security hazard

options = GetArgs()
ChangeMac(options.interface, options.new_mac)

#//END OF PROGRAM//
#OUTDATED-dev-notes: you can use Python 3 simply by switching 'raw_input' to 'input'
#'raw_input' removes the trailing new line // this was relevant before I switched to
#optparser command line options
