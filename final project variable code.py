# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:43:12 2021

@author: aidan
"""

import gurobipy as gp
from gurobipy import GRB

year = 10

stores = range(len(demandfy)) # k
plants = range(len(concostfy)) # i
warehouses = range(4) # j
years = range(year) # t


r = gp.Model("Retail Store")

zvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "z")
xvars = r.addVars(plants, warehouses, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "x")
yvars = r.addVars(warehouses, stores, years, vtype=GRB.CONTINUOUS, obj=whtocust, name = "y")
ivars = r.addVars(warehouses, years, vtype=GRB.CONTINUOUS, obj=whtocust, name = "i")
pvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "pvar")
fvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "fvar")
gvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostwh, lb = 0, ub = 1,  name = "gvar")
hvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostwh, lb = 0, ub = 1,  name = "hvar")