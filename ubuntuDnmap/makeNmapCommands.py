#!/usr/env/python

from argparse import ArgumentParser, RawTextHelpFormatter

jobsFast = []
# jobsIntermediate = []
jobsThorough = []

def main():
	
	parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
	parser.add_argument('-f', '--file',
		default='ips.txt',
		dest='file',
		help='The file containing IP addresses in one of three forms: \n    1. CIDR notation - 10.1.1.0/24\n    2. Range of IPs - 10.1.1.24-65\n    3. Individual IP - 10.1.1.4\n\n')
	parser.add_argument('-fa', '--fast-args',
		default='-Pn --top-ports 100',
		dest='fast',
		help='The arguments to be used in the initial fast scan. Use quotes to contain all arguments.')
	parser.add_argument('-ta', '--thorough-args',
		default='-p 0-65535',
		dest='thorough',
		help='The arguments to be used in the final thorough scan. Use quotes to contain all arguments.')
	args = parser.parse_args()

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
