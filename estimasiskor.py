import pickle
import streamlit as st

model = pickle.load(open('skor.sav', 'rb'))

st.title('Estimasi Jumlah Skor')

matches = st.number_input('Masukkan Total matches')
wins = st.number_input('Masukkan Total wins')
draws = st.number_input('Masukkan Total draws')
loses = st.number_input('Masukkan Total loses')

predict = ''

if st.button('Estimasi Skor'):
    predict = model.predict(
        [[matches, wins, draws, loses]]
    )
    st.write ('Estimasi Jumlah Skor : ', predict)