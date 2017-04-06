from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *
import pprint
import numpy

"""OSENCRYPTION"""

string = raw_input(" what do you want me to encrypt? ")
print "encrypting "+ string

"""convert string to binary"""

bin = '0'.join(format(ord(x), 'b') for x in string)
print string + " in binary is "+ bin

"""each ASCII character must be a binary octet, prepend enough zeros to do so."""

octet = '0' + bin

print len(octet)
print octet
print type(octet)

"""convert the string to an array, to be manipulated"""

numbits = list(octet)
print numbits
print len(numbits)
print type(numbits)

"""append a 1 to the end of the list"""

n1 = numbits + ['1']
print n1
n = list(map(int, n1)) 

"""Padding: add zeros such that dividing the list length by 512 yeilds a remainder of 448"""

while len(n)%512 != 448:
    n.append(0)
    print n
    """sleep(0.05)"""

"""Padding (second step): convert the number of bits of the origional message to its binary number and append that plus however many zeros necessary to make the total message length a multiple of 512"""

om = len(octet)
print om
p2 = '{0:b}'.format(om)
print p2

pf = 64 - len(p2)
print "number padded zeros necessary to make message length a multiple of 512: " + str(pf)
 
pfs = str(pf)
oms = str(om)
p2s = str(p2)

p2l = list(p2s)

padz = []

while len(padz) != pf:
    padz.append(0)


message = n + padz + p2l
print message
print len(message)

"""Break up the 512 bit message into a sixteen 32-bit words"""

def chunks(message, n):
    for i in range(0, len(message), n):
        yield message[i:i + n]

words = list(chunks(message, 32))
print words

h0 = '01100111010001010010001100000001'
h1 = '11101111110011011010101110001001'
h2 = '10011000101110101101110011111110'
h3 = '00010000001100100101010001110110'
h4 = '11000011110100101110000111110000'


