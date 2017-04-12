from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *
import pprint
import numpy
from collections import deque

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
    """sleep(0.02)"""

"""Padding (second step): convert the number of bits of the origional message to its binary number and append that plus however many zeros necessary to make the total message length a multiple of 512"""

om = len(octet)
print om
p2 = '{0:b}'.format(om)
print p2
omlength = list(map(int, p2))

pf = 64 - len(p2)
print "number padded zeros necessary to make message length a multiple of 512: " + str(pf)
 
pfs = str(pf)
oms = str(om)
p2s = str(p2)

p2l = list(p2s)

padz = []

while len(padz) != pf:
    padz.append(0)


message = n + padz + omlength
print message
print len(message)

"""Break up the 512 bit message into a sixteen 32-bit words"""

def chunks(message, n):
    for i in range(0, len(message), n):
        yield message[i:i + n]

words = list(chunks(message, 32))
print words


"""These are our (NSA's) 'nothing up the sleeve numbers' to show that there are no backdoors or hidden patterns to the algorithm """

h0 = [0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1]
h1 = [1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1]
h2 = [1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0]
h3 = [0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0]
h4 = [1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0]

print len(words)
"""
w3 = words[len(words)-3]
w8 = words[len(words)-8]
w14 = words[len(words)-14]
w16 = words[len(words)-16]
"""



"""This function made me want to smash my computer in a drunken rage because there has GOT to be an easier way to do this"""
"""I mean seriously, is python really this much of a ass-pain to work with bits, or am I missing something big?""" 
"""This function runs some boolean operators extending the words from 16 to 80 """

def w80(words):
    oul=[]
    w3 = words[len(words)-3]
    w8 = words[len(words)-8]
    w14 = words[len(words)-14]
    w16 = words[len(words)-16]
    oul2=[]
    oul3=[]
    for i in range(0, len(words[0])): 
        ou=w3[i] ^ w8[i]
        oul.append(ou)
    for i in range(0, len(words[0])): 
        ou2=oul[i] ^ w14[i]
        oul2.append(ou2)
    for i in range(0, len(words[0])): 
        ou3=oul2[i] ^ w16[i]
        oul3.append(ou3)
    
    oul3.insert(oul3[0], oul3[-1])
    del oul3[-1]
    
    words.append(oul3)

while len(words) != 80:
    cool= w80(words)
print words
print len(words)

"""
print w80(words)
print len(words)
print words
print w80(words)
print len(words)
print words
print w80(words)
print len(words)
print words
print w80(words)
print len(words)
print words
print w80(words)
print len(words)
print words
"""
a=h0
b=h1
c=h2
d=h3
e=h4

print len(h0)


"""This function runs on words 0-19"""
f1l=[]
f2l=[]
f3l=[]

for i in range(0, len(h0)):
    f1=b[i] & c[i]
    f1l.append(f1)
    f2= ~ b[i] & d[i] 
    f2l.append(f2)
    f3=f1l[i] | f2l[i]    
    f3l.append(f3)
    k=[0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1]
print "1st function output: ", f3l

"""This function runs on words 20-39"""
ff1l=[]
ff2l=[]

for i in range(0, len(h0)):
    ff1=b[i] ^ c[i]
    ff1l.append(ff1)
    ff2=ff1l[i] ^ d[i]
    ff2l.append(ff2)
    k=[0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1]
print "2nd function output: ", ff2l

""""This function runs on words 40-59"""
fff1l=[]
fff2l=[]
fff3l=[]
fff4l=[] 
fff5l=[]

for i in range(0, len(h0)):
    fff1=b[i] & c[i]
    fff1l.append(fff1)
    fff2=b[i] & d[i]
    fff2l.append(fff2)
    fff3=c[i] & d[i]
    fff3l.append(fff3)
    fff4=fff1l[i] | fff2l[i]
    fff4l.append(fff4)
    fff5=fff4l[i] | fff3l[i]
    fff5l.append(fff5)
    k=[1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0]
print "3rd function output: ", fff5l


"""This function runs on words 50-79"""
ffff1l=[]
ffff2l=[]

for i in range(0, len(h0)):
    ffff1=b[i] ^ c[i]
    ffff1l.append(ffff1)
    ffff2=ffff1l[i] ^ d[i] 
    ffff2l.append(ffff2)
    k=[1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0]
print "4th function output: ", ffff2l
