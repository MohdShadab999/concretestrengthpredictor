import pandas as pd
import streamlit as st
import pickle

predictor=pickle.load(open('ConcreteStrengthPredictor.pkl','rb'))

st.title("Concrete strength predictor")

st.subheader("Please enter the values")

col1,col2= st.columns(2)

with col1:
    cement=st.number_input("Cement(Kg/m3)")
with col2:
    superplasticizer=st.number_input("Superplasticizer(Kg/m3)")

col3,col4= st.columns(2)

with col3:
    bfs=st.number_input("Blast furnace slag(Kg/m3)")
with col4:
    ca=st.number_input("Coarse aggregate(Kg/m3)")

col5,col6= st.columns(2)

with col5:
    flyash=st.number_input("Fly ash(Kg/m3)")
with col6:
    fa=st.number_input("Fine aggregate(Kg/m3)")

col7,col8= st.columns(2)

with col7:
    water=st.number_input("Water(Kg/m3)")
with col8:
    age=st.number_input("age(Days)")

if st.button("Predict Strength"):

    input_df=pd.DataFrame({'cement':[cement],'blast_furnace_slag':[bfs],'fly_ash':[flyash],'water':[water],
                           'superplasticizer':[superplasticizer],'coarse_aggregate':[ca],'fine_aggregate':[fa],
                           'age':[age]})

    result=predictor.predict(input_df)


    st.metric(label="Concrete Strength in N/mm", value=result)
