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


# class PhoneClass:
#     def __init__(self, name: str, duration: int):
#         self.name = name
#         self.duration = duration
#
# resultList:list[PhoneClass] = []
#
# sendingTelephoneList = list(map(lambda sending: PhoneClass(sending[0], int(sending[3])), calls))
# receiveTelephoneList = list(map(lambda receiving: PhoneClass(receiving[1], int(receiving[3])), calls))
# allPhoneList = sendingTelephoneList + receiveTelephoneList
resultObject = {}

for item in calls:
    if item[0] in resultObject.keys():
        resultObject[item[0]] += int(item[3])
    else:
        resultObject[item[0]] = int(item[3])

    if item[1] in resultObject.keys():
        resultObject[item[1]] += int(item[3])
    else:
        resultObject[item[1]] = int(item[3])

(resultKey, resultValue) = "", 0
for dictionayKey in resultObject.keys():
    if resultObject[dictionayKey] > resultValue:
        (resultKey, resultValue) = (dictionayKey,resultObject[dictionayKey])

print("{telePhoneName} spent the longest time, {totalTime} seconds, on the phone during September 2016.".format(
    telePhoneName=resultKey,
    totalTime=resultValue,
    ))

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

