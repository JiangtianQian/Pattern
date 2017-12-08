#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 11:22:23 2017

@author: kaka
"""

import userId as a 

file = open("animal-welfare-6.txt")

lines = []

while 1:
    line = file.readline()
    if not line:
        break
    pass
    if line.find('\\') == -1:
        out = line[3:len(line) - 3]
        lines.append(out)

for s in lines:
    a.main(s)