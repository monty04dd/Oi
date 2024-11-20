import streamlit as st
import joblib
import pandas as pd
def somma(l1:float, l2:float):
    a = l1 + l2
    return a

def main():
    st.title("Inferenza per cars dataset")
    st.text("""questa applicazione web permette id fare inferenza 
sul dataset cars con un modello ridge""")
    # slider
    num1 = st.slider("inserisci lato1 rettangolo", 0, 100, 2)
    num2 = st.slider("inserisci lato2 rettangolo", 0, 100, 3)
    option = st.selectbox('How would you like to be contacted?',('Email', 'Home phone', 'Mobile phone'))
    r = somma(num1, num2)

    st.write(f"la somma è: {r}")

if __name__ == "__main__":
    main()