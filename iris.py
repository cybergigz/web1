# import numpy as np
# import pandas as pd
import streamlit as st
# import matplotlib.pyplot as plt
import seaborn as sns

st.title('Iris Dataset')
# read from seaborn
df = sns.load_dataset('iris')
# read df from csv iris dataset from UCI url, need pandas
# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# df = pd.read_csv(url, header=None)
# df.columns = ['sepal_length', 'sepal_width',
              # 'petal_length','petal_width','species']

x = st.selectbox('select X-axis', df.columns[:-1])
y = st.selectbox('select Y-axis', df.columns[:-1])
st.write('You selected:', x, y)
st.scatter_chart(df, x=x, y=y, color=df.columns[-1])