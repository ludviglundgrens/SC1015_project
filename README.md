# SC1015 - Football player valuation analysis
## About
This is a Mini-project 

## Contributors
- @ludviglundgrens (N2202950F@e.ntu.edu.sg)
- @zaphrode (NAHID001@e.ntu.edu.sg)
- @twoeasy3 (YOH014@e.ntu.edu.sg)

## Problem Definition
- Utilizing multiple sources, we investigate if we are able to predict player valuation for the next season (2022 season), based on the player historical  player statistics. 
- We also analyses what machine learning model is suitable for this prediction.

## Done: 
- Merge datasets
- Filter out player_valuation dataset for dates before start of this season (2021-08-13 : 2022-08-06, start of Premiere League). 
- list attributes important to positions

### To do:
- Remove Goalkeepers from Dataset
- Perform Exploratory Data Analysis & Visualisations



#Atrributes:
-Forwards: 
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

Player's age, MP, Min, 90s, Goals, Shots, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, PasTotCmp, PasTotCmp%, PasTotPrgDist, Assists, PasAss, PPA, CrsPA, PasProg, PasCrs, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklAtt3rd, Press%, PresSucc, Touches, TouAtt3rd, TouAttPen, DriSucc, DriSucc%, DriPast, Carries, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, AerWon, AerWon%

-Midfielders: Player's age, MP, Min, 90s, Goals, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, Assists, PasTotCmp, PasTotCmp%, PasTotDist, PasTotPrgDist, PasShoCmp, PasShoAtt, PasShoCmp%, PasMedCmp, PasMedAtt, PasMedCmp%, PasLonCmp, PasLonAtt, PasLonCmp%, Assists, PasAss, Pas3rd, PPA, CrsPA, PasProg, PasAtt, PasLive, PasDead, PasFK, TB, PasPress, Sw, PasCrs, CK, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouAttPen, TouLive, DriSucc, DriAtt, DriSucc%, DriPast, DriMegs, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, PKcon, Recov, AerWon, AerLost, AerWon%

-Defenders: Player's age, MP, Min, 90s, Goals, PasTotCmp, PasTotAtt, PasTotAtt, PasTotAtt, PasTotPrgDist, PasShoCmp%, PasMedCmp%, PasLonCmp%, Assists, PasAss, PPA, CrsPA, PasProg, TB, PasPress, Sw, PasCrs, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, ScaDef, GCA, GcaSh, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Tkl+Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouLive, DriSucc%, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKcon, OG, Recov, AerWon, AerLost, AerWon%  
