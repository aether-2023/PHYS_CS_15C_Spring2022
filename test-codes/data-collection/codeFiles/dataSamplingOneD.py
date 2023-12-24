import time
import board
from adafruit_lsm6ds.ism330dhcx import ISM330DHCX

i2c = board.I2C()
dhcx = ISM330DHCX(i2c)

dataFileName = "../dataFiles/accelGyroLog"+input('Enter the filename here: ')+".csv"
accelGyroLog = open(dataFileName, "a")

startTime = time.time_ns()
#take finite amount of data

for counter in range(1000000):
    #take rest data for calibration
    if counter == 0:
       print('Ready!')
    if input() == q:
        break
    accel = dhcx.acceleration
    gyro =  dhcx.gyro
    timeInterval = (time.time_ns() - startTime)/1000000000 # seconds
    startTime = time.time_ns()
    accelGyroLog.write("{0},{1}\n".format(str(timeInterval), str(accel[0]))
    
accelGyroLog.close()

print('Done!')