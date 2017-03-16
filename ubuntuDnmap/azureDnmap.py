#!/usr/bin/env python

from os import system,chdir
from argparse import ArgumentParser

jobsFast = []
# jobsIntermediate = []
jobsThorough = []

def main():

	parser = ArgumentParser()
	parser.add_argument('-f', '--file',
		default='ips.txt',
		dest='file',
		help='The file containing IP addresses in one of three forms: \n    1. CIDR notation - 10.1.1.0/24\n    2. Range of IPs - 10.1.1.24-65\n    3. Individual IP - 10.1.1.4\n\n')
	parser.add_argument('-fa', '--fast-args',
		default='-Pn -T4 --top-ports 100',
		dest='fast',
		help='The arguments to be used in the initial fast scan. Use quotes to contain all arguments.')
	# parser.add_argument('-ia', '--intermediate-args',
	# 	default='',
	# 	dest='intermediate',
	# 	help='The arguments to be used in the intermediate scan.')
	parser.add_argument('-ta', '--thorough-args',
		default='-T4 -p 0-65535',
		dest='thorough',
		help='The arguments to be used in the final thorough scan. Use quotes to contain all arguments.')
	args = parser.parse_args()

	system('apt -y update && apt -y install python3 python-twisted-bin python-twisted-core nmap python-netifaces')
	system('wget https://github.com/rabidang3ls/AzureTemplates/raw/master/ubuntuDnmap/dnmap_v0.6.tgz')
	system('tar -zxf dnmap_v0.6.tgz')
	chdir('dnmap_v0.6')
	system('mv * /home/dnmap/')
	chdir('/home/dnmap/')
	system('echo \"sudo -s\" > .bash_login && chown dnmap:dnmap .bash_login && chmod 644 .bash_login')
	system('wget https://raw.githubusercontent.com/rabidang3ls/AzureTemplates/master/ubuntuDnmap/ips.txt')

	try:
		import netifaces
	except:
		print('Please install python-netifaces manually: apt install python-netifaces')
		exit()

	netifaces.ifaddresses('eth0')
	ip = netifaces.ifaddresses('eth0')[2][0]['addr']
	if ip == '10.0.0.4':
		makeNmapCommands(args)
		system('screen -S dnmap -d -m /home/dnmap/dnmap_server.py -f nmapCommands.txt -v 3')

	else:
		system('screen -S dnmap -d -m /home/dnmap/dnmap_client.py -s 10.0.0.4 -d -a $(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk \'{ print $2 }\' | cut -f2 -d:)')

def makeNmapCommands(args):

	with open(args.file, 'r') as f:
		iplist = f.read().splitlines()

	for item in iplist:
		item2 = ''
		if '/' in item:
			item2 = item.replace('/', 'slash')
		if not item2:
			jobsFast.append('nmap ' + args.fast + ' -oA {0}.fast {0}'.format(item))
			# jobsIntermediate.append('nmap command')
			jobsThorough.append('nmap ' + args.thorough + ' -oA {0}.thorough {0}'.format(item))
		else:
			jobsFast.append('nmap ' + args.fast + ' -oA {0}.fast {1}'.format(item2,item)) #add -Pn?
			# jobsIntermediate.append('nmap command')
			jobsThorough.append('nmap ' + args.thorough + ' -oA {0}.thorough {1}'.format(item2,item))

	with open('nmapCommands.txt', 'w') as f:
		for item in jobsFast:
			f.write(item + '\n')
		for item in jobsThorough:
			f.write(item + '\n')

if __name__ == '__main__':
	main()
