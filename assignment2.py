#import libraries
import hashlib, sys, time

#initialize a timer
start = time.time()

#initialize a counter and read the password file
sha1hash = 0
listofpasswords = str(open('10millionpasswordlisttop.txt').read())

#Compare passwords in list with hash and print results
def forone(x):
    sha1hash = x
    counter = 0
    for password in listofpasswords.split('\n'):
        hashedpassword = hashlib.sha1(bytes(password)).hexdigest()
        if hashedpassword == sha1hash:
            print 'The password is', str(password),'the hash matched on comparison #', counter+1, '.'
            break
        elif hashedpassword != sha1hash:
            counter = counter + 1
#            Uncommenting the line below will print the passwords in the list that aren't matched. This will result in a longer run time.
#            print 'The password', str(password), 'does not match, trying next hash ... attempt #', counter, '.'
    
#Compare passwords in list with hash and print results
def forsalt(x):
    sha1hash = x
    counter = 0
    for password in listofpasswords.split('\n'):
        hashedpassword = hashlib.sha1(bytes(password)).hexdigest()
        if hashedpassword == sha1hash:
            print 'The salt term is', str(password),'the hash matched on comparison #', counter+1, '.'
            break
        elif hashedpassword != sha1hash:
            counter = counter + 1
#            Uncommenting the line below will print the passwords in the list that aren't matched. This will result in a longer run time.
#            print 'The password', str(password), 'does not match, trying next hash ... attempt #', counter, '.'
    return password

#Compare passwords in list with salted hash and print results
def fortwo(y,x):
    sha1hash = x
    salt = y
    counter = 0
    for password in listofpasswords.split('\n'):
        saltedhash = salt + password
        hashedpassword = hashlib.sha1(bytes(saltedhash)).hexdigest()
        if hashedpassword == sha1hash:
            print 'The password is', salt + str(password), 'the hash matched on comparison #', counter+1, '.'
            break
        elif hashedpassword != sha1hash:
            counter = counter + 1
#            Uncommenting the line below will print the passwords in the list that aren't matched. This will result in a longer run time.
#            print 'The password is', salt + str(password), 'does not match, trying next hash ... attempt #', counter, '.'
    
#Get the number of arguments to determine flow of program
if len(sys.argv) <= 1 or len(sys.argv) > 3:
    print 'Error, to few arguments or to many arguments.'
elif len(sys.argv) == 2:
    forone(sys.argv[1])
elif len(sys.argv) == 3:
    saltterm = forsalt(sys.argv[1])
    combhash = sys.argv[2]
    fortwo(saltterm,combhash)

#End counter and report runtime
end = time.time()    
print 'It took', round((end - start),2), 'seconds for the program to run.'
