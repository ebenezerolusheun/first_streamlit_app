import streamlit as st
import pandas as pd
import requests as req
import snowflake.connector
from urllib.error import URLError

st.title('My Parents New Healthy Diner')

st.header('Breakfast Favorites')
st.text('🥣 Omega 3  & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avocado Toast')

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## using pandas to read data from the S3 bucket 
my_fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruits_list.set_index('Fruit')

## Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

## Display the table on the page
st.dataframe(fruits_to_show)

## New Section to display fruityvice api response

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + this_fruit_choice )
    # To Flattening a simple JSON into a dataframe 
    fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

st.header("Fruityvice Fruit Advice!") 

try:
    fruit_choice = st.text_input('what fruits would you like information about?')
    if not fruit_choice:
        st.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        # Let streamlite to display the object as dataframe
        st.dataframe(back_from_function)

##try:
  ##  fruit_choice = st.text_input('what fruits would you like information about?')
    ##if not fruit_choice:
      ##  st.error("Please select a fruit to get information.")
    ##else:
      ##  fruityvice_response = req.get("https://fruityvice.com/api/fruit/" + fruit_choice )
        # To Flattening a simple JSON into a dataframe 
        ##fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
        # ##Let streamlite to display the object as dataframe
        ##st.dataframe(fruityvice_normalized)
##except URLError as e:
  ##  st.error()

##fruityvice_response = req.get("https://fruityvice.com/api/fruit/watermelon")


##streamlit.text(fruityvice_response.json())




