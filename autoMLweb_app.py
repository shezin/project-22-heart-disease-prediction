import streamlit as st
from multipages import Multipage
from pages import data_upload,test,home

app = Multipage()

st.title('WEB APPLICATION')

app.add_page('Home',home.app)
app.add_page('Dataset Details', data_upload.app)
app.add_page('Heart disease prediction', test.app)
app.run()