#AlphaMc Installer
#runs on first boot

print " "
print "Welcome to AlphaMc Server Software! You are going to setup the server now!"
print " "
print "Please pick a language"
lang = raw_input("language eng-> English: ")

if lang == 'eng':
    print lang, 'is picked'
else:
    print 'invalid language! try setup again!'
    exit()
print "	"

mcpename = raw_input("Please put in your mcpe server name: ")
print'You picked', mcpename
print "	"

print 'Do you accept the licanse? These codes are open for others to distribiutebut to give full credit to original owner?'
licanse = raw_input('Do you accept this? ')

if licanse == 'yes':
	print 'licanse is accepted!'
else:
	print 'Please acept the licanse! Try setup again!'
	exit()
