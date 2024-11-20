import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def main():
    loaded = joblib.load("pipeline_penguins.pkl")
    st.markdown("""### tramite il modello 
                RandomForestRegressoior ho creato la webapp""")
    st.markdown("# CHE PINGUINO SEI?😎")




if __name__ == "__main__":
    main()