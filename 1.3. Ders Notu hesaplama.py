#!/usr/bin/python
# -*- coding: utf-8 -*-

isim = input("Isminiz nedir? ")
soyisim = input("Soyisminiz nedir? ")

vize = int(input("Vize notunuz nedir? "))
final = int(input("Final notunuz nedir? "))
devamsizlik = int(input("Devamsızlığınız kaç ders? "))

dersTakipPuan = (100-(devamsizlik*5))
yilsonuortalama = vize*0.3 + final*0.5 + dersTakipPuan*0.2
print("Yıl sonu notunuz: ",yilsonuortalama)


dosya = open("ogrenciNotHesaplama.txt", "w")
dosya.write("isim                   : " + isim + "\n")
dosya.write("soyisim                : " + soyisim + "\n")
dosya.write("Vize notunuz           : " + str(vize) + "\n")
dosya.write("Final notunuz          : " + str(final) + "\n")
dosya.write("Devamsızlığınız        : " + str(devamsizlik) + "\n\n")
dosya.write("Yıl Sonu Ortalamanız   : " + str(yilsonuortalama) + "\n")

dosya.close()
