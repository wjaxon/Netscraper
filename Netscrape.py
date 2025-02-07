import pandas as pd
from netmiko import Netmiko
from getpass import getpass

print("Username:")
user = input()
password = getpass()
net_connect = Netmiko(host='10.28.160.254', username=user, password=password, device_type='cisco_ios')
mac_table = net_connect.send_command("show ip arp", use_textfsm=True) #use , use_textfsm=True parameter in net_connect to output in csv form

mac_data = {'mac_address':  [entry['mac_address'] for entry in mac_table],
            'interface': [entry['ip_address'] for entry in mac_table],
            'vlan': [entry['interface'] for entry in mac_table]
            }

df = pd.DataFrame(mac_data, columns=list(mac_data.keys()))

writer = pd.ExcelWriter('mac_table.xlsx', engine='xlsxwriter') #idk what this engine = 'xlsxwriteer
df.to_excel(writer, 'Sheet1')
writer.save()
print(mac_table)