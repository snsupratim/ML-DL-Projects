

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("tips_data.csv")
print(data.head())

figure = px.scatter(data_frame = data, x="Total Bill",
                    y="Tip", size="Size", color= "Day", trendline="ols")
figure.show()

figure = px.scatter(data_frame = data, x="Total Bill",
                    y="Tip", size="Size", color= "Sex", trendline="ols")
figure.show()

figure = px.scatter(data_frame = data, x="Total Bill",
                    y="Tip", size="Size", color= "Time", trendline="ols")
figure.show()

figure = px.pie(data,
             values='Tip',
             names='Day',hole = 0.5)
figure.show()

figure = px.pie(data,
             values='Tip',
             names='Sex',hole = 0.5)
figure.show()

figure = px.pie(data,
             values='Tip',
             names='Smoker',hole = 0.5)
figure.show()

figure = px.pie(data,
             values='Tip',
             names='Time',hole = 0.5)
figure.show()

print(data.head())

data["Sex"] = data["Sex"].map({"Female": 0, "Male": 1})
data["Smoker"] = data["Smoker"].map({"No": 0, "Yes": 1})
data["Day"] = data["Day"].map({"Thur": 0, "Fri": 1, "Sat": 2, "Sun": 3,"Mon":4,"Tue":5,"Wed":6,})
data["Time"] = data["Time"].map({"Lunch": 0, "Dinner": 1})
data.head(100)

x = np.array(data[["Total Bill", "Sex", "Smoker", "Day",
                   "Time", "Size"]])
y = np.array(data["Tip"])

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y,
                                                test_size=0.2,
                                                random_state=42)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)

# features = [[total_bill, "sex", "smoker", "day", "time", "size"]]
features = np.array([[24.50, 1, 0, 0, 1, 4]])
model.predict(features)

import pickle

# Assuming 'model' is your trained ML model object
filename = 'waiter_tips.pkl'  # Choose a filename for your pickle file
with open(filename, 'wb') as file:
    pickle.dump(model, file)