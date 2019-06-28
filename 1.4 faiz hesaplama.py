ana_para=int(input('ana para miktari:'))
faiz_suresi=int(input('paranizi kac yil yatirmak istiyorsunuz? :'))
faiz_orani=int(input('faiz orani:'))
faiz_miktari=ana_para*faiz_suresi*faiz_orani/100

guncel_para=ana_para+faiz_miktari
gun_sayisi=faiz_suresi*365
ay_sayisi=faiz_suresi*12
gunluk_faiz=faiz_miktari/gun_sayisi
aylik_faiz=faiz_miktari/ay_sayisi

print('ana paraniz:',ana_para)
print('arzu edilen faiz suresi:',faiz_suresi)
print('faiz orani:',faiz_orani)
print('faiz miktari:',faiz_miktari)
print('guncel para miktari:',guncel_para)
print('gunluk faiz miktari:',gunluk_faiz)
print('aylik faiz miktari:',aylik_faiz)
