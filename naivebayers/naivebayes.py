import csv 
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
"""
"abalone" hayvanı için yaş tahmini
"""

#veri oku değişkene ata


file = pd.read_csv("abalone.csv")#4177 veri

#features & class
xx = file.iloc[:,[0,1,2,3,4,5,6,7]].values
yy = file.iloc[:,-1].values
#print(len(set(yy)))
x=[]
for satir in xx:#M F I(infant) değerlerini 0 1 2 değerlerine dönüştürür
    temparr =[]
    for elementl in satir:
        tempvar = elementl
        if elementl == "M":
            tempvar=0
        if elementl == "F":
            tempvar=1
        if elementl == "I":#tüm değerleri dolaştığı için else yok
            tempvar=2
        temparr.append(tempvar)
    x.append(temparr)
#print(x)

y=[]
for yas in yy:
    if yas<=10:
        y.append("A")
    elif 10<yas<=20:
        y.append("B")
    elif yas > 20:
        y.append("C")
#print(y)

#üç cinsiyet tanımlı M F I
#print(x[:,0])
#c=x[:,0]
#c = list(set(c))
#print(c)


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3,random_state=42)
from sklearn.preprocessing import StandardScaler as sc
sc = sc()
x_train = sc.fit_transform(x_train)
x_test = sc.fit_transform(x_test)
#print(x_train)


from sklearn.naive_bayes import GaussianNB as gnb
gnb = gnb()
gnb.fit(x_train,y_train)
y_pred = gnb.predict(x_test)

#print(y_pred)
#print(y_test)
"""
#count =0
#for i in range(len(y_pred)):
#    if y_pred[i] == y_test[i]:
#        count +=1
#print("acc:%",(count/len(y_test))*100)
"""
#random state test size değerleri sabit     0.3        42
#1.feature olmadan acc = % 23.703112529928173
#cinsiyet değerleri int dönüştürüldü acc=% 23.623304070231445
#standart scaler uygulanmadan acc = 23.703112529928173
#sadece ilk 4 feature ile acc= %25.059856344772548
#standart scaler ile ilk 4 feature acc:% 25.139664804469277






from sklearn.metrics import confusion_matrix,accuracy_score
cm = confusion_matrix(y_test,y_pred)
ac =accuracy_score(y_test,y_pred)
print(cm)
print("%",ac*100)


#Çıkarım class uniqe özellik sayısı 28 olduğundan algoritma veri setine uygun değidir
#abalone yaş değerleri:1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 29
#Yaş aralığı sınıflandırması: 1-10 a sınıfı, 11-20 arsaı b sınıfı,21-29 arası c olarak ayarlanmıştır  line 33 41  #acc:% 67.9169992019154