import streamlit as st
from utils import *


movie_list = df['title']

st.title(title)
number = st.slider("Pick a number", 0, 100)
name = st.selectbox("Select Movie",options = movie_list)
if st.button("Click Me"):
    if number >0:
        result = recommend(name,number)
        for i in range(0,len(result)):
            st.write("*",result[i])
    else:
        st.write("Number Can't be zero")