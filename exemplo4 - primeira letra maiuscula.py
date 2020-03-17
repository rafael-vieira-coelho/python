#!/bin/python3

import math
import os
import random
import re
import sys

'''
Sample Input
chris 123jones alan

Sample Output
Chris 123jones Alan 
'''
def solve(s):
	r = ''
	for w in s.split():
		if type(w[0]) != int:
			r += str(w[0].upper() + w[1:len(w)]) + ' '
			#r += str(w.title()) + ' '
		else:
			r += str(w) + ' '
	return r    

if __name__ == '__main__':
    s = input()
    print(solve(s))
