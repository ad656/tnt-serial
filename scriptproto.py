import serial
from serial import SerialException
import sys
import time
import subprocess

try:
    ser = serial.Serial(port ='COM3',baudrate = 115200, timeout = 5)
except SerialException:
    print ('Cannot Open port')
    sys.exit(-1)

print('port connected')
ser.write(b'setenv opermode test\r')
time.sleep(0.25)

ser.write(b'saveenv\r')
time.sleep(4.5)

print('Mode: test, press the power button')
time.sleep(2)

ser.write(b'logerase\r')
time.sleep(6)
print(ser.readall())

ser.write(b'at AT%UPGCMD="CFGPART","543B70617274733D323632346B287030292C353639366B287031292C343238386B287032292C313032306B287033292C346B287034292C316D287035293B75736167653D323530306B287030292C343431366B287031292C343139326B287032292C306B287033292C306B287034292C306B2870352900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003FCBF205"\r')
time.sleep(4)
print(ser.readall())
ser.close()


print('press power button in case')
time.sleep(1)
cmd = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
cmd.stdin.write(b'cd Desktop\\bumblebeeUpgrade\n')
cmd.stdin.write(b'python file_Cmd.py -m b:/update_nomap.ua -o update_nomap.ua -p COM3 -c 2 -d 3 > output.txt\n')
print ("file.CMD.py ran successfully")
time.sleep(53)

print('press the power button')
time.sleep(2.5)

try:
    ser = serial.Serial(port ='COM3',baudrate = 115200, timeout = 5)
except SerialException:
    print ('Cannot Open port')
    sys.exit(-1)

ser.write(b'setenv logstart on\r')
print"logstart on"
time.sleep(0.25)

ser.write(b'setenv gps off\r')
print"gps off"
time.sleep(0.25)

ser.write(b'at AT%UPGCMD="UPGVRM","b:/update_nomap.ua"\r')
print "at'ed"
time.sleep(0.25)

ser.write(b'setenv rsrp -140\r')
print "rsrp -140"
time.sleep(0.25)

ser.write(b'setenv acclthreshold 0.19\r')
print "acclthreshold 0.19"
time.sleep(0.25)

ser.write(b'setenv acclconfig 0x0002\r')
print "acclconfig 0x0002"
time.sleep(0.25)

ser.write(b'setenv opermode batch\r')
print "opermode batch"
time.sleep(0.25)

ser.write(b'saveenv\r')
print "saved"
time.sleep(2)

ser.write(b'reset all\r')
print "resetted"
print ser.readall()
ser.close()

