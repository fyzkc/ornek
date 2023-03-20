import yaml

"""Ritmik sayma sayıları şu şekildedir.
2-4-6-8….
3-6-9-12…
4-8-12-16…
…
9-18-27-36
1'den 10'a kadar olan tüm sayıların 100'e kadar olan ritmik sayılar 
tablosunu iç-içe döngü yapılarını kullanarak python dilinde kodlayınız."""


for n in range(2,11):
    sayac_feyza_koc=n
    print("{}. sayının ritmik sayması:".format(n))
    for i in range(101):
        if i%n==0:
            print(n, end=" ")
            n=n+sayac_feyza_koc
    print("\n")