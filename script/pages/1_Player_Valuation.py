import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
import os
from sklearn.linear_model import RidgeCV, LinearRegression
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
    csvFileLocation = os.path.dirname(os.getcwd())+"/data/merged_data.csv"
    data = pd.read_csv(csvFileLocation)
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

    return data, regr

df, model = load_data()
df = df.sort_values(['Comp','Squad','Player'],
              ascending = [True,True,True])
pLeague = st.selectbox("Sort by League", pd.unique(df["Comp"]))
pClub = st.selectbox("Sort by Club", pd.unique(df.loc[df['Comp'] == pLeague, 'Squad']))
player = st.selectbox("Select the player to analyze", pd.unique(df.loc[df['Squad'] == pClub, 'Player']))
placeholder = st.empty()

if not player:
    st.error("Please select a player", icon="🚨")
else:
    st.write("### Input data for", player)

    # Extract player data
    df["col"] = df["Player"]==player
    player_df = df[df["col"]==1]
    # Plot all players
    st.write(player_df)
    ##Image file paths
    imageString = os.path.dirname(os.getcwd())+'/data/images/clubs/' + player_df.loc[df['Player'] == player, 'Squad'].item() + ".png"
    leagueString = os.path.dirname(os.getcwd())+'/data/images/leagues/' + player_df.loc[df['Player'] == player, 'Comp'].item() + ".png"
    playerString = os.path.dirname(os.getcwd())+'/data/images/players/' + player_df.loc[df['Player'] == player, 'Player'].item() + ".png"
    ##If player image does not exist, default image
    if os.path.isfile(playerString):
        playerImage = Image.open(playerString)
    else:
        playerImage = Image.open(os.path.dirname(os.getcwd())+'/data/images/players/!noImage.png')
    logo = Image.open(imageString)
    league = Image.open(leagueString)
    st.image([playerImage,logo,league,],width=100)

    stat = st.selectbox("Select the statistic to analyze", options = ["MP","Age","Starts","Min","90s","Goals","Shots","SoT","SoT%","G/Sh","G/SoT","ShoDist",
                                                               "ShoFK","ShoPK","PKatt","PasTotCmp","PasTotAtt","PasTotCmp%","PasTotDist",
                                                               "PasTotPrgDist","PasShoCmp","PasShoAtt","PasShoCmp%","PasMedCmp","PasMedAtt",
                                                               "PasMedCmp%","PasLonCmp","PasLonAtt","PasLonCmp%","Assists","PasAss","Pas3rd",
                                                               "PPA","CrsPA","PasProg","PasAtt","PasLive","PasDead","PasFK","TB","PasPress","Sw",
                                                               "PasCrs","CK","CkIn","CkOut","CkStr","PasGround","PasLow","PasHigh","PaswLeft",
                                                               "PaswRight","PaswHead","TI","PaswOther","PasCmp","PasOff","PasOut","PasInt","PasBlocks",
                                                               "SCA","ScaPassLive","ScaPassDead","ScaDrib","ScaSh","ScaFld","ScaDef","GCA",
                                                               "GcaPassLive","GcaPassDead","GcaDrib","GcaSh","GcaFld","GcaDef","Tkl","TklWon",
                                                               "TklDef3rd","TklMid3rd","TklAtt3rd","TklDri","TklDriAtt","TklDri%","TklDriPast",
                                                               "Press","PresSucc","Press%","PresDef3rd","PresMid3rd","PresAtt3rd","Blocks","BlkSh",
                                                               "BlkShSv","BlkPass","Int","Tkl+Int","Clr","Err","Touches","TouDefPen","TouDef3rd",
                                                               "TouMid3rd","TouAtt3rd","TouAttPen","TouLive","DriSucc","DriAtt","DriSucc%","DriPast",
                                                               "DriMegs","Carries","CarTotDist","CarPrgDist","CarProg","Car3rd","CPA","CarMis","CarDis",
                                                               "RecTarg","Rec","Rec%","RecProg","CrdY","CrdR","2CrdY","Fls","Fld","Off","Crs","TklW",
                                                               "PKwon","PKcon","OG","Recov","AerWon","AerLost","AerWon%"])

    scope = st.selectbox("Select the scope to analyze", options = ["All", "Same League", "Same Club"])
    if scope == "All":
        st.write("Comparison to all players in database")
        fig = px.scatter(df,
                        x = stat, 
                        y = "market_value_in_eur", 
                        hover_name = "Player", 
                        color = "col",
                        labels = {'col': 'Choosen player:', 'market_value_in_eur': 'Market Value (EUR)'},
                        color_discrete_sequence=px.colors.qualitative.G10)
        st.plotly_chart(fig)
        percentile_rank = round((df[df[stat] <= (player_df.loc[df['Player'] == player, stat].item())].size / df.size) * 100,2)
        st.write("{0} is in the {1}th percentile in {2}".format(player,percentile_rank,stat))
        
    if scope == "Same League":
        st.write("Comparison to all players in", pLeague)
        fig = px.scatter(df.loc[df['Comp'] == pLeague],
                        x = stat, 
                        y = "market_value_in_eur", 
                        hover_name = "Player", 
                        color = "col",
                        labels = {'col': 'Choosen player:', 'market_value_in_eur': 'Market Value (EUR)'},
                        color_discrete_sequence=px.colors.qualitative.G10)
        st.plotly_chart(fig)
        percentile_rank = round((df.loc[df['Comp'] == pLeague][df.loc[df['Comp'] == pLeague][stat] <= (player_df.loc[df['Player'] == player, stat].item())].size / df.loc[df['Comp'] == pLeague].size) * 100,2)
        st.write("{0} is in the {1}th percentile in {2}".format(player,percentile_rank,stat))
        
    if scope == "Same Club":
        st.write("Comparison to all players in", pClub, "," , pLeague)
        fig = px.scatter(df.loc[df['Squad'] == pClub],
                        x = stat, 
                        y = "market_value_in_eur", 
                        hover_name = "Player", 
                        color = "col",
                        labels = {'col': 'Choosen player:', 'market_value_in_eur': 'Market Value (EUR)'},
                        color_discrete_sequence=px.colors.qualitative.G10)
        st.plotly_chart(fig)
        percentile_rank = round((df.loc[df['Squad'] == pClub][df.loc[df['Squad'] == pClub][stat] <= (player_df.loc[df['Player'] == player, stat].item())].size / df.loc[df['Squad'] == pClub].size) * 100,2)
        st.write("{0} is in the {1}th percentile in {2}".format(player,percentile_rank,stat))
    
    st.write("### Model value prediction for", player)
    pred_df = player_df.drop(columns=["market_value_in_eur", "col"]).select_dtypes(exclude=['object'])
    pred_value = model.predict(pred_df).item(0)
    act_value = player_df["market_value_in_eur"].values.item(0)
    diff_pct = 100*(act_value/pred_value - 1)
    st.write("Estimated player value is", str(round(pred_value/(10**6),2)), "MEUR.")
    st.write("Actual player value is", str(round(act_value/(10**6),2)), "MEUR.")
    if act_value > pred_value:
        st.write("According to the model the  player is", str(round(diff_pct)), "percent overvalued.")
    else: 
        st.write("According to the model the  player is", str(round(-diff_pct)), "percent undervalued.")
    
