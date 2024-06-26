import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

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
        }).reset_index().rename(columns={'Row ID': 'Count'}).sort_values('Count', ascending=False)
        top_states = grouped_states_by_profit_data.head(10)
        x = top_states['State']
        y = top_states['Count']
        fig = px.bar(top_states, x=x, y=y, orientation='v', 
                    labels={'x': 'Count', 'y': 'States'},
                    title='Order Count By States')
        
        top_state = top_states.iloc[0]['State']
        top_states_order = top_states.iloc[0]['Count']    

        #Order Analysis By States- Visualization
        st.markdown('<h1 style="text-align:center; font-size:44px;">Order Analysis By States</h1>', unsafe_allow_html=True)
        col1, col2 = st.columns([1,2])
        with col1:
            st.dataframe(grouped_states_by_profit_data, use_container_width=True)
        
        with col2:
            st.plotly_chart(fig, use_container_width=True)

        st.markdown(f"""
            <div style="font-size: 18px; font-weight: bold;">{top_state} is the top order({top_states_order}) placing state</div>
        """, unsafe_allow_html=True)

        #Order Analysis By Country-City Visualization
        st.markdown('<h1 style="text-align:center; font-size:44px;">Order Count Grouped by States and Cities</h1>', unsafe_allow_html=True)
        grouped_data_by_States_and_Cities = df.groupby(['State', 'City']).size().reset_index(name='OrderCount').sort_values('OrderCount', ascending=True).tail(10)
        col1, col2 = st.columns([2,1])
        fig = px.bar(grouped_data_by_States_and_Cities, x='OrderCount', y='City', color='State',
                    title='Order Count Grouped by States and Cities',
                    labels={'OrderCount': 'Order Count', 'City': 'City'})
        with col1:
            st.plotly_chart(fig, use_container_width=True)
        with col2:            
            st.dataframe(grouped_data_by_States_and_Cities.reset_index(drop=True), use_container_width=True)
            
        #Order Analysis By Region- Visualization
        st.title('Order Analysis By Region')
        grouped_region_by_profit_data = df.groupby(['Country','Region']).agg({
            'Row ID': 'count'
        }).reset_index().rename(columns={'Row ID': 'Count'}).sort_values('Count', ascending=True)

        fig = go.Figure(data=[go.Pie(labels=grouped_region_by_profit_data['Region'], values=grouped_region_by_profit_data['Count'])])
        st.plotly_chart(fig, use_container_width=True)
        st.dataframe(grouped_region_by_profit_data, use_container_width=True)

        
        
            
        
    with order_report:
        pass

    with sales_report:
        st.header("Sales Report")
        st.write("Content for Tab 3 goes here.")

    with inventory_report:
        st.header("Inventory Report")
        st.write("Content for Tab 3 goes here.")
    
if __name__ == "__main__":
    app()

    