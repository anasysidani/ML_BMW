import streamlit as st
import pickle
import pandas as pd
import numpy as np
import datetime
import time
import streamlit as st
from streamlit_option_menu import option_menu
import seaborn as sns
import plotly
import plotly.figure_factory as ff
import chart_studio.plotly as py
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio


pio.templates.default = "simple_white"
#df=pd.read_csv(r"C:\Users\Sara\Desktop\prices.csv")
st.set_page_config(layout="wide")
# 1. as sidebar menu
selected = option_menu(menu_title=None,
    options=["Home","Data Overview","KPIs and EDA","Car Price Prediction"],
    icons=["gear fill","pie-chart","graph-up","piggy-bank"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
    "container": {"padding":"0!important"},"icon": {"color":"#grey"},
    "nav-link": {
    "font-size":"15px",
    "text-align":"left",
    "margin":"Opx","--hover-color":"#003DA5"},
    "nav-link-selected": {"background-color": "#003DA5"},
    },)#required


if selected =="Home":

    st.image("data:image/png;base64,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",width=600)
    st.header("Welcome:wave:")
    st.write("Explore the app and its features using the navigation bar")
if selected=="Data Overview":
    df=pd.read_csv(r"C:\Users\Asus\Desktop\DDDMML\BMW.csv")
   
   
    st.header('Dataframe:')
    st.write('*9 Columns & 13116 Rows*')    
    st.write(df)
    st.write('---')

    st.header("MetaData")
    st.write("""
         The data displayed above is aout car models that were resold by the company.
         The metrics of the car are included as well as the name of salesperson and the governerate in which the sale happened at.
         Columns include Car model, Year, Price, Transmission type, Mileage, Fuel type, Tax, miles per gallon, engine size, 
         Salesperson name, and Governoate
     """)
if selected =="KPIs and EDA":
    df=pd.read_csv(r"C:\Users\Asus\Desktop\DDDMML\BMW.csv")
    col1, col2,col3= st.columns([3,3,2])
    col1.metric("Total Sales", "323,966,104$")
    col2.metric("Salesperson with most sales", "Anna Sidon", "65,347,674$")
    col3.metric("Governerate with most sales","North Lebanon","66,451,431$")
    df_g=df.groupby("trans").count()
    df_groupby=df_g.reset_index()
    figure = px.scatter(df, x="year", y="price",
                hover_data=['price'],title="Year vs Price of car")
    figure.update_layout(xaxis_title=None,yaxis_title=None)
    figure.update_xaxes(showgrid=True,zeroline=False)
    figure.update_yaxes(showgrid=False,showticklabels = True)
    st.plotly_chart(figure,use_container_width=True)

    figure2 = px.scatter(df, x="mpg", y="price",
                hover_data=['price'],title="Miles per gallon vs Price of car")
    figure2.update_layout(xaxis_title=None,yaxis_title=None)
    figure2.update_xaxes(showgrid=True,zeroline=False)
    figure2.update_yaxes(showgrid=False,showticklabels = True)
    st.plotly_chart(figure2,use_container_width=True)
    figure3 = px.scatter(df, x="mileage", y="price",
                hover_data=['price'],title="Mileage vs Price of car")
    figure3.update_layout(xaxis_title=None,yaxis_title=None)
    figure3.update_xaxes(showgrid=True,zeroline=False)
    figure3.update_yaxes(showgrid=False,showticklabels = True)
    st.plotly_chart(figure3,use_container_width=True)

    figure4 = px.treemap(df, path=['trans', 'car_model'], values=df.nunique(axis=1),
                              color='price',
                              color_continuous_scale='blues',title="Car class per transmission type")
    figure4.update_layout(margin = dict(t=50, l=25, r=25, b=25))
    st.plotly_chart(figure4,use_container_width=True)

   

if selected =="Car Price Prediction": 
   def main():
       df=pd.read_csv(r"C:\Users\Asus\Desktop\DDDMML\BMW.csv")
       col1, col2,col3 = st.columns([1,1,1])
    

     
       with col1:
           st.subheader("Transmission Type")
           transt = st.selectbox("" , ['Manual', "Automatic",'Semi-Auto', 'Other'])
           st.write("The car's transmission is ",transt)
       if transt == "Manual":
           transt = 0
       elif transt == "Automatic":
           transt = 1
       elif transt == "Semi-Auto":
           transt = 2
       elif transt == "Other":
           transt = 3

       
       with col2:
           st.subheader("Fuel Type")
           fuelt = st.selectbox("" , ["Petrol","Diesel","Hybrid","Other"])
           st.write("The car's fuel type is " , fuelt)
       if fuelt == "Petrol":
           fuelt = 1
       elif fuelt == "Diesel":
           fuelt = 2
       elif fuelt == "Hybrid":
           fuelt = 3
       elif fuelt == "Other":
           fuelt = 4
       

       with col3:
           st.subheader("Mileage")
           mileage = st.slider('mileage', float(df.mileage.min()),float(df.mileage.max()),value= float(df.mileage.mean()))
           
           
       with col1:
           st.subheader("MPG")
           mpg = st.slider('mpg',float(df.mpg.min()), float(df.mpg.max()), float(df.mpg.mean()))
       with col2:
           st.subheader("Engine Size")
           engine_size = st.slider('engine size', min_value=float(df.engine_size.min()), max_value=float(df.engine_size.max()), value=float(df.engine_size.mean()))
       model = open(r"C:\Users\Asus\Desktop\DDDMML\model.pkl", "rb")
       modellr = pickle.load(model)
    
       variables = [ transt, fuelt , mileage ,mpg, engine_size]

       if st.button("Check Price"):
           pred = modellr.predict([variables])
           for i in pred:
               st.write("Predicted Selling Price : " , i  , '$')
   if __name__ == "__main__":
       main()

