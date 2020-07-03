import streamlit as st
import numpy as np
import pandas as pd
chart_data = pd.DataFrame(
     np.random.randn(10, 1),
     columns=['a'])

st.line_chart(chart_data)

