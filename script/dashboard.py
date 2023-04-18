
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from PIL import Image

st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)
st.title("Analysis of player valuation")

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
    X_train, _, Y_train, _ = train_test_split(X,Y,test_size = 0.33, shuffle = True)
    regr = RandomForestRegressor(max_depth=2, random_state=0).fit(X_train, Y_train)
    return data, regr

df, model = load_data()
df = df.sort_values(['Player'],
              ascending = [True])
player = st.selectbox("Select the player to analyze", pd.unique(df["Player"]))
placeholder = st.empty()

if not player:
    st.error("Please select a players", icon="🚨")
else:
    st.write("### Input data for", player)

    # Extract player data
    df["col"] = df["Player"]==player
    player_df = df[df["col"]==1]
    # Plot all players
    st.write(player_df)
    imageString = '../data/images/clubs/' + player_df.loc[df['Player'] == player, 'Squad'].item() + ".png"
    leagueString = '../data/images/leagues/' + player_df.loc[df['Player'] == player, 'Comp'].item() + ".png"
    playerString = '../data/images/players/' + player_df.loc[df['Player'] == player, 'Player'].item() + ".png"
    if os.path.isfile(playerString):
        playerImage = Image.open(playerString)
    else:
        playerImage = Image.open('../data/images/players/!noImage.png')
    logo = Image.open(imageString)
    league = Image.open(leagueString)
    st.image([playerImage,logo,league,],width=100)

    fig = px.scatter(df,
                    x = "Goals", 
                    y = "market_value_in_eur", 
                    hover_name = "Player", 
                    color = "col",
                    labels = {'col': 'Choosen player:', 'market_value_in_eur': 'Market Value (EUR)'},
                    color_discrete_sequence=px.colors.qualitative.G10)
    st.plotly_chart(fig)

    st.write("### Model value prediction for", player)
    pred_df = player_df.drop(columns=["market_value_in_eur", "col"]).select_dtypes(exclude=['object'])
    pred_value = model.predict(pred_df).item(0)
    act_value = player_df["market_value_in_eur"].values.item(0)
    diff_pct = 100*(act_value/pred_value - 1)
    st.write("Estimated player value is", str(round(pred_value/(10**6))), "MEUR.")
    st.write("Actual player value is", str(round(act_value/(10**6))), "MEUR.")
    if act_value > pred_value:
        st.write("According to the model the  player is", str(round(diff_pct)), "percent overvalued.")
    else: 
        st.write("According to the model the  player is", str(round(-diff_pct)), "percent undervalued.")
    


