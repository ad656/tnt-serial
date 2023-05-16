import serial
import subprocess
import time

ser = serial.Serial('COM3', 9600)

if(ser.isOpen() == False):
    ser.open()
    
ser.write('setenv opermode batch')
time.sleep(0.25)  
print "OK"
ser.write('saveenv')
time.sleep(0.25)
print "OK2"
ser.write('logerase')
ser.write('at AT%UPGCMD="CFGPART","543B70617274733D323632346B287030292C353639366B287031292C343238386B287032292C313032306B287033292C346B287034292C316D287035293B75736167653D323530306B287030292C343431366B287031292C343139326B287032292C306B287033292C306B287034292C306B2870352900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000003FCBF205"\r')

ser.close()  
print "OK3"
cmd = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
cmd.stdin.write(b'cd Desktop\\bumblebeeUpgrade\n')
print "make sure power is on"
cmd.stdin.write(b'python file_Cmd.py -m b:/update_nomap.ua -o update_nomap.ua -p COM3 -c 2 -d 3 > output.txt\n')
print "OK4"
time.sleep(60)

ser = serial.Serial('COM3', 9600)

if(ser.isOpen() == False):
    ser.open()
print "OK5"
ser.write('setenv logstart on\r')
print"logstart on"

ser.write('setenv gps off\r')
print"gps off"

ser.write('at AT%UPGCMD="UPGVRM","b:/update_nomap.ua"')
print "at'ed"

ser.write('setenv rsrp -140')
print "rsrp -140"

ser.write('setenv acclthreshold 0.19')
print "acclthreshold 0.19"

ser.write('setenv acclconfig 0x0002')
print "acclconfig 0x0002"

ser.write('setenv opermode batch')
print "opermode batch"

ser.write('saveenv')
print "saved"

ser.write('reset all')
print "resetted"

ser.close()
