##Prerequisites to using DNMAP with Azure Resource Manager Template:
1. Must have access to an Azure account

##Running DNMAP:
1. Edit this file to match the nmap command(s) you want run: https://github.com/rabidang3ls/AzureTemplates/blob/master/ubuntuDnmap/nmapCommands.txt
2. Download the template and parameters files:
  1. [Template](https://github.com/rabidang3ls/AzureTemplates/blob/master/ubuntuDnmap/azuredeploy.json)
  2. [Parameters](https://github.com/rabidang3ls/AzureTemplates/blob/master/ubuntuDnmap/azuredeploy.parameters.json)
3. Run the following commands:
```
RecGroup=dnmaprg-`date +%s`
azure group create -n $RecGroup -l "West US"
azure group deployment create -f azureDeploy.json -e azureDeploy.parameters.json -g $RecGroup -n $RecGroup
```
Get the public IP addresses of the newly created VMs with the following command (depending on the number of VMs in your azure subscription, this command can take a while. I've got 35 VMs and it takes about 32 seconds to complete):
`azure vm list-ip-address | grep data | grep dnmapVM | awk '{print $4}'`
