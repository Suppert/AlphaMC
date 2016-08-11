# AlphaMC Installer
# runs on first boot

print(" ")
print("Welcome to AlphaMC Server Software! You are going to setup the server now!")
print(" ")
print("Please pick a language")
lang = raw_input("language eng-> English: ")

if lang == 'eng':
    print(lang, 'is picked')
else:
    print('invalid language! try setup again!')
    exit()
print "	"

mcpename = raw_input("Please put in your mcpe server name: ")
print('You picked', mcpename)
print("")

print('Do you accept the license? These codes are open for others to distribiute but to give full credit to original owners?')
license = raw_input('Do you accept this? ')

if license == 'yes':
	print('license is accepted!')
else:
	print 'Please acept the license! Try setup again!'
	exit()
