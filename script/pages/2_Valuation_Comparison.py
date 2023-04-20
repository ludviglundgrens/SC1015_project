import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import os
from sklearn.linear_model import RidgeCV, LinearRegression
from sklearn.model_selection import train_test_split
from PIL import Image

st.set_page_config(
    page_title="Valuation Comparison",
    page_icon="✅",
    layout="wide",
)
st.title("Valuation comparison")

@st.cache_data # make this function only run once (memoized)
def load_data():
    data = pd.read_csv("./data/merged_data.csv")
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
    Y_log = np.log(Y)

    X_train, _, Y_train, _ = train_test_split(X,Y_log,test_size = 0.33, shuffle = True, random_state = 0)
    regr = LinearRegression().fit(X_train, Y_train)
    pred_Y_log = regr.predict(X)
    pred_Y = np.exp(pred_Y_log)
    
    return data, regr, pred_Y, Y

df, model, pred_Y, Y = load_data()
df = df.sort_values(['Comp','Squad','Player'],
              ascending = [True,True,True])

#pLeague = st.selectbox("Sort by League", pd.unique(df["Comp"]))
#pClub = st.selectbox("Sort by Club", pd.unique(df.loc[df['Comp'] == pLeague, 'Squad']))
#player = st.selectbox("Select the player to analyze", pd.unique(df.loc[df['Squad'] == pClub, 'Player']))
#placeholder = st.empty()

info = pd.DataFrame(df[["name", 'Comp', 'Squad']])
pred_Y = pd.DataFrame(pred_Y, columns = ["predicted_market_value_in_eur"])

comparison = info.join(Y).join(pred_Y).round().reset_index(drop = True)
comparison["Undervalued(+) / Overvalued(-)"] = round((comparison["predicted_market_value_in_eur"]/comparison["market_value_in_eur"] - 1)*100, 2)

st.write(comparison)

