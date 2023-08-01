#!/usr/bin/env python
# coding: utf-8

# In[16]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from dataset import *


# In[17]:


# Define model and add layers
model = Sequential()
model.add(Dense(12, input_shape=(8,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[18]:


# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[19]:


# Fit the model
model.fit(x, y, epochs=150, batch_size=10)

