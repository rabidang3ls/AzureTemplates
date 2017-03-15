apt -y update && apt -y install python3 python-twisted-bin python-twisted-core nmap
wget https://github.com/rabidang3ls/AzureTemplates/raw/master/ubuntuDnmap/dnmap_v0.6.tgz
tar -zxf dnmap_v0.6.tgz
cd dnmap_v0.6
mv * /home/dnmap/
cd /home/dnmap/
echo "sudo -s" > .bash_login && chown dnmap:dnmap .bash_login && chmod 644 .bash_login
wget https://raw.githubusercontent.com/rabidang3ls/AzureTemplates/master/ubuntuDnmap/ips.txt https://raw.githubusercontent.com/rabidang3ls/AzureTemplates/master/ubuntuDnmap/makeNmapCommands.py
if [ $(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:) == 10.0.0.4 ]; then
#  /home/dnmap/dnmap_server.py -f nmapCommands.txt -v 3
  python3 makeNmapCommands.py
  screen -S dnmap -d -m /home/dnmap/dnmap_server.py -f nmapCommands.txt -v 3
else
#  /home/dnmap/dnmap_client.py -s 10.0.0.4 -d -a $(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:)
  screen -S dnmap -d -m /home/dnmap/dnmap_client.py -s 10.0.0.4 -d -a $(ifconfig | grep -E "([0-9]{1,3}\.){3}[0-9]{1,3}" | grep -v 127.0.0.1 | awk '{ print $2 }' | cut -f2 -d:)
fi
