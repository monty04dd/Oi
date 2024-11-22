import streamlit as st
import joblib
import pandas as pd
from PIL import Image

# Funzione per la predizione del pinguino
def predizione_pinguino():
    st.text("Tramite il modello RandomForestRegressor ho creato la webapp")
    st.markdown("# CHE PINGUINO SEI? 😎")

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


    # regole per l'indentazione all'interno dei futuri elenchi indipendenti 
    st.markdown(
    """
    <style>
    ul {
        list-style-type: disc;
        margin-left: 20px; /* Base indent for the first level */
    }
    ul ul {
        list-style-type: circle; /* Second level uses circle bullets */
        margin-left: 20px; /* Indent for the second level */
    }
    ul ul ul {
        list-style-type: square; /* Third level uses square bullets */
        margin-left: 20px; /* Indent for the third level */
    }
    ul ul ul ul {
        list-style-type: disc; /* Fourth level reverts to discs */
        margin-left: 20px; /* Indent for the fourth level */
    }
    </style>
    """,
    unsafe_allow_html=True,
    )

    
    st.markdown("<h1 style='text-align: center; color: white;'> <b> E.D.A. </b> </h1>", unsafe_allow_html=True)

    # grafico isole
    st.markdown("<h2 style= 'text-align: center; color:white;'>Grafico Isole</h2>", unsafe_allow_html=True)
    st.image(grafico_isole, use_column_width=True)
    st.markdown("###### da questo grafico possiamo notare che:") 
    st.markdown("###### - nell'isola Torgersen sono presenti solo pinguini di razza Adelie")
    st.markdown("###### - nell'isola Biscoe sono presenti in grande quantità i pinguini di razza Gentoo e pinguini Adelie in piccole quantità")
    st.markdown("###### - nell'isola Dream sono presenti pinguini di razza Chinstrap e Adelie in quantità simili, leggermente prevalente la razza Chinstrap")

    st.markdown("""<h2><br><h2>""", unsafe_allow_html=True)
    

    # violin plot becco
    st.markdown("<h1 style='text-align: center; color: white;'>Grafico Lunghezza Becco</h1>", unsafe_allow_html=True)
    st.image(grafico_bill_length, use_column_width=True)
    st.markdown(
    """
    <h6>
    <ul>
        <li>La lunghezza del becco è un <strong>ottimo discriminante</strong> per separare gli <strong>Adelie</strong> dalle altre specie.</li>
        <li>Tra <strong>Gentoo</strong> e <strong>Chinstrap</strong>:
            <ul>
                <li>I <strong>Chinstrap</strong> hanno una maggiore tendenza verso becchi lunghi, come mostrato dalla mediana più alta e dalla distribuzione spostata verso la fascia superiore.</li>
                <li>I <strong>Gentoo</strong>, invece, hanno una distribuzione leggermente più ampia, ma una mediana inferiore rispetto ai <strong>Chinstrap</strong>.</li>
            </ul>
        </li>
    </ul>
    </h6>
    """,
    unsafe_allow_html=True
)
    st.markdown("""<h2><br><h2>""", unsafe_allow_html=True)

    # grafico del peso 
    st.markdown("<h1 style='text-align: center; color: white;'>Grafico Perso del Pinguino</h1>", unsafe_allow_html=True)
    st.markdown(
    """
    <h6>
    <ul>
        <li><strong>Adelie:</strong> Mostrano una distribuzione stretta e uniforme della massa corporea, indicando una variabilità ridotta. Questo rende gli Adelie facilmente separabili dalle altre specie.</li>
        <li><strong>Gentoo:</strong> Presentano la massa corporea più elevata e una distribuzione ampia, segnalando una maggiore variabilità. La massa corporea è un forte discriminante per questa specie rispetto alle altre.</li>
        <li><strong>Chinstrap:</strong> Hanno una distribuzione che si sovrappone parzialmente con gli Adelie, ma tendono verso masse più elevate. La massa corporea, quindi, è meno efficace per distinguere Chinstrap dagli Adelie.</li>
    </ul>
    <p><strong>Valore statistico nel modello:</strong></p>
    <ul>
        <li>La massa corporea è un ottimo predittore per distinguere i Gentoo dalle altre specie.</li>
        <li>Tuttavia, per separare Adelie e Chinstrap, la variabile ha una capacità discriminante inferiore a causa della significativa sovrapposizione. È necessaria una combinazione con altre variabili, come la lunghezza del becco, per migliorare le performance del modello.</li>
    </ul>
    </h6>
    """,
    unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # grafico becco isole

    st.markdown("<h2 style='text-align: centre; color:white;'>Analisi per la discriminazione delle specie basata su lunghezza del becco, peso, sesso e isola del pinguino </h2>", unsafe_allow_html=True)
    st.image(grafico_bill_isole, use_column_width=True)
    st.markdown("""
    <h6>
    <strong>Isola Dream</strong><br>
    <ul>
        <li><strong>Maschi:</strong>
            <ul>
                <li>C'è una netta separazione nella lunghezza del becco:</li>
                <ul>
                    <li>Pinguini con becchi più corti (lunghezza < 46 mm) sono chiaramente della specie <strong>Adelie</strong>.</li>
                    <li>Becchi più lunghi (> 46 mm) appartengono alla specie <strong>Chinstrap</strong>.</li>
                </ul>
                <li>Il peso non sembra influenzare significativamente la discriminazione tra le specie: i pinguini delle due specie si sovrappongono nei valori di peso.</li>
            </ul>
        </li>
        <li><strong>Femmine:</strong>
            <ul>
                <li>La distinzione tra le due specie è meno chiara rispetto ai maschi.</li>
                <li>Anche qui, generalmente, i becchi più lunghi (> 46 mm) sono associati ai pinguini <strong>Chinstrap</strong>, ma c'è una certa sovrapposizione.</li>
                <li>Il peso, come nei maschi, non permette di distinguere le specie.</li>
            </ul>
        </li>
    </ul>
    <strong>Isola Biscoe</strong><br>
    <ul>
        <li><strong>Maschi e femmine:</strong>
            <ul>
                <li>La separazione basata sulla lunghezza del becco tra <strong>Adelie</strong> e <strong>Gentoo</strong> non è netta:</li>
                <ul>
                    <li><strong>Adelie:</strong> Becchi più corti (< 45 mm).</li>
                    <li><strong>Gentoo:</strong> Becchi più lunghi (> 45 mm).</li>
                </ul>
                <li>Tuttavia, c'è una relazione più evidente con il peso:</li>
                <ul>
                    <li>I pinguini <strong>Gentoo</strong>, sia maschi che femmine, tendono a pesare di più rispetto agli <strong>Adelie</strong>.</li>
                    <li>Il peso quindi rappresenta un criterio importante per discriminare le specie in questa isola.</li>
                </ul>
            </ul>
        </li>
    </ul>
    <strong>Isola Torgersen</strong><br>
    <ul>
        <li>In questa isola, tutti i pinguini appartengono alla specie <strong>Adelie</strong>.</li>
        <li>Non ci sono differenze nella lunghezza del becco o nel peso per distinguere altre specie.</li>
    </ul>
    <strong>Conclusioni statistiche</strong><br>
    <ul>
        <li>La lunghezza del becco è un parametro discriminante nelle isole con più specie:</li>
        <ul>
            <li><strong>Dream:</strong> È un buon indicatore della specie, soprattutto per i maschi.</li>
            <li><strong>Biscoe:</strong> È utile ma con sovrapposizioni tra le specie.</li>
        </ul>
        <li>Il peso è un discriminante secondario:</li>
        <ul>
            <li><strong>Biscoe:</strong> Aiuta a distinguere i pinguini <strong>Gentoo</strong> (più pesanti) dagli <strong>Adelie</strong>.</li>
            <li><strong>Dream:</strong> Non è utile per discriminare tra le specie.</li>
        </ul>
        <li>Nelle isole con una sola specie (<strong>Torgersen</strong>), questi parametri non sono utili per distinguere differenze.</li>
    </ul>
    </h6>
    """, unsafe_allow_html=True)


    # st.markdown("### Modello usato:")
    # st.text("- RandomForestRegressor")
    # st.markdown("### Dataset:")
    # st.text("Il dataset utilizzato proviene dal Palmer Penguins dataset.")

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