import struct

def parse_id_message(msg: bytes):
    # msg structure | 6 bytes MAC | 4 byte data port | 1 byte name_length | * bytes name
    mac = msg[0:6]
    mac_string = "%x:%x:%x:%x:%x:%x" % struct.unpack("BBBBBB", mac)
    data_port = struct.unpack("I", msg[6:10])
    name_len = msg[10]
    light_type = msg[11]
    name = msg[12: 12+name_len]

    return (mac_string, data_port, name, light_type)