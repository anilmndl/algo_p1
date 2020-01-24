"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

longest_index = 0
longest_duration = 0
for index, item in enumerate(calls):
    num1, num2, call_date, call_duration = item

    if int(call_duration) > longest_duration:
        longest_duration = int(call_duration)
        longest_index = index

call = calls[longest_index]
print("{} spent the longest time, {} seconds, on the phone during {}.".format(call[0], call[3], call[2]))
