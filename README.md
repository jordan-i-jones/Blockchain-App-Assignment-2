# *Blockchain-& App-Assignment-2*

## SHA1 Hashes with Brute Force:
Code a Python 2.7 program that breaks SHA1 hashes in a brute force manner.

## My Code:
To break the SHA1 hash with brute force, my code loads a file containing a list of the top 1,000,000 top password from the your directory. It then compares a hash, given in the form of an argument, and compare the hashed password with each password in the file till it finds a match.
The code uses a few libraries that my be unfamiliar to some. These libraries include: hash, sys, and time. The first library, hash, is used by implementing a common interface to many different secure hash and message digest algorithms. It is imported so that the SHA1 hash algorithm can be used. The next library, sys, is used to read command line inputs as parameters for the program. The hash that is being match is input here to find a matching password. The final library, time, is used to get the program's run time.


To run this program, one must first download the files in the 
