print("......................................................")
print(".*.*.*.*.*Welcome to the Interest Calculator*.*.*.*.*.")
print("......................................................")

#Açılışı print komutu ile yazdırdım

Adiniz = input("Lütfen adınızı giriniz:")
yillik_faiz_orani = float(input("Yıllık faiz oranını giriniz:"))
kredi_tutari = float(input("Kredi tutarını giriniz:"))
maksimum_yil = int(input("Kredi vadesini yıl olarak giriniz:"))
maksimum_ay = int(input("Kredi vadesini ay olarak giriniz:"))
yineleme_araligi = int(input("Yineleme aralığını giriniz:"))

#Değişken adlarını atadım ve kullanıcının girebilmesi için input oluşturdum.Ayrıca ondalıklı sayı olarak olması gereken sayı değerleri için float, tam sayı olması gereken sayı değerleri için integer'a dönüştürdüm.

toplam_faiz = (kredi_tutari/100)*(yillik_faiz_orani/12)*(maksimum_ay+maksimum_yil*12)
 
toplam_odeme = toplam_faiz / ((maksimum_ay+maksimum_yil*12)/yineleme_araligi)

#faiz işlemlerinin tam ve doğru yapılabilmesi için gereken formülleri yazdım

def print_duration(ay):
    yil = int(ay/12)
    ay = ay%12
    print("yil: {}, ay: {}".format(yil,ay))

#Oluşturmuş olduğum fonksiyon, ay olarak bir integer değeri girildiğinde bunu yıl ve aya dönüştürmüş olur.

def print_money(para): 
    para = int(para*10)
    para = para/10
    print("{0}$".format(para)) 

#Oluşturmuş olduğum fonksiyon, para olarak bir float girildiğinde ondalıklı sayının virgülden sonra fazla olan kısımlarını kaldırır.

def print_entry(kredi_tutari,yillik_faiz_orani,ay):
    print("............................")
    print_duration(ay)
    print("Total payment")
    print_money(kredi_tutari)
    print("Monthly payment")
    print_money(yillik_faiz_orani)
    print("............................")

#Oluşturmuş olduğum bu fonksiyonda print_duration ve print_money fonksiyonlarını çağırdım ve tek bir giriş yazdırmış oldum.

def print_ful_report(kredi_tutari,yillik_faiz_orani,maksimum_yil,maksimum_ay,yineleme_araligi,Adiniz): 
    print("Report for {}".format(Adiniz))
    a = yineleme_araligi
    while a <= (maksimum_ay+maksimum_yil*12):
          kredi_tutari = kredi_tutari + toplam_odeme
          aylik_odeme = kredi_tutari / a
          print_entry(kredi_tutari,aylik_odeme,a)
          a = a + yineleme_araligi
print_ful_report(kredi_tutari,yillik_faiz_orani,maksimum_yil,maksimum_ay,yineleme_araligi,Adiniz) 

  ##Oluşturmuş olduğum bu fonksiyonda işlemlerimi bir döngüye sokarak tüm raporu yazdırdım. Rapor, maksimum_yil ve maksimum_ay parametreleri tarafından belirtilen süreye kadar olan girdileri görüntüledi.
  
"""Kaynakça:https://docs.python.org/3/tutorial/controlflow.html""" 
  
while True:
      pass    # Exe için
    