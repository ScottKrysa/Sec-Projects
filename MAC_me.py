"""
Problem: MAC Address can be used to track individuals when using public
wifi - e.g. executives traveling abroad using airport/hotel/coffee shop wifi.

Solution: Anonymize MAC address through command line when needed.

Goal here is to make a quick command line program to 
change a MAC address for OSX. Options should include:

Randomizing the MAC
Changing to a Specific MAC
Reverting to original MAC

NOTE: Create a file named "orig_mac_addresses.py" in the same folder 
	as this program with your original MAC addresses defined as below 
	before executing.
"""

import random
import os # for executing command line commands
import re # For MAC address format check
import orig_mac_addresses # Original MAC addresses for reference

# Display original Values
orig_en0 = orig_mac_addresses.orig_en0
orig_en1 = orig_mac_addresses.orig_en1
orig_en2 = orig_mac_addresses.orig_en2

print("\nOriginal MAC Addresses: ")
print('\t' + orig_en0)
print('\t' + orig_en1)
print('\t' + orig_en2 + '\n')

# Reading that subprocess.popen() is a better way to do the following, How?
try:
	current_en0 = os.popen("ifconfig en0 | awk '/ether/{print $2}'").read()
	current_en1 = os.popen("ifconfig en1 | awk '/ether/{print $2}'").read()
	current_en2 = os.popen("ifconfig en2 | awk '/ether/{print $2}'").read()

	print('Current MAC Addresses:')
	print('\ten0 = ', current_en0)
	print('\ten1 = ', current_en1)
	print('\ten2 = ', current_en2, '\n')
except:
	print('Error displaying current MAC')

# MAC Randomizer 
def gen_hex(length):
	return ''.join(random.choice('0123456789abcdef') for _ in range(length))

def gen_mac():
	generated = gen_hex(2) + ":" + gen_hex(2) + ":" + gen_hex(2) + ":" + gen_hex(2) + ":" + gen_hex(2) + ":" + gen_hex(2)
	return generated

# Options Menu
print('1 = Revert en0 to original MAC')
print('2 = Enter Specific MAC')
print('3 = Generate New Random MAC\n')

prompt = input('Choice: ')

"""
Executing the options.

Questions:
Is it necessary to use try/except?
Are there any reasons to change this command line program to one of functions?
"""
try:
	if prompt == '1':
		os.system('sudo ifconfig en0 ether ' + orig_en0)
		print('[+] Complete')
	elif prompt == '2':
		def_mac = input("Enter MAC: ")
		if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", def_mac.lower()):
			os.system('sudo ifconfig en0 ether ' + def_mac)
			print('[+] Complete')
		else:
			print('Invalid Format')
	elif prompt == '3':
		while True:
			random_mac = gen_mac()
			print(random_mac)
			accept_mac_prompt = input("Accept? (y/n) ")
			if accept_mac_prompt == "y":
				break
		os.system('sudo ifconfig en0 ether ' + random_mac)
		print('[+] Complete')
	else:
		print('\nERROR: Invalid Response')
except:
	print('\nERROR: Invalid Response')

