#!/usr/bin/python
import math




def ricecod(x,m):
    c = int(math.ceil(math.log(m,2)))
    remin = x % m
    quo =int(math.floor(x / m))
    #print "quo is",quo
    #print "reminder",remin
    #print "c",c
    div = int(math.pow(2,c) - m)
    #print "div",div
    first = ""
    for i in range(quo):
	first = first + "1"
    #print first

    if (remin < div):
	b = c - 1
	a = "{0:0" + str(b) + "b}"
	#print "1",a.format(remin)
	bi = a.format(remin)
    else:
	b = c
	a = "{0:0" + str(b) + "b}"
	#print "2",a.format(remin+div)
	bi = a.format(remin+div)

    final = first + "0" +str(bi)
    print "final",final
    return final


def bwt(x):
    array = []
    newarr = ""
    for i in range(len(x)):
	#print x
	array.append(x)
	x = x[1:]+x[0]
	array.sort()
	if i == len(x)-1:
	    return array
		


rco = ricecod(18,16)
#print bwt(rco)
array = bwt(rco)

newarr = ""
for i in  array:
    newarr = newarr + i[-1:]

print newarr
