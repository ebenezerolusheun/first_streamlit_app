import streamlit
import pandas as pd



streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3  & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

## using pandas to read data from the S3 bucket 
my_fruits_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")



my_fruit_list = my_fruits_list.set_index('Fruit')

## Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

## Display the table on the page
streamlit.dataframe(fruits_to_show)

## New Section to display fruityvice api response
import requests
streamlit.header("Fruityvice Fruit Advice!") 

def read_api(value:str):
  return requests.get(f"https://fruityvice.com/api/fruit/{value}")

fruityvice_response = read_api('kiwi')

##fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")


streamlit.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
## fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# write your own comment - what does this do?
## streamlit.dataframe(fruityvice_normalized)
