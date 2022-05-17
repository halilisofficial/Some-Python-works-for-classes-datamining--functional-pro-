# csv oku diziye ata sınıflandırma sütunu ekle
# rastgele k nokta seç ikinci diziye ata csv verisinde uzaklıkları bu diziye göre hesapla
# not: noktaların merkeze uzaklık toplamları en küçükse o iterasyon en iyi

"""
veri seti hakkında:
        link:  https://archive.ics.uci.edu/ml/datasets/Wholesale+customers
        toptan alım yapan müşterilerin yıllık harcamalarını içerir
            1) FRESH: annual spending (m.u.) on fresh products (Continuous);
            2) MILK: annual spending (m.u.) on milk products (Continuous);
            3) GROCERY: annual spending (m.u.)on grocery products (Continuous);
            4) FROZEN: annual spending (m.u.)on frozen products (Continuous)
            5) DETERGENTS_PAPER: annual spending (m.u.) on detergents and paper products (Continuous)
            6) DELICATESSEN: annual spending (m.u.)on and delicatessen products (Continuous)
            7) CHANNEL: customersâ€™ Channel - Horeca (Hotel/Restaurant/CafÃ©) or Retail channel (Nominal)
                işletme türü: yemek şirketi 298 parakende 142
            8) REGION: customersâ€™ Region â€“ Lisnon, Oporto or Other (Nominal)
                işletmenin bulunduğu bölge: Lisbon 77 Oporto 47 Other Region 316
        bir müşteri için örnek veri:
            Channel,Region,Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen
            2,3,12669,9656,7561,214,2674,1338

    Challenge -> müşterileri yıllık harcamalarına göre 3 gruba ayır
                 en az harcama yapan grubun çoğunlukla hangi türde işletme olduğunu bul
"""
def visualizedata():
    import matplotlib.pyplot as plt
    import csv
    x = []
    y = []
    with open('Wholesalecustomersdata.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        flag =True
        #temp =0#işletme türü için kod değerlerinin anlamı verilmemiş
        for row in plots:

            if flag:#csv açıklama satırını alıyor ->  Channel,Region,Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen
                flag = not flag
                continue
            #print(row)  1266996567561214464
            x.append(row[0])
            """
            if(int(row[0])==2):
                temp +=1
            """
            #print(int(int((int(row[2])+int(row[3])+int(row[4])+int(row[5])+int(row[6])+int(row[7])))/10000))  not: csvden aldığı veriyi string olarak topladı
            y.append(int(int((int(row[2])+int(row[3])+int(row[4])+int(row[5])+int(row[6])+int(row[7])))/10000))
        #print(temp)#parakende 2  yemek şirketi 1 olarak kodlanmış
    plt.scatter(x, y)
    plt.xlabel('İşletme türü (parakende 2) (yemek şirketi 1)')
    plt.ylabel('Toplam yıllık harcama/10k')
    plt.title('İşletme türüne göre toplam yıllık harcama/10k')
    plt.legend()
    plt.show()
#visualizedata()

def smallest(num1, num2, num3):
    if (num1 < num2) and (num1 < num3):
        smallest_num = num1
    elif (num2 < num1) and (num2 < num3):
        smallest_num = num2
    else:
        smallest_num = num3
    return smallest_num

def largest(num1, num2, num3):
    if (num1 > num2) and (num1 > num3):
        largest_num = num1
    elif (num2 > num1) and (num2 > num3):
        largest_num = num2
    else:
        largest_num = num3
    return largest_num

def kmeans():
    import csv
    import random
    iterasyon = 10
    veriler = []
    secilenrandomgruplar = []
    with open('Wholesalecustomersdata.csv', 'r') as csvfile:
        plots = csv.reader(csvfile, delimiter=',')
        flag =True
        for row in plots:
            temp = []#işletme türü, yıllık harcama/1k, tür(az harcama,orta harcama, çok harcama)->tür(0,1,2) default=0
            if flag:
                flag = not flag
                continue
            temp.append(int(row[0]))
            temp.append(int(int((int(row[2])+int(row[3])+int(row[4])+int(row[5])+int(row[6])+int(row[7])))/1000))
            temp.append(0)
            veriler.append(temp)
        #print(veriler)
        toplam_merkezlere_uzaklik_dizisi = []
        for iter1 in range(iterasyon):
            try:

                random.seed(iter1)
                r1 = random.randint(0, len(veriler)-1)
                r2 = random.randint(0, len(veriler)-1)
                r3 = random.randint(0, len(veriler) - 1)

                #sort random numbers
                arr = [r1,r2,r3]
                for i in range(0, len(arr)):
                    for j in range(i + 1, len(arr)):
                        if (arr[i] > arr[j]):
                            temp = arr[i]
                            arr[i] = arr[j]
                            arr[j] = temp
                #print(arr)



                veriler[arr[0]][2] = 0 #az harcama
                veriler[arr[1]][2] = 1 #orta harcama     ## Kodu yazarken yaptığım hata yüzünden 0,1,2 dinamik harcama grubu Az Orta Çok ifade etmez  ##
                veriler[arr[2]][2] = 2 #çok harcama


                #print(veriler)
                index = 0
                azharca = 0
                azharcayanyemeksirketi = 0
                ortaharca = 0
                ortaharcayyanyemeksirketi = 0
                cokharca = 0
                cokharcayanyemeksirketi = 0
                for rows in veriler:#veriler tek boyutlu düzlemde olduğundan mutlak değerinin en kısa uzunluğuna göre sınıflandırma yapılmıştır
                    if smallest(abs(rows[1] - veriler[arr[0]][1]), abs(rows[1] - veriler[arr[1]][1]), abs(rows[1] - veriler[arr[2]][1])) == abs(rows[1] - veriler[arr[0]][1]):
                        veriler[index][2] = 0
                        azharca +=1
                        if veriler[index][0] == 1:
                            azharcayanyemeksirketi+=1
                    elif smallest(abs(rows[1] - veriler[arr[0]][1]), abs(rows[1] - veriler[arr[1]][1]), abs(rows[1] - veriler[arr[2]][1])) == abs(rows[1] - veriler[arr[1]][1]):
                        veriler[index][2] = 1
                        ortaharca +=1
                        if veriler[index][0] == 1:
                            ortaharcayyanyemeksirketi+=1
                    elif smallest(abs(rows[1] - veriler[arr[0]][1]), abs(rows[1] - veriler[arr[1]][1]), abs(rows[1] - veriler[arr[2]][1])) == abs(rows[1] - veriler[arr[2]][1]):
                        veriler[index][2] = 2
                        cokharca +=1
                        if veriler[index][0] == 1:
                            cokharcayanyemeksirketi+=1
                    index +=1
                print(f"Seçilen harcama merkezleri: {veriler[arr[0]]} , {veriler[arr[1]]} , {veriler[arr[2]]}")
                print(f"Harcama merkezleri grup adeti / %yemek şirketi :{azharca}  %{int((azharcayanyemeksirketi/azharca)*100)} , {ortaharca}  %{int((ortaharcayyanyemeksirketi/ortaharca)*100)} , {cokharca}  %{int((cokharcayanyemeksirketi/cokharca)*100)} ")
                #print(arr)
                #print(veriler[arr[0]])
                #print(veriler[arr[1]])
                #print(veriler[arr[2]])
                #print(veriler)

                #iterasyon için noktalarin merkeze uzakliği
                sifirgrubutoplammerkezeuzaklik  =0
                for sifirgrubu in veriler:
                    if sifirgrubu[2] == 0:
                        sifirgrubutoplammerkezeuzaklik += abs(sifirgrubu[1]-veriler[arr[0]][1])
                birgrubutoplammerkezeuzaklik = 0
                for birgrubu in veriler:
                    if birgrubu[2] == 1:
                        birgrubutoplammerkezeuzaklik += abs(birgrubu[1]-veriler[arr[1]][1])
                ikigrubutoplammerkezeuzaklik  =0
                for ikigrubu in veriler:
                    if ikigrubu[2] == 2:
                        ikigrubutoplammerkezeuzaklik += abs(ikigrubu[1]-veriler[arr[2]][1])
                toplam_merkezlere_uzaklik = sifirgrubutoplammerkezeuzaklik+birgrubutoplammerkezeuzaklik+ikigrubutoplammerkezeuzaklik
                seeduzaklik = []
                seeduzaklik.append(iter1)
                seeduzaklik.append(toplam_merkezlere_uzaklik)
                toplam_merkezlere_uzaklik_dizisi.append(seeduzaklik)
                print("Toplam noktaların kendi merkezlerine uzaklığı:",toplam_merkezlere_uzaklik)
                print("seçilen random seed:",iter1)
                print("\n\n")
            except:#divide by zero exception
                continue
        print("\n\n [seçilen random seed,toplam merkezlere uzaklık]\nnot: noktaların merkeze uzaklık toplamları en küçükse o iterasyon en iyi\n",toplam_merkezlere_uzaklik_dizisi)




    pass
kmeans()