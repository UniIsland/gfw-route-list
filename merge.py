#!/usr/bin/python

import sys,string,fileinput

r = dict()

for line in fileinput.input():
	addr = string.split(string.strip(line), '.')
	key = addr[0] + '.' + addr[1]
	if not key in r:
		r[key] = dict()

	if not addr[2] in r[key]:
		r[key][addr[2]] = []

	r[key][addr[2]].append(addr[3])

for key, val in r.items():
	if len(val) > 2:
		print key + '.0.0 255.255.0.0'
		continue

	for k, v in val.items():
		if len(v) > 1:
			print key + '.' + k + '.0 255.255.255.0'
			continue

		print key + '.' + k + '.' + v[0] + ' 255.255.255.255'

#print r
