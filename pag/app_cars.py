import streamlit as st
import joblib
import pandas as pd
def somma(l1:float, l2:float):
    a = l1 + l2
    return a

def main():
    loaded = joblib.load("pipe_ridge_cars.pkl")
    st.title("Inferenza per cars dataset")
    st.text("""questa applicazione web permette id fare inferenza 
sul dataset cars con un modello ridge""")
    # slider
    kms_driven = st.slider("quanti km ha la tua macchina?", 0, 1000000, 0)
    old = st.slider("quanti anni ha la tua macchina", 0, 100, 0)
    brand = st.selectbox('che brand è la tua macchina?',('Hyundai', 'Mahindra', 'Ford', 'Maruti', 'Skoda', 'Audi', 'Toyota',
       'Renault', 'Honda', 'Datsun', 'Mitsubishi', 'Tata', 'Volkswagen',
       'Chevrolet', 'Mini', 'BMW', 'Nissan', 'Hindustan', 'Fiat', 'Force',
       'Mercedes', 'Jeep', 'Volvo'), key="brand")
    fuel_type = st.selectbox('che carburante usa la tua macchina?',('Petrol', 'Diesel', 'LPG'), key="carburante")
    
    inferenza = pd.DataFrame({
        "kms_driven" : [kms_driven],
        "old" : [old],
        "brand" : [brand],
        "fuel_type" : [fuel_type]
    })

    predict = loaded.predict(inferenza)
    
    st.write(f"il prezzo di vendita della tua macchina è: {round(predict,2)}")

if __name__ == "__main__":
    main()


