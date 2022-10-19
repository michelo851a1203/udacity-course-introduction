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

resultList:list[str] = []

for textItem in texts: 
    if textItem[0] not in resultList:
        resultList.append(textItem[0])
    if textItem[1] not in resultList:
        resultList.append(textItem[1])

for callItem in calls:
    if callItem[0] not in resultList:
        resultList.append(callItem[0])
    if callItem[1] not in resultList:
        resultList.append(callItem[1])


print("There are {count} different telephone numbers in the records.".format(
    count=len(resultList)
    ))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
