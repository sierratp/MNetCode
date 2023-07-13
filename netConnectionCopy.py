import csv
from netmiko import ConnectHandler




def netConnection(sHost,description):
    
    with open('output.csv', 'a', newline='') as o:
        outfile = csv.writer(o) # removes quotation around description =  quoting=csv.QUOTE_NONE, escapechar=' '
        #outfile.writerow([sHost, description])
    
    

        net_connect = ConnectHandler(device_type="",host= sHost,username="",password="",)
        output = net_connect.send_command("show ip arp")

        #print(output) 
        outfile.writerow([output])



def netConnectionTestReader():
    
    print("reading server...")
    count = 0
    with open('data1.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            #if not row:
                #continue
            count += 1
            sHost = row[3]
            description = row[7]
            
            netConnection(sHost,description)
            #print(sHost)
    print("finished printing to outfile")   
    print(count)   
    



netConnectionTestReader()