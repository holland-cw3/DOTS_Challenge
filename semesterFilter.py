import pandas as pd



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



    term_dates