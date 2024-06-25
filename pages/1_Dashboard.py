import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
df = pd.read_csv('./data/Cleaned_data_06_25_2024.csv')
def app():
    # Create tabs
    index_tab, order_report, sales_report, inventory_report = st.tabs(["Order Analysis By Demographics", "Order Report", "Sales Report", "Inventory Report"])

    with index_tab:
        grouped_states_by_profit_data = df.groupby(['Country', 'State']).agg({
            'Row ID': 'count'
        }).reset_index().rename(columns={'Row ID': 'Count'}).sort_values('Count', ascending=True)
        top_states = grouped_states_by_profit_data.tail(10)
        x = top_states['State']
        y = top_states['Count']
        fig = px.bar(top_states, x=y, y=x, orientation='h', 
                    labels={'x': 'Count', 'y': 'States'},
                    title='Order Count By States')
        
        top_state = top_states.iloc[-1]['State']
        top_states_order = top_states.iloc[-1]['Count']    

        st.title('Order Analysis By States')
        col1, col2 = st.columns([1,2])
        with col1:
            st.dataframe(grouped_states_by_profit_data)
        
        with col2:
            st.plotly_chart(fig)

        st.markdown(f"""
            <div style="font-size: 18px; font-weight: bold;">{top_state} is the top order({top_states_order}) placing state</div>
        """, unsafe_allow_html=True)

    with order_report:
        st.header("Order Report")
        # Set the title of the Streamlit app
        st.title('Interactive Pie Chart')
        labels = st.text_input('Enter labels (comma-separated)', 'Label 1, Label 2, Label 3')
        values = st.text_input('Enter values (comma-separated)', '30, 40, 50')

        labels = [label.strip() for label in labels.split(',')]
        values = [int(val.strip()) for val in values.split(',')]

        # Create a pie chart using Plotly
        fig = px.pie(values=values, names=labels, title='Pie Chart')

        # Display the plot in Streamlit
        st.plotly_chart(fig)

    with sales_report:
        st.header("Sales Report")
        st.write("Content for Tab 3 goes here.")

    with inventory_report:
        st.header("Inventory Report")
        st.write("Content for Tab 3 goes here.")
    
if __name__ == "__main__":
    app()

    