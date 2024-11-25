import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import importlib
import os

st.set_page_config(
    page_title="Portfolio web application",
    page_icon=Image.open("pag/img/web.png"),
    layout="centered" # "wide"
)

def get_pages():
        pages = []
        icons = []
        modules = []

        BLACKLIST_FILES = ['__init__', 'test']  # aggiungi qui i file da escludere    
        # page_order = []
        page_order = ["app_penguins", "app_cars", "app_titanic", "app_dataupload"]

        files = [f[:-3] for f in os.listdir('pag') if f.endswith('.py') and f[:-3] not in BLACKLIST_FILES]
        files.sort(key=lambda x: page_order.index(x) if x in page_order else len(page_order))

        icon_mapping = {
                "app_penguins" : "pag/img/penguin_logo.png",    
                "app_cars" : "pag/img/car.png", 
                "app_titanic" : "pag/img/boat.png",
                "app_dataupload" : "pag/img/boat.png"
        }

        for file in files:
                page_name = file.capitalize()
                pages.append(page_name.replace("_", " "))
                icons.append(icon_mapping.get(file, "bi-file"))
                module = importlib.import_module(f"pag.{file}")
                modules.append(module)

        return pages, icons, modules

pages, icons, modules = get_pages()

class MultiApp:
        def __init__(self):
                self.apps = []

        def add_app(self, title, funcion):
                title = title.replace("_", " ")
                self.apps.append({
                        "tile" : title,
                        "function" : funcion
                })

        def main():
            with st.sidebar:
                    app = option_menu(
                            menu_title="Menu",
                            options=pages,
                            menu_icon="bi-list",
                            default_index=0,
                            styles={
                                    "container": {"padding": "5!important", "background-color": "black"},
                                    "icon": {"color": "white", "font-size": "23px"},
                                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px"},
                                    "nav-link-selected": {"color": "black", "background-color": "#9ac280"}
                            }
                    )
            selected_index = pages.index(app)
            modules[selected_index].main()
if __name__ == "__main__":
       MultiApp.main()