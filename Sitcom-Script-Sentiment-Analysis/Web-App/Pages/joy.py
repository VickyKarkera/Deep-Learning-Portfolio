import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Friends Sentiment Guide"
)

st.title("Friends Sentiment Episode Guide")
st.header("Joy")
st.image("images\joy.gif",use_column_width="always")
st.sidebar.success("Select a page above.")

df=pd.read_excel("friends_episode_emotion_app\data\\final_friends_data.xlsx")
df.sort_values(by=["joy"],ascending=False,inplace=True)
st.dataframe(df[["Title","joy"]],hide_index=True,use_container_width=True)

