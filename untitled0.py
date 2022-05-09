# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 00:13:33 2022

@author: casper
"""


    #veri seti kütüphane indirme

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#import os
#os.chdir('Calisma_Dizniniz')
dataset = pd.read_csv('SosyalMedyaReklamKampanyası.csv')

    # target feature belirle

x = dataset.iloc[:, [2,3]].values#features  1?
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

    # eğitim seti için grafik
from matplotlib.colors import ListedColormap

X_set, y_set = x_train, y_train
X1, X2 = np.meshgrid(np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
                     np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha=0.75, cmap=ListedColormap(('blue', 'yellow')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c=ListedColormap(('blue', 'yellow'))(i), label=j)
plt.title('Karar Ağacı (Eğitim seti)')
plt.xlabel('Yaş')
plt.ylabel('Maaş')
plt.legend()
plt.show()

