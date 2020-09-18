import logging

log = logging.getLogger(__name__)

class LightDevice(object):

    def __init__(self, mac, ip, port, name):
        self.mac = mac
        self.ip = ip
        self.port = port
        self.name = name

        self.light_configuration = []

    def set_light_map(self, rows: int, cols: int, coord_list: list):
        self.light_configuration = [[-1]*cols]*rows
        print(self.light_configuration)

        for i, (y, x) in enumerate(coord_list):
            print(i, x, y)
            self.light_configuration[y][x] = i

        print(self.light_configuration)
        
        
        
        
