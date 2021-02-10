#!/usr/bin/python

#LIBRARIES
import subprocess

#HEADER
print("\n.\n.\n.\n\nCCON MAC Address Modifier v.01b\n\nThis tool can be used \
to modify the MAC address of any interface on your host. This\
 program was written for Python 2 and requires you to use \
sudo to function correctly.\n")
print("\nYour current network settings are as follows -")
subprocess.call("ifconfig", shell=True)

#VARIABLES
interface = raw_input("Modify MAC address for which interface?\n")
new_mac = raw_input("New MAC? ( xx:xx:xx:xx:xx:xx )\n")
#dev-notes: you can use Python 3 simply by switching 'raw_input' to 'input'
#'raw_input' removes the trailing new line

#MAIN
print("[+] Changing MAC address for " + interface + " to " + new_mac)
subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["sudo", "ifconfig", interface, "up"])
#dev-notes: by using [brackets] to LIST the entire command argument rather
#than using '+', you make the script more secure, by not allowing the user
#to inject additional commands with ';'. This avoids shell=True, a known
#security hazard
