import os
import numpy as np
import streamlit as st
from screens import fitness_statistics, home, theme_selection
from screens import device_integration, today_statistics
import soundfile as sf
from gtts import gTTS
import streamlit_scrollable_textbox as stx
from difflib import get_close_matches
import base64

# Path to the logo
logo_path = 'static/logo.jpg'

# Set page configuration
st.set_page_config(page_title="QuickFit Max", page_icon="❤️", layout='wide', initial_sidebar_state="auto")
st.logo(logo_path)


# Read the logo file and encode it in base64
with open(logo_path, "rb") as logo_file:
    logo_base64 = base64.b64encode(logo_file.read()).decode("utf-8")

# Path to the font files
# Path to the font files
header_font_path = 'static/fonts/pattanakarn-font/Pattanakarn Bold.ttf'
subheader_font_path = 'static/fonts/pattanakarn-font/Pattanakarn Regular.ttf'
body_font_path = 'static/fonts/pattanakarn-font/Pattanakarn Light.ttf'

# # Ensure the font file exists
# if not os.path.exists(title_font_path):
#     st.error(f"Font file not found at path: {title_font_path}")
#     st.stop()  # Stop the app if the font file is not found

# Read the font file and encode it in base64
with open(header_font_path, "rb") as font_file:
    header_font_base64 = base64.b64encode(font_file.read()).decode("utf-8")
with open(subheader_font_path, "rb") as font_file:
    subheader_font_base64 = base64.b64encode(font_file.read()).decode("utf-8")
with open(body_font_path, "rb") as font_file:
    body_font_base64 = base64.b64encode(font_file.read()).decode("utf-8")

# Custom CSS for the title and app background
st.markdown(
    f"""
    <style>
    @font-face {{
        font-family: 'Pattanakarn Bold';
        font-style: normal;
        font-weight: bold;
        src: url(data:font/ttf;base64,{header_font_base64}) format('truetype');
    }}
    @font-face {{
        font-family: 'Pattanakarn';
        font-style: normal;
        font-weight: normal;
        src: url(data:font/ttf;base64,{subheader_font_base64}) format('truetype');
    }}

    @font-face {{
        font-family: 'Pattanakarn';
        font-style: normal;
        font-weight: 300;
        src: url(data:font/ttf;base64,{body_font_base64}) format('truetype');
    }}
    /* Sidebar background color */
    [data-testid="stSidebar"] {{
        background-color: #4B0082; /* Change this color to your desired color */
    }}
    /* Sidebar text color */
    [data-testid="stSidebar"] .css-1lcbmhc, [data-testid="stSidebar"] .css-10trblm {{
        color: white;
    }}
        /* Top menu bar */
    header[data-testid="stHeader"] {{
        background-color: #4B0082; /* Change this color to your desired color */
    }}

    /* Optional: change font color in top menu */
    header[data-testid="stHeader"] .css-1v3fvcr, header[data-testid="stHeader"] .css-1siy2j7 {{
        color: white; /* Change this to your desired font color */
    }}

    .header-style {{
        color: #dd2282;
        font-family: 'Pattanakarn', sans-serif;
        font-size: 36px;
        text-align: left;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Shadow effect */
        transform: translateY(-5px); /* Lift effect */

    }}
    .subheader-style {{
        color: #0000;
        font-family: 'Pattanakarn', sans-serif;
        font-weight: normal;
        font-size: 36px;
        text-align: left;
    }}
    .body-style {{
        color: #545454;
        font-family: 'Pattanakarn', sans-serif;
        font-weight: normal;
        font-size: 36px;
        text-align: left;
        font-weight: 300;
    }}
    .stApp {{
        background-color: #f2cccc;
    }}
    .header {{
        display: flex;
        align-items: center;
        padding: 10px 20px;
        background-color: #ffffff;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }}
    .header img {{
        width: 50px; /* Adjust the size of the logo as needed */
        margin-right: 10px;
        box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* Shadow effect */
        transform: translateY(-5px); /* Lift effect */
    }}
 
    </style>
    """,
    unsafe_allow_html=True
)

# Display the logo and title together
st.markdown(
    f"""
    <div class="header">
        <img src="data:image/jpeg;base64,{logo_base64}" alt="Logo">
        <h1 class="header-style">QuickFit Max - Your REHIT Fitness AI Coach</h1>
        
    </div><br>
    """,
    unsafe_allow_html=True
)


def app():
    pass

PAGES = {
    "Home": home,
    "Today's Statistics": today_statistics,
    "Theme Selection": theme_selection,
    "Fitness Insights": fitness_statistics,
    "Devices": device_integration,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

page = PAGES[selection]
page.app()



