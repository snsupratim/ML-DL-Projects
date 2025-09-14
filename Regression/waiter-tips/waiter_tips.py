import streamlit as st
import pickle
import numpy as np

#load the model

model_filename='waiter_tips.pkl'
with open(model_filename,'rb') as file:
    model=pickle.load(file)

#function for prediction:
def predict(total_bill,sex,smoker,day,time,size):
    features=np.array([[total_bill,sex,smoker,day,time,size]])
    tip_prediction=model.predict(features)
    return tip_prediction[0]

#streamlit interface:
def main():
    st.title("Waiter Tips Prediction")
    #user inputs
    total_bill=st.number_input('Total Bill',min_value=1.0)
    sex=st.selectbox('Sex',['Male','Female'])
    smoker=st.selectbox('Smoker',['No','Yes'])
    day=st.selectbox('Day',['Sun','Sat','Mon','Tue','Wed','Thur','Fri'])
    time=st.selectbox('Time',['Lunch','Dinner'])
    size=st.number_input('Size',min_value=1,step=1)

    #convert categorical data into numeric
    sex_num=1 if sex== 'Male' else 0
    smoker_num=1 if smoker=='Yes' else 0
    day_num=['Sun','Sat','Mon','Tue','Wed','Thur','Fri'].index(day)
    time_num=['Lunch','Dinner'].index(time)

    if st.button('Predict'):
        tip_prediction=predict(total_bill,sex_num,smoker_num,day_num,time_num,size)
        st.success(f'Predicted Tip: ${tip_prediction:.2f}')

if __name__=='__main__':
    main()

