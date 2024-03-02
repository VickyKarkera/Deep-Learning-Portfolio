import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Friends Sentiment Guide"
)

st.title("Friends Sentiment Episode Guide")
st.image("images\Friends_image.jpg")
st.sidebar.success("Select a page above.")
df= pd.read_excel("friends_episode_emotion_app\data\\final_friends_data.xlsx")
st.header("The links to the scripts: ")
st.dataframe(df[["Season","Episode","Title","URL"]],use_container_width=True,hide_index=True)


