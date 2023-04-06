import streamlit as st
import pickle
import pandas as pd
import math


sprint1=pickle.load(open('prediction.pkl','rb'))
df2=pd.DataFrame(sprint1)


st.title("Welcome to the price prediction model of Laptop.")

company_name = ['Lenovo', 'ASUS', 'HP', 'DELL', 'RedmiBook', 'realme', 'acer',
       'MSI', 'APPLE', 'Infinix', 'SAMSUNG', 'Ultimus', 'Vaio', 'Nokia', 'ALIENWARE']
rams = ["4 GB","8 GB","16 GB","32 GB"]
processors = ["Intel Core i3","Intel Core i5","Intel Core i7","Intel Core i9","AMD Ryzen 3","AMD Ryzen 5","AMD Ryzen 7","AMD Ryzen 9"]
st.write("Select the laptop company : ")
choice1 = st.selectbox("pick one ",company_name)

st.write("Select the Ram capacity : ")
choice2 = st.selectbox("pick one",rams,key=1)

st.write("Select the processor : ")
choice3 = st.selectbox("pick one",processors,key=3)


def find_amount(company_name,ram,processor):
    new_df = df2[df2['Product'].str.contains(company_name)]
    new_df1 = new_df[new_df['Feature'].str.contains(ram)]
    new_df2 = new_df1[new_df1['Feature'].str.contains(processor)]
    return new_df2['MRP'].median()



if st.button('Predict Price'):
    amount = find_amount(choice1,choice2,choice3)
    if(math.isnan(amount)):
        amount = 45454.00
    st.write("The predicted amount is : ",amount)
    