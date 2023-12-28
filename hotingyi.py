#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

import streamlit as st

import numpy as np
import pandas as pd

import webbrowser

# In[2]:
st.set_page_config(page_title='Tingyi Ho\'s Portfolio', layout='wide')
st.title('Tingyi Ho\'s Portfolio')
st.subheader('Summary')
st.write('3+ years professional experiences')
st.subheader('Project')
st.write('3+ years professional experiences')

# In[3]
st.sidebar.write('Wish to connect?')
email = 'th3019@columbia.edu'
linkedin_profile_url = 'https://www.linkedin.com/in/ting-yi-ho/'

#Insert image
st.sidebar.image('gradphoto01.jpg')

# Create a button
if st.sidebar.button('Connect via email'):
    # Open the default email client
    subject = 'Invitation to connect'
    body = 'Dear Ting'
    webbrowser.open(f'mailto:{email}?subject={subject}&body={body}')
    
# Create a button
if st.sidebar.button('Visit LinkedIn'):
    # Open the LinkedIn profile in a new tab
    st.sidebar.markdown(f'<a href="{linkedin_profile_url}" target="_blank">Click for visiting LinkedIn</a>', unsafe_allow_html=True)

