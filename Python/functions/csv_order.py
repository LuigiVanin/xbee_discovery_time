# header = [" ESTACAO_BASE", " ROUTER_01", " ROUTER_03"
from csv import reader as rd
from csv import writer as wt

def order_device_list(network_info):
    header = [" ROUTER_01"," ROUTER_03" , " ESTACAO_BASE"]
    seq =[]

    with open("table.csv", "r", newline="") as csvfile:
        reader = rd(csvfile)
        l = list(reader)
        seq.append(len(l))
    
    for col in header:
        if col in network_info.devices_id:
            i = network_info.devices_id.index(col)
            seq.append(network_info.discovery_time[i])
        else:
            seq.append("-")
    return seq


def send_data_to_csv(csvfile_name, info):
    with open(csvfile_name, "a", newline="") as csvfile:
        input_csv = wt(csvfile, delimiter=',')
        input_csv.writerow(info)
