import streamlit
import pandas

streamlit.title('Healthy New diner!')

streamlit.header('Breakfast Favorites')

streamlit.text('🥣 Omege 3 & Blueberry oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boild Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruit_list = my_fruit_list.set_index('Fruit')
#putting a pick list
streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index))

#display the table
streamlit.dataframe(my_fruit_list)
