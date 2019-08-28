import json
import os
import datetime

rst_pwr_btn = False
path = "/home/pi/Documents/Scripts/"

def timestamp():
    current_time = datetime.datetime.now(datetime.timezone.utc)
    unix_timestamp = current_time.timestamp() # works if Python >= 3.3
    return str(int(unix_timestamp))

def pwr_rst_btn():
    print("system buttons set to: " + str(rst_pwr_btn))
    if(rst_pwr_btn is True):
        os.system("python" + path + "pwr_rst_buttons.py &")
        print("system buttons enabled")
    else:
        print("system buttons disabled")


print("last update: " + timestamp())

with open(path + 'config.txt') as json_file:
    
    data = json.load(json_file)
    
    last_update = data["last_update"]
    
    prg_1 = bool(data["1"])
    prg_2 = bool(data["2"])
    prg_3 = bool(data["3"])
    prg_4 = bool(data["4"])
    prg_5 = bool(data["5"])
    prg_6 = bool(data["6"])
    
    rst_pwr_btn = bool(data["rst_btn_service"])
    
    data["last_update"] = str(timestamp())
    
pwr_rst_btn()

with open(path + 'config.txt', 'w') as outfile:
    json.dump(data, outfile)
    
