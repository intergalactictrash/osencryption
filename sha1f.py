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

bin = ''.join(format(ord(x), 'b').zfill(8) for x in string)
print string + " in binary is "+ bin

"""each ASCII character must be a binary octet, prepend enough zeros to do so."""
"""
octet = '0' + bin

print len(octet)
print octet
print type(octet)
"""
"""convert the string to an array, to be manipulated"""

numbits = list(bin)
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

om = len(bin)
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
    
    oul3.insert(len(oul3), oul3[0])
    del oul3[0]
    
    words.append(oul3)

while len(words) != 80:
    cool= w80(words)
print words
print len(words)


class shuffle(object):
    w = words
    a=h0
    b=h1
    c=h2
    d=h3
    e=h4
   
    def __init__(self):
        self.f=[]
        
    
    def function1(self):
        self.f1l=[]
        self.f2l=[]
    	self.f=[]
    	for i in range(0, len(h0)):
        	self.f1=self.b[i] & self.c[i]
        	self.f1l.append(self.f1)
        	self.f2= ~ self.b[i] & self.d[i] 
        	self.f2l.append(self.f2)
        	self.f3=self.f1l[i] | self.f2l[i]    
        	self.f.append(self.f3)
        	self.k=[0,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1,1,0,0,1,1,0,0,1]
    	print "1st function output: ", self.f
    	print "k-value is: ", self.k
    	f = self.f
    	k = self.k
    	return f
    	return k
    
    """This function runs on words 20-39"""
    def function2(self):
        self.ff1l=[]
        self.ff2l=[]
        self.f=[]
        for i in range(0, len(h0)):
            self.ff1=self.b[i] ^ self.c[i]
            self.ff1l.append(self.ff1)
            self.ff2=self.ff1l[i] ^ self.d[i]
            self.ff2l.append(self.ff2)
	    self.f.append(ff2l)
            self.k=[0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,0,0,0,0,1]
        print "2nd function output: ", self.f
        f = self.f
        return f
        
    def function3(self):
    	self.fff1l=[]
    	self.fff2l=[]
    	self.fff3l=[]
    	self.fff4l=[] 
    	self.f=[]
    	for i in range(0, len(h0)):
        	self.fff1=self.b[i] & self.c[i]
        	self.fff1l.append(self.fff1)
        	self.fff2=self.b[i] & self.d[i]
        	self.fff2l.append(self.fff2)
        	self.fff3=self.c[i] & self.d[i]
        	self.fff3l.append(self.fff3)
        	self.fff4=self.fff1l[i] | self.fff2l[i]
        	self.fff4l.append(self.fff4)
        	self.fff5=self.fff4l[i] | self.fff3l[i]
        	self.f.append(self.fff5)
        	self.k=[1,0,0,0,1,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,1,0,0,1,1,0,1,1,1,0,0]
    	print "3rd function output: ", self.f
    	f = self.f
    	return f
    	
    def function4(self):
        self.ffff1l=[]
        self.f=[]
        for i in range(0, len(h0)):
            self.ffff1=self.b[i] ^ self.c[i]
            self.ffff1l.append(self.ffff1)
            self.ffff2=self.ffff1l[i] ^ self.d[i] 
            self.f.append(self.ffff2)
            self.k=[1,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0]
        print "4th function output: ", self.f
        f = self.f
        return f

    	
    def show(self):
        print "this is f: ", self.f
   
       
    def iter1(self):
        for i in range(0, 20):
            self.wbin = "".join(map(str, self.w[i]))
            self.function1()
            self.blend()
            wbin = self.wbin
    
        for i in range(21, 40):
            self.wbin = "".join(map(str, self.w[i]))
            self.function2()
            self.blend()
            print self.wbin
            wbin = self.wbin
        for i in range(41, 60):
            self.wbin = "".join(map(str, self.w[i]))
            self.function3()
            self.blend()
            print self.wbin
            wbin = self.wbin
        for i in range(61, 80):
            self.wbin = "".join(map(str, self.w[i]))
            self.function4()
            self.blend()
            print self.wbin
            wbin = self.wbin
        
        print "outstide for loop: ", self.wbin
     
    def blend(self):
    	print "this is f: in blend function", self.f
    	print "This is a prior to leftrotate by 5: ", self.a
    	self.a.extend(self.a[:5])
    	del self.a[:5]
    	print "a leftrotated by 5: ", self.a
    	self.abin = "".join(map(str, self.a))
    	self.fbin = "".join(map(str, self.f))
    	self.ebin = "".join(map(str, self.e))
    	self.kbin = "".join(map(str, self.k))
    	#self.wbin = "".join(map(str, self.w[0]))
    	print "a expressed in binary: ", self.abin
    	print "w[i] expressed in binary: ", self.wbin
    	self.anum = int(self.abin, base=2)
    	self.fnum = int(self.fbin, base=2)
    	self.enum = int(self.ebin, base=2)
    	self.knum = int(self.kbin, base=2)
    	self.wnum = int(self.wbin, base=2)
    	print "w[i] as a number: ", self.wnum
    	#self.doubt = bin()
    	#print "DOUBTFUL ", self.doubt
    	while len(self.abin) < 32:
    	    self.abin = '0' + self.abin
    	
    	self.af = self.anum + self.fnum
    	print "a + f = ", self.af  	    	
        self.afbin = "{0:b}".format(self.af)
        print "added numbers in binary: ", self.afbin
        print len(self.afbin)
        while len(self.afbin) < 33:
             self.afbin = '1' + self.afbin
        print "afbin w/ carried 1: ", self.afbin
        print len(self.afbin)
        self.cafnum = int(self.afbin, base=2)
        print "caf as number: ", self.cafnum
    	
    	self.afe = self.cafnum + self.enum
        print "cafnum + enum = ", self.afe
        self.afebin = "{0:b}".format(self.afe)
        print "afebin before carry: ", self.afebin
        print "afe before carry ", int(self.afebin, base=2)
        print len(self.afebin)
        while len(self.afebin) < 34:
            self.afebin = '1' + self.afebin
        print "afebin after carry: ", self.afebin
        print len(self.afebin)
        self.cafenum = int(self.afebin, base=2)
        print "afe after carry: ", self.cafenum
        
        self.afek = self.cafenum + self.knum
        print "cafenum + knum = ", self.afek
        self.afekbin = "{0:b}".format(self.afek)
        print "afebin before carry: ", self.afekbin
        print len(self.afekbin)
        while len(self.afekbin) < 35:
            self.afekbin = '1' + self.afekbin
        print "afekbin after carry: ", self.afekbin
        print len(self.afekbin)
        self.cafeknum = int(self.afekbin, base=2)
		
        self.afekw = self.cafeknum + self.wnum
        print "cafeknum + wnum = ", self.afekw
        self.afekwbin = "{0:b}".format(self.afekw)
        print "afekwbin before carry: ", self.afekwbin
        print len(self.afekwbin)
        while len(self.afekwbin) < 36:
            self.afekwbin = '1' + self.afekwbin    
        print "afekwbin after carry: ", self.afekwbin
        print len(self.afekwbin)
		
        self.temp = list(map(int, self.afekwbin))
    	while len(self.temp) > 32:
    	    del self.temp[0]
    	print "temp variable: ", self.temp
    	print len(self.temp)
    	
    	while len(self.temp) > 32:
    	    del self.temp[0]
    	print "temp variable: ", self.temp
    	print len(self.temp)
    	
    	self.e = self.d
    	self.d = self.c
    	print "b before LROT 30 ", self.b 
    	self.b.extend(self.b[:30])
    	del self.b[:30]
    	print "b after LROT 30", self.b
    	self.c = self.b
    	self.a = self.a[-5:] + self.a
    	del self.a[-5:]
    	print "this is 'A' right rotated by 5: ", self.a
    	self.b = self.a
    	self.a = self.temp   
    	print "new a variable: ", self.a 
    	print "new b variable: ", self.b
    	print "new c variable: ", self.c
    	print "new d variable: ", self.d
    	print "new e variable: ", self.e
    	print "new temp variable: ", self.temp
    	
    	return self.e
    	return self.d
    	return self.c
    	return self.b
    	return self.a
    	return self.temp
    	
    def hash(self):
        self.abinary = "".join(map(str, self.a))
    	self.bbinary = "".join(map(str, self.b))
    	self.cbinary = "".join(map(str, self.c))
    	self.dbinary = "".join(map(str, self.d))
    	self.ebinary = "".join(map(str, self.e))
    	
    	self.anumber = int(self.abinary, base=2)
    	self.bnumber = int(self.bbinary, base=2)
    	self.cnumber = int(self.cbinary, base=2)
    	self.dnumber = int(self.dbinary, base=2)
    	self.enumber = int(self.ebinary, base=2)
    	
    	
    	self.hh0 = [0,1,1,0,0,1,1,1,0,1,0,0,0,1,0,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,1]
        self.hh1 = [1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,1,1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,1]
        self.hh2 = [1,0,0,1,1,0,0,0,1,0,1,1,1,0,1,0,1,1,0,1,1,1,0,0,1,1,1,1,1,1,1,0]
        self.hh3 = [0,0,0,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,0]
        self.hh4 = [1,1,0,0,0,0,1,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0]
        
        self.hh0binary = "".join(map(str, self.hh0))
        self.hh1binary = "".join(map(str, self.hh1))
        self.hh2binary = "".join(map(str, self.hh2))
        self.hh3binary = "".join(map(str, self.hh3))
        self.hh4binary = "".join(map(str, self.hh4))
        
        self.hh0number = int(self.hh0binary, base=2)
        self.hh1number = int(self.hh1binary, base=2)
        self.hh2number = int(self.hh2binary, base=2)
        self.hh3number = int(self.hh3binary, base=2)
        self.hh4number = int(self.hh4binary, base=2)
        
        self.hash0num = self.hh0number + self.anumber
        self.hash1num = self.hh1number + self.bnumber
        self.hash2num = self.hh2number + self.cnumber
        self.hash3num = self.hh3number + self.dnumber
        self.hash4num = self.hh4number + self.enumber
        
        self.hash0bin = "{0:b}".format(self.hash0num)
        self.hash0list = list(map(int, self.hash0bin))
        while len(self.hash0list) > 32:
    	    del self.hash0list[0]
        self.hash1bin = "{0:b}".format(self.hash1num)
        self.hash1list = list(map(int, self.hash1bin))
        while len(self.hash1list) > 32:
    	    del self.hash1list[0]
        self.hash2bin = "{0:b}".format(self.hash2num)
        self.hash2list = list(map(int, self.hash2bin))
        while len(self.hash2list) > 32:
    	    del self.hash2list[0]
        self.hash3bin = "{0:b}".format(self.hash3num)
        self.hash3list = list(map(int, self.hash3bin))
        while len(self.hash3list) > 32:
    	    del self.hash3list[0]
        self.hash4bin = "{0:b}".format(self.hash4num)
        self.hash4list = list(map(int, self.hash4bin))
        while len(self.hash4list) > 32:
    	    del self.hash4list[0]
        
        print self.hash0list
        print self.hash1list
        print self.hash2list
        print self.hash3list
        print self.hash4list
        print type(self.hash4list)
        
        self.hhh0binary = "".join(map(str, self.hash0list))
        self.hhh1binary = "".join(map(str, self.hash1list))
        self.hhh2binary = "".join(map(str, self.hash2list))
        self.hhh3binary = "".join(map(str, self.hash3list))
        self.hhh4binary = "".join(map(str, self.hash4list))
        
        self.hhh0number = int(self.hhh0binary, base=2)
        self.hhh1number = int(self.hhh1binary, base=2)
        self.hhh2number = int(self.hhh2binary, base=2)
        self.hhh3number = int(self.hhh3binary, base=2)
        self.hhh4number = int(self.hhh4binary, base=2)
        
        print self.hhh0number
        
        self.hex0 = hex(self.hhh0number).lstrip("0x")
        print self.hex0
        self.hex1 = hex(self.hhh1number).lstrip("0x")
        print self.hex1
        self.hex2 = hex(self.hhh2number).lstrip("0x")
        print self.hex2
        self.hex3 = hex(self.hhh3number).lstrip("0x")
        print self.hex3
        self.hex4 = hex(self.hhh4number).lstrip("0x")
        print self.hex4
        print type(self.hex4)
        
        self.hash = self.hex0 + self.hex1 + self.hex2 + self.hex3 + self.hex4
        
        print self.hash
        print len(self.hash)
	
        
print  
        


      
   
          
        
al=shuffle()
al.show()
#al.function1()
al.show()
al.iter1()
al.hash()




