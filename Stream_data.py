import streamlit as st
import pygame

# Inisialisasi Pygame
pygame.mixer.init()

# Load file audio
audio_file_path = "music.mp3"

# Memainkan file audio
pygame.mixer.music.load(audio_file_path)
pygame.mixer.music.play()

# Menampilkan teks atau elemen lainnya di aplikasi Streamlit
st.write("Selamat datang di aplikasi Streamlit!")
