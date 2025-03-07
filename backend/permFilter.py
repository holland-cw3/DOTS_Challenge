import pandas as pd
from datetime import datetime, timedelta

# for testing
date = '3/7/2025'
time = '18:00'
permissions = ['Everyone']

date = pd.to_datetime(date)

lots = []
with open('backend/lots.txt', 'r') as file:
    lines = file.read().splitlines() 
    lots.extend(lines)
# end testing data

def permFilter(date, time, lots, permissions):

    print("Day of the week?: ", date.weekday())

    if (len(permissions) == 0):
        permissions.add('Everyone')

    df_perms = pd.read_csv('backend/InfoChallenge Dataset_ DOTS - Lots & Permissions.csv')
    
    # function to determine if time is outside of checked inerval
    def is_time_inside_interval(time_str, start_time_str, end_time_str):
        if (start_time == "00:00:00" == end_time_str):
            return True

        # Convert strings to time objects
        time_obj = datetime.strptime(time_str, "%H:%M").time()
        start_time_obj = datetime.strptime(start_time_str, "%H:%M:%S").time()
        end_time_obj = datetime.strptime(end_time_str, "%H:%M:%S").time()

        if end_time_obj < start_time_obj:
            end_time_obj = (datetime.strptime(end_time_str, "%H:%M:%S") + timedelta(days=1)).time()

        # Check if time is outside the interval
        return time_obj >= start_time_obj and time_obj <= end_time_obj

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

            if row['Permits Type (Category)'] == 'Metered Parking':
                allowedToPark = True

            # save lot times
            start_time = row['Start Time - Daily']
            end_time = row['End Time - Daily']
            # check when lot is enforced
            if row['Enforcement Days'] == 'Weekdays':
                # if lot is enforced on weekdays and its inside the rule time check if parking is allowed
                if date.weekday() < 5 and is_time_inside_interval(time, start_time, end_time):
                    if row[perm] == 1.0:
                        allowedToPark = True
            elif row['Enforcement Days'] == 'Weekends':
                # if lot is enforced on weekends and its inside the rule time check if parking is allowed
                if date.weekday() >= 5 and is_time_inside_interval(time, start_time, end_time):
                    if row[perm] == 1.0:
                        allowedToPark = True
            else:
                # rule always applys
                if row[perm] == 1.0:
                    allowedToPark = True


        # if permissions are valid for this lot, add it to allowed
        if (allowedToPark):
            allowed_lots.add(row['Parking Lot / Zone Name'])
    
    return allowed_lots

final_lots = permFilter(date, time, lots, permissions)

print(len(final_lots))

for lot in final_lots:
    print(lot)