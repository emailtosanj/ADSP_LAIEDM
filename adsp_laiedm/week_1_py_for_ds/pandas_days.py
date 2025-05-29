import pandas as pd

series = pd.Series([420, 380, 390], index=['day1', 'day2', 'day3'])
print(series[0])
print(series[:'day3'])

cal_data = pd.DataFrame({'day': ['day1', 'day2', 'day3', 'day4', 'day5'],
                         'calories': [450, 300, 345, 520, 600],
                         'duration_min': [30, 25, 29, 39, 48]})

print(cal_data[:2])

print(cal_data['calories'])

# sanj - python notes

# DataFrame loc method - label based retrieval
    #syntax df.loc(index, columns)
        #index - ':'
        #columns -  ['col1','col2', 'col3']

# how do I get the top 3 rows skipping first row of data frame having selective columns
    # dataframe.loc[row selection, column selection]
    # ss.loc[1:3,['CustomerID','location','gender']]



# to access the last 2 rows with steps / skipping 2 rows - so if the step value is 3 its exclusive
# len(ss)
# syntax df[::-STEP_NUM]
    # ss[::2]

# sanj
# accessing the rows in reverse and create a copy / clone of a existing dataframe
# w = store_data[::-2].copy()

# Pandas DataFrame uses element-wise operator '&', it DOES NOT use 'and'.
# always use data frame box bracket then '()' brackets for filtering, refer to syntax below
    # syntax --> df[(df['col'] > )]

# reference element-wise operator
# == # != # < # > # <= # >= # + # - # * # / # // # % # **
# example
    # w = w[(w['total_bill'] >= 80) & (w['total_bill'] <= 100)]

# DataFrame iloc method - index based retrieval
# dataframe.iloc[row selection, column selection]

# DataFrame
# CustomerID	location	gender	type	quantity	total_bill
# 0	CustID00	Chicago	M	Electronics	1	100
# 1	CustID01	Boston	M	Food&Beverages	3	75
# 2	CustID02	Seattle	F	Food&Beverages	4	125
# 3	CustID03	San Francisco	M	Medicine	2	50
# 4	CustID04	Austin	F	Beauty	1	80

#Get all records pertaining to F&B exception gender
    #ss.iloc[:,[0,1,3,4,5]]

# DataFrame create a new column
# CustomerID	location	gender	type	quantity	total_bill	rating
# 0	CustID00	Chicago	M	Electronics	1	100	2
# 1	CustID01	Boston	M	Food&Beverages	3	75	5
# 2	CustID02	Seattle	F	Food&Beverages	4	125	3
# 3	CustID03	San Francisco	M	Medicine	2	50	4
# 4	CustID04	Austin	F	Electronics	1	80	4

# Assign the rating based on the following criteria
# 50  to 70   : 5
# 70  to 80   : 4
# 80  to 100  : 3
# 100 to 120  : 2
# 120 to 140  : 1

# [From python 3.10 - switch case statement of java equivalent of match
# def assignRating(x):
#   match x:
#     case x if 50<=x<70:
#       return 5
#     case x if 70<=x<80:
#       return 4
#     case x if 80<=x<100:
#       return 3
#     case x if 100<=x<120:
#       return 2
#     case x if 120<=x<140:
#       return 1

    #w['rating'] = w['total_bill'].apply(lambda x: 5 if 50<=x<70 else 4 if 70<x<80 else 3 if 80<=x<100 else 2 if 100<=x<120 else 1 if 120<=x<140 else None)
    #w['rating'] = w['total_bill'].apply(lambda x: assignRating(x))

# 	CustomerID	location	gender	type	quantity	total_bill	rating
# 4	CustID04	Austin	F	Beauty	1	80	3
# 0	CustID00	Chicago	M	Electronics	1	100	2

# Dataframe drop column
#from data frame drop gender
#help(w.drop)
# w = w.drop('gender', axis=1)
#w = w.drop(labels='gender', axis='columns')
    # axis = 1 - is column
    # inplace=True - makes the change in the dataframe and does not need assignment
#w.drop('CustomerID',axis=1,inplace=True) #-


# resetting the index of data frame
#store_data_new.reset_index()


# We will examine 3 methods for combining dataframes
# concat
# join
# merge


