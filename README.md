# *Blockchain & App*

## Assignment 2: SHA1 Hashes with Brute Force
Code a Python 2.7 program that breaks SHA1 hashes in a brute force manner.

### My Code:
To break the SHA1 hash with brute force, my code loads a file containing a list of the top 1,000,000 top password from the your directory. It then compares a hash, given in the form of an argument, and compare the hashed password with each password in the file till it finds a match.

The code uses a few libraries that my be unfamiliar to some. These libraries include: [hash](https://docs.python.org/2/library/hashlib.html), [sys](https://docs.python.org/2/library/sys.html), and [time](https://docs.python.org/2/library/time.html). The first library, hash, is used by implementing a common interface to many different secure hash and message digest algorithms. It is imported so that the SHA1 hash algorithm can be used. The next library, sys, is used to read command line inputs as parameters for the program. The hash that is being match is input here to find a matching password. The final library, time, is used to get the program's run time.

The program begins by first check the number of command line arguments. In the case of one or fewer arguments or more than three the program will terminate and give an error, due to either too few or too many arguments. If there are only two arguments the program will take the hash value or the second argument, and hash it then through brute force compare it with the list of words to find a match. If there are three arguments the program will behave similar to the first, but a few extra steps are involved. The first hash value or second argument, is hashed and a password is found and returned. This password is then concatenated to the second hash value or third argument, which is hashed to then find a match to that value. After solving the hash through brute force, the result is then printed with the time and the number of comparisons it took to find a match.

### Running this program:
