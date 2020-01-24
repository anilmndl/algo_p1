"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def get_numbers_who_texted(text_list):
    text_set = set()
    for item in text_list:
        text_set.add(item[0])
    return text_set


def get_numbers_who_called(call_list):
    call_set = set()
    for item in call_list:
        call_set.add(item[0])
    return call_set


those_who_texted = get_numbers_who_texted(texts)
those_who_called = get_numbers_who_called(calls)
tele_marketers = set()

for tel_num in those_who_called:
    if tel_num not in those_who_texted:
        tele_marketers.add(tel_num)


for tel_num in sorted(tele_marketers):
    print(tel_num)

