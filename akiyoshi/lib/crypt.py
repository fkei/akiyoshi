#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sha

def sha1encrypt(v):
    salt = ''
    for x in xrange(0,16):
        salt += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

    r = sha.sha(v+salt).hexdigest()
    return r, salt

def sha1compare(target, plain, salt=''):
    x = sha.sha(plain+salt).hexdigest()
    if target == x:
        return True
    else:
        return False

if __name__ == '__main__':
    word = 'password'
    print 'word=' + word
    v, salt = sha1encrypt(word)
    print 'encrypt=' + v
    print 'salt=' + salt

    if sha1compare(v, word, salt) is True:
        print 'Success'
    else:
        print 'Failure'
