import csv
from netmiko import ConnectHandler



# prints the server and description; more-so for a check to make sure the code parses the right data
def netConnection(sHost,description):
    
    with open('output.csv', 'a', newline='') as o:
        outfile = csv.writer(o) # removes quotation around description =  quoting=csv.QUOTE_NONE, escapechar=' '
        #outfile.writerow([sHost, description])
    
        #print(output) 




def netConnectionTestReader():
    
    print("reading server...")
    count = 0
    with open('sample8thFloor.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            #if not row:
                #continue
            count += 1
            sHost = row[3]
            description = row[7]
            
            #netConnection(sHost,description)

            # sets device equal to 
            net_connect = ConnectHandler(device_type="cisco_xe",host= sHost,username="nettools",password="jrfoO6wPR3eGnoHC8Sh",)
            #output = net_connect.send_command("show ip arp")

            # configuration 
            net_connect.send_config_set()
            net_connect.save_config()
    print("finished printing to outfile")   
    print(count)   
    



netConnectionTestReader()