import csv
import numpy as np
#veri seti https://www.youtube.com/watch?v=HSwKVfnFwoU linkli youtube videosundan alınmıştır
file = open("minmaxdata.csv")

csvreader = csv.reader(file)
veriler = []
for row in csvreader:
        veriler.append(row)

yas =[]
tecrube = []
maas = []
for satir in veriler:#csv içeriği birbirinden ayrıştırıldı
    yas.append(int(satir[0]))
    tecrube.append(int(satir[1]))
    maas.append(int(satir[2]))

norm_yas=[]#veriler 0 ve 1 arasında normalize edildi
for veri in yas:
    norm_yas.append(float((int(veri)-np.min(yas))/(np.max(yas)-np.min(yas))))
print(norm_yas)

norm_tecrube=[]
for t_veri in tecrube:
    norm_tecrube.append(float((int(t_veri)-np.min(tecrube))/(np.max(tecrube)-np.min(tecrube))))
print(norm_tecrube)

norm_maas=[]
for veri in maas:
    norm_maas.append(float((int(veri)-np.min(maas))/(np.max(maas)-np.min(maas))))
print(norm_maas)

file.close()