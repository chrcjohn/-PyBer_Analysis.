#!/usr/bin/env python
# coding: utf-8

# # Pyber Challenge

# ### 4.3 Loading and Reading CSV files

# In[15]:


# Add Matplotlib inline magic command
get_ipython().run_line_magic('matplotlib', 'inline')
# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd

# File to Load (Remember to change these)
city_data_to_load = "city_data.csv"
ride_data_to_load = "ride_data.csv"

# Read the City and Ride Data
city_data_df = pd.read_csv(city_data_to_load)
ride_data_df = pd.read_csv(ride_data_to_load)


# ### Merge the DataFrames

# In[ ]:


# Combine the data into a single dataset
pyber_data_df = pd.merge(ride_data_df, city_data_df, how="left", on=["city", "city"])

# Display the data table for preview
pyber_data_df.head()


# ## Deliverable 1: Get a Summary DataFrame 

# In[3]:


#  1. Get the total rides for each city type
type_rides_count = pyber_data_df.groupby(["type"]).count()["ride_id"]
type_rides_count


# In[4]:


# 2. Get the total drivers for each city type
type_drivers_count = city_data_df.groupby(["type"]).sum()["driver_count"]
type_drivers_count


# In[5]:


#  3. Get the total amount of fares for each city type
type_fares_count = pyber_data_df.groupby(["type"]).sum()["fare"]
type_fares_count


# In[6]:


#  4. Get the average fare per ride for each city type. 
type_avg_fare = pyber_data_df.groupby(["type"]).mean()["fare"]
type_avg_fare


# In[7]:


# 5. Get the average fare per driver for each city type. 
driver_avg_fare = type_fares_count / type_drivers_count
driver_avg_fare


# In[10]:


#  6. Create a PyBer summary DataFrame. 
pyber_summary_df=pd.DataFrame(
    { "Total Rides": type_rides_count,
      "Total Drivers": type_drivers_count,
      "Total Fares": type_fares_count,
      "Average Fare per Ride": type_avg_fare,
      "Average Fare per Driver": driver_avg_fare})

pyber_summary_df


# In[11]:


#  7. Cleaning up the DataFrame. Delete the index name
pyber_summary_df.index.name = None
pyber_summary_df


# In[9]:


#  8. Format the columns.
pyber_summary_df["Total Fares"] = pyber_summary_df["Total Fares"].map("${:,.2f}".format)
pyber_summary_df["Average Fare per Ride"] = pyber_summary_df["Average Fare per Ride"].map("${:,.2f}".format)
pyber_summary_df["Average Fare per Driver"] = pyber_summary_df["Average Fare per Driver"].map("${:,.2f}".format)

pyber_summary_df


# ## Deliverable 2.  Create a multiple line plot that shows the total weekly of the fares for each type of city.

# In[12]:


# 1. Read the merged DataFrame
pyber_data_df.head()


# In[13]:


# 2. Using groupby() to create a new DataFrame showing the sum of the fares 
#  for each date where the indices are the city type and date.
type_dates_count = pyber_data_df.groupby(["date", "type"]).sum()["fare"]
type_dates_count


# In[14]:


# 3. Reset the index on the DataFrame you created in #1. This is needed to use the 'pivot()' function.
# df = df.reset_index()
type_dates_count = type_dates_count.reset_index()

type_dates_count


# In[ ]:


# 4. Create a pivot table with the 'date' as the index, the columns ='type', and values='fare' 
# to get the total fares for each type of city by the date. 
pyber_pivot_table = pd.pivot_table(type_dates_count, values='fare', index = 'date', columns ='type')

pyber_pivot_table.head(10)


# In[ ]:


# 5. Create a new DataFrame from the pivot table DataFrame using loc on the given dates, '2019-01-01':'2019-04-29'.
loc_pyber_pivottable = pyber_pivot_table.loc['2019-01-01':'2019-04-29']
loc_pyber_pivottable.head(10)


# In[ ]:


# 6. Set the "date" index to datetime datatype. This is necessary to use the resample() method in Step 8.
# df.index = pd.to_datetime(df.index)
loc_pyber_pivottable.index = pd.to_datetime(loc_pyber_pivottable.index)
loc_pyber_pivottable.info()


# In[ ]:


# 7. Check that the datatype for the index is datetime using df.info()
loc_pyber_pivottable_res=loc_pyber_pivottable.resample('W').sum()

loc_pyber_pivottable_res.info()


# In[ ]:


# 8. Create a new DataFrame using the "resample()" function by week 'W' and get the sum of the fares for each week.
loc_pyber_pivottable_res.head(10)


# In[2]:


# 8. Using the object-oriented interface method, plot the resample DataFrame using the df.plot() function. 

from matplotlib import style
# Use the graph style fivethirtyeight.
style.use('fivethirtyeight')

loc_pyber_pivottable_res.plot(figsize=(20,10))
plt.ylabel("Fare($USD)")
plt.title("Total Fare by City Type")

# Save Figure
plt.savefig("analysis/PyBer_fare_summary.png")
plt.legend()


# In[ ]:





# In[ ]:




