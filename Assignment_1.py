#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# # Reading a dataset to python environment

# In[2]:


data=pd.read_excel( r'E:\blessy\ict\iris.xls')


# In[3]:


data#displaying the data set contents


# # Displaying the columns in a dataset

# In[4]:


data.columns


# # Calculating the mean of each columns

# In[5]:


data.mean(numeric_only=True)


# # Check for the null value present in a dataset 

# In[6]:


data.isna().sum()


# # Barchart visualization

# In[7]:


plt.bar(data['Classification'],data['PL'],color='Green')
plt.xticks(rotation=90)
plt.title('Classification of iris flower with petal length')
plt.xlabel('Classification')
plt.ylabel('Petal length(PL)')
plt.show()


# # Boxplot visualization

# In[8]:


plt.boxplot(data['PL'])
plt.show()


# # Histogram visualization

# In[9]:


plt.hist(data['PL'],color='pink',rwidth=0.9)
plt.title('Petal Length Distribution',fontsize=20)#to display title
plt.xlabel('Petal length')
plt.ylabel('Frequency')
plt.show()


# In[ ]:




