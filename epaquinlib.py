from netmiko import Netmiko

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
            output = net_connect.send_command(line)
            filename = row[0] + "_" + line.replace(" ", "_") + ".txt"
            writefile = open(filename, 'w')
            writefile.write(output)
            writefile.close()
