import streamlit as st
import pandas as pd
import requests as req



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
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

## Display the table on the page
st.dataframe(fruits_to_show)

## New Section to display fruityvice api response

st.header("Fruityvice Fruit Advice!") 

def read_api(value:str):
  return req.get(f"https://fruityvice.com/api/fruit/{value}")

fruityvice_response = read_api('kiwi')

##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


##streamlit.text(fruityvice_response.json())

# To Flattening a simple JSON into a dataframe 
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())

# Let streamlite to display the object as dataframe
st.dataframe(fruityvice_normalized)
