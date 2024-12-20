def salam():
    print("hello,selamat pagi")

salam()

def luas_persegi(sisi):
 luas = sisi * sisi
 return luas
print("Iuas persegi: %d" % luas_persegi(6))

def luas_persegi(sisi):
     luas = sisi * sisi
     return luas

def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume
sisi = 5
print("luas persegi:",luas_persegi(sisi))
print("volume kubus:",volume_persegi(sisi))

##nama = "belajar kode"
#versi ="1.0.0"

#def help():
    #nama =

buku = []
def show_data():
    if len(buku) <= 0:
        print("belum ada data")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s"% (indeks,buku[indeks]))

def insert_data():
    buku_baru = input("judul buku:")
    buku.append(buku_baru)


def edit_data():
    show_data()
    indeks = int(input("inputkan id buku"))
    if indeks > len(buku):
        print("id salah")
    else:
        buku.remove(buku[indeks])

def menu():
    print("\n")
    print('------------menu-------')
    print("[1]show data")
    print("[2] insert_data")
    print("[3] edit_data")
    print("[4] delete data")
    print("[5]exit")

    menu = int(input('pilih menu: '))
    if int(menu) == 1:
        show_data()
    elif int(menu) == 2:
        insert_data()
    elif int(menu) == 3:
        edit_data()
    elif int(menu) == 4:
        exit()
    else:
        print("salah pilih!")

def main():
    while True:
        menu()

main()
