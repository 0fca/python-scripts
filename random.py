#!/usr/bin/env python
import sys

class Random:
    @staticmethod
    def gcd(a,b):
        rest = None
        while rest != 0:
            rest = a % b
            a = b
            b = rest
        return b

    @staticmethod
    def euler(a):
        out = 0
        if a % 2 == 0 & a % 3 == 0:
            return a - 1;
        else:
            i = a;
            while i > 0:
                divisor = Random.gcd(a,i)
                if divisor == 1:
                    out += 1
                i = i - 1;

            return out


def main():
    p = int(sys.argv[1])
    q = int(sys.argv[2])

    while q > 0:
        print(Random.euler(p))
        q = q - 1;


main()
