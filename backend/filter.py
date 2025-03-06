import pandas as pd
from specialFilter import specialFilter

lots = []

date = '1/3/2023'
time = '03:00'
visitorType = 'Student'
permissions = []

date = pd.to_datetime(date)

with open('lots.txt', 'r') as file:
    lines = file.read().splitlines() 
    lots.extend(lines) 

print(lots)


# print(len(lots))
# print(len(specialFilter(date, lots)))
# print(specialFilter(date, lots))