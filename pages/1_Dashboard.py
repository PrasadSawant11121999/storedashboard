import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="🛒",         # Optional: Set an icon for the app
    layout="wide"           # Optional: Set the layout to wide
)
st.markdown("""
    <style>
            .st-emotion-cache-15ecox0.ezrtsby0{
                display:none !important;
            }
            .eczjsme10::first-letter {
                text-transform: uppercase;
            }
            .st-emotion-cache-1jicfl2 {
                padding-top: 32px !important;
            }
    </style>
""",unsafe_allow_html=True)
def app():
    # Create tabs
    index_tab, order_report, sales_report, inventory_report = st.tabs(["Index", "Order Report", "Sales Report", "Inventory Report"])

    with index_tab:
        st.header("Index")
        st.write("Content for Tab 1 goes here.")

    with order_report:
        st.header("Order Report")
        st.write("Content for Tab 2 goes here.")

    with sales_report:
        st.header("Sales Report")
        st.write("Content for Tab 3 goes here.")

    with inventory_report:
        st.header("Inventory Report")
        st.write("Content for Tab 3 goes here.")
    
if __name__ == "__main__":
    app()