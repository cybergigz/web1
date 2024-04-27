import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title('Visualize')
ds = st.selectbox('Select Dataset',
        sns.get_dataset_names())
df = sns.load_dataset(ds)
# select number only
corr = df.corr(numeric_only=True)
fig = plt.figure()
sns.heatmap(corr, annot=True)

fig