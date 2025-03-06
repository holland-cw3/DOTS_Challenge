import pandas as pd


# Intersemesters, Breaks, Exams, & Winter Term	Any vehicle with OR without a current DOTS permit/CLPR may park in Lots 1, 2, 3, 4, 5, 6, 9, 11, and 16. Faculty/Staff Lots and meters are enforced as usual.
# Fall Semester	Parking Restrictions By Date; Posted Restrictions In Effect
# University-Observed Holiday	On most university-observed holidays, any vehicle may park in any lot on campus and meters are not enforced. On the university-observed Labor Day holiday, parking restrictions will be in place as if it were a Sunday (parkers should obey all posted lot signage and restrictions; meters are enforced). Additional restrictions apply for athletic and/or special events that occur during university-observed holidays.
# Spring Semester	Parking Restrictions By Date; Posted Restrictions In Effect
# Summer Term	Any vehicle with a current DOTS permit/CLPR may park in Lots 1, 2, 3, 4, 5, 6, 9, 11, and 16. Faculty/Staff Lots and meters are enforced as usual.


def semesterFilter(date, lots):
   
    df_dates = pd.read_csv('InfoChallenge Dataset_ DOTS - Dates.csv')
    df_dates = df_dates.drop(['Special Restrictions (Start)', 'Special Restrictions (End)'], axis = 1)
    df_dates['Date'] = pd.to_datetime(df_dates['Date'])
    df_dates['End Year'] = df_dates['Date'].dt.year
    week_ranges = df_dates.groupby(['Week Number', 'End Year']).agg(
        Start_Date=('Date', 'min'),
        End_Date=('Date', 'max')
    ).reset_index()
    df_dates = df_dates.drop(columns=['Date', 'Weekday']).drop_duplicates()
    df_dates = df_dates.merge(week_ranges, on='Week Number', how='right')
    df_dates['End Year'] = df_dates['End_Date'].dt.year
    df_dates = df_dates.drop(columns=[ 'Academic Year',  'Fiscal Year','Parking Restrictions - Simplified', 'Week Number', 'End Year_x', 'End Year_y'])
    df_dates = df_dates.drop_duplicates(subset=['Start_Date', 'End_Date'])


    term_dates = df_dates.groupby(["Parking Restrictions - Specific", 'End Year']).agg(
        Start_Date=('Start_Date', 'min'),
        End_Date=('End_Date', 'max')
    ).reset_index()


    term_dates = term_dates.sort_values(by='Start_Date').reset_index(drop=True)

    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Spring Study Days, Final Exams, and Commencement', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Fall Study Days, Final Exams, & Commencement', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Spring-Summer Intersemester', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Summer-Fall Intersemester', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Winter Term', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Winter Break; University-Observed Holiday', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Spring Break', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'
    term_dates.loc[term_dates['Parking Restrictions - Specific'] == 'Winter Break', 'Parking Restrictions - Specific'] = 'Intersemesters, Breaks, Exams, & Winter Term'



    events_hashmap = {}
    for _, row in term_dates.iterrows():
        date_range = (row['Start_Date'], row['End_Date'])
        event_details = row.drop(['Start_Date', 'End_Date']).to_dict()  
        events_hashmap[date_range] = event_details
        


    def sem_check (date):
        for range in events_hashmap.keys():
            start, end = range
            print('range', start, end)
            if start <= date <= end:
                return events_hashmap[range]
        
        return None

    target = sem_check(date)['Parking Restrictions - Specific']

    print(lots)

    potential_lots = ["1b","1c","1d","1e","1f","2a","2b","2f","3","4a","4b","4h","4k","4m","4n","6","8","9b","11b","16a","16b","16f"]
    potential_lots = [lot for lot in potential_lots if lot in lots]

    print('potential', potential_lots)


    if target == 'Intersemesters, Breaks, Exams, & Winter Term' :
        return (potential_lots, False) # Meaning no perm required
    elif target == 'Summer Term':
        return (potential_lots, True) # Perm required
    else:
        return (lots, True) # proceed to check for permissions