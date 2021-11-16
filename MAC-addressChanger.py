#!/usr/bin/env python
"""
Creating a basic mac address changeer and see if it works
"""
#subprocess module contails a number of functions can execute os commands
import subprocess
import optparse
import re

def get_arguments():
    parse= optparse.OptionParser() # used to get options from user when trying to write up in command line 
    parse.add_option("-i", "--interface", dest="interfacer", help="enter interface that you want to change MAC address")
    parse.add_option("-m", "--mac", dest="new_mac", help="enter mac address")
    (options,arguments) = parse.parse_args()

    if options.interface:
        parse.error("[-] Please specify an interface , use -- help for more info.")
    elif not options.new_mac:
        parse.error("[-] Please specify an new mac , use -- help for more info.")
    return options

def change_mac(interface, new_mac):
    print("[+] changing mac address for" + interface + " to " + new_mac)

    subprocess.call(["ifconfig" +  interface + "down"])
    subprocess.call(["ifconfig "+  interface + " hw ether" + new_mac])
    subprocess.call(["ifconfig " +  interface + " up"])

def get_current_mac(interface):
    ifconfig_result= subprocess.check_output(["ifconfig", interface])

    mac_address_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search:
        return mac_address_search.group(0)
    else:
        print("[+] could not find the mac address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print("Current MAC = "+ str(current_mac))
change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[+] MAC address was not changed ")


