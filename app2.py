#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install streamlit


# In[4]:


import streamlit as st
import pandas as pd
import numpy as np


# In[5]:


HairEye = pd.read_csv("HairEyeColor.csv")


# In[6]:


st.title("Hair Eye Colour Database")


# In[ ]:


InputHair = st.sidebar.selectbox("Select Hair Colour", ("Brown", "Black", "Blond", "Red"))


# In[ ]:


HairEyeselect = HairEye[HairEye["Hair"] == InputHair]


# In[ ]:


st.dataframe(HairEyeSelect)

