import pandas as pd
from datetime import datetime

# for testing
date = '1/1/2024'
time = '03:00'
permissions = ['Lot 1']

date = pd.to_datetime(date)

lots = []
with open('backend/lots.txt', 'r') as file:
    lines = file.read().splitlines() 
    lots.extend(lines)
# end testing data

def permFilter(date, time, lots, permissions):

    if (len(permissions) == 0):
        permissions.add('No Permits')

    df_perms = pd.read_csv('backend/InfoChallenge Dataset_ DOTS - Lots & Permissions.csv')
    
    # function to determine if time is outside of checked inerval
    def is_time_outside_interval(time_str, start_time_str, end_time_str):
        # Convert strings to time objects
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        start_time_obj = datetime.strptime(start_time_str, "%H:%M:%S").time()
        end_time_obj = datetime.strptime(end_time_str, "%H:%M:%S").time()
        
        # Check if time is outside the interval
        return time_obj < start_time_obj or time_obj > end_time_obj

    # summer term start and end
    # can we make this dynamic?
    summer_start = datetime(2025, 5, 21)
    summer_end = datetime(2025, 8, 26)

    # If the users has permissions for any valid lot check if its summer
    # If it is summer return all lots
    if (len(permissions) > 0 and summer_start < date < summer_end):
        return set(lots)

    # use a set to store the allowed lots
    allowed_lots = set([])

    # check what lots are valid with no permissions
    # return them here

    # traverse the lots in the csv file, this is every lot
    # check the end boolean section of csv, to check if permission allow the lot
    for index, row in df_perms.iterrows():

        # check if one of the lot permissions is allowed for this lot
        allowedToPark = False
        for perm in permissions:
            # check if permission is allowed
            if row[perm] == 1.0:
                allowedToPark = True
            # check if lot is unrestricted
            if row['Enforcement Days'] != 'Always':
                # save lot times
                start_time = row['Start Time - Daily']
                end_time = row['End Time - Daily']
                # check when lot is enforced
                if row['Enforcement Days'] == 'Weekdays':
                    # if lot is enforced on weekdays and its a weekend or outisde the enforcement time, parking is allowed
                    if date.weekday() > 5 or (date.weekday() < 5 and is_time_outside_interval(time, start_time, end_time)):
                        allowedToPark = True
                else:
                    # if lot is enforced on weekends and its a weekday or outisde the enforcement time, parking is allowed
                    if date.weekday() < 5 or (date.weekday() > 5 and is_time_outside_interval(time, start_time, end_time)):
                        allowedToPark = True


        # if permissions are valid for this lot, add it to allowed
        if (allowedToPark):
            # check other requirements here
            allowed_lots.add(row['Parking Lot / Zone Name'])

            # check time and date restrictions
    
    return allowed_lots

final_lots = permFilter(date, time, lots, permissions)

print(len(final_lots))

for lot in final_lots:
    print(lot)