import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
fruits_selected = streamlit.multiselect('Pick some fruits:', list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table
streamlit.dataframe(fruits_to_show)


#New Section to display fruityvice api response 


#Updated version

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
        return my_cur.fetchall()
    


streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?', 'kiwi')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_func = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_func)

except URLError as e:
    streamlit.error()

streamlit.stop()

streamlit.header("The fruit load list from Snowflake contains:")

#snowflake connector 
if streamlit.button('Get Fruit Load List')
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    streamlit.dataframe(my_data_rows)


streamlit.header('What fruit would you like to add?')
added_fruit = streamlit.text_input('What fruit would you like to add?', 'kiwi')
streamlit.write('Thanks for adding: ', added_fruit)

#will not work for now..
my_cur.execute("insert into fruit_load_list values('from streamlist!')")
