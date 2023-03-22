import streamlit as st
#import pandas as pd
#import requests as req
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

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
##my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")


# To fetch just ine line
##my_data_row = my_cur.fetchone()

# To fetch all rows
my_data_row = my_cur.fetchall()

## st.text("The fruit load list contains:")
st.header("The fruit load list contains:")

##st.text(my_data_row)
st.dataframe(my_data_row)

st.text("What fruit would you lie to add?")
add_my_fruit = 'banana'
st.text(f"Thanks for adding {add_my_fruit}")

option = st.selectbox(
    'What fruit would you lie to add?',
    list(my_data_row))

st.write('Thanks for adding:', option)

my_cur.execute("insert into FRUIT_LOAD_LIST values ('from streamlit')")

st.stop()
