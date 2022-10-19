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

firstOfText = texts[0]
print("First record of texts, {incomintNumber} texts {answeringNumber} at time {time}".format(
    incomintNumber=firstOfText[0],
    answeringNumber=firstOfText[1],
    time=firstOfText[2],
    ))

lastOfCalls = calls[len(calls) - 1]
print("Last record of calls, {incomingNumber} calls {answerNumber} at time {time}, lasting {during} seconds".format(
    incomingNumber=lastOfCalls[0],
    answerNumber=lastOfCalls[1],
    time=lastOfCalls[2],
    during=lastOfCalls[3],
    ))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

