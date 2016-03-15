#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random
import time
N = 0
l = []
while (N<1000000):
	l.append(random.randint(1,10000000))
	N+=1

def fuck(fucksort):
	start = time.time()
	fucksort.sort()
	end = time.time()
	return end-start
print fuck(l)
