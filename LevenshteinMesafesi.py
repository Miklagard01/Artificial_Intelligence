import numpy
#Girilen 3 değerden küçüğünü döndüren min.Fonksiyonu
def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    if b<=c and b<=a:
        return b
    if c<=a and c<=b:
        return c;
#Girilen 3 değerden büyüğünü döndüren max. Fonksiyonu
def max(a,b):
    if(a < b):
        return b
    else:
        return a
#Benzerlik oranını tespit edip,iki diziyi aynı uzunluğa bos eleman ekleyip
#olması gereken boyuta getiriyor.
#Normalizasyon Fonksiyonu
def normalize (X,size):
    if len(X) < size:
        fark = size - len(X)
        for i in range(fark):
            X = X + " "
    return X
#Levenshtein tablosu üerinde tam dönüşüm için gerekli işlem sayılarını hesaplayarak ilerleyen Döngü
def LevenshteinMesafesi(A,B):
    K = numpy.zeros((len(A)+ 1, len(B)+ 1))
    A_len = len(A)
    B_len = len(B)
#A ve B uzunlukları alınıp (A+1)X(B+1) boyutlarında "0" matrisi olusturuldu.
    for i in range(A_len):
        K[i][0] = 1
    for i in range(B_len):
        K[0][i] = 1
#Tüm satır ve sütun başlarını artan bir indis olarak güncellendi.
    silme = 0
    ekleme = 0
    yerdegirme = 0

    for i in range(1,A_len + 1):
        for j in range(1,B_len + 1):
            if A[i-1] == B[j-1]:
                K[i][j] = K[i-1][j-1]
            else:
                silme = K[i-1][j] +1
                ekleme = K[i][j-1] +1
                yerdegirme =K[i-1][j-1] +1
                K[i][j] = minimum(silme,ekleme,yerdegirme)
    return K[B_len -1][A_len -1]
"""Döngü tüm satır ve sütunları gezerek elemanları kıyaslıyor.Eğer iki eleman aynı değil ise silme,
ekleme ve yerdegistirme işlemlerinden her birini deneyerek arasında en az adımlı olanı esas alıp
güncelleme işlemi yapıyor.böylece Lev.Mes. +1 etki edeceke şekilde tabloya ekliyor"""
print("İlk Kelimeyi Giriniz:")
kelime_1 = input()
print("Diğer Kelimeyi Giriniz:")
kelime_2 = input()
max_len = max(len(kelime_1), len(kelime_2))

kelime_1 = normalize(kelime_1,max_len)
kelime_2 = normalize(kelime_2,max_len)
mesafe = LevenshteinMesafesi(kelime_1,kelime_2)

print("'"+ kelime_1+ "'ve'"+kelime_2+"' arasındaki Levenshtein Mesafesi:")
print(mesafe)
benzerlik_oran = (max_len - mesafe)/max_len
print("Benzerlik oranı:")
print(benzerlik_oran)