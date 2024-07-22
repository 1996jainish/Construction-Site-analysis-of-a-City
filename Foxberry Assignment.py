#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import libraries

import pandas as pd


# In[2]:


# importing data into python

md = pd.read_excel('Downloads/Master_Data Demo.xlsx', sheet_name='Master_Data')


# In[3]:


df = pd.DataFrame(md)
df


# In[4]:


# Standardize column names
df.rename(columns={
    'assessmentdate': 'Assessment_Date',
    'last payment amount': 'Last_Payment_Amount',
    'last payment date': 'Last_Payment_Date',
    'Current Bill': 'Current_Bill',
}, inplace=True)

# remove duplicates if any
df = df.drop_duplicates()


# In[5]:



# replace null with Others
df['Construction_Type'] = df['Construction_Type'].fillna('Other')

# proper case 
df['Construction_Type'] = df['Construction_Type'].str.title()

#replace not avaiable with इतर .
df['Use_Type'] = df['Use_Type'].replace('Not-Available', 'इतर')

df


# In[6]:


df.to_excel('Master_data.xlsx', index=False)


# In[7]:


pa = pd.read_excel('Downloads/Master_Data Demo.xlsx', sheet_name='Paid Amount')


# In[8]:


df = pd.DataFrame(pa)
df


# In[9]:


# Standardize column names
df.rename(columns={
    'paidamount': 'Paid_Amount',
    'modeofpayment': 'Mode_of_Payment'
}, inplace=True)

# remove duplicates if any
df = df.drop_duplicates()

df


# In[10]:


df.to_excel('Paid_Amount.xlsx', index=False)


# In[ ]:




