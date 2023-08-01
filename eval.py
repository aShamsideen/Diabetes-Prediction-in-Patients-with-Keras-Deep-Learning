#!/usr/bin/env python
# coding: utf-8

# In[4]:


from dataset import *
from model import model


# In[5]:


# Evaluate model
_, accuracy = model.evaluate(x, y)
print('Accuracy: %.2f' % (accuracy*100))


# In[7]:


model.fit(x, y, epochs=150, batch_size=10, verbose=0)


# In[8]:


_, accuracy = model.evaluate(x, y, verbose=0)
print('Accuracy: %.2f' % (accuracy*100))

