import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
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
        st.title('Interactive Horizontal Bar Plot')

        categories = st.text_input('Enter categories (comma-separated)', 'Category A, Category B, Category C, Category D')
        values = st.text_input('Enter values (comma-separated)', '23, 45, 56, 78')

        categories = [cat.strip() for cat in categories.split(',')]
        values = [int(val.strip()) for val in values.split(',')]

        # Create a horizontal bar plot using Plotly
        fig = go.Figure(go.Bar(
            y=categories,
            x=values,
            orientation='h'
        ))

        fig.update_layout(
            title='Horizontal Bar Plot',
            xaxis_title='Values',
            yaxis_title='Categories',
        )

        # Display the plot in Streamlit
        st.plotly_chart(fig)

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

    