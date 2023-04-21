import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st
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

info = pd.DataFrame(df[["name", 'Comp', 'Squad','Pos']])
pred_Y = pd.DataFrame(pred_Y, columns = ["predicted_market_value_in_eur"])

comparison = info.join(Y).join(pred_Y).round().reset_index(drop = True)
comparison["Undervalued(+) / Overvalued(-)"] = round((comparison["predicted_market_value_in_eur"]/comparison["market_value_in_eur"] - 1)*100, 2)

st.write(comparison)
#////This entire code here is for the best value 11
st.write("### Best Value XI")
st.write("Picking the most undervalued players in a standard 4-4-2 formation, our algorithm deems this squad to be the best value for money")

xCoord = [0.25,0.5,0,0.25,0.5,0.75,0,0.25,0.5,0.75,0.375]
yCoord = [1,1,0.75,0.75,0.75,0.75,0.5,0.5,0.5,0.5,0.25]
sort_order = ["FW","FWMF","FWDF","MF","MFFW","MFDF","DF","DFMF","DFFW","GK"]


bargainEleven = ['Felipe','Álvaro González','Kike Hermoso','Óscar Gil','Luca Wollschläger','Vanderson',
                 'Davide Marfella','Ibrahima Diallo','Fabinho','Luca Gagliano','Jonas Hofmann']


selectedPlayers = df['Player'].isin(bargainEleven)
df11 = df[selectedPlayers]
df11['Pos']= pd.Categorical(df11['Pos'], categories=sort_order, ordered=True)
df11=df11.sort_values('Pos')
df11 = df11.assign(xCoord = xCoord)
df11 = df11.assign(yCoord = yCoord)

fig = px.scatter(df11,
                x = 'xCoord', 
                y = 'yCoord', 
                hover_name = "Player",
                width = 600,
                height = 800,
                opacity = 0,
                hover_data={'xCoord':False,'yCoord':False,'Squad':True,'Comp':True},
                color_discrete_sequence=px.colors.qualitative.G10)


fig.update_layout(
    coloraxis_showscale=False,
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
)

fig.update_xaxes(showticklabels=False,range = [-0.125,0.875])
fig.update_yaxes(showticklabels=False,range = [0.110,1.125])
fig.update_xaxes(title_text='')
fig.update_yaxes(title_text='')
fig.update_traces(marker={'size': 100})

import base64
pitch = base64.b64encode(open("./data/images/data/pitch.jpg",'rb').read())
fig.update_layout(images = [dict(source='data:image/jpg;base64,{}'.format(pitch.decode()), xref="paper", yref="paper",
                    x=0, y=1,
                    sizex=1, sizey=1,
                    xanchor="left",
                    yanchor="top",
                    sizing="stretch",
                    layer="below")])

for index, row in df11.iterrows():
    imageLocation = './data/images/players/'+row['Player'] +'.png'
    imageEncode = base64.b64encode(open(imageLocation,'rb').read())
    fig.add_layout_image(dict(source='data:image/png;base64,{}'.format(imageEncode.decode()),
                        x=row['xCoord']+0.125,
                        y=row['yCoord']-0.1,
                        xref='paper',
                        yref='paper',
                        sizex=0.20, sizey=0.20,
                        xanchor="center",
                        yanchor="middle",
                        layer="above"))

fig.update_layout()
st.plotly_chart(fig)

#////This entire code here is for the worst value 11
st.write("### Overvalued XI")
st.write("Our algorithm picked out this team to command transfer fees far beyond their recent contributions on the pitch.")

valueEleven = ['Moise Kean','Joel Pohjanpalo','Baptiste Santamaria','Cesc Fàbregas','Kalvin Phillips',
              'Wilfred Ndidi','Chris Richards','Leonardo Spinazzola','Lennard Maloney','Andrea Conti','David Raya']


selectedPlayers = df['Player'].isin(valueEleven)
df11o = df[selectedPlayers]
df11o['Pos']= pd.Categorical(df11o['Pos'], categories=sort_order, ordered=True)
df11o=df11o.sort_values('Pos')
df11o = df11o.assign(xCoord = xCoord)
df11o = df11o.assign(yCoord = yCoord)

fig = px.scatter(df11o,
                x = 'xCoord', 
                y = 'yCoord', 
                hover_name = "Player",
                width = 600,
                height = 800,
                opacity = 0,
                hover_data={'xCoord':False,'yCoord':False,'Squad':True,'Comp':True},
                color_discrete_sequence=px.colors.qualitative.G10)


fig.update_layout(
    coloraxis_showscale=False,
    xaxis=dict(showgrid=False, zeroline=False),
    yaxis=dict(showgrid=False, zeroline=False),
)

fig.update_xaxes(showticklabels=False,range = [-0.125,0.875])
fig.update_yaxes(showticklabels=False,range = [0.110,1.125])
fig.update_xaxes(title_text='')
fig.update_yaxes(title_text='')
fig.update_traces(marker={'size': 100})

import base64
pitch = base64.b64encode(open("./data/images/data/pitch.jpg",'rb').read())
fig.update_layout(images = [dict(source='data:image/jpg;base64,{}'.format(pitch.decode()), xref="paper", yref="paper",
                    x=0, y=1,
                    sizex=1, sizey=1,
                    xanchor="left",
                    yanchor="top",
                    sizing="stretch",
                    layer="below")])

for index, row in df11o.iterrows():
    imageLocation = './data/images/players/'+row['Player'] +'.png'
    imageEncode = base64.b64encode(open(imageLocation,'rb').read())
    fig.add_layout_image(dict(source='data:image/png;base64,{}'.format(imageEncode.decode()),
                        x=row['xCoord']+0.125,
                        y=row['yCoord']-0.1,
                        xref='paper',
                        yref='paper',
                        sizex=0.20, sizey=0.20,
                        xanchor="center",
                        yanchor="middle",
                        layer="above"))


fig.update_layout()
st.plotly_chart(fig)

