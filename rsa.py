#!/usr/bin/env python

import sys
import math
import random
from ctypes import *

def lcm(a,b):
   out = (a*b)/gcd(a,b)
   return out

def gcd(a,b):
    rest = -1
    while i != 0:
        rest = a % b
        a = b
        b = rest
    return b
            

def primes(limit):
    iterator = 0;
    while (iterator<=limit):
        iterator = iterator + 1
        if iterator % 2 != 0 & iterator % 3 != 0:
           print(iterator)

def is_prime(limit):
    is_prime = False
    while True:
        rand = random.randint(2,int(limit)-1)
        if rand % 2 != 0 and rand % 3 != 0 or rand == 2:
            return rand


class RSA:

    @staticmethod
    def get_input():
        p = int(sys.argv[1])
        q = int(sys.argv[2])
        n = p*q;
        lmbd = lcm(p-1,q-1)
        #print(lmbd)
        get =  is_prime(lmbd)
        print("Your message: ")
        data = sys.stdin.readline()

        for c in data:
            asc = int(ord(c))
            result = asc**get % n
            print(result)

        #print(dec_test())
RSA.get_input()
