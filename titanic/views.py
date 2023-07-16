from django.core import paginator
from django.shortcuts import render, redirect,get_object_or_404
from .models import data
from .forms import DataForm
import numpy as np
import pandas as pd
import tensorflow as tf
import sklearn

from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages





dataset = pd.read_csv("static/train.csv")
X = dataset.filter(['Pclass','Sex','Age','SibSp','Parch','Embarked'],axis = 1).values
Y = dataset.filter(['Survived'],axis = 1).values


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:, 1] = le.fit_transform(X[:, 1])


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [-1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values = np.nan, strategy = 'mean' )
imputer.fit(X[:,0:8])
X[:,0:8] = imputer.transform(X[:,0:8])
 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


model = tf.keras.models.load_model('static/model')





def data_list(request):
    form = DataForm(request.POST, request.FILES)
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            pclass = int(form.cleaned_data['pclass'])
            sex = int(form.cleaned_data['sex'])
            age = int(form.cleaned_data['age'])
            sibsp = int(form.cleaned_data['sibsp'])
            parch = int(form.cleaned_data['parch'])
            embark = form.cleaned_data['embark']
            inp = [[pclass,sex,age,sibsp,parch,embark]]
            z = np.array(ct.transform(inp))
            result = round(model.predict(sc.transform(z))[0][0]*100,2)
            form.save()
            return render(request,'result.html', {'result':result})
        
    return render(request, 'index.html', {'form': form})


