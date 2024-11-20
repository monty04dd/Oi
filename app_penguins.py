import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def main():
    loaded = joblib.load("pipeline_penguins.pkl")
    st.markdown("""## Ciao, tramite il modello di regressione 'RandomForestRegressor' ho creato la webapp:""")
    st.markdown("# SCOPRI CHE PINGUINO SEI!")






if __name__ == "__main__":
    main()