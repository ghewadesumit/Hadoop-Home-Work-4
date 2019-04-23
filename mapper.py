#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
count = 0

# Traversing all the lines of the nyc.data
for line in sys.stdin:
        # Skipping the header line from the nyc.data
        if count == 0:
            count += 1
            continue
        # rstrip() function is used to strip \n from end of the line
        #splitting the data using ','
        # x holds the list created from the data created
        x = line.rstrip().split(',')
        # Traversing through the Vehicle type 1 to 5 
        for j in range(24,29):
            # If there is integer in any of the Vehicle type then don't consider the data
            try:
                x[j] = int(x[j])
            except:
                # If there is space in the data then don't consider
                try:
                    if x[j] == '':
                        continue
                    else:
                        # printing the data with count 1 for every time the data appears 
                        print '%s\t%s' % (x[j].upper(),1)
                except:
                        pass

        