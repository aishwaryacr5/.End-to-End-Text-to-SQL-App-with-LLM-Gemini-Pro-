from dotenv import load_dotenv
load_dotenv() #load all the envirnoment

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
#configure our API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide query as a response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

#function to retrieve query from sql database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

##define your prompt 
prompt=[
    """
    You are an expert in converting  English questions to SQL query!
    The sql database has the name product and has following columns - NAME, PRICE, STOCK, SOLD \n\n
    For example,\n Example 1 - How many entries of records are present ?,the sql command will be something like this SELECT COUNT(*) FROM product ;\n
    Example 2 - How many soaps are left?, the SQL command will be something like this SELECT STOCK FROM product WHERE NAME = 'Soaps';\n
    Example 3 - How many Notebooks are sold?, the SQL command will be something like this SELECT SOLD FROM product WHERE NAME = 'Notebook';\n
    Example 5- What is the price of peanut butter?, the sql command will be something like this SELECT PRICE FROM product WHERE NAME = 'Peanut butter';\n
    also the sql should not have ''' in beginning or end and sql word in the output

"""
]
##streamlit app
st.set_page_config(page_title="I'm your Chatbot ")
st.header("Gemini App to retrieve your stock from warehouse")

question=st.text_input("Input:",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)  
    print(response)
    data=read_sql_query(response,"warehouse.db")
    st.subheader("In your warehouse:")
    for row in data:
        print(row)
        st.header(row)