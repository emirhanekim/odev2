# bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.
# Bu öğrenci kayıt sistemine;
# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

#adım1. boş bir liste oluşturalım
#adım2. kullanıcıdan isim soy isim şeklinde bir girdi isteyelim
#adım3. aldığımız girdiyi "append" veya "extend" komutu ile listeye ekleyelim
#adım4. aldığımız inputu atadığımız değişkeni if koşulu ile listede var olup olmadığını sorgulatırız
#adım5. eğer varsa "remove" komutu ile listeden kaldırırız

# ogrenciler= ["Ahmet","Veli","Cemin"]

# print(ogrenciler.index("Veli"))##

ogrenciler = []

caseList = [1,2,3,4,5,6,7,8,9]

def ogrenciListele():
    print("\n\n\nÖĞRENCİLER LİSTESİ\n")
    for ogrenci in ogrenciler:
        print(ogrenciler.index(ogrenci)+1 , "ncı öğrenci bilgileriniz ",ogrenci)

def ogrenciEkle():
    try:
        ogrenci = (str)(input("Lütfen eklemek istediğiniz öğrenciyi isim soy isim şeklinde giriniz: "))
        if ogrenci not in ogrenciler:
           ogrenciler.append(ogrenci)
    except:
        print("Lütfen isim giriniz ...")
        ogrenciEkle()



def ogrenciSil():
    while True:
        try:
            deleteOgrenci = (int)(input("Silmek istediğiniz öğrenci numarasını giriniz(Çıkış için 0 a basınız) = "))
            if deleteOgrenci == 0:
                break
            else:
                ogrenciler.pop(deleteOgrenci-1)
        except:
            print("geçerli öğrenci numarası giriniz")
            ogrenciSil()        


def getirOgrenciNo():
    try:
        ogrenci = (input("Okul numarasını öğrenmek istediğiniz öğrenci ismi giriniz : "))
        print(ogrenci,"isimli öğrencinizin okul numarası = ",ogrenciler.index(ogrenci))
    except:
        case = (int)(input("Girdiğiniz bilgiere ait öğrenci bulunmamaktadır. Başka öğrenci giriniz. Menu dönmek için (0) a basınız."))
        if(case == 0):
            switch()
        getirOgrenciNo()
        

def switch():
    print("\n\nMENU\n","1-Öğrenci Ekle\n","2-Öğrenci Listele\n","3-Öğrenci Sil\n","4-Öğrenci No Bul\n","0-Çıkış\n")
    try:
        case =(int) (input("Seçiminizi giriniz :  "))
    except:
        print("Lütfen 0 ve 9 arasında değer girişi yapınız")
        switch()
    if( case == 0):
        print("Çıkış yapıldı...")
        exit()
    elif(case != 0):
        while case>0 & case <10:
            if(case == 1):
                ogrenciEkle()
                switch()
            elif(case == 2):
                ogrenciListele()
                switch()
            elif(case == 3):
                ogrenciSil()
                switch()
            elif(case == 4):
                getirOgrenciNo()
                switch()
        if case not in caseList:
            print("Hatalı Seçim tekrar giriş yapınız ! ")
            switch()

    


def main():
    switch()

main()
  