import streamlit as st
from pages import Dashboard, Sales_By_State

# Set page configuration
st.set_page_config(
    page_title="Welcome",  # Set the page title
    page_icon="📝",  # Set the page icon (optional)
    layout="centered",  # Can be "centered" or "wide"
    initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
)

# Dictionary to map page names to page modules
PAGES = {
    "Dashboard": Dashboard,
    "Sales By State": Sales_By_State,
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page
page = PAGES[selection]
page.app()

