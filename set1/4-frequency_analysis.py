# Program that simply prints hex frequency of a given input

import sys
import operator

input = sys.argv[1]
lst = []
for i in range(0, len(input), 2):
	lst += [input[i:i+2]]

m = {}
for hex_val in lst:
	if hex_val not in m:
		m[hex_val] = 1
	else:
		m[hex_val] += 1

if (sorted(m.items(), key=operator.itemgetter(1))[-1][1] > 4):
	print input
	print sorted(m.items(), key=operator.itemgetter(1))[::-1]
