import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

from portfolio import portfolio

# ********** Initializing the application **********
st.set_page_config(page_title="Image Processing Portal", page_icon=":large_blue_circle:", layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# **********Driver Class********** #
class HomePage:

    def initializeMainMenu(self) -> None:
        """
        Displaying the options the user can click on and handling the event performed
        """
        with st.sidebar:
            self.selectedOption = option_menu(
                menu_title="Menu",
                options=["Portfolio", "Sell"],
                default_index=0,
            )

        if self.selectedOption == "Portfolio":
            df = pd.read_csv('local.csv')
            portfolio(df)
        elif self.selectedOption == "Sell":
            pass


if __name__ == "__main__":
    page = HomePage()
    page.initializeMainMenu()



