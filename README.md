# INFO-Grabber-Discord-Webhook
Python program that grabs info of os, hardware, discord username etc. and sends it to a Discord WebHook.

!!!!! In the 78th line of code, past your webhook url into 'your webhook url'. Username doesn't need to be changed, but you can to everything you want.
If you don't do it, you won't receive any grabbed info!!!!

This program was not created to be all-in-one grabber. It was created to do some fake app and then add this program's source code to your creation to have something that will take victim's guard off while the script grabs his PCs info.
If you want to use only this script it is recommended to change webhook URL and name then encrypt the file so the victim won't be able to see its source code.


What does this program do? (Version 1.0.0)
This program grabs: IP address and MAC address, Operating System name,version and hostname, CPU architecture information.
After it obtains those information it creates a file named z3k1wm6pf37wash4.txt and writes all grabbed informations into this file.
After these informations were written the program sends it on the discord server as a webhook and then deletes the file so the victim won't figure out what happened.

To-Do:
Be able to grab discord username of victim.
Make option to receive embed massage insted of a text file.


Discord webhook sends this informations as a .text file

IP address: [victim's ip address]
HOSTNAME: [computer hostname]
MAC ADDRESS: [victim's mac address]
OPERATING SYSTEM: [os name]
OPERATING SYSTEM VERSION: [os version / linux kernel version]
CPU ARCHITECTURE: [cpu architecture]
