#!/usr/bin/env python
# coding: utf-8

# In[22]:


from dataset import *
from model import model


# In[23]:


# Make predictions with the model
predictions = model.predict(x)
rounded = [round(x[0]) for x in predictions]


# In[24]:


predictions = (model.predict(x) > 0.5).astype(int)


# In[25]:


for i in range(10):
    print('%s => %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))


# In[26]:


from sklearn.metrics import precision_score, recall_score
print('Precision Score is:', precision_score(predictions, y))
print('Recall Score is:', recall_score(predictions, y))


# In[27]:


from sklearn.metrics import f1_score
print(f1_score(predictions, y))


# In[ ]:




