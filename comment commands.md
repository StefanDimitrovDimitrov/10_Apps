#pandas

1.data = pandas.read_csv("name_file")
    - read csv file 
    
    1. data.head()
        - display first 5 row in a table
    
    2.data.shape
        - show size of the dataFrame (row, colm)

    3.data.column
        - show only name of the  column

    4.data.hist('name_column')
        - display histagram of how much we have of something

    5. data['name_column']
        - select column in series (data type)

    6. data[['name_col1', 'name_col2']]
        - select multiple colm in dataframe(data type)

    7. data.iloc[index]
        - select row (type Series)

    8. type(data.iloc[3])
        pandas.core.series.Series -type

    9.data.iloc[1:3]
        select multiple rows

    10.data[['name_col1']['name_col2]].iloc[1:3]
        select a few rol for 2 specific colm in DataFrame

    11.data['name_colm'].iloc[2]
        or
        data.at[2, 'name_colm']
        -select one sell

# Pandas Filtering base on conditions

    12. data[data['name_colm'] > 4]
       - select all rows whare the selected colum value is gr 4

    13. data[data['name_colm'] > 4]['same name colm']
        -select only the selected coum

    14. data[(data['name_colm'] > 4) & (data['name_colm2'] == 'Some String)]
        - Multiple conditions 
        
# Pandas Filtering base on time
    import datatime from datatime
    from pytz import utc

    data = pandas.read_csv('file.csv', parse_dates=['Timestamp'])


    15.data[(data['Timestamp'] >= datatime(2020, 7, 1, tzinfo=utc) & 
        (data['Timestamp'] <= datatime(20200, 12, 31, tzinfo=utc))]

    
# Turning Data into Information - this is analysis

    task: 1 - Average rating
    task: 2 - Average rating per course
    task: 3 - Average rating for particular period
    task: 4 - Average rating for period for course
    task: 5 - Average of uncommented ratings
    task: 6 - Average of commented ratings
    task: 7 - Number of uncommented ratings
    task: 8 - Number of commented ratings
    task: 9 - Number of comments containing words
    task: 9 - Average of comments containing words
    


    task 1: data['Rating].mean()
    task 2: data[data['Course Name'] == 'The name of course']['Rating].mean()
    task 3: data[(data['Timestamp'] >= datatime(2020, 7, 1, tzinfo=utc) &
            (data['Timestamp'] <= datatime(20200, 12, 31, tzinfo=utc))]['Rating].mean()
    task 4:data[(data['Timestamp'] >= datatime(2020, 7, 1, tzinfo=utc) &
            (data['Timestamp'] <= datatime(20200, 12, 31, tzinfo=utc))&
            (data['Course Name'] == 'The name of course')]['Rating].mean()
    task 5:data[data['Comment].isnull()]['Rating].mean()
    task 6:data[data['Comment].notnull()]['Rating].mean()
    task 7:data[data['Comment].isnull()]['Rating].count()
    task 8:data[data['Comment].notnull()]['Rating].count()
    task 9:data[data['Comment].str.contains('accent', na=False)]['Ratings'].count() - na=False - ignor NAN value 
    task 10:data[data['Comment].str.contains('accent', na=False)]['Ratings].mean() - na=False - ignor NAN value 


# Aggregating and Plotting Average Ratings by Day

    create new colm only with the specific Day
    Group by this new column

        data['Day] = data["Timestamp"].dt.date
        day_average=data.groupby(['Day]).mean()

    2. import matplotlib.pyplot as plt
        
        plt.figure(figsize = (25, 3))
        plt.plot(day_average.index, day_average['Rating'] )
        - create plot by day


    3. data['Week'] = data["TimeStamp"].dt.strftime('%Y-%U')
        week_average = data.groupby([Week]),mean()
        plt.figure(figsize = (25, 3))
        plt.plot(week_average.index, week_average['Rating'] )

        - rating average by week

    4. data['Month'] = data["TimeStamp"].dt.strftime('%Y-%m')
        month_average = data.groupby(['Month']).mean()
        plt.figure(figsize = (25, 3))
        plt.plot(month_average.index, month_average['Rating'] )

        - average raiting by month

    5. data['Month] = data["TimeStamp"].dt.strftime('%Y-%m')
        month_average_crs = data.groupby(['Month', 'Course Name'])['Rating"].mean().unstack()  - unstack something like pivot table
        
        month_average.crs.plot(figsize=(25,8))

        - average raiting by month and course

    6. What day are people the happiest?

        data['Weekday] = data['Timestamp'].dt.strftime('%A')
        data['Daynumber'] = data['Timestamp'].dt.strftime('%w')

        weekday_average = data.groupby(['Weekday','Daynumber']).mean()
        weekdy_average = weekday_average.sort_values('Daynumber')

        plt.figure(figsize=[15, 3])
        plt.plot(weekday_average.index.get_level_value[0], weekday_average['Rating])

