import streamlit as st
import pickle
import pandas as pd
# import scikit_learn

teams=['Delhi Capitals',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Kings XI Punjab',
 'Kolkata Knight Riders',
 'Royal Challengers Bangalore',
 'Mumbai Indians',
 'Sunrisers Hyderabad']


cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe=pickle.load(open('pipe.pkl','rb'))

st.title('IPL Win Predictor')
st.write('This is a simple web app that predicts the winner of an IPL match. (IPL Dataset 2008-2019)')

col1 , col2 = st.columns(2)

with col1:
    batting_team=st.selectbox('Batting Team',teams)

with col2:
    balling_team=st.selectbox('Balling Team',teams)


selected_city=st.selectbox('Host City',cities)

target=st.number_input('Target')

col3, col4, col5 = st.columns(3)

with col3:
    score=st.number_input('Score')
with col4:
    overs=st.number_input('Overs Completed')
with col5:
    wickets=st.number_input('Wickets Out')


if st.button('Predict Win'):
    runs_left = target-score
    balls_left=120-(overs*6)
    wickets_left=10-wickets
    crr=score/overs
    rrr=(runs_left*6)/balls_left


    input_df=pd.DataFrame({'batting_team':[batting_team],'bowling_team':[balling_team],'city'
    :[selected_city],'runs_left':[ runs_left],'balls_left':[balls_left],'wickets_left':[wickets_left],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    results=pipe.predict_proba(input_df)
    loss=(results[0][0])*100
    win=(results[0][1])*100

    st.text(batting_team +" - " + str(round(win)) + "%")
    st.text(balling_team +" - " + str(round(loss)) + "%")