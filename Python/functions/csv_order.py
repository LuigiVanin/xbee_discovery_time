# header = [" ROUTER_01"," ROUTER_02"]
# header = [" ROUTER_01"," ROUTER_02", " ROUTER_03"]
# header = [" ROUTER_01"," COORDINATOR"]
from csv import reader as rd
from csv import writer as wt

csvfile_name = "/home/htnek/Documentos/Project/Python/Database/Model_04.csv"
header = [" ROUTER_01"," COORDINATOR"]
# header_table = ["Attempt"] + header

def order_device_list( network_info):
    seq =[]

    with open(csvfile_name, "r", newline="") as csvfile:
        reader = rd(csvfile)
        l = list(reader)
        if len(l) == 0 :
            seq.append(1)
        else:
            seq.append(len(l))
    
    for col in header:
        if col in network_info.devices_id:
            i = network_info.devices_id.index(col)
            seq.append(network_info.discovery_time[i])
        else:
            seq.append("-")
    return seq




def send_data_to_csv( info):
    # print(header_table)

    with open(csvfile_name, "r", newline="") as csvfile:
        reader = rd(csvfile)
        l = list(reader)

    with open(csvfile_name, "a", newline="") as csvfile:
        input_csv = wt(csvfile, delimiter=',')

        if len(l) == 0 :
            input_csv.writerow(["Attempt"] + header)
        
        input_csv.writerow(info)
