import openai
import tabulate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents.agent_types import AgentType
from langchain.agents import create_csv_agent
import streamlit as st
import os
import pandas as pd




df=pd.read_csv("teststream.csv")

# Add sidebar content
st.sidebar.title("ChatGPT-")
#st.sidebar.markdown("This app demonstrates a ChatGPT-like clone using Streamlit and the OpenAI API.")
#st.sidebar.markdown("Enter your OpenAI API Key in the input field on the sidebar to get started.")

# Request API Key in the sidebar
#api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

os.environ['OPENAI_API_KEY'] = st.secrets["my_api_key"]

agent = create_csv_agent(
    OpenAI(temperature=0),
    path="teststream.csv",  # Replace with the actual file path
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)



agent.run("which bowlers gave the most total wides ")
