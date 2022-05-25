import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('ssports_model2.pickle', 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

def load_scaler():
    with open('ssports_scaler.pickle', 'rb') as f:
        scaler = pickle.load(f)
    return scaler

scaler = load_scaler()

def predict_view(like,comment,category,year):
    z = []
    x = []
    if category == 'Formula 1':
        a = [1,0,0,0,0,0,0]
    elif category == 'International':
        a = [0,1,0,0,0,0,0]
    elif category == 'NBA':
        a = [0,0,1,0,0,0,0]
    elif category == 'Premier League':
        a = [0,0,0,1,0,0,0]
    elif category == 'Serie A':
        a = [0,0,0,0,1,0,0]
    elif category == 'WWE':
        a = [0,0,0,0,0,1,0]
    elif category == 'other':
        a = [0,0,0,0,0,0,1]
        
    if year == '2021':
        b = [1,0]
    else:
        b = [0,1]
        
    z = [like,comment] + a + b
    z = np.expand_dims(z, axis=0)
    z = scaler.transform(z) 
    
    return round(model.predict(z)[0])

def show_predict_page():
    st.title('S Sports View Prediction')

    st.write("""### We need some information to predict the views """ )

    categories = (
        'Formula 1',
        'International',
        'NBA',
        'Premier League',
        'Serie A',
        'WWE',
        'other'
    )

    years = (
        '2022',
        '2021'
    )

    category = st.selectbox("category",categories)
    year = st.selectbox("year",years)

    like = st.number_input('Insert like amount',format='%d',step=1000)
    st.write('The current like amount is ', like)

    comment = st.number_input('Insert comment amount',format='%d',step=1000)
    st.write('The current comment amount is ', comment)

    ok = st.button("Calculate View")
    if ok:
        prediction = predict_view(like,comment,category,year)
        st.subheader(f"The estimated view amount is {prediction}")
