import pandas as pd

def specialFilter(date, lots):
    df_special_events = pd.read_csv('InfoChallenge Dataset_ DOTS - Special Events _ Construction.csv')

    df_special_events = df_special_events.drop(['Days Impacted'], axis = 1)

    df_special_events['Start Date'] = pd.to_datetime(df_special_events['Start Date'])
    df_special_events['End Date'] = pd.to_datetime(df_special_events['End Date'])

    df_special_events.loc[df_special_events['End Date'] < df_special_events['Start Date'], ['Start Date', 'End Date']] = \
        df_special_events.loc[df_special_events['End Date'] < df_special_events['Start Date'], ['End Date', 'Start Date']].values

    events_hashmap = {}
    for _, row in df_special_events.iterrows():
        date_range = (row['Start Date'], row['End Date'])
        event_details = row.drop(['Start Date', 'End Date']).to_dict()  
        events_hashmap[date_range] = event_details

    def special_event_and_cons_check (date):
        for range in events_hashmap.keys():
            start, end = range
            if start <= date <= end:
                return events_hashmap[range]
            else:
                return None


    target = special_event_and_cons_check(date)

    return list(filter(lambda x: x is not target['Affected Lot/Populations'], lots))