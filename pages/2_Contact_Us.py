import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Contact Me",
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
   # Sample DataFrame with state and order count
    data = {
        'State': ['CA', 'TX', 'NY', 'FL', 'IL', 'PA', 'OH', 'GA', 'NC', 'MI'],
        'OrderCount': [1500, 1200, 900, 850, 700, 650, 600, 550, 500, 450]
    }

    df = pd.DataFrame(data)

    # Creating the choropleth map for US states
    fig = px.choropleth(df, locations='State', locationmode='USA-states', 
                        color='OrderCount', hover_name='State',
                        color_continuous_scale=px.colors.sequential.Plasma,
                        scope='usa', title='Order Count by State')

    # Setting the layout to make the map more readable
    fig.update_layout(
        margin={"r":0,"t":30,"l":0,"b":0}
    )

    # Displaying the map in Streamlit
    st.title('Order Distribution by State in USA')
    st.plotly_chart(fig, use_container_width=True)

    
if __name__ == "__main__":
    app()

