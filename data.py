import pandas as pd
import streamlit as st

'''This notebook contains only one method: load_data'''

@st.cache_data(show_spinner=False) # this is a decorator --> really need it for streamlit to function effectively
# path variable tells where the data needs to be loaded from; returns a dataframe
def load_data(path: str) -> pd.DataFrame:
    '''Loading a small CSV and caching it so the app stays responsive.'''
    df = pd.read_csv(path) # create dataframe
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    return df

'''We might create some additional functions/methods in here for data transformations'''
'''Data transformations would take place in THIS file (but cleaning would take place elsewhere, seems like??)'''