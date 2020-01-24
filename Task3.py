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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def tel_nums_called_by_people_in_bangalore(call_list):
    output = set()
    for item in call_list:
        num1, num2, call_time, call_duration = item
        if is_number_from_bangalore(num1):
            output.add(num2)
    return output


def fetch_area_code(tel_num):
    if is_fixed_line(tel_num):
        return tel_num[:5]
    if is_mobile_phone(tel_num):
        return tel_num[:4]
    return ""


def is_number_from_bangalore(tel_num):
    if tel_num[:5] == "(080)":
        return True
    return False


def is_fixed_line(tel_num):
    if tel_num[0] == "(" and tel_num[4] == ")":
        return True
    return False


def is_mobile_phone(tel_num):
    if tel_num[5] == " ":
        return True
    return False


def test():
    # print(tel_nums_called_by_people_in_bangalore(calls))
    assert is_mobile_phone('74064 33807') == True
    assert is_mobile_phone('(040)4 33807') == False
    assert is_fixed_line('74064 33807') == False
    assert is_fixed_line('(040)4 33807') == True
    pass


test()

area_codes = set()
tel_numbers = tel_nums_called_by_people_in_bangalore(calls)
for tel_num in tel_numbers:
    area_code = fetch_area_code(tel_num)
    if area_code != "":
        area_codes.add(area_code)


print("The numbers called by people in Bangalore have codes:")
for area_code in sorted(area_codes):
    print(area_code)


all_calls_from_bangalore = []
all_calls_to_fixed_line = []
for call in calls:
    num1, num2, time, duration = call
    if is_number_from_bangalore(num1):
        all_calls_from_bangalore.append(call)

        if is_number_from_bangalore(num2):
            all_calls_to_fixed_line.append(call)


percentage = format(len(all_calls_to_fixed_line)/len(all_calls_from_bangalore) * 100, '.2f')
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

