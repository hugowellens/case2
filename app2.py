#!/usr/bin/env python
# coding: utf-8

# In[3]:


# pip install streamlit


# In[10]:


import streamlit as st
import pandas as pd
import numpy as np


# In[11]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[12]:


st.title("Hair Eye Colour Database")


# In[13]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[14]:


HairEyeselect = HairEye[HairEye["Hair"] == InputHair]


# In[15]:


st.dataframe(HairEyeselect)


# In[ ]:




