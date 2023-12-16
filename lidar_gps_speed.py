import smbus
import time
import serial
import string
import pynmea2
import sys
import requests
import smtlib
bus = smbus.SMBus(1) # Change the I2C bus number based on the actual device

ser = serial.Serial (“/dev/serial0”)
gnrmc_info = "$GNRMC,"
GNRMC_buffer = ''
NMEA_buff = ''

address = 0x10 # Radar default address 0x10
getLidarDataCmd = [0x5A,0x05,0x00,0x01,0x60]  # Gets the distance value instruction

def getVeLoc():
    received_data = (str)(ser.readline())
    GNRMC_data_available = received_data.find(gnrmc_info)
    
    if(GNRMC_data_available):
        GNRMC_buffer = received_data.split("$GNRMC,",1)[1]
        NMEA_buff = GNRMC_buffer.split(',')
        lat = NMEA_buff[2]
        a = float(str(lat[:2]))
        b = float(str(lat[2:]))/60
        lat = a + b
        lon = NMEA_buff[4]
        a = float(str(lon[:3]))
        b = float(str(lon[3:]))/60
        lon = a+b
        vel = float(NMEA_buff[6])*1.852*1.03
        return lat, lon, vel
        

def getR_Vel(i2c_addr):
    temp = [0] * 9
    bus.write_i2c_block_data(i2c_addr, 0, [0x5A,0x05,0x00,0x01,0x60])
    

    temp=bus.read_i2c_block_data(i2c_addr, 0, 9)
    if temp[0] == 0x59 and temp[1] == 0x59 :
        distance0 = temp[2] + temp[3] * 256
        time.sleep(0.2)
        
    bus.write_i2c_block_data(i2c_addr, 0, [0x5A,0x05,0x00,0x01,0x60])
    temp=bus.read_i2c_block_data(i2c_addr, 0, 9)
    if temp[0] == 0x59 and temp[1] == 0x59 :
        distance1 =  temp[2] + temp[3] * 256
        
    r_velocity = ((distance1 - distance0)*0.01*0.001)/0.2*3600
    return r_velocity

time.sleep(1) 
while True:
    
    lat, lon, vel = getVeLoc()
    r_vel = getR_Vel(address)
    final_vel = vel + r_vel
    print(f'lat: {lat}, lon: {lon}, vel: {vel}, r_vel: {r_vel}, final_vel: {final_vel}')
    time.sleep(0.01)
    url = "https://apis.openapi.sk.com/tmap/road/nearToRoad?version=1&lat={}&lon={}".format(lat,lon}
    
    headers = {
    "accept": "application/json",
    "appKey": "lL3gfX8XTy4VDwBSjTJll85tZifT41Gm5CEomOg2"
    }
    
    response = requests.get(url, headers=headers)
    
    limit = int(response['resultData']['header']['speed'])
    
    if final_vel > limit:
        capture_license()