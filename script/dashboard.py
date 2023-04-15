
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.title("Player valuation dashboard")

@st.cache_data # make this function only run once (memoized)
def load_data():
    data = pd.read_csv("../data/merged_data.csv")
    positions = [(data.Pos == "FW") | (data.Pos == "FWMF") | (data.Pos == "FWDF"),
                (data.Pos == "MF") | (data.Pos == "MFFW") | (data.Pos == "MFDF"),
                (data.Pos == "DF") | (data.Pos == "DFMF") | (data.Pos == "DFFW")]
    posNames = ["Forward","Midfielder","Defender"]
    gPos = np.select(positions,posNames)

    # Create encoding for the categorical variable
    new_var = pd.get_dummies(gPos, drop_first=True)
    data = data.join(new_var)

    X = data.drop(columns=["market_value_in_eur"]).select_dtypes(exclude=['object'])
    Y = data['market_value_in_eur']
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.33, shuffle = True)
    regr = RandomForestRegressor(max_depth=2, random_state=0).fit(X_train, Y_train)
    return data, regr

df, model = load_data()

player = st.selectbox("Select the Job", pd.unique(df["Player"]))
placeholder = st.empty()

if not player:
    st.error("Please select a players")
else:
    st.write("Analysis of", player)
    
    # Extract player data
    df["col"] = df["Player"]==player
    # Plot all players
    fig = px.scatter(df,
                    x = "Goals", 
                    y = "market_value_in_eur", 
                    hover_name = "Player", 
                    color = "col",
                    labels = {'col': 'Choosen player:', 'market_value_in_eur': 'Market Value (EUR)'},
                    color_discrete_sequence=px.colors.qualitative.G10)

    # Mark out point with player
    # fig.add_scatter(player_df,
    #                 x = "Goals", 
    #                 y = "market_value_in_eur", 
    #                 hover_name = "Player")
    
    # Render chart to dashboard
    st.plotly_chart(fig)


