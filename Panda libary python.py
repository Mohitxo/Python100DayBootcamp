# What is Pandas library in python ??? 
# Python data analysis using pandas is a great start to Exploratory Data Analysis (EDA) for a data scientist.
# Learn to create and analyze your data using python DataFrames and export/import it as csv and excel

# what is Pandas pandas is an open source data analysis liabry written in python it leverage teh power
# and speed tp numpy to make data analysis and preprocessing easy for data science it provides rich and highly robust data opereations

# pandas has two types of data Structure: 
# sereis - its a one dimensional array wtih indexes dataframe - its a tabular spreadsheet like Structure representing rows each of which contains one or more multiple columns
import numpy as np
import pandas as pd

dict1={
    " name":['Mohit','rohan','harry','ruchi','mehak'],
    "marks":[97,67,88,91,98],
    "city":['pune','delhi','mumbai','pune','jammu']
}


# data frame is used to framing the data in the row and column file format
df=pd.DataFrame(dict1)
print(df)

# output:
#     name  marks    city
# 0  Mohit     97    pune
# 1  rohan     67   delhi
# 2  harry     88  mumbai
# 3  ruchi     91    pune
# 4  mehak     98   jammu

#  too convert this file to csv format we use .to_csv code
df.to_csv('friends.csv')

# too convert this row column file format to csv we will use .to_csv but we at the same time 
# we dont want the indexing we will write
df.to_csv('friends_index_False.csv',index=False)

# head() returns the first n rows(observe the index values)
df.head(2)
# output:
# index 	name	marks	 city
# 0	     Mohit	  97	 pune
# 1	     rohan	  67	 delhi

#  tail() returns the last n rows(observe the index values)
 df.tail(2)
#  output:
# name	marks	city
# 3	   ruchi	91	pune
# 4	   mehak	98	jammu

# Pandas describe() is used to view some basic statistical details like percentile, mean, std etc.
#  of a data frame or a series of numeric values
df.describe()
# output
# marks
# count 	5.000000
# mean	  88.200000
# std   	12.557866
# min	    67.000000
# 25%	    88.000000
# 50%	    91.000000
# 75%	    97.000000
# max	    98.000000

# reading a csv file through pandas libary importing the csv file from the computer
data_file=pd.read_csv('friends.csv')
print(data_file)
# output-
#    name    marks    city
# 0  Mohit     97    pune
# 1  rohan     67   delhi
# 2  harry     88  mumbai
# 3  ruchi     91    pune
# 4  mehak     98   jammu


# to display the data ( name column only)
data_file['name']
# output
# 0    Mohit
# 1    rohan
# 2    harry
# 3    ruchi
# 4    mehak
# Name: name, dtype: object

# to change the sno number we will use filename.index method
data_file.index=['first','second','third','forth','fivth']
print(data_file)

# output -
#          name  marks    city
# first   Mohit     97    pune
# second  rohan     67   delhi
# third   harry     88  mumbai
# forth   ruchi     91    pune
# fivth   mehak     98   jammu

# we are making a series by using a pandas libary 
ser=pd.Series(np.random.rand(35))
type(ser)
print(ser)

# output
# 0     0.974084
# 1     0.941065
# 2     0.474382
# 3     0.788680
# 4     0.495080
# 5     0.238494
# 6     0.737306
# 7     0.716380
# 8     0.541169
# 9     0.095061
# 10    0.000207
# 11    0.904384
# 12    0.607762
# 13    0.865155
# 14    0.388409
# 15    0.902560
# 16    0.611202
# 17    0.499784
# 18    0.005463
# 19    0.381931
# 20    0.758540
# 21    0.581018
# 22    0.468413
# 23    0.035592
# 24    0.578401
# 25    0.892775
# 26    0.271024
# 27    0.167414
# 28    0.330264
# 29    0.958243
# 30    0.041315
# 31    0.645613
# 32    0.703093
# 33    0.922253
# 34    0.273207
# dtype: float64


newdf = pd.DataFrame(np.random.rand(100,5),index=np.arange(100))
print(newdf)
# too print type of newdf
print(type(newdf))
# too print describe of newdf
print(newdf.describe())
print(newdf.dtypes)

# output
#            0         1         2         3         4
# 0   0.159901  0.272504  0.137663  0.752951  0.174245
# 1   0.211110  0.780082  0.010068  0.440921  0.266512
# 2   0.973556  0.667765  0.126085  0.711750  0.111196
# 3   0.019998  0.402879  0.829483  0.248259  0.976690
# 4   0.292506  0.914388  0.767520  0.815775  0.453795
# ..       ...       ...       ...       ...       ...
# 95  0.397284  0.975548  0.680286  0.835782  0.625389
# 96  0.906153  0.351608  0.513043  0.563338  0.759882
# 97  0.850705  0.573111  0.263297  0.601646  0.615038
# 98  0.994734  0.752209  0.846399  0.488390  0.127836
# 99  0.492217  0.258156  0.243535  0.385576  0.956248

# [100 rows x 5 columns]
# <class 'pandas.core.frame.DataFrame'>
#                 0           1           2           3           4
# count  100.000000  100.000000  100.000000  100.000000  100.000000
# mean     0.531797    0.535897    0.531523    0.509822    0.496028
# std      0.304216    0.290012    0.275369    0.289139    0.287269
# min      0.009462    0.012446    0.010068    0.004497    0.001834
# 25%      0.267514    0.298288    0.327812    0.264603    0.236683
# 50%      0.548241    0.552969    0.520480    0.510585    0.507800
# 75%      0.813257    0.808142    0.762739    0.741460    0.715881
# max      0.997927    0.999408    0.986502    0.993637    0.976690
# 0    float64
# 1    float64
# 2    float64
# 3    float64
# 4    float64
# dtype: object

newdf.head(5)
# output
# 	0	          1	        2	           3        	4
# 0	0.159901	0.272504	0.137663	0.752951	0.174245
# 1	0.211110	0.780082	0.010068	0.440921	0.266512
# 2	0.973556	0.667765	0.126085	0.711750	0.111196
# 3	0.019998	0.402879	0.829483	0.248259	0.976690
# 4	0.292506	0.914388	0.767520	0.815775	0.453795

newdf.tail(5)
# output  
# 0	                 1	       2	       3          4
# 95	0.397284	0.975548	0.680286	0.835782	0.625389
# 96	0.906153	0.351608	0.513043	0.563338	0.759882
# 97	0.850705	0.573111	0.263297	0.601646	0.615038
# 98	0.994734	0.752209	0.846399	0.488390	0.127836
# 99	0.492217	0.258156	0.243535	0.385576	0.956248

newdf.index
# output
# Int64Index([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
#             17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
#             34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#             51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
#             68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
#             85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99],
#            dtype='int64')

newdf.columns
# output
# RangeIndex(start=0, stop=5, step=1)


# too change an element we use this code
newdf[0][0]="Mohit Panjikar"
newdf[0][1]="Moni Panjikar"
newdf.head(5)

# output
# 0	    1               	2           	3	                4
# 0	  Mohit Panjikar	Moni Panjikar	0.137663	0.752951	0.174245
# 1	  Moni Panjikar	0.780082	0.010068	0.440921	0.266512
# 2	  0.973556	0.667765	0.126085	0.711750	0.111196
# 3	  0.019998	0.402879	0.829483	0.248259	0.976690
# 4	  0.292506	0.914388	0.767520	0.815775	0.453795

# Too transpose the matrix we will use .T method
# rows become columns and columns will become rows
newdf.T











