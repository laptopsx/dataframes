#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[5]:


grades = pandas.DataFrame({'Student': ['Daenerys Targaryen', 'Jon Snow', 'Tyrion Lanister', 'Joeffrey Baratheon'],
                            'Exam 1' : [85, 82, 100, 42],
                            'Exam 2' : [92, 89, 100, 36],
                            'Average': [88.5, 85.5, 100, 39]})
print(grades)


# In[6]:


gradesSortedByAverageAscending = grades.sort_values(by='Average')
print(gradesSortedByAverageAscending)


# In[7]:


gradesSortedByAverageDecending = grades.sort_values(by='Average', ascending=False)
print(gradesSortedByAverageDecending)


# In[8]:


print(grades.min())


# In[9]:


print(grades.max())


# In[10]:


print(grades.mean())


# In[ ]:




