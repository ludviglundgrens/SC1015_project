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
|Age|Player Age|
|MP|Matches Played|
|Min|Minutes Played|
|90s|Minutes Played/90|
|Goals|Goals Scored|
|Shots|Shots Taken (minus Penalties)|
|SoT|Shots on Target (minus Penalties)|
|SoT%|SoT as a percentage of shots taken|
|G/Sh|Goals per Shot|
|G/SoT|Goals per Shot on Target|
|ShoDist|Avg. Distance of shots from goal|
|ShoFK|Shots from Free Kicks|
|ShoPK|Penalty Kicks Taken|
|PasTotCmp|Passes Completed|
|PasTotCmp%|Pass Completion %|
|PasTotPrgDist|Total Dist. of Completed Forward Passes towards Goal|
|Assists|Assists that lead to goals|
|PasAss|Passes to lead to shots|
|PPA|Completed Passes into box|
|CrsPA|Completed Crosses into box|
|PasProg|Progressive Passes|
|PasCrs|
|SCA|

Player's age, MP, Min, 90s, Goals, Shots, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, PasTotCmp, PasTotCmp%, PasTotPrgDist, Assists, PasAss, PPA, CrsPA, PasProg, PasCrs, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklAtt3rd, Press%, PresSucc, Touches, TouAtt3rd, TouAttPen, DriSucc, DriSucc%, DriPast, Carries, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, AerWon, AerWon%

-Midfielders: Player's age, MP, Min, 90s, Goals, SoT, SoT%, G/Sh, G/SoT, ShoDist, ShoFK, ShoPK, Assists, PasTotCmp, PasTotCmp%, PasTotDist, PasTotPrgDist, PasShoCmp, PasShoAtt, PasShoCmp%, PasMedCmp, PasMedAtt, PasMedCmp%, PasLonCmp, PasLonAtt, PasLonCmp%, Assists, PasAss, Pas3rd, PPA, CrsPA, PasProg, PasAtt, PasLive, PasDead, PasFK, TB, PasPress, Sw, PasCrs, CK, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, SCA, ScaPassLive, ScaPassDead, ScaDrib, ScaSh, ScaFld, ScaDef, GCA, GcaPassLive, GcaPassDead, GcaDrib, GcaSh, GcaFld, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouAttPen, TouLive, DriSucc, DriAtt, DriSucc%, DriPast, DriMegs, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CPA, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKwon, PKcon, Recov, AerWon, AerLost, AerWon%

-Defenders: Player's age, MP, Min, 90s, Goals, PasTotCmp, PasTotAtt, PasTotAtt, PasTotAtt, PasTotPrgDist, PasShoCmp%, PasMedCmp%, PasLonCmp%, Assists, PasAss, PPA, CrsPA, PasProg, TB, PasPress, Sw, PasCrs, PasGround, PasLow, PasHigh, PaswLeft, PaswRight, PaswHead, TI, PaswOther, PasCmp, PasOff, PasOut, PasInt, PasBlocks, ScaDef, GCA, GcaSh, GcaDef, Tkl, TklWon, TklDef3rd, TklMid3rd, TklAtt3rd, TklDri, TklDriAtt, TklDri%, TklDriPast, Press, PresSucc, Press%, PresDef3rd, PresMid3rd, PresAtt3rd, Blocks, BlkSh, BlkShSv, BlkPass, Int, Tkl+Int, Clr, Err, Touches, TouDefPen, TouDef3rd, TouMid3rd, TouAtt3rd, TouLive, DriSucc%, Carries, CarTotDist, CarPrgDist, CarProg, Car3rd, CarMis, CarDis, RecTarg, Rec, Rec%, RecProg, CrdY, CrdR, Fls, Fld, Off, Crs, TklW, PKcon, OG, Recov, AerWon, AerLost, AerWon%  
