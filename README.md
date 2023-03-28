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
|Age|Player Age|ScaPassLive|Completed live-ball passes that lead to a shot attempt|DriPast|
|MP|Matches Played|ScaPassDead|Completed dead-ball passes that lead to a shot attempt|
|Min|Minutes Played|ScaDrib|Successful dribbles that lead to a shot attempt|
|90s|Minutes Played/90|ScaSh|Shots that lead to another shot attempt|
|Goals|Goals Scored|ScaFld|Fouls drawn that lead to a shot attempt|
|Shots|Shots Taken (minus Penalties)|ScaDef|Defensive actions that lead to a shot attempt|
|SoT|Shots on Target (minus Penalties)|GCA|Goal-creating actions|
|SoT%|SoT as a percentage of shots taken|GcaPassLive|Completed live-ball passes that lead to a goal|
|G/Sh|Goals per Shot|GcaPassDead|Completed dead-ball passes that lead to a goal
|G/SoT|Goals per Shot on Target|GcaDrib|Successful dribbles that lead to a goal
|ShoDist|Avg. Distance of shots from goal|GcaSh|Shots that lead to another goal-scoring shot
|ShoFK|Shots from Free Kicks|GcaFld|Fouls drawn that lead to a goal
|ShoPK|Penalty Kicks Taken|GcaDef|Defensive actions that lead to a goal
|PasTotCmp|Passes Completed|Tkl|Number of players tackled
|PasTotCmp%|Pass Completion %|TklWon|Tackles in which the tackler's team won possession of the ball
|PasTotPrgDist|Total Dist. of Completed Forward Passes towards Goal|TklAtt3rd|
|Assists|Assists that lead to goals|Press%|Percentage of time the squad gained possession withing five seconds of applying pressure
|PasAss|Passes to lead to shots|PresSucc|Number of times the squad gained possession withing five seconds of applying pressure
|PPA|Completed Passes into box|Touches|Number of times a player touched the ball. Note: Receiving a pass, then dribbling, then sending a pass counts as one touch
|CrsPA|Completed Crosses into box|TouAtt3rd|Touches in attacking 1/3
|PasProg|Progressive Passes|TouAttPen|Touches in attacking penalty area
|PasCrs|Crosses|DriSucc|Dribbles completed successfully
|SCA|Shot-creating actions|DriSucc%|Percentage of dribbles completed successfully

Player's age, MP, Min, 90s, Goals, Shots, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, PasTotCmp, PasTotCmp%, PasTotPrgDist, Assists, PasAss, PPA, CrsPA, PasProg, PasCrs, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklAtt3rd, Press%, PresSucc, Touches, TouAtt3rd, TouAttPen, DriSucc, DriSucc%, DriPast, Carries, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, AerWon, AerWon%

-Midfielders: Player's age, MP, Min, 90s, Goals, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, Assists, PasTotCmp, PasTotCmp%, PasTotDist, PasTotPrgDist, PasShoCmp, PasShoAtt, PasShoCmp%, PasMedCmp, PasMedAtt, PasMedCmp%, PasLonCmp, PasLonAtt, PasLonCmp%, Assists, PasAss, Pas3rd, PPA, CrsPA, PasProg, PasAtt, PasLive, PasDead, PasFK, TB, PasPress, Sw, PasCrs, CK, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouAttPen, TouLive, DriSucc, DriAtt, DriSucc%, DriPast, DriMegs, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, PKcon, Recov, AerWon, AerLost, AerWon%

-Defenders: Player's age, MP, Min, 90s, Goals, PasTotCmp, PasTotAtt, PasTotAtt, PasTotAtt, PasTotPrgDist, PasShoCmp%, PasMedCmp%, PasLonCmp%, Assists, PasAss, PPA, CrsPA, PasProg, TB, PasPress, Sw, PasCrs, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, ScaDef, GCA, GcaSh, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Tkl+Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouLive, DriSucc%, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKcon, OG, Recov, AerWon, AerLost, AerWon%  
