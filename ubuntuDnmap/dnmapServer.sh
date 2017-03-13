apt -y update
apt -y install python-twisted-bin python-twisted-core nmap
wget https://github.com/rabidang3ls/AzureTemplates/raw/master/ubuntuDnmap/dnmap_v0.6.tgz
tar -zxf dnmap_v0.6.tgz
cd dnmap_v0.6
mv * /home/dnmap/
cd /home/dnmap/
wget https://raw.githubusercontent.com/rabidang3ls/AzureTemplates/master/ubuntuDnmap/ipRanges.txt https://raw.githubusercontent.com/rabidang3ls/AzureTemplates/master/ubuntuDnmap/nmapCommands.txt
if [ $(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:) == 10.0.0.4 ]; then
  screen -S dnmap -d -m /home/dnmap/dnmap_server.py -f nmapCommands.txt -v 3
else
  screen -S dnmap -d -m /home/dnmap/dnmap_client.py -s 10.0.0.4 -d -a $(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:)
fi
