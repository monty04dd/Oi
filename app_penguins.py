import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def main():
    loaded = joblib.load("pipeline_penguins.pkl")
    st.text("""### tramite il modello RandomForestRegressoior ho creato la webapp""")
    st.markdown("# CHE PINGUINO SEI?😎")



    bill_length_mm = st.number_input("Inserisci la lunghezza del becco", value=None, placeholder="0.00")
    bill_length_mm = st.number_input("Inserisci la profondità del becco", value=None, placeholder="0.00")
    flipper_length_mm = st.slider("inserisci la lunghezza delle ali", 0, 232, 0)
    body_mass_g = st.slider("inserisci il peso in grammi", 0, 6300, 0)
    sex = st.selectbox("di che sesso è?", ("male","female"), key="Pclass")
    island = st.selectbox("di che sesso è?", ("Torgersen","Biscoe","Dream"), key="Pclass")
    

if __name__ == "__main__":
    main()