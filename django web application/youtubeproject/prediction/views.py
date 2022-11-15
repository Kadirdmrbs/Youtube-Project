from django.shortcuts import render
from . forms import MlForm
from joblib import load
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

model_filename = 'mlmodels/model_04-11-22_new_RF.pickle'
scaler_filename = 'mlmodels/scaler_04-11-22.pickle'

model = load(model_filename)
scaler = load(scaler_filename)

def predict_view(likes,comments,duration,category,year):

    z = []

    if category == 'Basketball-Highlights':
        c = [0,0,0,0,0]
        s = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif category == 'Basketball-NBA':
        c = [0,0,0,0,0]
        s = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif category == 'Basketball-European':
        c = [0,0,0,0,0]
        s = [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif category == 'Soccer-Highlights':
        c = [0,0,0,1,0]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif category == 'Soccer-LaLiga':
        c = [0,0,0,1,0]
        s = [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif category == 'Soccer-SerieA':
        c = [0,0,0,1,0]
        s = [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif category == 'Soccer-International':
        c = [0,0,0,1,0]
        s = [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]

    elif category == 'Fighting-Highlights':
        c = [0,1,0,0,0]
        s = [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif category == 'Fighting-UFC':
        c = [0,1,0,0,0]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif category == 'Fighting-WWE':
        c = [0,1,0,0,0]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]

    elif category == 'Racing-Formula 1':
        c = [0,0,1,0,0]
        s = [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif category == 'Racing-Formula 2':
        c = [0,0,1,0,0]
        s = [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif category == 'Racing-MotoGP':
        c = [0,0,1,0,0]
        s = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif category == 'Racing-Highlights':
        c = [0,0,1,0,0]
        s = [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif category == 'Racing-Son Viraj':
        c = [0,0,1,0,0]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]

    elif category == 'Tennis-Highlights':
        c = [0,0,0,0,1]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif category == 'Tennis-Wimbledon':
        c = [0,0,0,0,1]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    elif category == 'Tennis-ATP':
        c = [0,0,0,0,1]
        s = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    elif category == 'Betting':
        c = [0,0,0,0,0]
        s = [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


    if year == '2018':
        y = [0,0,0,0]
    elif year == '2019':
        y = [1,0,0,0]
    elif year == '2020':
        y = [0,1,0,0]
    elif year == '2021':
        y = [0,0,1,0]
    elif year == '2022':
        y = [0,0,0,1]


    z = [likes,comments,duration] + c + y + s
    z = np.expand_dims(z, axis=0)
    z = scaler.transform(z)
    pred = model.predict(z)

    return pred


def ml_view(request):

	if request.method == "POST":
		form = MlForm(request.POST)

		if form.is_valid():
			form.save()
			result = form.cleaned_data

			likes = result['likes']
			comments = result['comments']
			duration = result['duration']
			category = result['category']
			year = result['year']

			pred = predict_view(likes,comments,duration,category,year)
			pred = round(pred[0])

			return render(request,'prediction/ml.html',context={'form':form,
																'likes':likes,
																'comments':comments,
																'duration':duration,
																'category':category,
																'year':year,
																'pred':pred})
	
	else:
		form = MlForm()
	

	return render(request,'prediction/ml.html',context={'form':form})



