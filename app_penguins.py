import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# Funzione per la predizione del pinguino
def predizione_pinguino():
    st.markdown("# CHE PINGUINO SEI? 😎")
    st.text("Tramite il modello RandomForestRegressor ho creato la webapp")

    # Carica il modello
    loaded = joblib.load("pipeline_penguins.pkl")

    # Input dell'utente
    bill_length_mm = st.number_input("Inserisci la lunghezza del becco", value=0.0)
    bill_depth_mm = st.number_input("Inserisci la profondità del becco", value=0.0)
    flipper_length_mm = st.slider("Inserisci la lunghezza delle ali", 0, 232, 0)
    body_mass_g = st.slider("Inserisci il peso in grammi", 0, 6300, 0)
    sex = st.selectbox("Di che sesso è?", ("maschio", "femmina"))
    island = st.selectbox("Da che isola proviene?", ("Torgersen", "Biscoe", "Dream"))

    # Conversione sesso
    sex = "male" if sex == "maschio" else "female"

    # Crea il DataFrame
    data = pd.DataFrame({
        "bill_length_mm": [bill_length_mm],
        "bill_depth_mm": [bill_depth_mm],
        "flipper_length_mm": [flipper_length_mm],
        "body_mass_g": [body_mass_g],
        "sex": [sex],
        "island": [island],
    })

    # Predizione
    predict = loaded.predict(data)

    st.text(f"Se tu fossi un pinguino saresti: {predict[0]}")

    # Mostra immagine in base al risultato
    immagine_pinguino_adelia = Image.open("immagine_pinguino_adelia.jpg")
    immagine_pinguino_gentoo = Image.open("immagine_pinguino_gentoo.jpeg")
    immagine_pinguino_chinstrap = Image.open("immagine_pinguino_chinstrap.webp")

    if predict[0] == "Adelie":
        st.image(immagine_pinguino_adelia, use_column_width=True)
    elif predict[0] == "Gentoo":
        st.image(immagine_pinguino_gentoo, use_column_width=True)
    else:
        st.image(immagine_pinguino_chinstrap, use_column_width=True)

# Funzione per la pagina "Informazioni"
def grafici():

    grafico_isole = Image.open("grafico_isole.png")
    grafico_bill_length = Image.open("grafico_bill_length.png")
    grafico_bodymass = Image.open("grafico_bodymass.png")
    grafico_bill_isole = Image.open("grafico_bill_isole.png")
 
    st.markdown("# GRAFICI E SPIEGAZIONI")
    st.markdown("### qui sotto sono riportati i grafici che aiutano a spiegare come il modello discrimina le 3 classi di pinguini in base alle variabili date")

    # grafico isole
    st.image(grafico_isole, use_column_width=True)
    st.markdown("""#### da questo grafico possiamo notare che: 
    markdown("- nell'isola Torgersen sono presenti solo pinguini di razza Adelie
    #### - nell'isola Biscoe sono presenti in grande quantità i pinguini di razza Gentoo e pinguini Adelie in piccole quantità")
    "#### - nell'isola Dream sono presenti pinguini di razza Chinstrap e Adelie in quantità simili, leggermente prevalente la razza Chinstrap")
    
    st.markdown("### Modello usato:")
    st.text("- RandomForestRegressor")
    st.markdown("### Dataset:")
    st.text("Il dataset utilizzato proviene dal Palmer Penguins dataset.")

# Funzione principale per la navigazione
def main():
    # Sidebar per la navigazione
    st.sidebar.title("Navigazione")
    pagina = st.sidebar.selectbox("Seleziona una pagina:", ["Predizione Pinguino", "Grafici"])

    # Mostra la pagina selezionata
    if pagina == "Predizione Pinguino":
        predizione_pinguino()
    elif pagina == "Grafici":
        grafici()

# Esegui l'app
if __name__ == "__main__":
    main()