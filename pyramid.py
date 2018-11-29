#! /usr/bin/python3.6

""" A program to figure out how often they would need to cut & lay a block
during the contruction of the Great Pyramid. """
# It took 20 years to build with 2,300,000 blocks

#sec_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365.25
blocks = 2300000


min_in_year = (minutes_in_hour * hours_in_day * days_in_year)
total_secs = min_in_year * 20
total_time = blocks / total_secs
time_it_takes = "It takes {} minutes to cut & lay one block to build the Great Pyramid."

min_in_year = (minutes_in_hour * hours_in_day * days_in_year
total_secs = min_in_year * 20
total_time = blocks / total_secs
time_it_takes = "It takes {} seconds to cut & lay one block to build the Great Pyramid.
print(time_it_takes.format(total_time))

