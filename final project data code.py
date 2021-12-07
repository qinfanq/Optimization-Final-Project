# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:01:46 2021

@author: kiraqian
"""

import pandas as pd


# dataframe for retail centers demands
demand = []
demandfy = [1000,1200,1800,1200,1000,1400,1600,1000]
for x in demandfy:
    retailcenter = []
    for t in range(1,11):
        if x == demandfy[1-1] or x == demandfy[2-1] or x == demandfy[4-1] or x == demandfy[5-1] or x == demandfy[8-1]:
            d = x+0.20*(x)*(t-1)
            retailcenter.append(d)
        else:
            d = x+0.25*(x)*(t-1)
            retailcenter.append(d)
    demand.append(retailcenter)
dfdemand = pd.DataFrame(demand,columns=[1,2,3,4,5,6,7,8,9,10])
dfdemand.index = [1,2,3,4,5,6,7,8]
dfdemand
print(dfdemand)

# columns are years, rows are retaliers
# select values through indexing column and row: dfdemand[1][2]

# dataframe for construction costs
conscost = []
conscostfy = [2000,1600,1800,900,1500]
for x in conscostfy:
    plant = []
    for t in range(1,11):
        cc = x*(1+0.03)**(t-1)
        plant.append(cc)
    conscost.append(plant)

dfconscost = pd.DataFrame(conscost,columns=[1,2,3,4,5,6,7,8,9,10])
dfconscost.index = [1,2,3,4,5]
dfconscost

# dataframe for annual operating costs
aocost = []
aocostfy = [420,380,460,280,340]
for x in aocostfy:
    plant = []
    for t in range(1,11):
        aoc = x*(1+0.03)**(t-1)
        plant.append(aoc)
    aocost.append(plant)

dfaocost = pd.DataFrame(aocost,columns=[1,2,3,4,5,6,7,8,9,10])
dfaocost.index = [1,2,3,4,5]
dfaocost

# dataframe for reopening costs
rocost = []
rocostfy = [190,150,160,100,130]
for x in rocostfy:
    plant = []
    for t in range(1,11):
        roc = x*(1+0.03)**(t-1)
        plant.append(roc)
    rocost.append(plant)

dfrocost = pd.DataFrame(rocost,columns=[1,2,3,4,5,6,7,8,9,10])
dfrocost.index = [1,2,3,4,5]
dfrocost

# dataframe for shutdown costs
sdcost = []
sdcostfy = [170,120,130,80,110]
for x in sdcostfy:
    plant = []
    for t in range(1,11):
        sdc = x*(1+0.03)**(t-1)
        plant.append(sdc)
    sdcost.append(plant)

dfsdcost = pd.DataFrame(sdcost,columns=[1,2,3,4,5,6,7,8,9,10])
dfsdcost.index = [1,2,3,4,5]
dfsdcost

# dataframes for warehouse shipping costs
# warehouse 1
w1scost = []
w1scostfy = [0.12,0.1,0.05,0.06,0.06]
for x in w1scostfy:
    plant = []
    for t in range(1,11):
        ws = x*(1+0.03)**(t-1)
        plant.append(ws)
    w1scost.append(plant)

dfw1scost = pd.DataFrame(w1scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfw1scost.index = [1,2,3,4,5]
dfw1scost

# warehouse 2
w2scost = []
w2scostfy = [0.13,0.03,0.07,0.03,0.02]
for x in w2scostfy:
    plant = []
    for t in range(1,11):
        ws = x*(1+0.03)**(t-1)
        plant.append(ws)
    w2scost.append(plant)

dfw2scost = pd.DataFrame(w2scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfw2scost.index = [1,2,3,4,5]
dfw2scost

# warehouse 3
w3scost = []
w3scostfy = [0.08,0.1,0.06,0.07,0.04]
for x in w3scostfy:
    plant = []
    for t in range(1,11):
        ws = x*(1+0.03)**(t-1)
        plant.append(ws)
    w3scost.append(plant)

dfw3scost = pd.DataFrame(w3scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfw3scost.index = [1,2,3,4,5]
dfw3scost

# warehouse 4
w4scost = []
w4scostfy = [0.05,0.09,0.03,0.07,0.08]
for x in w4scostfy:
    plant = []
    for t in range(1,11):
        ws = x*(1+0.03)**(t-1)
        plant.append(ws)
    w4scost.append(plant)

dfw4scost = pd.DataFrame(w4scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfw4scost.index = [1,2,3,4,5]
dfw4scost

# dataframes for retail center shipping costs
# retail 1
r1scost = []
r1scostfy = [0.09,0.05,0.06,0.07]
for x in r1scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r1scost.append(wh)

dfr1scost = pd.DataFrame(r1scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr1scost.index = [1,2,3,4]
dfr1scost

# retail 2
r2scost = []
r2scostfy = [0.1,0.07,0.09,0.08]
for x in r2scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r2scost.append(wh)

dfr2scost = pd.DataFrame(r2scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr2scost.index = [1,2,3,4]
dfr2scost

# retail 3
r3scost = []
r3scostfy = [0.06,0.12,0.07,0.09]
for x in r3scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r3scost.append(wh)

dfr3scost = pd.DataFrame(r3scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr3scost.index = [1,2,3,4]
dfr3scost

# retail 4
r4scost = []
r4scostfy = [0.05,0.04,0.09,0.06]
for x in r4scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r4scost.append(wh)

dfr4scost = pd.DataFrame(r4scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr4scost.index = [1,2,3,4]
dfr4scost

# retail 5
r5scost = []
r5scostfy = [0.08,0.03,0.09,0.1]
for x in r5scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r5scost.append(wh)

dfr5scost = pd.DataFrame(r5scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr5scost.index = [1,2,3,4]
dfr5scost

# retail 6
r6scost = []
r6scostfy = [0.09,0.09,0.04,0.07]
for x in r6scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r6scost.append(wh)

dfr6scost = pd.DataFrame(r6scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr6scost.index = [1,2,3,4]
dfr6scost

# retail 7
r7scost = []
r7scostfy = [0.02,0.03,0.11,0.06]
for x in r7scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r7scost.append(wh)

dfr7scost = pd.DataFrame(r7scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr7scost.index = [1,2,3,4]
dfr7scost

# retail 8
r8scost = []
r8scostfy = [0.12,0.08,0.07,0.09]
for x in r8scostfy:
    wh = []
    for t in range(1,11):
        rs = x*(1+0.03)**(t-1)
        wh.append(rs)
    r8scost.append(wh)

dfr8scost = pd.DataFrame(r8scost,columns=[1,2,3,4,5,6,7,8,9,10])
dfr8scost.index = [1,2,3,4]
dfr8scost

# raw material costs
# alloy cost
acost = []
acostfy = [0.02,0.02,0.02,0.02,0.02]
for x in acostfy:
    a = []
    for t in range(1,11):
        ac = x*(1+0.03)**(t-1)
        a.append(ac)
    acost.append(a)

dfacost = pd.DataFrame(acost,columns=[1,2,3,4,5,6,7,8,9,10])
dfacost.index = [1,2,3,4,5]
dfacost

# Widget subassemblies original cost
wocost = []
wocostfy = [0.15,0.15,0.15,0.15,0.15]
for x in wocostfy:
    wo = []
    for t in range(1,11):
        woc = x*(1+0.03)**(t-1)
        wo.append(woc)
    wocost.append(wo)

dfwocost = pd.DataFrame(wocost,columns=[1,2,3,4,5,6,7,8,9,10])
dfwocost.index = [1,2,3,4,5]
dfwocost

# Widget subassemblies discounted cost
wdcost = []
wdcostfy = [0.12,0.12,0.12,0.12,0.12]
for x in wdcostfy:
    wd = []
    for t in range(1,11):
        wdc = x*(1+0.03)**(t-1)
        wd.append(wdc)
    wdcost.append(wd)

dfwdcost = pd.DataFrame(wdcost,columns=[1,2,3,4,5,6,7,8,9,10])
dfwdcost.index = [1,2,3,4,5]
dfwdcost
