ilistkota =[
    'jakarta','bandaung','bogor','makssar','surabaya','depok','bekasi','solo','jokakarta','semarang',]
i =0
while i<=len(ilistkota):
    print(ilistkota[i])
    i + 1
    a= int(input('masukan bilangan ganjil lebih dari 50:' ))
    while a% 2 != 1 or a <= 50:
        a = int(input('salah,masukkan lagi:')) 
        print('benar')
        listkota =[
            'jakarta','surabaya','depok','bekasi','solo','jogakarta','semarang','makassar'
        ]
        kotayangdicari = input('masukkan kota yang cari:')
        i =0
        while i < len(listkota):
            if listkota[i].lower()== kotayangdicari.lower():
                print('ketemu di index', i)
                break
            print('bukan',listkota[i])
            i+=1
        else:
            print('maaf, kota yang anda cari tidak ditemukan.')