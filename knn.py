# -*- coding: utf-8 -*-
from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
def main():
    iris = datasets.load_iris()
    X = iris.data[:, :4]  # data_set değişkeni
    Y = iris.target
    x_train, x_test, y_train, y_test = train_test_split(X,Y)
    accuracy = 0
    #print(x_test[0])
    for i in range(len(y_test)):
        result= calculate_knn(x_test[i],x_train,y_train,neirest=5)
        #print(result)
        tur_sonuc_dizisi=[]
        for row in result:
            j=0#kind[1] çalışmadı
            for kind in row:
                j+=1
                if(j%2==0):
                    tur_sonuc_dizisi.append(kind)
        d = {x: tur_sonuc_dizisi.count(x) for x in tur_sonuc_dizisi}
        c=0
        for key in d.keys():
            c=key
            break
        print(x_test[i],"noktası için tahmin edilen değer:",c,"\tgerçek değer:",y_test[i])#x_test[0] tahmin edilen değer
        if c==y_test[i]:
            accuracy+=1
    print("Model için doğruluk değeri:%",((accuracy*100)/len(y_test)))
    pass



def calculate_knn(new_dot,data_set,data_flag,neirest=3):#[x değişkeni][y değişkeni]
    nearest_list=[]
    x_new = new_dot[0]
    y_new = new_dot[1]
    z_new = new_dot[2]
    t_new = new_dot[3]
    index = -1
    for j in data_set:
        index += 1
        new = []
        x = j[0]
        y = j[1]
        z = j[2]
        t = j[3]
        la_formule= ((x - x_new)**2 + (y - y_new)**2 + (z-z_new)**2 + (t-t_new)**2)**0.5
        new.append(la_formule)
        new.append(data_flag[index])
        nearest_list.append(new)
    a = sorted(nearest_list, key=lambda nearest_list:nearest_list[0])
    b =[]
    for i in range(neirest):
        b.append(a[i])
    return b

main()