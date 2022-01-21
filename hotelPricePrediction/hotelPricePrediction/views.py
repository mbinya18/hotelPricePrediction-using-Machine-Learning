from django.shortcuts import render, redirect
from django.http import HttpResponse
from.forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import NewUserForm
from django.contrib import messages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):
    return render(request,"home.html")

def predict(request):
    return render(request,"predict.html")

def result(request):
    data = pd.read_csv(r'C:\Users\USER\PycharmProjects\hotelPricePrediction\hotelPricePrediction\static\hotelpredict.csv')
    data = data.drop(['Address'],  axis=1)
    X= data.drop('Price',axis=1)
    y= data['Price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.30)
    model = LinearRegression()
    model.fit(X_train, y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])

    pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1))
    pred = round(pred[0])
    price = "The predicted Hotel price is ksh" + str(pred)

    return render(request,"predict.html",{"result2":price})

def explore(request):
    return render(request,"explore.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})
