"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

print(calls[0])

# resultList = []
totalResultCount = 0

matchRegx = "^" + re.escape("(") + "080" + re.escape(")")

for callItem in calls:
    if re.match(r"^(7|8|9).*?\s.*?$", callItem[0]) != None and re.match(matchRegx, callItem[1]):
        totalResultCount += 1
        # resultList.append(callItem)

print("The numbers called by people in Bangalore have codes: {count}".format(
    count=totalResultCount
    ))

# anotherList = []

totalAnother = 0

for callItem in calls:
    if re.match(matchRegx, callItem[0]) != None or re.match(matchRegx, callItem[1]) != None:
        totalAnother += 1
        # anotherList.append(callItem)

resultPercent = (totalAnother / len(calls)) * 100
# resultPercent = (len(anotherList) / len(calls)) * 100

print("{percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    percent=resultPercent
    ))


"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
