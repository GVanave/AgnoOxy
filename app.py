from agno.agent import Agent

from agno_agent import fuelstationsearchagent, hotelsearchagent
import streamlit as st 


st.header("AgnoScrapely")
st.sidebar.title("Select Options")
selected_task = st.sidebar.selectbox("Select Task", options=["None", "Search Hotels", "Search Fuel Stations"])

st.write(f"Using Tool {selected_task}")

input_location = st.text_input("Enter Location Below: ")

submit_button = st.button("Get Results 😀 ")

if selected_task == "Search Hotels":
    agent = hotelsearchagent()
elif selected_task == "Search Fuel Stations":
    agent = fuelstationsearchagent()


if input_location and submit_button:
    response = agent.run(input_location)  # or agent.invoke(input_location) based on your Agno version
    st.markdown(response.content)














