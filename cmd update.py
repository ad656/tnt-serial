import subprocess
import time
import sys

#tterm_path = r"C:\Program Files (x86)\teraterm\ttermpro.exe"

#ttl_path = r"C:\Users\tnt\Desktop\bumblebeeUpgrade\connectCOM3.ttl"

#command = '"{}" /C=3 /M="{}"'.format(tterm_path, ttl_path)

#subprocess.call(command, shell=True)

cmd = subprocess.Popen('cmd.exe', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
cmd.stdin.write(b'cd Desktop\\bumblebeeUpgrade\n')
cmd.stdin.write(b'python file_Cmd.py -m b:/update_nomap.ua -o update_nomap.ua -p COM3 -c 2 -d 3 > output.txt\n')
#print "OK"
#time.sleep(60)
#print "OK2"

#tterm_path = r"C:\Program Files (x86)\teraterm\ttermpro.exe"

#ttl_path = r"C:\Users\tnt\Desktop\com3pt2.ttl"

#command = '"{}" /C=3 /M="{}"'.format(tterm_path, ttl_path)

#subprocess.call(command, shell=True)
#print"OK3"
