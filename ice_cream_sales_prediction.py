# -*- coding: utf-8 -*-
"""ice_cream_sales_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cOijz4s9rzxTBnzMnF9uGdG7h_NckRLn
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('IceCreamData.csv')

df.shape

df.head()

df.describe()

x = df[['Temperature']]
y = df.drop('Temperature',axis=1)

plt.scatter(x,y,color='red',marker='*')
plt.xlabel('Temperature')
plt.ylabel('Revenue')

sns.jointplot(x='Temperature',y='Revenue',data=df,color='red',)

sns.pairplot(df)

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

model = LinearRegression()
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

model.score(X_test,y_test)

X_test['Prediction'] = y_pred

X_test

model.predict([[24.566884]])

plt.scatter(X_train,y_train,color="gray")
plt.plot(X_train,model.predict(X_train),color="red")

