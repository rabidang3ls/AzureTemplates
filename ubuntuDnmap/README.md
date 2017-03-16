## Prerequisites to using DNMAP with Azure Resource Manager Template:
1. Must have access to an Azure account (tested on Adobe's DMa/Sandbox shared R&D but should work with any account).
1. Must be a collaborator of https://github.com/rabidang3ls/AzureTemplates
    1. OR clone the repo and update the links to your local files.
1. Must have private key to access VMs.
    1. OR change public key in the parameters file.

## Running DNMAP:
1. Put the IPs/hostnames you want to be scanned in `ips.txt`
1. Download the template and parameters files:
    1. [Template](https://github.com/rabidang3ls/AzureTemplates/blob/master/ubuntuDnmap/azuredeploy.json)
    1. [Parameters](https://github.com/rabidang3ls/AzureTemplates/blob/master/ubuntuDnmap/azuredeploy.parameters.json)
1. Run the following commands:
```
RecGroup=dnmaprg-`date +%s`
azure group create -n $RecGroup -l "West US"
azure group deployment create -f azureDeploy.json -e azureDeploy.parameters.json -g $RecGroup -n $RecGroup
```

Get the public IP addresses of the newly created VMs with the following command (depending on the number of VMs in your azure subscription, this command can take a while. I've got 35 VMs and it takes about 32 seconds to complete):
`azure vm list-ip-address | grep data | grep dnmapVM | awk '{print $4}'`

It is possible to add commands to the server after it is started. Ensure you append to the nmapCommands.txt file and DO NOT overwrite. Do something like the following:
`echo "nmap 8.8.8.8 -sT -oA 8.8.8.8" >> nmapCommands.txt`
