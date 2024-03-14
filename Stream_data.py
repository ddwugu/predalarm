import pickle
import streamlit as st

# Load the model
try:
    with open('Pred_lokasi11.sav', 'rb') as file:
        LokasiKM = pickle.load(file)
except Exception as e:
    st.error(f"Error loading the model: {e}")
    LokasiKM = None  # Assign None if there is an error loading the model

# Web Title
st.title('Pertamina Field Jambi')
st.subheader('Prediksi Lokasi Kebocoran Line BJG-TPN')
# User Inputs
Titik_1_PSI = st.text_input('Input Pressure di titik 1 (PSI)')
Titik_2_PSI = st.text_input('Input Pressure di titik 2 (PSI)')
a = 135 - float(Titik_1_PSI) if Titik_1_PSI else None
b = 86 - float(Titik_2_PSI) if Titik_2_PSI else None

# Code prediction
suspect_loct = ''

# Prediction Button
if LokasiKM is not None and st.button('Prediksi Lokasi'):
    try:
        if a is not None and b is not None:
            prediksi_lokasi = LokasiKM.predict([[a, b]])
            if prediksi_lokasi[0] == 0: # titik nol
                suspect_loct = 'It is safe that there is no fluid flowing'
            elif prediksi_lokasi[0] >= 26.3: # total panjang trunkline
                suspect_loct = 'Safe, there are no leaks'
            else:
                suspect_loct = f'!!!estimated leak location {prediksi_lokasi[0]} KM'
            st.success(suspect_loct)
        else:
            st.warning("Masukkan tekanan yang valid untuk kedua titik.")
    except Exception as e:
        st.error(f"Error predicting location: {e}")
