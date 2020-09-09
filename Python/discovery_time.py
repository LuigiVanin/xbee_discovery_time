from digi.xbee.models.status import NetworkDiscoveryStatus
from digi.xbee.devices import ZigBeeDevice
from time import sleep, time
from classes.discovery_time_process import network_info
from functions.csv_order import order_device_list
from functions.csv_order import send_data_to_csv


print()

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600

csvfile = "table.csv"
device = ZigBeeDevice(PORT, BAUD_RATE)
# : ---
info = network_info()

# Callback for discovery device -------------------------
def callback_device_discovered(remote):

    info.add_time(remote.get_node_id())
    print("\n- Device discovered: %s" % remote)
    print(f"- discovery time of device number {info.n_devices}: {info.discovery_time[info.n_devices - 1]} s\n")


# Callback for discovery finished. -----------------------
def callback_discovery_finished(status):
    if status == NetworkDiscoveryStatus.SUCCESS:
        print("\n\t--------- Discovery process finished successfully. ---------\n")
    else:
        print("There was an error discovering devices: %s" % status.description)


# main execution code has to be runned into a try because of the open() and close() methods from ZigBeeDevice(device)
try:
    device.open()
    print("Aparelho Local: ", device.get_node_id(), "\n")

# seting up and starting the xbee network discovery process
    xbee_network = device.get_network()


    info.start_timer()
    
    
    xbee_network.set_discovery_timeout(15)  # 15 seconds.
    xbee_network.clear()

    xbee_network.add_device_discovered_callback(callback_device_discovered)

    xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

    print("\t--------- Starting Device discover process ---------\n")

    xbee_network.start_discovery_process()

    while xbee_network.is_discovery_running():
        sleep(0.1)


    print("\nNumber of devices found on the network:", info.n_devices)
    print("Discovery time of each device:",info.discovery_time)

finally:
    if device is not None and device.is_open():
        device.close()
        print("\n\t--------- Device Closed Successfully ---------\n")

print("*discovery time order to be printed in the csv file:", order_device_list(info))

send_data_to_csv(order_device_list( info))


        




