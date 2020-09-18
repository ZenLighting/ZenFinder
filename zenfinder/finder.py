import socket
from threading import Thread
from zenfinder.messageparser import parse_id_message
from zenfinder.mongo.light_device import deactive_light, activate_light
import time

class UDPFinder(Thread):

    def __init__(self, listen_port: int):
        Thread.__init__(self)

        self.exit_f = False
        self.listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.setup_socket(listen_port)

    def setup_socket(self, port: int):
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.listen_socket.settimeout(1)
        self.listen_socket.bind(("", port))

    def run(self):
        print("Listening for devices")
        while not self.exit_f:
            try:
                msg, addr = self.listen_socket.recvfrom(1024)
            except:
                continue
            print(msg)
            mac, data_port, dev_name, light_type = parse_id_message(msg)
            timestamp = time.time()
            activate_light(mac, dev_name, addr[0], data_port, timestamp, light_type)
            # database key is mac address