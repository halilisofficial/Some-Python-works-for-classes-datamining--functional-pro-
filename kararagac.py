
    #veri seti kütüphane indirme

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import os
#os.chdir('Calisma_Dizniniz')
dataset = pd.read_csv('SosyalMedyaReklamKampanyası.csv')

    # target feature belirle

def convert(cinsiyet):
    if cinsiyet == "Erkek":
        return 1
    else:
        return 0

#x = 1,#features  1?
x = dataset.iloc[:,[1,2,3]].values
for i in range(len(x)):
    x[i][0] = convert(x[i][0])
#print(x)


y = dataset.iloc[:, -1].values#target
#print(len(Y))

    #train test split

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)#random state ?= new Random(number) java
#print(x_train)

    #normalizasyon feature scaling
"""
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)       
x_test = sc_x.transform(x_test)
"""
#print(x_train)
#print(x_test)

    #karar ağacı entropi tabanlı oluşturuldu
from sklearn.tree import DecisionTreeClassifier as dtc
classifier = dtc(criterion= 'entropy',random_state=42)
classifier.fit(x_train,y_train)
#print(classifier)
    #tahmin
y_prediction = classifier.predict(x_test)

#print(y_prediction)
#print(y_test)

count= 0
for i in range(len(y_prediction)):
    if y_test[i] == y_prediction[i]:
        count +=1
print("accuracy:%",(count/len(y_prediction))*100)

    #hata matrisi
from sklearn.metrics import confusion_matrix as cmx
cm = cmx(y_test,y_prediction)
print(cm)

