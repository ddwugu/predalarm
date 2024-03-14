import streamlit as st
import requests
import pandas as pd
import pygame
from pygame import mixer

pygame.mixer.init()

# Web Title
st.title('Pertamina Field Jambi')
st.subheader('Line BJG-TPN')

# User Inputs
READ_API_KEY = 'SPYMD6ONS3YT6HKN'
CHANNEL_ID = '2405457'
FIELD_ID_1 = '1'
FIELD_ID_2 = '3'

# URL untuk mengakses data dari ThingSpeak untuk field 1
url_field_1 = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{FIELD_ID_1}.csv?api_key={READ_API_KEY}'

# URL untuk mengakses data dari ThingSpeak untuk field 2
url_field_2 = f'https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{FIELD_ID_2}.csv?api_key={READ_API_KEY}'

# Function to fetch data
def fetch_data():
    response_field_1 = requests.get(url_field_1)
    response_field_2 = requests.get(url_field_2)
    if response_field_1.status_code == 200 and response_field_2.status_code == 200:
        data_field_1 = pd.read_csv(url_field_1)
        data_field_2 = pd.read_csv(url_field_2)
        Titik_1_PSI = data_field_1['field1'].iloc[0] if not data_field_1.empty else None
        Titik_2_PSI = data_field_2['field3'].iloc[0] if not data_field_2.empty else None
        return Titik_1_PSI, Titik_2_PSI
    else:
        return None, None

# Initialize placeholders for real-time updates
placeholder1 = st.empty()
placeholder2 = st.empty()

# Loop for real-time updates
while True:
    Titik_1_PSI, Titik_2_PSI = fetch_data()
    if Titik_1_PSI is not None and Titik_2_PSI is not None:
        placeholder1.write(f"Pressure at Point 1 (Titik 1 PSI): {Titik_1_PSI}")
        placeholder2.write(f"Pressure at Point 2 (Titik 2 PSI): {Titik_2_PSI}")
        
        # Check conditions for buzzer
        if Titik_2_PSI < 90 or Titik_1_PSI < 150:
            # Trigger buzzer sound
            pygame.mixer.init()
            pygame.mixer.Sound('s.mp3').play()  # Adjust the file name as needed
        
    else:
        placeholder1.error("Failed to fetch data. Please try again later.")
        placeholder2.error("Failed to fetch data. Please try again later.")

