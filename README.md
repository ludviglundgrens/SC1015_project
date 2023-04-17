# SC1015 - Football player valuation analysis
## About
This is a mini-project where we research the valuation of soccer players as a funciton of their performance in the season 2021/2022. The implications of our findings is easies explored thru the featured dashboard (built with [Streamlit](https://streamlit.io/)). To run the dashboard, make sure all dependencies are installed and run 

```console
  streamlit run ./script/dashboard.py
```

## Contributors
- @ludviglundgrens (N2202950F@e.ntu.edu.sg)
- @zaphrode (NAHID001@e.ntu.edu.sg)
- @twoeasy3 (YOH014@e.ntu.edu.sg)

## Problem Definition
- Utilizing multiple sources, we investigate if we are able to predict player valuation for the next season (2022 season), based on the player historical  player statistics
- We also analyses what machine learning model is suitable for this prediction.
- Using these player valuations, we identify potential undervalued players for clubs with budget constraints to purchase

## Problems Encountered:
- Player statistic dataset did not contain player valuation. Hence, needed to merge player statistic and player valuation dataset
- Dataset only contains outfield player attributes. Goalkeeping attributes not present, hence Goalkeepers need to be removed to prevent innacurate valuations.
- Attribute's importance varies between Attackers, Midfielders, Defenders. Hence, needed to filter out which attributes were important for each player. We first filtered it manually based on our football knowledge, trying to keep as many attributes as possible (below are tables of the manually filtered attributes). Then, we used SKLearn to find out which attributes were less important and could be removed.

## To do:
- Choose best model
- Do Neural Network
- Highlight Undervalued Players

## Done: 
- Merge datasets
- Filter out player_valuation dataset for dates before start of this season (2021-08-13 : 2022-08-06, start of Premiere League). 
- list attributes important to positions
- Remove Goalkeepers from Dataset
- Perform Exploratory Data Analysis & Visualisations

## Atrributes:

<details>
  <summary>Forwards</summary>

  |column|name|column|name|column|name|
  |------|----|------|----|------|----|
  |Age|Player Age|ScaPassLive|Completed live-ball passes that lead to a shot attempt|DriPast|Number of players dribbled past
  |MP|Matches Played|ScaPassDead|Completed dead-ball passes that lead to a shot attempt|Carries|Number of times the player controlled the ball with their feet
  |Min|Minutes Played|ScaDrib|Successful dribbles that lead to a shot attempt|CarPrgDist|Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal
  |90s|Minutes Played/90|ScaSh|Shots that lead to another shot attempt|CarProg|Carries that move the ball towards the opponent's goal at least 5 yards, or any carry into the penalty area
  |Goals|Goals Scored|ScaFld|Fouls drawn that lead to a shot attempt|Car3rd|Carries that enter the 1/3 of the pitch closest to the goal
  |Shots|Shots Taken (minus Penalties)|ScaDef|Defensive actions that lead to a shot attempt|CPA|Carries into the 18-yard box
  |SoT|Shots on Target (minus Penalties)|GCA|Goal-creating actions|CarMis|Number of times a player failed when attempting to gain control of a ball
  |SoT%|SoT as a percentage of shots taken|GcaPassLive|Completed live-ball passes that lead to a goal|CarDis|Number of times a player loses control of the ball after being tackled by an opposing player
  |G/Sh|Goals per Shot|GcaPassDead|Completed dead-ball passes that lead to a goal|RecTarg|Number of times a player was the target of an attempted pass
  |G/SoT|Goals per Shot on Target|GcaDrib|Successful dribbles that lead to a goal|Rec|Number of times a player successfully received a pass
  |ShoDist|Avg. Distance of shots from goal|GcaSh|Shots that lead to another goal-scoring shot|Rec%|Percentage of time a player successfully received a pass
  |ShoFK|Shots from Free Kicks|GcaFld|Fouls drawn that lead to a goal|RecProg|Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area
  |ShoPK|Penalty Kicks Taken|GcaDef|Defensive actions that lead to a goal|CrdY|Yellow cards
  |PasTotCmp|Passes Completed|Tkl|Number of players tackled|CrdR|Red cards
  |PasTotCmp%|Pass Completion %|TklWon|Tackles in which the tackler's team won possession of the ball|Fls|Fouls committed
  |PasTotPrgDist|Total Dist. of Completed Forward Passes towards Goal|TklAtt3rd|Tackles in attacking 1/3|Fld|Fouls drawn
  |Assists|Assists that lead to goals|Press%|Percentage of time the squad gained possession withing five seconds of applying pressure|Off|Offsides
  |PasAss|Passes to lead to shots|PresSucc|Number of times the squad gained possession withing five seconds of applying pressure|Crs|Crosses
  |PPA|Completed Passes into box|Touches|Number of times a player touched the ball. Note: Receiving a pass, then dribbling, then sending a pass counts as one touch|TklW|Tackles in which the tackler's team won possession of the ball
  |CrsPA|Completed Crosses into box|TouAtt3rd|Touches in attacking 1/3|PKwon|Penalty kicks won
  |PasProg|Progressive Passes|TouAttPen|Touches in attacking penalty area|AerWon|Aerials won
  |PasCrs|Crosses|DriSucc|Dribbles completed successfully|AerWon%|Percentage of aerials won
  |SCA|Shot-creating actions|DriSucc%|Percentage of dribbles completed successfully

  Age, MP, Min, 90s, Goals, Shots, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, PasTotCmp, PasTotCmp%, PasTotPrgDist, Assists, PasAss, PPA, CrsPA, PasProg, PasCrs, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklAtt3rd, Press%, PresSucc, Touches, TouAtt3rd, TouAttPen, DriSucc, DriSucc%, DriPast, Carries, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, AerWon, AerWon%

</details>


<details>
  <summary>Midfielders</summary>
  
|column|name|column|name|column|name|
|------|----|------|----|------|----|
|Age|Player's age|PasLonCmp%|Pass completion percentage (Passes longer than 30 yards)|PaswOther|Passes attempted using body parts other than the player's head or feet|TklMid3rd|Tackles in middle 1/3|TouLive|Live-ball touches. Does not include corner kicks, free kicks, throw-ins, kick-offs, goal kicks or penalty kicks|Crs|Crosses|
|MP|Mathces played|Assists|Assists|PasCmp|Passes completed|TklAtt3rd|Tackles in attacking 1/3|DriSucc|Dribbles completed successfully|TklW|Tackles in which the tackler's team won possession of the ball|
|90s|Minutes played divided by 90|PasAss|Passes that directly lead to a shot (assisted shots)|PasOff|Offsides|TklDri|Number of dribblers tackled|DriAtt|Dribbles attempted|PKwon|Penalty kicks won|
|Goals|Goals scored or allowed|Pas3rd|Completed passes that enter the 1/3 of the pitch closest to the goal|PasOut|Out of bounds|TklDriAtt|Number of times dribbled past plus number of tackles|DriSucc%|Percentage of dribbles completed successfully|PKcon|Penalty kicks conceded|
|SoT|Shots on target (Does not include penalty kicks)|PPA|Completed passes into the 18-yard box|PasInt|Intercepted|TklDri%|Percentage of dribblers tackled|DriPast|Number of players dribbled past|Recov|Number of loose balls recovered|
|SoT%|Shots on target percentage (Does not include penalty kicks)|CrsPA|Completed crosses into the 18-yard box|PasBlocks|Blocked by the opponent who was standing it the path|TklDriPast|Number of times dribbled past by an opposing player|DriMegs|Number of times a player dribbled the ball through an opposing player's legs|AerWon|Aerials won|
|G/Sh|Goals per shot|PasProg|Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area|SCA|Shot-creating actions|Press|Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball|Carries|Number of times the player controlled the ball with their feet|AerLost|Aerials lost|
|G/SoT|Goals per shot on target (Does not include penalty kicks)|PasAtt|Passes attempted|ScaPassLive|Completed live-ball passes that lead to a shot attempt|PresDef3rd|Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the defensive 1/3|CarTotDist|Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction|AerWon%|Percentage of aerials won|
|ShoDist|Average distance, in yards, from goal of all shots taken (Does not include penalty kicks)|PasLive|Live-ball passes|ScaPassDead|Completed dead-ball passes that lead to a shot attempt|PresMid3rd|Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the middle 1/3|CarPrgDist|Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal|
|ShoFK|Shots from free kicks|PasDead|Dead-ball passes|ScaDrib|Successful dribbles that lead to a shot attempt|PresAtt3rd|Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the attacking 1/3|CarProg|Carries that move the ball towards the opponent's goal at least 5 yards, or any carry into the penalty area|
|ShoPK|Penalty kicks made|PasFK|Passes attempted from free kicks|ScaSh|Shots that lead to another shot attempt|Blocks|Number of times blocking the ball by standing in its path|Car3rd|Carries that enter the 1/3 of the pitch closest to the goal|
|PasTotCmp|Passes completed|TB|Completed pass sent between back defenders into open space|ScaFld|Fouls drawn that lead to a shot attempt|BlkSh|Number of times blocking a shot by standing in its path|CPA|Carries into the 18-yard box|
|PasTotCmp%|Pass completion percentage|PasPress|Passes made while under pressure from opponent|ScaDef|Defensive actions that lead to a shot attempt|BlkShSv|Number of times blocking a shot that was on target, by standing in its path|CarMis|Number of times a player failed when attempting to gain control of a ball|
|PasTotDist|Total distance, in yards, that completed passes have traveled in any direction|Sw|Passes that travel more than 40 yards of the width of the pitch|GCA|Goal-creating actions|BlkPass|Number of times blocking a pass by standing in its path|CarDis|Number of times a player loses control of the ball after being tackled by an opposing player|
|PasTotPrgDist|Total distance, in yards, that completed passes have traveled towards the opponent's goal|PasCrs|Crosses|GcaPassLive|Completed live-ball passes that lead to a goal|Int|Interceptions|RecTarg|Number of times a player was the target of an attempted pass|
|PasShoCmp|Passes completed (Passes between 5 and 15 yards)|CK|Corner kicks|GcaPassDead|Completed dead-ball passes that lead to a goal|Clr|Clearances|Rec|Number of times a player successfully received a pass|
|PasShoAtt|Passes attempted (Passes between 5 and 15 yards)|PasGround|Ground passes|GcaDrib|Successful dribbles that lead to a goal|Err|Mistakes leading to an opponent's shot|Rec%|Percentage of time a player successfully received a pass|
|PasShoCmp%|Pass completion percentage (Passes between 5 and 15 yards)|PasLow|Passes that leave the ground, but stay below shoulder-level|GcaSh|Shots that lead to another goal-scoring shot|Touches|Number of times a player touched the ball. Note: Receiving a pass, then dribbling, then sending a pass counts as one touch|RecProg|Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area|
|PasMedCmp|Passes completed (Passes between 15 and 30 yards)|PasHigh|Passes that are above shoulder-level at the peak height|GcaFld|Fouls drawn that lead to a goal|TouDefPen|Touches in defensive penalty area|CrdY|Yellow cards|
|PasMedAtt|Passes attempted (Passes between 15 and 30 yards)|PaswLeft|Passes attempted using left foot|GcaDef|Defensive actions that lead to a goal|TouDef3rd|Touches in defensive 1/3|CrdR|Red cards|
|PasMedCmp%| Pass completion percentage (Passes between 15 and 30 yards)|PaswRight|Passes attempted using right foot|Tkl|Number of players tackled|TouMid3rd|Touches in middle 1/3|Fls|Fouls committed|
|PasLonCmp|Passes completed (Passes longer than 30 yards)|PaswHead|Passes attempted using head|TklWon|Tackles in which the tackler's team won possession of the ball|TouAtt3rd|Touches in attacking 1/3|Fld|Fouls drawn|
|PasLonAtt|Passes attempted (Passes longer than 30 yards)|TI|Throw-Ins taken|TklDef3rd|Tackles in defensive 1/3|TouAttPen|Touches in attacking penalty area|Off|Offsides|

Age, MP, Min, 90s, Goals, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, Assists, PasTotCmp, PasTotCmp%, PasTotDist, PasTotPrgDist, PasShoCmp, PasShoAtt, PasShoCmp%, PasMedCmp, PasMedAtt, PasMedCmp%, PasLonCmp, PasLonAtt, PasLonCmp%, Assists, PasAss, Pas3rd, PPA, CrsPA, PasProg, PasAtt, PasLive, PasDead, PasFK, TB, PasPress, Sw, PasCrs, CK, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouAttPen, TouLive, DriSucc, DriAtt, DriSucc%, DriPast, DriMegs, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, PKcon, Recov, AerWon, AerLost, AerWon%

</details>

<details>
  <summary>Defenders</summary>
  
|column|name|column|name|column|name|
|------|----|------|----|------|----|
|Age|Player's age|PaswLeft|Passes attempted using left foot|Press| Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball|CarPrgDist|Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent's goal|
|MP|Matches played|PaswRight|Passes attempted using right foot|PresSucc|Number of times the squad gained possession withing five seconds of applying pressure|CarProg|Carries that move the ball towards the opponent's goal at least 5 yards, or any carry into the penalty area|
|Min|Minutes played|PaswHead|Passes attempted using head|Press%|Percentage of time the squad gained possession withing five seconds of applying pressure|Car3rd|Carries that enter the 1/3 of the pitch closest to the goal|
|90s|Minutes played divided by 90|TI|Throw-Ins taken|PresDef3rd|Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the defensive 1/3|CarMis|Number of times a player failed when attempting to gain control of a ball|
|Goals|Goals scored or allowed|PaswOther|Passes attempted using body parts other than the player's head or feet|PresMid3rd| Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the middle 1/3|CarDis|Number of times a player loses control of the ball after being tackled by an opposing player|
|PasTotCmp|Passes completed|PasCmp|Passes completed|PresAtt3rd|Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the attacking 1/3|RecTarg|Number of times a player was the target of an attempted pass|
|PasTotAtt|Passes attempted|PasOff|Offsides|Blocks| Number of times blocking the ball by standing in its path|Rec|Number of times a player successfully received a pass|
|PasTotCmp%|Pass completion percentage|PasOut|Out of bounds|BlkSh|Number of times blocking a shot by standing in its path|Rec%|Percentage of time a player successfully received a pass|
|PasShoCmp%|Pass completion percentage (Passes between 5 and 15 yards)|PasInt|Intercepted|BlkShSv|Number of times blocking a shot that was on target, by standing in its path|RecProg|
|PasMedCmp%|Pass completion percentage (Passes between 15 and 30 yards)|PasBlocks|Blocked by the opponent who was standing it the path|BlkPass|Number of times blocking a pass by standing in its path|CrdY|Yellow cards|
|PasLonCmp%|Pass completion percentage (Passes longer than 30 yards)|ScaDef|Defensive actions that lead to a shot attempt|Int|Interceptions|CrdR|Red cards|
|Assists|Assists|GCA|Goal-creating actions|Tkl+In|Number of players tackled plus number of interceptions|Fls|Fouls committed|
|PasAss|Passes that directly lead to a shot (assisted shots)|GcaSh|Shots that lead to another goal-scoring shot|Clr|Clearances|Fld|Fouls drawn|
|PPA|Completed passes into the 18-yard box|GcaDef|Defensive actions that lead to a goal|Err|Mistakes leading to an opponent's shot|Off|Offsides|
|CrsPA|Completed crosses into the 18-yard box|Tkl|Number of players tackled|Touches|Number of times a player touched the ball. Note: Receiving a pass, then dribbling, then sending a pass counts as one touch|Crs|Crosses|
|PasProg| Completed passes that move the ball towards the opponent's goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area|TklWon|Tackles in which the tackler's team won possession of the ball|TouDefPen|Touches in defensive penalty area|TklW|Tackles in which the tackler's team won possession of the ball|
|TB|Completed pass sent between back defenders into open space|TklDef3rd|Tackles in defensive 1/3|TouDef3rd|Touches in defensive 1/3|PKcon|Penalty kicks conceded|
|PasPress|Passes made while under pressure from opponent|TklMid3rd|Tackles in middle 1/3|TouMid3rd|Touches in middle 1/3|OG|Own goals|
|Sw|Passes that travel more than 40 yards of the width of the pitch|TklAtt3rd|Tackles in attacking 1/3|TouAtt3rd|Touches in attacking 1/3|Recov|Number of loose balls recovered|
|PasCrs|Crosses|TklDri|Number of dribblers tackled|TouLive|Live-ball touches. Does not include corner kicks, free kicks, throw-ins, kick-offs, goal kicks or penalty kicks|AerWon|Aerials won|
|PasGround|Ground passes|TklDriAtt|Number of times dribbled past plus number of tackles|DriSucc%|Percentage of dribbles completed successfully|AerLost|Aerials lost|
|PasLow|Passes that leave the ground, but stay below shoulder-level|TklDri%|Percentage of dribblers tackled|Carries|Number of times the player controlled the ball with their feet|AerWon%|Percentage of aerials won|
|PasHigh|Passes that are above shoulder-level at the peak height|TklDriPast|Number of times dribbled past by an opposing player|CarTotDist|Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction|

Age, MP, Min, 90s, Goals, PasTotCmp, PasTotAtt, PasTotCmp%, PasTotDist, PasTotPrgDist, PasShoCmp%, PasMedCmp%, PasLonCmp%, Assists, PasAss, PPA, CrsPA, PasProg, TB, PasPress, Sw, PasCrs, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, ScaDef, GCA, GcaSh, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Tkl+Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouLive, DriSucc%, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKcon, OG, Recov, AerWon, AerLost, AerWon% 

</details>

