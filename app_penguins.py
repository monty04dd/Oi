import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def main():
    loaded = joblib.load("pipeline_penguins.pkl")
    st.text("""### tramite il modello RandomForestRegressoior ho creato la webapp""")
    st.markdown("# CHE PINGUINO SEI?😎")



    bill_length_mm = st.number_input("Inserisci la lunghezza del becco", value=None, placeholder="0.00")
    bill_depth_mm = st.number_input("Inserisci la profondità del becco", value=None, placeholder="0.00")
    flipper_length_mm = st.slider("inserisci la lunghezza delle ali", 0, 232, 0)
    body_mass_g = st.slider("inserisci il peso in grammi", 0, 6300, 0)
    sex = st.selectbox("di che sesso è?", ("maschio","femmina"), key="sex")
    island = st.selectbox("da che isola proviene?", ("Torgersen","Biscoe","Dream"), key="island")

    if sex == "maschio":
        sex = "male"
    else:
        sex = "female"

    
    data = pd.DataFrame({
        "bill_length_mm":[bill_length_mm],
        "bill_depth_mm":bill_depth_mm,
        "flipper_length_mm":flipper_length_mm,
        "body_mass_g":body_mass_g,
        "sex":sex,
        "island":island,
    })
    
    predict = loaded.predict(data)

    st.header(predict)
    

if __name__ == "__main__":
    main()