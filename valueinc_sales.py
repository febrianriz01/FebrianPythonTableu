# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:53:18 2024

@author: Febrian
"""

import pandas as pd
# file_name = pd.read_csv('file.csv')  <--- format
#data = pd.read_csv('D:/Febrian/Udemy/transaction2.csv')
#D:\Febrian\Udemy\Python and Tableau The Complete Data Analytics Bootcamp!\Data
#D:/Febrian/Udemy/Python and Tableau The Complete Data Analytics Bootcamp!/Data
data = pd.read_csv('D:/Febrian/Udemy/transaction2.csv')
data = pd.read_csv('D:/Febrian/Udemy/transaction2.csv', sep=';')

#summary of the data
data.info()

#Playing around with variable
#var = {'name':'febrian','location':'Depok'}
var ={'apple','pear','banana'}
CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberOfItemsPurchased

#adding a new colom to dataframe
data['CostPerTransaction']=data['CostPerItem']*data['NumberOfItemsPurchased']
data['SalesPerTransaction']=data['SellingPricePerItem']*data['NumberOfItemsPurchased']

#ProfitperTransaction
data['ProfitperTransaction']=data['SalesPerTransaction']-data['CostPerTransaction']

#Markup =(Sales - Cost)/Cost

data['Markup']=(data['SalesPerTransaction']-data['CostPerTransaction'])-data['CostPerTransaction']

data['Markup']=(data['ProfitperTransaction'])-data['CostPerTransaction']

#Rounding marking
roundmarkup = round(data['Markup'],2)


data['Markup'] = round(data['Markup'],2 )


#combining data fields

my_name = 'febrian'+'rizkiono'

#my_date = data['Day']+data['Month']+data['Year']

#checking colums data type
print(data['Day'].dtype)


#change column type
day = data['Day'].astype(str)
print(day.dtype)

Year = data['Year'].astype(str)
print(Year.dtype)

my_date=day+'-'+data['Month']+'-'+Year

data['date']= my_date

#using iloc to view specific columns / rows
data.iloc[0] #view the row with index=0
data.iloc[0:3] #first 3 row
data.iloc[-5:] #last 5 row


data.head(5)  #bring in first 5 row
data.iloc[:,2]  #bring all rows on the 2nd column

data.iloc[4,2]  #bring it 4 row,2nd column

data.iloc[1,1]  #bring it 4 row,2nd column


#using split to split the ClientKeywords 
#new_var = column.str.split('sep' , expand= true)
split_col = data['ClientKeywords'].str.split(',' , expand = True)


#creating new columns for the split columns in client keyword

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LenghtofContract'] = split_col[2]


#using the replace function
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LenghtofContract']=data['LenghtofContract'].str.replace(']','')

#using the lowercase to change item to lowercase
data['ItemDescription']= data['ItemDescription'].str.lower()

#how to merge files

#bringing in a new dataset



season = pd.read_csv('D:/Febrian/Udemy/value_inc_seasons.csv', sep=';')

#merging files: merge_df = pd.merge(df_old, df_new, on = 'key)

data = pd.merge(data, season, on ='Month')

#dropping column
# df = df.drop('columnname', axis = 1)

data= data.drop('ClientKeywords', axis = 1)

data= data.drop('Day', axis = 1)

data= data.drop(['Year','Month'], axis = 1)

data.to_csv('ValueInc_Cleaned.csv')