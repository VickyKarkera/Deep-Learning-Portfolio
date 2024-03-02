import streamlit as st
st.set_page_config(
    page_title="Friends Sentiment Guide"
)

st.title("Friends Sentiment Episode Guide")
st.header("Fear")
st.image("images/fear.gif",use_column_width="always")
st.sidebar.success("Select a page above.")

import pandas as pd

df=pd.read_excel("friends_episode_emotion_app\data\\final_friends_data.xlsx")
df.sort_values(by=["fear"],ascending=False,inplace=True)
st.dataframe(df[["Title","fear"]],hide_index=True,use_container_width=True)

