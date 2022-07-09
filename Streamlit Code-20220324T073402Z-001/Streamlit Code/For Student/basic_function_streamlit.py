# import module
import streamlit as st
 
# Title
st.title("Semangat Belajar Streamlit, Orbitians!")

# Header
st.header("Ini adalah Header, Orbitians!")
 
# Subheader
st.subheader("Ini adalah Sub-Header, Orbitians!")

# Text
st.text("Hello Orbitians, hari ini kita akan belajar tentang penggunaan Streamlit.")

# Markdown
st.markdown("# Mardown 1")
st.markdown("## Mardown 2")
st.markdown("### Mardown 3")

# success
st.success("Success")
# info
st.info("Information")
# warning
st.warning("Warning")
# error
st.error("Error")

# Write text
st.write("Hari ini aku sangat senang sekali!! yuhuu yeay")

# Writing python inbuilt function range()
st.write(range(20))

# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.jpg") 

# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
# display the text if the checkbox returns True value
	st.text("Hai, ini penggunaan checkbox")

# radio button
# first argument is the title of the radio button
# second argument is the options for the ratio button
status = st.radio("Pilih Program: ", ('Gen Z', 'Mastery'))

# conditional statement to print
# Male if male is selected else print female
# show the result using the success function
if (status == 'Gen Z'):
	st.success("Gen Z")
else:
	st.success("Mastery")

# Selection box
# first argument takes the titleof the selectionbox
# second argument takes options
domain = st.selectbox("Pembagian Coach Domain AI di Orbit: ",
					['Data Science', 'NLP', 'CV', 'Technical'])

# print the selected hobby
st.write("Domain Kamu adalah: ", domain)

# Multiselect
# first argument takes the titleof the selectionbox
# second argument takes options
domain = st.multiselect("Pembagian Coach Domain AI di Orbit: ", 
	['Data Science', 'NLP', 'CV', 'Technical'])

# print the selected hobby
st.write("Domain Kamu ada", len(domain), 'domain')

# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):
	st.text("Welcome To Orbitian!! :))")

# Text Input
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
	result = name.title()
	st.success(result)

# slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))

# INPUT TEXT
st.text_input("Enter your name", "")  # Default Value

# NUMBER INPUT
# 0.0 Start
# 100.0 End
# 99.0 Default Value
st.number_input("Enter a number", 0.0, 100.0, 99.0)

# TEXT AREA
st.text_area("Enter a Message", "")

# INPUT DATE
st.date_input("Enter Date")

# TIME INPUT
st.time_input("Enter Time")

# FILE UPLOADER

st.file_uploader("Upload file", type=["csv", "txt"])
