#googled 1/27/1756 born mozart
#gives http://www.pythonchallenge.com/pc/return/mozart.html
#! /usr/bin/env python

import calendar

if __name__ == '__main__':
    years = []
    for year in range(1006, 2007, 10):
        if calendar.isleap(year) and calendar.weekday(year, 1, 1) == 3:
            years.append(year)
    print(years)
