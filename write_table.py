#!/usr/bin/env python3
"""
An minimal emulation of write.table that can be used for list of lists. 
"""

import csv

def write_table(x, file, sep = " ", col_names = None):
    with open(file, 'w', newline = '') as tabfile:
        tab = csv.writer(tabfile,
                         delimiter = sep,
                         quotechar = '"',
                         quoting = csv.QUOTE_NONNUMERIC
        )
        if col_names:
            tab.writerow(col_names)
        for row in range(len(x)):
            tab.writerow(x[row])


def __test():
    a = [[1,2,'c'], [2,3,'b'], [3,4,'a']]
    write_table(x = a, sep = "\t",
                file = '/tmp/write_table_test.tab',
                col_names = ['x', 'y', 'z'])
    
if __name__ == '__main__':
    __test()

