from RPLCD.i2c import CharLCD
#from gpiozero import Button
import datetime
from time import sleep
import os
#button = Button(2)
start_line = 0
cycle_limit = 3
temp_hist = [0]
graph_data = [1,2,3,3,3,3,2,1,2,3,3,3,2,1,0,0,0,0,1,2]

def mapval(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def draw_bits(data):
    
    # Create an empty list of lists to fill the data into
    data_list = [[],[],[],[]]
    #print(data)
    for val in data:
        col = mapval(val, 40, 55, 0, 3)
        
        if col > 3:
            col = 3
        if col <= 0:
            col = 0
            
        if col == 0:
            for i in range(len(data_list)):
                data_list[i].append(0)
        if col == 1:
            for i in range(len(data_list)):
                if i == 3:
                    data_list[i].append(1)
                else:
                    data_list[i].append(0)
        if col == 2:
            for i in range(len(data_list)):
                if i >= 2:
                    data_list[i].append(1)
                else:
                    data_list[i].append(0)
        if col == 3:
            for i in range(len(data_list)):
                data_list[i].append(1)
    
    # Create custom character - black field
    blk_bar = (0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111,0b11111)
    lcd.create_char(0, blk_bar)
    
    row_counter = 0
    #print(data_list)
    for row in data_list:
        bit_counter = 0 
        for bit in row:
            char = bool(bit)
            lcd.cursor_pos = (row_counter, bit_counter)
            if char:
                lcd.write_string("\x00")
            else:
                lcd.write_string(" ")
            bit_counter += 1
        row_counter += 1


def walker(number):
    lcd.cursor_pos = (start_line + 0, 16)
    lcd.write_string("    ")
    state_list = [".", "..", '...', '....']
    string = state_list[int(number)]
    lcd.cursor_pos = (start_line + 0, 16)
    lcd.write_string(string)
    return state_list[int(number)]

def sys_status(state):
    stat = bool(state)
    if stat:
        string = "System OK!"
    else:
        string = "System Error!"
    
    lcd.cursor_pos = (start_line + 0, 0)
    lcd.write_string(string)

def get_temp():
    
    global temp_hist
    
    cmd = "vcgencmd measure_temp"
    temp_val = str(os.popen(cmd).read())
    temp_val = float(temp_val.replace("temp=", "").replace("'C",""))
    if len(temp_hist) >= 20:
        temp_hist.pop(0)
    temp_hist.append(int(temp_val))
    
    return "CPU Tmp: " + str(temp_val) + '"' + "C"

def get_ip():
    cmd = "hostname -I"
    ip = str(os.popen(cmd).read())
    ip = str(ip)[0:15]
    return "IP: " + ip

def write_temp():
    lcd.cursor_pos = (start_line + 3, 0)
    lcd.write_string(str(get_temp()))
    
def write_ip():
    lcd.cursor_pos = (start_line + 1, 0)
    lcd.write_string(str(get_ip()))
    
def write_date():
    lcd.cursor_pos = (start_line + 2, 0)
    x = datetime.datetime.now()
    x = x.strftime("%X")
    #print(x)
    lcd.write_string("Sys Time: " + str(x))
    
# A00 or A02 or ST0B
lcd = CharLCD(i2c_expander='PCF8574',
              address=0x27, port=1, cols=20,
              rows=4, dotsize=8, charmap="A02",
              auto_linebreaks=True,
              backlight_enabled=True)

try:
    lcd.clear()
    #lcd.home()
    #lcd.backlight_enabled = True
    screen = 0
    cycle_count = 0
    
    while True:
        time = datetime.datetime.now()
        time = time.strftime("%S")
        chng = int(time) % 10
        #print(time, chng)
        if  chng == 0:
            #lcd.clear()
            #print("hit")
            prev_sec = int(time)
            if screen == 0:
                screen = 1
                lcd.clear()
            elif screen == 1:
                screen = 0
                lcd.clear()
            #print(screen)
        
        if screen == 0:
            write_temp()
            write_date()
            write_ip()
            sys_status(True)
            if(cycle_count >= cycle_limit):
                cycle_count = 0
            else:
                cycle_count = cycle_count + 1
            walker(cycle_count)
        
        if screen == 1:
            get_temp()
            #print(temp_hist)
            draw_bits(temp_hist)
        
        sleep(1)
        
        
        
        
except KeyboardInterrupt:
    print("end") 



# Custom characters
#