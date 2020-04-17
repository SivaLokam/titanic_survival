# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 20:22:11 2020

@author: ADMIN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(pd.get_option("display.max_columns"))
pd.set_option("display.max_columns",30)

train_df = pd.read_csv('train.csv')
train_df.info()

des = train_df.describe().T

print(train_df.describe().T)

total = train_df.isnull().sum().sort_values(ascending=False)

perc1 = train_df.isnull().sum()/train_df.isnull().count()*100

perc2 = (round(perc1,1)).sort_values(ascending=False)

missing_data = pd.concat([total,perc2],axis=1,keys = ['Total','%'])

train_df.columns.values


sns.pairplot(train_df[['Age','Sex']])
plt.show()

women = train_df[train_df['Sex']=='female']

fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(18,8))
ax = sns.distplot(women[women['Survived']==1].Age.dropna(), bins=40,label='Survived',ax = axes[0],kde=False)
ax = sns.distplot(women[women['Survived']==0].Age.dropna(), bins=18,label='Survived',ax = axes[0],kde=False)
ax.legend()




type(sql)
sql = sql.replace("(", "[")
sql = sql.replace(")", "]")

type(sql)

sql = "(10001,'AEX','CCC','X12344','John, Doe','Not indicated','None','No','No','No','\r\n'),(10002,'AEX','CCC','X12344','John, Doe','Not indicated','None','No','No','No','\r\n')"
lsql = sql.split(",")



























