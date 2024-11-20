import streamlit as st
import joblib
import pandas as pd
from PIL import Image

def centered_image(image_path, width):
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="{image_path}" style="width: {width}px;">
        </div>
        """,
        unsafe_allow_html=True,
    )

def main():
    loaded = joblib.load("pipe_randomforest_titanic.pkl")
    st.title("Inferenza per TITANIC dataset")
    st.text("""questa applicazione web permette id fare inferenza 
sul dataset Titanic con un modello di random forest classifier""")
    # slider


    img = Image.open("image.png")

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
    st.write(f"il/la passeggero/a che hai scielto è: : {predict}")
    st.image("https://www.quotidiano.net/magazine/enrico-tavernini-morto-a-57-anni-addio-al-regista-di-riva-del-garda-fipenqtl", caption="Questa è la mia immagine", use_column_width=True)

if __name__ == "__main__":
    main()

