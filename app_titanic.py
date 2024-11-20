import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def main():
    loaded = joblib.load("pipe_randomforest_titanic.pkl")
    st.title("Inferenza per TITANIC dataset")
    st.text("""questa applicazione web permette id fare inferenza 
sul dataset Titanic con un modello di random forest classifier""")
    # slider


    age = st.slider("quanti anni aveva il passeggero?", 0, 100, 0)
    fare = st.slider("costo del biglietto", 0, 270, 0)
    parch = st.slider("numero di parenti a bordo", 0, 15, 0)
    pclass = st.selectbox("in che clsse si trovava l'alloggio del passeggero?", (1,2,3), key="Pclass")
    embarked = st.selectbox("porto di imbarco passeggero", ("S","C","Q"), key="embarked")
    sex = st.selectbox('che brand è la tua macchina?',("male","female"), key="sex")

    sibsp = st.selectbox('era sposato?',("si", "no"), key="sibsp")
    
    inferenza = pd.DataFrame({
        "Age" : [age],
        "Fare" : [fare],
        "Parch" : [parch],
        "Pclass" : [pclass],
        "Embarked": [embarked],
        "Sex": [sex],
        "SibSp": [sibsp]
    })

    predict = loaded.predict(inferenza)
    
    # dict_res = {0:"morto male", 1:"femmina"}

    # predict = dict_res[predict]

    # immagine "vivo":
    img_sopravvissuti = Image.open("immagine_sopravvissuti.webp")
    img_affogati = Image.open("immagine_affogati.webp")
    img_sopravvissuta_donna = Image.open("immagine_sopravvissuta_donna.webp")

    dict_previsioni = {0: "sei morto male", 1: "sei donna"}

    st.write(f"il/la passeggero/a che hai scielto è: : {dict_previsioni[int(predict)]}")

    if predict == 0:
        st.image(img_affogati, use_column_width=True)
    if predict == 1:
        if sex == "male":
            st.image(img_sopravvissuti, use_column_width=True)
        else:
            st.image(img_sopravvissuta_donna, use_column_width=True)

if __name__ == "__main__":
    main()

