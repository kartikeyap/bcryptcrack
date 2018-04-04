#!/usr/bin/env python

"""bcryptcrack_dict.py: A lame bcrypt bruteforcer, that takes advantage of multiple cores for dictionary attack."""
__author__  = "@xenvito"
__license__ = "GPL"
__version__ = "0.0.1"


import bcrypt
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool


# Load your wordlist
# ToDo: Need to figure out the right way to load very large wordlists i.e. crackstation, weakpass etc
#
keywords = open('/path/to/rockyou.txt', 'r').read().splitlines()

# Update the hash to be cracked
hashed = '$2b$10$T.S676x8nCybOknL6PnOjOmUf52wOAmWnXmFLvfcT3QHBDfcRvZ9K'

def check_hash(keyword):
    if bcrypt.hashpw(keyword, hashed) == hashed:
        print 'Cracked hash: %s' % keyword
    return

def main():
    pool = ThreadPool(20)
    results = pool.map(check_hash,keywords)
    pool.close()
    pool.join()


if __name__=="__main__":
    main()

