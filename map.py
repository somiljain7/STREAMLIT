
import streamlit as st
import numpy as np
import pandas as pd
map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [22.7196, 75.8577],
    columns=['lat', 'lon'])

st.map(map_data)


