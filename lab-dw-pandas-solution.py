#!/usr/bin/env python
# coding: utf-8

# # Lab | Pandas

# Objective: practice how to use the pandas library in Python for data analysis and manipulation.

# In this lab, we will be working with the customer data from an insurance company, which can be found in the CSV file located at the following link: https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv
# 
# The data includes information such as customer ID, state, gender, education, income, and other variables that can be used to perform various analyses.
# 
# Throughout the lab, we will be using the pandas library in Python to manipulate and analyze the data. Pandas is a powerful library that provides various data manipulation and analysis tools, including the ability to load and manipulate data from a variety of sources, including CSV files.

# ## Challenge 1: Understanding the data
# 
# In this challenge, you will use pandas to explore a given dataset. Your task is to gain a deep understanding of the data by analyzing its characteristics, dimensions, and statistical properties.

# - Identify the dimensions of the dataset by determining the number of rows and columns it contains.
# - Determine the data types of each column and evaluate whether they are appropriate for the nature of the variable. You should also provide suggestions for fixing any incorrect data types.
# - Identify the number of unique values for each column and determine which columns appear to be categorical. You should also describe the unique values of each categorical column and the range of values for numerical columns, and give your insights.
# - Compute summary statistics such as mean, median, mode, standard deviation, and quartiles to understand the central tendency and distribution of the data for numerical columns. You should also provide your conclusions based on these summary statistics.
# - Compute summary statistics for categorical columns and providing your conclusions based on these statistics.

# In[ ]:


# Your code here

import pandas as pd

# Read the dataset using pandas
df = pd.read_csv('https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv')
df.head()


# In[ ]:


# Note that students are not required to do this in this lab, we will do it in order to do cleaner code

# Standardize the column names
df.columns = df.columns.str.lower().str.replace(" ", "_")


# Rename columns for clarity
df = df.rename(columns={
    "st": "state"
})

# Print the resulting DataFrame
df.head()


# In[ ]:


# Check the number of rows and columns in the dataset
print("Number of rows: ", df.shape[0])
print("Number of columns: ", df.shape[1])


# In[ ]:


# Explore the data types of each column in the dataset
print(df.dtypes)


# In[ ]:


# Examine the unique values of categorical columns and the range of values for numerical columns
for col in df.columns:
    if df[col].dtype == 'object':
        print(col)
        print(df[col].nunique())
        print(df[col].unique())
    else:
        print(col)
        print(df[col].nunique())
        print(df[col].min(), df[col].max())


# In[ ]:


# Compute summary statistics of the dataset such as mean, median, mode, standard deviation, and quartiles to understand the central tendency and distribution of the data
print(df.describe(include='number'))


# In[ ]:


print(df.describe(include='object'))


# ## Challenge 2: analyzing the data

# ### Exercise 1

# The marketing team wants to know the top 5 less common customer locations. Create a pandas Series object that contains the customer locations and their frequencies, and then retrieve the top 5 less common locations in ascending order.

# In[ ]:


# Your code here

# Create a Series with the customer locations and their frequencies
locations = df['state'].value_counts()

# Retrieve the top 5 most common locations
top_locations = locations.tail(5).sort_values()

print(top_locations)


# ### Exercise 2
# 

# Your goal is to identify customers with a high policy claim amount.
# 
# Instructions:
# 
# - Review again the statistics for total claim amount to gain an understanding of the data.
# - To identify potential areas for improving customer retention and profitability, we want to focus on customers with a high policy claim amount. Consider customers with a high policy claim amount to be those in the top 25% of the total claim amount. Create a pandas DataFrame object that contains information about customers with a policy claim amount greater than the 75th percentile.
# - Use DataFrame methods to calculate summary statistics about the high policy claim amount data. 

# *Note: When analyzing data, we often want to focus on certain groups of values to gain insights. Percentiles are a useful tool to help us define these groups. A percentile is a measure that tells us what percentage of values in a dataset are below a certain value. For example, the 75th percentile represents the value below which 75% of the data falls. Similarly, the 25th percentile represents the value below which 25% of the data falls. When we talk about the top 25%, we are referring to the values that fall above the 75th percentile, which represent the top quarter of the data. On the other hand, when we talk about the bottom 25%, we are referring to the values that fall below the 25th percentile, which represent the bottom quarter of the data. By focusing on these groups, we can identify patterns and trends that may be useful for making decisions and taking action.*
# 
# *Hint: look for a method that gives you the percentile or quantile 0.75 and 0.25 for a Pandas Series.*

# In[ ]:


# Your code here
# Look at statistics for total claim amount and customer lifetime value
print("Total Claim Amount Stats:\n", df["total_claim_amount"].describe())
print("\nIncome Stats:\n", df["income"].describe())


# In[ ]:


# Define threshold values for high claim amount and low customer lifetime value
high_claim_amount = df["total_claim_amount"].quantile(0.75)

# Filter the data to identify customers with high claim amount 
df_high = df[(df["total_claim_amount"] > high_claim_amount)]

# Calculate summary statistics for the filtered data
print("\nSummary Statistics for High Claim Amount and Low Income Customers:")
print(df_high[["total_claim_amount"]].describe())


# ### Exercise 3
# 
# The sales team wants to know the total number of policies sold for each type of policy. Create a pandas Series object that contains the policy types and their total number of policies sold, and then retrieve the policy type with the highest number of policies sold.

# *Hint:*
# - *Using value_counts() method simplifies this analysis.*
# - *Futhermore, there is a method that returns the index of the maximum value in a column or row.*
# 

# In[ ]:


# Your code here

# Create a pandas Series object with the policy types and their total number of policies sold
policy_counts = df["policy_type"].value_counts()

# Retrieve the policy type with the highest number of policies sold
top_policy_type = policy_counts.idxmax()

print(f"The policy type with the highest number of policies sold is {top_policy_type}")


# ### Exercise 4
# 
# The sales team wants to know if customers with Personal Auto have a income than those with Corporate Auto. How does the average income compare between the two policy types?

# - Use loc to create two dataframes: one containing only Personal Auto policies and one containing only Corporate Auto policies.
# - Calculate the average income for each policy.
# - Print the results.

# In[ ]:


# Your code here
# Use loc to select rows with policy type 'Personal Auto' and 'Corporate Auto'
personal_auto_df = df.loc[df['policy_type'] == 'Personal Auto']
corporate_auto_df = df.loc[df['policy_type'] == 'Corporate Auto']


# In[ ]:


# Calculate the mean for each policy type
personal_auto_avg_clv = personal_auto_df['income'].mean()
corporate_auto_avg_clv = corporate_auto_df['income'].mean()

print("Average income for Personal Auto policies:", personal_auto_avg_clv)
print("Average income for Corporate Auto policies:", corporate_auto_avg_clv)

