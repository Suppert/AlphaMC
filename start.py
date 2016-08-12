import socket
import os
from shutil import copyfile

if not os.path.isfile('config.py'):
    os.chdir('Core/AlphaMc/wizard')
    os.system('python installer.py')
print "AlphaMc is starting! Please wait! Version 1 beta!"
 
HOST = '0.0.0.0'
PORT = 19132
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Opening host on 0.0.0.0!'
 
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Server failed to start! Maybe another server is using the port?'
    sys.exit()
     
print 'Server started!'

 
s.listen(10)

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
s.close()
