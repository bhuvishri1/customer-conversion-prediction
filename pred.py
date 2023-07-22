import pickle
import streamlit as st
import numpy as np
pickled =pickle.load(open("model.pkl","rb"))

st.title(":white[Customer Conversion Prediction using Machine Learning Model]")
# st.pyplot(fig)

st.subheader("Enter Age")
age=st.number_input("Age: ",min_value=1,max_value=100) 
st.subheader("Enter Job")
job=st.selectbox("Job:",['student','retired','unemployed','management','admin.','self-employed','technician','services','housemaid','entrepreneur','blue-collar'])
if job=="student":
   job=11
if job=="retired":
   job=10
if job=="unemployed":
   job=9
if job=="management":
   job=8
if job=="admin.":
   job=7
if job=="self-employed":
   job=6
if job=="technician":
   job=5
if job=="services":
   job=4
if job=="housemaid":
   job=3
if job=="entrepreneur":
   job=2
if job=="blue-collar":
   job=1

st.subheader("Enter Marital Status")
marital = st.selectbox("Marital: ",["married","single","divorced"])  
if marital=="married":
   marital=1
if marital=="single":
   marital=3
if marital=="divorced":
   marital=2

st.subheader("Enter Education_qualification")     
education_qual =st.selectbox("Education:",["tertiary","secondary","primary"])
if education_qual=="tertiary":
   education_qual=3
if education_qual=="secondary":
   education_qual=2
if education_qual=="primary":
   education_qual=1

st.subheader("Enter call_type")  
call_type = st.selectbox("call_type:",["unknown","cellular","telephone"])   
if call_type=="unknown":
   call_type =1
if call_type=="cellular":
   call_type=3
if call_type=="telephone":
   call_type=2   

st.subheader("Enter day")  
day=st.number_input("Day: ",min_value=1,max_value=31)

st.subheader("Enter mon")
mon= st.selectbox("mon: ",["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"])
if mon=="jan":
   mon=3
if mon=="feb":
   mon=7
if mon=="mar":
   mon=12
if mon=="apr":
   mon=8
if mon=="may":
   mon=1
if mon=="jun":
   mon=5
if mon=="jul":
   mon=2
if mon=="aug":
   mon=6
if mon=="sep":
   mon=10
if mon=="oct":
   mon=9
if mon=="nov":
   mon=4
if mon=="dec":
   mon=11

st.subheader("Enter Duration")
dur= st.number_input("dur : ",min_value=0,max_value=769)

st.subheader("Enter num_calls ")
num_calls= st.number_input("num_calls :",min_value=1,max_value=6)
   
st.subheader("Enter prev_outcome ")
prev_outcome =st.selectbox("prev_outcome: ",["unknown","failure","other","success"])
if prev_outcome=="unknown":
   prev_outcome=1
if prev_outcome=="failure":
   prev_outcome=2
if prev_outcome=="other":
   prev_outcome=3
if prev_outcome=="success":
   prev_outcome=4

button=st.button("predict conversion")
if button:
    a=np.array([[age,job,marital,education_qual,call_type,day,mon,dur,num_calls,prev_outcome]])
    st.write(a)
    st.write(pickled.predict(a))