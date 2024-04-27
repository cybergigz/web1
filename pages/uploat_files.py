import streamlit as st
import pandas as pd
# from PIL import Image, ImageColor
# import numpy as np

files = st.file_uploader('Upload files', type=['csv', 'xlsx'])
if files is not None:
    # st.file_uploader(files.open(files))
    df = pd.read_csv(files)
    st.dataframe(df)