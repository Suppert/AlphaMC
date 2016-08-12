#AlphaMc Installer
#runs on first boot
import os
from shutil import copyfile

print " "
print "Welcome to AlphaMc Server Software! You are going to setup the server now!"
print " "
install = True
while install:
    choice = raw_input("Please accept the license. You are able to download and share this codes but cannot use in your builds without giving credit to owner. Y/N: ")
    if choice == "Y":
        print "License agreed!"
        install = False
        print " "
    else:
        print 'Please accept licence'

print "	"
servername = raw_input("Please put in your mcpe server name: ")
print'You picked', servername
print "	"

install = True
while install:
    skip_installer = raw_input('Do you want to skip the installer? Y/N ')
    if skip_installer == 'Y':
        install = False
    else:
        print 'You will setup the server now!'
        print ' '
        
	
os.chdir('/home/pi/Desktop/AlphaMc')
if not os.path.exists('worlds'):
    os.makedirs('worlds')
if not os.path.exists('plugins'):
    os.makedirs('plugins')
if not os.path.exists('crashes'):
    os.makedirs('crashes')
if not os.path.exists('players'):
    os.makedirs('players')
if not os.path.isfile('config.py'):
    copyfile('/home/pi/Desktop/AlphaMc/Core/AlphaMc/res/config.py', '/home/pi/Desktop/AlphaMc/config.py')
print 'Setup complete!'
