from zenfinder.mongo import device_table

def activate_light(mac, name, ip, dport, last_time, light_type):
    light_dict_query = {"mac": mac}
    light_device_obj = device_table.find_one(light_dict_query)
    light_device_new = {
        "mac": mac,
        "name": name,
        "type": light_type,
        "address": ip,
        "data_port": dport,
        "last_time": last_time,
        "active": True
    }
    if light_device_obj == None:
        print("Found device", light_device_new)
        result = device_table.insert_one(light_device_new)
        print(result)
    else:
        if light_device_obj != light_device_new:
            result = device_table.update_one({
                            "mac": mac
                        }, {
                            "$set": light_device_new
                        })
            if result.modified_count > 0:
                print(f"Found device {light_device_new}")
            #print(result)

def deactive_light(mac):
    light_query = {"mac": mac}
    result = device_table.update_one(light_query, {"$set": {"active": False}})
    print(result)