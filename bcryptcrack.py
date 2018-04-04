#!/usr/bin/env python

"""bcryptcrack.py: A lame bcrypt bruteforcer, that takes advantage of multiple cores."""
__author__  = "@xenvito"
__license__ = "GPL"
__version__ = "0.0.1"


from string import ascii_letters
import bcrypt
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from itertools import product
from string import ascii_lowercase

# If you want to try a full AlphaNumeric keyspace, use the following keyspace.
# Warning: this will take a long long time. Ideally you should be using hashcat or JTR.
#keyspace = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
keyspace = 'abcdefghijklmnopqrstuvwxyz'

# Change the keyspace as per your need
# Warning: Larger pass_length will take exponentially longer to crack. Size does matter
# Recommendation: Ideally you should be using hashcat or JTR for any real cracking
pass_length = 4

keywords = [''.join(i) for i in product(keyspace, repeat = pass_length)]
print 'Trying %s keywords' % len(keywords)


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
