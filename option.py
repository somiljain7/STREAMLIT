import streamlit as st
import numpy as np
import pandas as pd
st.title('DATA EXTRACTION')
st.write("IMPLEMENTATION MULTIPLE TYPES:")
df=pd.DataFrame({
    'TYPES': [1, 2, 3, 4],
    
})
option = st.selectbox(
    'Which number do you like best?',
     df['TYPES'])

'You selected: ', option
