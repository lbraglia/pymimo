#!/usr/bin/env python3
"""
A simple Python class to handle a list of pages (generally speaking,
integers) specified in (eg) `120,123-127` format.

Input value for the costructor is a string(s), stored/returned value is a
uniqued, sorted, list of integers; "public" methods are:
- `get`
- `set`

"""

# TODO
# allow multiple parameter input eg PagesList('2001', '2004-2007')


import re

class PagesList():
    """Class to handle a list of pages specified in 120,123-127 format."""
    def __init__(self, x):
        self.set(x)
    def get(self):
        return(self.__value)
    def set(self, x):
        self.__value = self.__preprocess(x)
    def __preprocess(self, x):
        # clean: keep only digits, '-' and ','
        x = re.sub(r'[^\d\-\,]', '', x)
        # split by commas
        x = x.split(",")
        # change ranges to proper
        expanded = []
        single_page_re = re.compile("^\d+$")
        pages_range_re = re.compile("^(\d+)-(\d+)$")
        for i in range(len(x)):
            # Check if the single element match one of the regular expression
            single_page = single_page_re.match(x[i])
            pages_range =  pages_range_re.match(x[i])
            if single_page:
                # A) One single page: append it to results
                expanded.append(x[i])
            elif pages_range:
                # B) Pages range: append a list of (expanded) pages to results
                first = int(pages_range.group(1))
                second = int(pages_range.group(2))
                # step is 1 if first is less than or equal to second or -1
                # otherwise 
                step = 1 * int(first <= second)  - 1 * int(first > second)
                if step == 1:
                    second += 1
                elif step == -1:
                    second -= 1
                else:
                    # do nothing (ignore if they don't match)
                    pass
                expanded_range = [str(val) for \
                                  val in range(first, second, step)]
                expanded += expanded_range
        # coerce to integer expanded
        for i in range(len(expanded)):
            expanded[i] = int(expanded[i])
        # remove duplicated
        x = list(set(expanded))
        return(x)

def __test():
    a = PagesList("2012, 2011-2014")
    print(a.get())
    a.set('100, @@104-asdasd110  ')
    print(a.get())

if __name__ == '__main__':
    __test()
