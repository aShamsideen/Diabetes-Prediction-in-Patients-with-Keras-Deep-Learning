#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load libraries 
from numpy import loadtxt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[18]:


# Load the dataset
dataset = loadtxt('pima-indians-diabetes.data.csv', delimiter=',')

# Split the dataset into input and output element
x = dataset[:, 0:8]
y = dataset[:,8]