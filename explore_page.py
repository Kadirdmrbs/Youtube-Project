import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

@st.cache
def load_data():
    df = pd.read_csv('finall.csv',index_col=0)
    
    return df

df = load_data()
df = df.astype({"year": object})
df.rename(columns = {'view_count':'View', 'like_count':'Like', 'comment_count':'Comment'}, inplace = True)
df2 = df.drop(columns=['video_id', 'video_title','upload_date','categories','year'])
df2.rename(columns = {'view_count':'View', 'like_count':'Like', 'comment_count':'Comment'}, inplace = True)
columns = df2.columns
clist = ['categories','year']
def show_explore_page():
    st.title('Explore S Sports')

    color = st.selectbox("Select a coloring:",clist)
    axis_X = st.selectbox("Select X axis:",columns,key='Like')
    axis_Y = st.selectbox("Select Y axis:",columns,key='View')

    st.header(f"{axis_X} vs {axis_Y} by {color}")

    fig = px.scatter(df, color=color,
    x = axis_X, y = axis_Y)
    st.plotly_chart(fig)