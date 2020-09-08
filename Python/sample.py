# Copyright 2017, Digi International Inc.
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import time

from digi.xbee.models.status import NetworkDiscoveryStatus
#from digi.xbee.devices import *
from digi.xbee.devices import XBeeDevice
from digi.xbee.devices import ZigBeeDevice
from digi.xbee.devices import DigiMeshDevice
from digi.xbee.devices import DiscoveryOptions
from digi.xbee.util import utils
from digi.xbee.models.mode import OperatingMode
#import digi.xbee 

# TODO: Replace with the serial port where your local module is connected to.
PORT = "/dev/ttyUSB1"
# TODO: Replace with the baud rate of your local module.
BAUD_RATE = 9600


def main():
    print(" +---------------------------------------------+")
    print(" | XBee Python Library Discover Devices Sample |")
    print(" +---------------------------------------------+\n")

    device = ZigBeeDevice(PORT, BAUD_RATE)

    try:
        device.open()

        protocolo = device.get_protocol()

        print(protocolo)

        funcao = device.get_role()

        print("Funcao: %s" % funcao)

        xbee_network = device.get_network()

        xbee_network.set_discovery_timeout(15)  # 15 seconds.

        xbee_network.clear()

        # Callback for discovered devices.
        def callback_device_discovered(remote):
            print("Device discovered: %s" % remote)

        # Callback for discovery finished.
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
        #print("Dispositivo %s " % devices[1].get_node_id())
        print("PAN ID %s " % utils.hex_to_string(devices[0].get_pan_id()))

        #ver como usar esse metodo
        #device.build_aggregate_routes()

        print(device.get_routes())


        sourceAddres=device.get_64bit_addr()
        print("Endereco Local: %s" % sourceAddres)
        destAddress=device.get_dest_address()
        print("Endereco Destino: %s" % destAddress)

        modoDeOperacao=device.operating_mode
        print("Mode de Operacao: %s" % modoDeOperacao)

        print(device.get_route_to_node(devices[0],timeout=30))

        print(device.get_neighbors())

        #neighbors=device.get_neighbors()
        #print("Vizinhos: %s" % modoDeOperacao)

    finally:
        if device is not None and device.is_open():
            device.close()


if __name__ == '__main__':
    main()
