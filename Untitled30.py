#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("i am going to \nmru college \nto learn thr nlp")


# In[2]:


print("i am going to \nmru college \tto learn thr nlp")


# In[4]:


print("i am going to \nmru college \rto learn the nlp")


# In[5]:


import re
pattern=r'\d+'
string="007 james bond wants to learn the python"
matching=re.match(pattern,string)
matching.group()


# In[6]:


import re
pattern=r'\d+'
string="james bond 007 wants 008 to learn the python"
matching=re.search(pattern,string)
matching.group()


# In[9]:


import re
pattern=r'\d+'
string="james bond 007 wants 008 to learn23 the python"
matching=re.findall(pattern,string)
matching


# In[12]:


import re
pattern=r'\d'
string="james bond 007 wants 008 to learn23 the python"
matching=re.sub(pattern,"*",string)
matching


# In[13]:


import re
pattern=r'\d+'
string="james bond 007 wants 008 to learn23 the python"
matching=re.sub(pattern,"*",string)
matching


# In[18]:


import re
pattern=r'\d*'
string="james bond 007 wants 008 to learn23 the python"
matching=re.sub(pattern,"*",string)
matching


# In[23]:


# Test case
text = """
Hello world! Contact us at info@example.com or support123@company.org. Follow us on social media: #AI #MachineLearning.
Visit <a href="http://example.com">our website</a> for more details. This is a test with number 1234.
"""


# In[27]:


emails=re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',text)
emails


# In[29]:


##hash tags
hash_tags=re.findall(r'#[a-zA-Z0-9]+',text)
hash_tags


# In[ ]:




