## Construction Sites Analysis of a city.

## Below is the cleaning done in Python.


# Import libraries
import pandas as pd

# Importing data into python
md = pd.read_excel('Downloads/Master_Data Demo.xlsx', sheet_name='Master_Data')
df = pd.DataFrame(md)
# Standardize column names 
df.rename(columns={
 'assessmentdate': 'Assessment_Date',
 'last payment amount': 'Last_Payment_Amount',
 'last payment date': 'Last_Payment_Date',
 'Current Bill': 'Current_Bill',
}, inplace=True)

# Remove duplicates if any
df = df.drop_duplicates()

# Replace null with Others
df['Construction_Type'] = df['Construction_Type'].fillna('Other')
# proper case 
df['Construction_Type'] = df['Construction_Type'].str.title()
# replace not avaiable with इतर .
df['Use_Type'] = df['Use_Type'].replace('Not-Available', 'इतर')

# Import paid amount file
pa = pd.read_excel('Downloads/Master_Data Demo.xlsx', sheet_name='Paid Amount')
df = pd.DataFrame(pa)

# Standardize column names
df.rename(columns={
 'paidamount': 'Paid_Amount',
 'modeofpayment': 'Mode_of_Payment'
}, inplace=True)

# Remove duplicates if any
df = df.drop_duplicates()
df

# DOWNLOAD CLEAN FILE
df.to_excel('Master_data.xlsx', index=False)
df.to_excel('Paid_Amount.xlsx', index=False)


## Maain Page 
![page1](https://github.com/user-attachments/assets/0e8d7a44-7ab4-4c72-8ae4-26d2386264c4)

##Zone wise Analysis
![page2](https://github.com/user-attachments/assets/1926a6ee-1379-44d3-970a-68f539c7156b)

## Key Insights 
![page3](https://github.com/user-attachments/assets/2ee181ce-3732-4e35-9842-d4654c8e185c)

