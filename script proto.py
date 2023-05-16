import subprocess
import time
import serial


ser = serial.Serial(port='COM3',baudrate=9600, bytesize=8)

cmd = "setenv opermode batch"
ser.write(cmd.encode())
print "OK"
print ser.readline()

cmd = "saveenv"
ser.write(cmd.encode())
print "KO"
print ser.readline()

