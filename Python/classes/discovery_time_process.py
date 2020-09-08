from time import time, sleep

class network_info:
    def __init__(self):
        self.time = 0
        self.discovery_time = []
        self.n_devices = len(self.discovery_time)
        self.devices_id = []
    
    def start_timer (self):
        self.time = time()
    
    def add_time(self, node_id):
        self.discovery_time.append(round(time() - self.time, 2))
        self.n_devices = len(self.discovery_time)
        self.devices_id.append(node_id)




