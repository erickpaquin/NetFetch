from netmiko import Netmiko
import json
import csv

def get_devices(row):
    net_connect = Netmiko(
    row[0],
    username=row[1],
    password=row[2],
    secret=row[3],
    device_type=row[4],
    port=row[5],
    )
    net_connect.enable()
    with open(row[6], 'r') as commands:
        for line in commands:
            line = line.rstrip('\r\n')
            output = net_connect.send_command(line, use_textfsm=True)
            #output = json.dumps(output)
            #output_parsed = json.loads(output)
            #print (output)
            filename = row[0] + "_" + line.replace(" ", "_") + ".csv"
            with open(filename, 'w') as resultFile:
                for data in output:
                    w = csv.DictWriter(resultFile, data.keys())
                    w.writeheader()
                    w.writerow(data)
            resultFile.close()
