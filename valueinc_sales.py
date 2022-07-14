# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#libraries
import pandas as pd

#import data
data = pd.read_csv('transaction.csv', sep=';')

#display variables' name, count N & type (int, float etc.)
data.info()

#define variables
CostPerItem = data['CostPerItem']
SellingPricePerItem = data['SellingPricePerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']

#calculations
CostPerTransation = CostPerItem * NumberOfItemsPurchased

#add a new column to the dataframe
data['CostPerTransaction'] = CostPerTransation
data['SalesPerTransaction'] = SellingPricePerItem * NumberOfItemsPurchased
data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']
data['Markup'] = data['ProfitPerTransaction']/data['CostPerTransaction']

#round values in the "Markup" column to 2 decimals
data['Markup'] = round(data['Markup'],2)

#change columns' data type
day = data['Day'].astype(str)
month = data['Month'].astype(str)
year = data['Year'].astype(str)

#combine data fields
data['Date'] = day + '-' + month + '-' + year

#use iloc to view specific columns/rows
data.iloc[0] #row with index 0
data.iloc[0:3] #first 3 rows
data.iloc[-5:] #last 5 rows
data.iloc[:,2] #all rows on the column with index 2

#split "ClientKeywords" field into 3 separate columns
split_col = data['ClientKeywords'].str.split(',', expand = True)

#create new columns for the previously split field
data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#replace "][" in the newly split values
data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#transform "ItemDescription" field values from capital case to lower case
data['ItemDescription'] = data['ItemDescription'].str.lower() 

#merge existing dataset with a new dataset
#bring in the new dataset
seasons = pd.read_csv('value_inc_seasons.csv', sep=';') 
#merge files
data = pd.merge(data, seasons, on = 'Month')

#drop columns (axis = 1 means that you drop a column; axis = 0 would mean that you drop a row)
#drop "Day", "Month", "Year" columns 
data = data.drop(['Day','Month','Year'], axis = 1)
#drop "ClientKeywords" column
data = data.drop('ClientKeywords', axis = 1)

#export cleaned dataset into CSV (index = False means that you will not import the index column from your dataset into the new csv file)
data.to_csv('ValueInc_Cleaned.csv', index = False)
