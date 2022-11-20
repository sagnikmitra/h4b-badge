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
st.set_page_config(
    page_title="Qwiklabs Progress Generator",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)
image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
miletry = 1
if image_file is not None:
    size = (750, 750)
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
    card = Image.open(image_file)

    card = card.resize(size, Image.ANTIALIAS)

    card2 = Image.open(image_file)

    card2 = card2.resize(size, Image.ANTIALIAS)

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
