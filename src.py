import random
import os



def Harita_Oluştur(satır,sütun):
    Harita={}
    for x in range(1,satır+1):
        for y in range(1,sütun+1):
            Harita.update({(x,y):0})
    return Harita



def Gözüken_Ekran_Oluştur(satır,sütun):
    Gözüken_Harita={}
    for x in range(1,satır+1):
        for y in range(1,sütun+1):
            Gözüken_Harita.update({(x,y):"#"})
    return Gözüken_Harita



def Mayınlar_Oluştur(satır,sütun):
    k=True
    while k==True:
        try:
            Mayın_Sayısı=int(input("Mayın sayısı gir: "))
            if Mayın_Sayısı>=satır*sütun or Mayın_Sayısı<=0:
                10/0
            else:
                k=False
        except Exception:
            print(f"{satır*sütun}'ten küçük 0'dan büyük herhangi bir tam sayı gir.")
    Mayınlar=set()
    while len(Mayınlar) <Mayın_Sayısı:
        x, y = random.randint(1,satır), random.randint(1,sütun)
        if (x,y) in Mayınlar:
            continue
        else:
            Mayınlar.add((x, y))
    return Mayınlar



def Harita_Mayın_Yerleştir(Mayınlar,Harita,satır,sütun):
    for x in range(1,satır+1):
        for y in range(1,sütun+1):
            if (x,y) in Mayınlar:
                if (x,y) in Harita:
                    Harita.update({(x,y):"*"})
            else:
                continue
    return Harita



def Mayın_Hesap_Algortması(Harita,satır,sütun):
    for x in range(1,satır+1):
        for y in range(1,sütun+1):
            k=0
            if Harita.get((x,y))=="*":
                continue
            else:
                for i in range(-1,2):
                    for j in range(-1,2):
                        if Harita.get((x+i,y+j))=="*":
                            k+=1
                Harita.update({(x,y):k})
    return Harita



def Kontrol_Mekanizması(Mevcut_Ekran,Mayınlar,satır,sütun):
    n=0
    for x in range(1,satır+1):
        for y in range(1,sütun+1):
            if Mevcut_Ekran.get((x,y))=="#":
                n+=1
            else:
                continue
    m=len(Mayınlar)
    if m==n:
        return 1
    else:
        return 0



def Ekranda_Parsel_Aç(Mevcut_Ekran,Mayınlar,Harita,satır,sütun):
    k=True
    while k==True:
        try:
            Seçilen_Mayın_X=int(input(f"Satır nosu için 1-{satır} dahil olmak üzere arası tam sayı gir: "))
            if Seçilen_Mayın_X>=satır+1 or Seçilen_Mayın_X<=0:
                10/0
            else:
                k=False
        except Exception:
            print("Geçerli sayı gir.")
    k=True
    while k==True:
        try:
            Seçilen_Mayın_Y=int(input(f"Sütun nosu için 1-{sütun} dahil olmak üzere arası tam sayı gir: "))
            if Seçilen_Mayın_Y>=sütun+1 or Seçilen_Mayın_Y<=0:
                10/0
            else:
                k=False
        except Exception:
            print("Geçerli sayı gir.")
    os.system('cls')
    while (Seçilen_Mayın_X,Seçilen_Mayın_Y) not in Mayınlar:
        if (Seçilen_Mayın_X,Seçilen_Mayın_Y) not in Mayınlar:
            k=Harita.get((Seçilen_Mayın_X,Seçilen_Mayın_Y))
            if k==0:
                Mevcut_Ekran.update({(Seçilen_Mayın_X,Seçilen_Mayın_Y):"."})
            else:
                Mevcut_Ekran.update({(Seçilen_Mayın_X,Seçilen_Mayın_Y):k})
            if Harita.get((Seçilen_Mayın_X,Seçilen_Mayın_Y))==0:
                for s in range(1,int((satır*sütun)**(1/2))):
                    for x in range(1,satır+1):
                        for y in range(1,sütun+1):
                            for i in range(-1,2):
                                for j in range(-1,2):
                                    if Mevcut_Ekran.get((x,y))==".":
                                        if Mevcut_Ekran.get((x+i,y+j))==".":
                                            Mevcut_Ekran.update({(x+i,y+j):"."})
                                        else:
                                            if Harita.get((x+i,y+j))==0:
                                                Mevcut_Ekran.update({(x+i,y+j):"."})
                                            else:
                                                Mevcut_Ekran.update({(x+i,y+j):Harita.get((x+i,y+j))})
            Harita_Test(Mevcut_Ekran,satır,sütun)
            if Kontrol_Mekanizması(Mevcut_Ekran,Mayınlar,satır,sütun)==1:
                return 1
        k=True
        while k==True:
            try:
                Seçilen_Mayın_X=int(input(f"Satır nosu için 1-{satır} dahil olmak üzere arası tam sayı gir: "))
                if Seçilen_Mayın_X>=satır+1 or Seçilen_Mayın_X<=0:
                    10/0
                else:
                    k=False
            except Exception:
                print("Geçerli sayı gir.")
        k=True
        while k==True:
            try:
                Seçilen_Mayın_Y=int(input(f"Sütun nosu için 1-{sütun} dahil olmak üzere arası tam sayı gir: "))
                if Seçilen_Mayın_Y>=sütun+1 or Seçilen_Mayın_Y<=0:
                    10/0
                else:
                    k=False 
            except Exception:
                print("Geçerli sayı gir.")
        os.system('cls')
    return 0



def Mayın_Haritası(Harita,satır,sütun):
    for i in range(1,satır+1):
        for j in range(1,sütun+1):
            if Harita.get((i,j))=="*":
                continue
            elif Harita.get((i,j))==1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                Harita.update({(i,j):" "})    
    Harita_Test(Harita,satır,sütun)



def Harita_Test(Harita,satır,sütun):
        k=0
        for i in range(1,satır+1):
            for j in range(1,sütun+1):
                k+=1
                print(Harita.get((i,j)), end=" " if k%sütun!=0 else "\n")



def Oynat():
    print("Mayın Tarlası Oyununa Hoşgeldiniz!")
    satır=int(input("Satır değeri giriniz: "))
    sütun=int(input("Sütun değeri giriniz: "))
    Mayınlar=Mayınlar_Oluştur(satır,sütun)
    Harita=Harita_Oluştur(satır,sütun)
    Harita_Mayın_Yerleştir(Mayınlar,Harita,satır,sütun)
    Mayın_Hesap_Algortması(Harita,satır,sütun)
    Mevcut_Ekran=Gözüken_Ekran_Oluştur(satır,sütun)
    Sonuç=Ekranda_Parsel_Aç(Mevcut_Ekran,Mayınlar,Harita,satır,sütun)
    if Sonuç==0:
        Mayın_Haritası(Harita,satır,sütun)
        print("GAME OVER")
    else:
        print("Kutlarız!!")
    input("Oyunu kapatmak için entere bas: ")
    os.system('cls')