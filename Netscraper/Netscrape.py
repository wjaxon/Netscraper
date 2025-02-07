import pandas as pd
from netmiko import Netmiko
from getpass import getpass
import openpyxl
import xlsxwriter

print("Username:")
user = input()
password = getpass()
net_connect = Netmiko(host='10.28.160.254', username=user, password=password, device_type='cisco_ios') #enter switch ip in for host
mac_table = net_connect.send_command("show ip arp", use_textfsm=True) #use  parameter in net_connect to output in csv form

mac_data = {'mac_address':  [entry['mac_address'] for entry in mac_table],
            'interface': [entry['ip_address'] for entry in mac_table],
            'vlan': [entry['interface'] for entry in mac_table]
            }

df = pd.DataFrame(mac_data, columns=list(mac_data.keys()))

# writer = pd.ExcelWriter('mac_table.xlsx', engine='xlsxwriter') #idk what this engine = 'xlsxwriteer
# df.to_excel(writer, 'Sheet1')
with pd.ExcelWriter('output.xlsx', engine='xlsxwriter') as writer:
   df.to_excel(writer, sheet_name='Sheet1', index=False)
print(mac_table)