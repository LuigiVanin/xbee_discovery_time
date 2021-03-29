import time

from digi.xbee.models.status import NetworkDiscoveryStatus
#from digi.xbee.devices import *
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.devices import DigiMeshDevice
from digi.xbee.devices import DiscoveryOptions
from digi.xbee.util import utils
from digi.xbee.models.mode import OperatingMode

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB1"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 115200


def main():
    print(" +----------------------------------------+")
    print(" | XBee Python discovery time chronometer |")
    print(" +----------------------------------------+\n")

    device = DigiMeshDevice(PORT, BAUD_RATE)

    try:
        device.open()

        protocolo = device.get_protocol()

        print(protocolo)

        funcao = device.get_role()

        print("Funcao: %s" % funcao)

        xbee_network = device.get_network()

        xbee_network.set_discovery_timeout(15)  # 15 seconds.

        xbee_network.clear()

        def callback_device_discovered(remote):
            print("Device discovered: %s" % remote)
            
        def callback_discovery_finished(status):
            if status == NetworkDiscoveryStatus.SUCCESS:
                print("Discovery process finished successfully.")
            else:
                print("There was an error discovering devices: %s" % status.description)

        xbee_network.add_device_discovered_callback(callback_device_discovered)

        xbee_network.add_discovery_process_finished_callback(callback_discovery_finished)

        options = xbee_network.get_discovery_options()
        print(utils.hex_to_string(options))

        xbee_network.start_discovery_process()

        print("Discovering remote XBee devices...")

        while xbee_network.is_discovery_running():
            time.sleep(0.1)

        devices=xbee_network.get_devices()
        remote = devices[0]
        print(remote.get_protocol())
        print("Dispositivo %s " % devices[0].get_node_id())


        sourceAddres=device.get_64bit_addr()
        print("Endereco Local: %s" % sourceAddres)
        destAddress=device.get_dest_address()
        print("Endereco Destino: %s" % destAddress)

        modoDeOperacao=device.operating_mode
        print("Mode de Operacao: %s" % modoDeOperacao)

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
