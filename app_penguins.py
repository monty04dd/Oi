import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def main():
    loaded = joblib.load("pipeline_penguins.pkl")
    st.title("""Ciao, tramite il modello di regressione
'RandomForestRegressor' ho creato la webapp SCOPRI CHE PINGUINO SEI! """)
    
    