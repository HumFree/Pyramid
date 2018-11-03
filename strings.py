#! /usr/bin/python3.6

#x = "Happy Birthday!"
#upper = x.upper()
#lower = x.lower()
#print(upper,lower)

""" A program to figure out how often they would need to lay a block
during the contruction of the great pyramid. """
# It took 20 years to build with 2,300,000 blocks
# find the seconds in a year multiplied by 20
#and divide it by 2,300,000

sec_in_minute = 60
minutes_in_hour = 60
hours_in_day = 24
days_in_year = 365
blocks = 2300000
sec_in_year = sec_in_minute * minutes_in_hour * hours_in_day * days_in_year
total_secs = sec_in_year * 20
total_time = total_secs / blocks / 60
total_time = round(total_time)
time_it_takes = "It takes {} minutes to cut & lay one block to build the Great Pyramid."
print(time_it_takes.format(total_time))
