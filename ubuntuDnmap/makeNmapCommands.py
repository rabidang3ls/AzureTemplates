#!/usr/env/python

jobsFast = []
# jobsIntermediate = []
jobsThorough = []

def main():
	with open('ips.txt', 'r') as f:
		iplist = f.read().splitlines()
	for item in iplist:
		item2 = ''
		if '/' in item:
			item2 = item.replace('/', 'slash')
		if not item2:
			jobsFast.append('nmap -Pn --top-ports 100 -oA {0}.fast {0}'.format(item))
			jobsThorough.append('nmap -p 0-65535 -oA {0}.thorough {0}'.format(item))
		else:
			jobsFast.append('nmap -Pn --top-ports 100 -oA {0}.fast {1}'.format(item2,item)) #add -Pn?
			jobsThorough.append('nmap -p 0-65535 -oA {0}.thorough {1}'.format(item2,item))
	with open('nmapCommands.txt', 'w') as f:
		for item in jobsFast:
			f.write(item + '\n')
		for item in jobsThorough:
			f.write(item + '\n')

if __name__ == '__main__':
	main()
