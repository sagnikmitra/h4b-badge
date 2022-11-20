from openpyxl import load_workbook
import openpyxl as pxl
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events
from io import StringIO
from PIL import Image
from streamlit_cropper import st_cropper
st.set_option('deprecation.showfileUploaderEncoding', False)

# Upload an image and set some options for demo purposes
st.header("Cropper Demo")
image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=[
                                 "1:1", "16:9", "4:3", "2:3", "Free"])
aspect_dict = {
    "1:1": (1, 1)
}
aspect_ratio = aspect_dict[aspect_choice]

if image_file:
    img = Image.open(image_file)
    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = st_cropper(img, realtime_update=realtime_update, box_color=box_color,
                             aspect_ratio=aspect_ratio)

    # Manipulate cropped image at will
    # st.write("Preview")
    # _ = cropped_img.thumbnail((150, 150))
    miletry = 1
    size = (1200, 1200)
    if miletry == 1:
        img = Image.open("frame.png")
        img2 = Image.open("frameblack.png")
    elif miletry == 2:
        img = Image.open("second.png").convert("RGB")
    elif miletry == 3:
        img = Image.open("third.png").convert("RGB")
    elif miletry == 4:
        img = Image.open("ultimate.png").convert("RGB")
    elif miletry == 0:
        img = Image.open("nomile.png").convert("RGB")
    img = img.resize(size, Image.ANTIALIAS)
    img2 = img2.resize(size, Image.ANTIALIAS)
    # card = Image.open(image_file)

    card = cropped_img.resize(size, Image.ANTIALIAS)

    # card2 = Image.open(image_file)

    card2 = cropped_img.resize(size, Image.ANTIALIAS)

    card.paste(img, (0, 0), img)

    card2.paste(img2, (0, 0), img2)
    card.save("frame_white.jpg", format="png")

    card2.save("frame_black.jpg", format="png")
    st.image(card)
    st.image(card2)
miletry = 0
# st.video('https://www.youtube.com/watch?v=Lf_tQWluHWA&t=10s')

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# credentials = ServiceAccountCredentials.from_json_keyfile_name('covidoff-ecef33b9fe0b.json', scope)

# gc = gspread.authorize(credentials)
# df = gc.open('covidoff-test-r').sheet1

# st.write(df.get_all_records())
