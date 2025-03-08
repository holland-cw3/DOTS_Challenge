import pandas as pd
from datetime import datetime, timedelta

def permFilter(date, time, lots, permissions):

    print("Day of the week?: ", date.weekday())

    permissions.append('Everyone')

    lots = set(lots)

    df_perms = pd.read_csv('InfoChallenge Dataset_ DOTS - Lots & Permissions.csv')
    
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

    # use a set to store the allowed lots
    allowed_lots = set([])

    # use a set to store the lots that can't be used
    restricted_lots = set([])

    # traverse the lots in the csv file, this is every lot
    # check the end boolean section of csv, to check if permission allow the lot
    for index, row in df_perms.iterrows():

        # check if one of the lot permissions is allowed for this lot
        allowedToPark = False

        blockedFromLot = False

        if row['Permits Type (Category)'] == 'Metered Parking':
            allowedToPark = True

        # save lot times
        start_time = row['Start Time - Daily']
        end_time = row['End Time - Daily']
        # check when lot is enforced
        if row['Enforcement Days'] == 'Weekdays':
            # if lot is enforced on weekdays and its inside the rule time check if parking is allowed
            if date.weekday() < 5 and is_time_inside_interval(time, start_time, end_time):
                for perm in permissions:
                    if row[perm] == 1.0:
                        allowed_lots.add(row['Parking Lot / Zone Name'])
                        if (row['Parking Lot / Zone Name'] in restricted_lots):
                            restricted_lots.remove(row['Parking Lot / Zone Name'])
                    else:
                        if (not row['Parking Lot / Zone Name'] in allowed_lots):
                            restricted_lots.add(row['Parking Lot / Zone Name'])
            elif row['Posted Restrictions'] == "Unrestricted after 4PM":
                allowedToPark = True
        elif row['Enforcement Days'] == 'Weekends':
            # if lot is enforced on weekends and its inside the rule time check if parking is allowed
            if date.weekday() >= 5 and is_time_inside_interval(time, start_time, end_time):
                for perm in permissions:
                    if row[perm] == 1.0:
                        allowed_lots.add(row['Parking Lot / Zone Name'])
                        if (row['Parking Lot / Zone Name'] in restricted_lots):
                            restricted_lots.remove(row['Parking Lot / Zone Name'])
                    else:
                        if (not row['Parking Lot / Zone Name'] in allowed_lots):
                            restricted_lots.add(row['Parking Lot / Zone Name'])
        else:
            # rule always applys
            for perm in permissions:
                if row[perm] == 1.0:
                    allowed_lots.add(row['Parking Lot / Zone Name'])
                    if (row['Parking Lot / Zone Name'] in restricted_lots):
                        restricted_lots.remove(row['Parking Lot / Zone Name'])
                else:
                    if (not row['Parking Lot / Zone Name'] in allowed_lots):
                        restricted_lots.add(row['Parking Lot / Zone Name'])

    if date.weekday() >= 5 or not is_time_inside_interval(time, "7:00:01", "15:59:59"):
        return lots - restricted_lots
    else:
        return allowed_lots
