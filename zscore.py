import csv
import numpy as np

def average(lst):
    return sum(lst) / len(lst)

def standartSapma(vektor):
    sd = 0.0 # standart sapma
    veriAdedi = len(vektor)
    if veriAdedi <= 1:
        return 0.0
    else:
        for _ in vektor:
            sd += (float(_) - average(vektor)) ** 2
        sd = (sd / float(veriAdedi)) ** 0.5
        return sd

file =open("minmaxdata.csv")

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

z_yas=[]
for veri in yas:
    z_yas.append(float((veri-np.mean(yas))/standartSapma(yas)))
print(z_yas)

z_tecrube=[]
for t_veri in tecrube:
    z_tecrube.append(float((t_veri-average(tecrube))/np.std(tecrube)))
print(z_tecrube)

z_maas=[]
for m_veri in maas:
    z_maas.append(float((m_veri-average(maas))/np.std(maas)))
print(z_maas)

file.close()
