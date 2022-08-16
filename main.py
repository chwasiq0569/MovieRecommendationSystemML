# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import streamlit as st
import pickle

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_list['title'].values

st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
     'How would you like to be contacted?',
     movies_list)

if st.button('Recommend'):
    st.write(selected_movie_name)