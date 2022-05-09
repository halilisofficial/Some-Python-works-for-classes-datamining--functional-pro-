from random import randint

def secilensayilar():
    i = 0
    secilenler = [0,0,0,0,0,0]
    for rastgele in secilenler:
        while i < len(secilenler):
            secilen = randint(1, 49)
            if secilen not in secilenler:
                secilenler[i] = secilen
                i+=1
        i=0
        return(sorted(secilenler))

def main():
    sec=[0,0,0,0,0,0]
    for i in range(len(sec)):
        sec[i]=input(f"%s. sayı:"%(i+1))
    secilen=secilensayilar()
    counter=0
    print(secilen)
    dogru_tahmin=[]
    for x in range(len(secilen)):
        for y in range(len(sec)):
            if(int(secilen[x])==int(sec[y])):
                dogru_tahmin.append(int(secilen[x]))
                counter +=1
    print(f'%s adet sayıyı doğru tahmin ettiniz:'%counter,dogru_tahmin)
    pass

main()